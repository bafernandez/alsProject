
import webapp2
from google.appengine.api import users
from model.Aviso import Aviso
from webapp2_extras import jinja2
from google.appengine.ext import ndb
import time

class AvisoEditHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        admin = users.is_current_user_admin()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')

        try:
            id = self.request.GET['id']
        except KeyError:
            self.redirect("/")
            return

        try:
            aviso = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/")
            return

        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "asunto": aviso.asunto,
            "descripcion": aviso.descripcion,
            "id": id,
            "usuario": usuario,
            "logout": log,
            "admin": admin
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("aviso_edit.html",**values))

    def post(self):
        try:
            id = self.request.get("id", "").strip()
        except KeyError:
            self.redirect("/")
            return

        try:
            aviso = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/avisos/list")
            return

        aviso.asunto = self.request.get("asunto", "").strip()
        aviso.descripcion = self.request.get("descripcion", "").strip()

        Aviso.update(aviso)
        time.sleep(0.1)
        self.redirect("/avisos/list")

app = webapp2.WSGIApplication([
    ("/avisos/edit", AvisoEditHandler),
], debug=True)
