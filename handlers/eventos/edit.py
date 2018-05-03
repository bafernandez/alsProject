
import webapp2
from google.appengine.api import users
from model.Evento import Evento
from model.Lugar import Lugar
from webapp2_extras import jinja2
from google.appengine.ext import ndb
import time
import datetime

class EditEvento(webapp2.RequestHandler):
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
            evento = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/")
            return

        lugares = Lugar.query()
        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "nombre": evento.nombre,
            "descripcion": evento.descripcion,
            "nombre_lugar": evento.nombre_lugar,
            "pagweb": evento.pagweb,
            "fecha": evento.fecha.strftime("%Y-%m-%d"),
            "hora": evento.hora.strftime("%H:%M"),
            "foto": evento.foto,
            "precio": evento.precio,
            "id": id,
            "usuario": usuario,
            "logout": log,
            "lugares": lugares,
            "admin": admin
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("evento_edit.html",**values))

    def post(self):
        try:
            lugar_id = self.request.get("lugar_id", "").strip()
            id = self.request.get("id", "").strip()
        except KeyError:
            self.redirect("/")
            return

        try:
            evento = ndb.Key(urlsafe=id).get()
            lugar = ndb.Key(urlsafe=lugar_id).get()
        except:
            self.redirect("/")
            return

        evento.nombre = self.request.get("nombre", "").strip()
        evento.descripcion = self.request.get("descripcion", "").strip()
        evento.nombre_lugar = lugar.nombre
        evento.pagweb = self.request.get("email", "").strip()
        evento.lugar_id = lugar_id
        evento.fecha =  datetime.datetime.strptime(self.request.get("fecha", "").strip(), "%Y-%m-%d").date()
        evento.hora = datetime.datetime.strptime(self.request.get("hora", "").strip(), '%H:%M').time()
        evento.precio = self.request.get("precio", "").strip()
        foto = self.request.get("foto")
        if len(foto) > 0:
            evento.foto = foto

        Evento.update(evento)
        time.sleep(0.1)
        self.redirect("/eventos/list")

app = webapp2.WSGIApplication([
    ("/eventos/edit", EditEvento),
], debug=True)
