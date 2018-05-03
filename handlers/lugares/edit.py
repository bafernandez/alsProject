
import webapp2
from google.appengine.api import users
from model.Lugar import Lugar
from webapp2_extras import jinja2
from google.appengine.ext import ndb
import time

class EditLugar(webapp2.RequestHandler):
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
            lugar = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/")
            return

        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "nombre": lugar.nombre,
            "descripcion": lugar.descripcion,
            "num_telefono": lugar.num_telefono,
            "pagweb": lugar.pagweb,
            "lugar": lugar.lugar,
            "categoria": lugar.categoria,
            "foto": lugar.foto,
            "id": id,
            "usuario": usuario,
            "logout": log,
            "admin": admin
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("lugar_edit.html",**values))

    def post(self):
        try:
            id = self.request.get("id", "").strip()
        except KeyError:
            self.redirect("/")
            return

        try:
            lugar = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/")
            return

        lugar.nombre = self.request.get("nombre", "").strip()
        lugar.descripcion = self.request.get("descripcion", "").strip()
        lugar.num_telefono = self.request.get("num_telefono", "").strip()
        lugar.pagweb = self.request.get("email", "").strip()
        lugar.lugar = self.request.get("lugar", "").strip()
        lugar.categoria = self.request.get("categoria", "").strip()
        foto = self.request.get("foto")
        if len(foto) > 0:
            lugar.foto = foto

        Lugar.update(lugar)
        time.sleep(0.1)
        self.redirect("/lugares/list")

app = webapp2.WSGIApplication([
    ("/lugares/edit", EditLugar),
], debug=True)
