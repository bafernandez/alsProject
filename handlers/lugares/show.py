#!/usr/bin/env python2

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.Lugar import Lugar

class ShowHandler(webapp2.RequestHandler):
    def get(self):
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

        user = users.get_current_user()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')

        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "nombre": lugar.nombre,
            "descripcion": lugar.descripcion,
            "num_telefono": lugar.num_telefono,
            "pagweb": lugar.pagweb,
            "lugar": lugar.lugar,
            "categoria": lugar.categoria,
            "foto": lugar.foto,
            "usuario": usuario,
            "logout": log
        }

        self.response.write(jinja.render_template("lugar_show.html", **values))

app = webapp2.WSGIApplication([
    ('/lugares/show', ShowHandler)
], debug=True)



