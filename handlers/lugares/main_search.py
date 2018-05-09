#!/usr/bin/env python2
#
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.Lugar import Lugar
import google.appengine.ext.ndb as ndb

class LugarMainSearchHandler(webapp2.RequestHandler):
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
        Lugar.query().map(self.search)
        if len(self.result) is 0:
            lugares = Lugar.query()

        else:
            lugares = Lugar.query(Lugar.key.IN(self.result))


        values = {
            "lugares": lugares,
            "usuario": usuario,
            "log": log,
            "admin": admin
        }

        jinja = jinja2.get_jinja2(app=self.app)
        print(self.result)
        self.response.write(jinja.render_template("main.html", **values))

    def search(self, lugar):
        nombre = lugar.nombre.lower()
        telefono = lugar.num_telefono
        web = lugar.pagweb
        categoria = lugar.categoria.lower()

        if (self.patt in nombre or self.patt in web or self.patt in categoria
                or self.patt in telefono):
            self.result.append(lugar.key)


app = webapp2.WSGIApplication([
    ('/lugares/main_search', LugarMainSearchHandler)
], debug=True)



