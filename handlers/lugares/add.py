
import webapp2
from google.appengine.api import users
from model.Lugar import Lugar
from webapp2_extras import jinja2
import time
from google.appengine.api import images

class AddLugar(webapp2.RequestHandler):
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

        self.response.write(jinja.render_template("lugar_add.html",**values))

    def post(self):
        nombre = self.request.get("nombre", "").strip()
        descripcion = self.request.get("descripcion", "").strip()
        num_telefono = self.request.get("num_telefono", "").strip()
        pagweb = self.request.get("pagweb", "").strip()
        lugar = self.request.get("lugar", "").strip()
        categoria = self.request.get("categoria", "").strip()
        foto = self.request.get("foto")
        foto = images.resize(foto, 1200,580)
        if (len(nombre) == 0 or len(descripcion) == 0 or len(num_telefono) == 0 or len(lugar) == 0
            or len(categoria) == 0):
            self.response.write("Error")
            return

        lugar = Lugar(nombre=nombre, descripcion=descripcion, num_telefono = num_telefono, pagweb = pagweb, lugar = lugar, categoria = categoria, foto = foto)
        lugar.put()
        time.sleep(0.1)
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/lugares/add", AddLugar),
], debug=True)
