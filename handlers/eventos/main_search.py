#!/usr/bin/env python2
#
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.Evento import Evento
import google.appengine.ext.ndb as ndb

class EventoMainSearchHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        admin = users.is_current_user_admin()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')


        patt = self.request.get("pattern", "")
        self.patt = patt.strip().lower()

        self.result = []
        Evento.query().map(self.search)
        if len(self.result) is 0:
            eventos = Evento.query()

        else:
            eventos = Evento.query(Evento.key.IN(self.result))


        values = {
            "eventos": eventos,
            "usuario": usuario,
            "log": log,
            "admin": admin
        }

        jinja = jinja2.get_jinja2(app=self.app)
        print(self.result)
        self.response.write(jinja.render_template("evento_main_list.html", **values))

    def search(self, evento):
        nombre = evento.nombre.lower()
        lugar = evento.nombre_lugar.lower()
        web = evento.pagweb
        precio = evento.precio

        if (self.patt in nombre or self.patt in web or self.patt in lugar
                or self.patt in precio):
            self.result.append(evento.key)


app = webapp2.WSGIApplication([
    ('/eventos/main_search', EventoMainSearchHandler)
], debug=True)



