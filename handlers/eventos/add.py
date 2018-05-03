
import webapp2
from google.appengine.api import users
from model.Lugar import Lugar
from model.Evento import Evento
from webapp2_extras import jinja2
import time
from google.appengine.api import images
from google.appengine.ext import ndb
import datetime

class EventAddHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        admin = users.is_current_user_admin()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')

        lugares = Lugar.query()
        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "usuario": usuario,
            "logout": log,
            "admin": admin,
            "lugares": lugares
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("evento_add.html",**values))

    def post(self):

        lugar_id = self.request.get("lugar_id", "").strip()

        try:
            lugar = ndb.Key(urlsafe=lugar_id).get()
        except:
            self.redirect("/")
            return

        nombre = self.request.get("nombre", "").strip()
        descripcion = self.request.get("descripcion", "").strip()
        nombre_lugar = lugar.nombre
        pagweb = self.request.get("email", "").strip()
        fecha = datetime.datetime.strptime(self.request.get("fecha", "").strip(), "%Y-%m-%d").date()
        hora = datetime.datetime.strptime(self.request.get("hora", "").strip(), '%H:%M').time()
        precio = self.request.get("precio", "").strip()
        foto = self.request.get("foto")
        if (len(nombre) == 0 or len(descripcion) == 0 or len(nombre_lugar) == 0):
            self.response.write("Error")
            return

        evento = Evento(nombre=nombre, descripcion=descripcion, nombre_lugar=nombre_lugar, pagweb=pagweb,
                       lugar_id=lugar_id, fecha=fecha, hora=hora, precio=precio, foto=foto)
        evento.put()
        time.sleep(0.1)
        self.redirect("/")


app = webapp2.WSGIApplication([
    ("/eventos/add", EventAddHandler),
], debug=True)
