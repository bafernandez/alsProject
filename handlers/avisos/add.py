
import webapp2
from google.appengine.api import users
from model.Aviso import Aviso
from webapp2_extras import jinja2
import time
import datetime

class AddAviso(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        admin = users.is_current_user_admin()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')

        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "usuario": usuario,
            "logout": log,
            "admin": admin
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("aviso_add.html",**values))

    def post(self):
        asunto = self.request.get("asunto", "").strip()
        descripcion = self.request.get("descripcion", "").strip()
        fecha = datetime.datetime.now()

        if (len(asunto) == 0 or len(descripcion) == 0):
            self.response.write("Error")
            return

        aviso = Aviso(asunto=asunto, descripcion=descripcion, fecha = fecha)
        aviso.put()
        time.sleep(0.1)
        self.redirect("/avisos/list")

app = webapp2.WSGIApplication([
    ("/avisos/add", AddAviso),
], debug=True)
