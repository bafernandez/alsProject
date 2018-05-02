#!/usr/bin/env python2
#
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.Aviso import Aviso

class AvisosListHandler(webapp2.RequestHandler):
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
        avisos = Aviso.query().order(-Aviso.fecha)

        values = {
            "avisos": avisos,
            "usuario": usuario,
            "log": log,
            "admin": admin
        }

        self.response.write(jinja.render_template("aviso_list.html", **values))

app = webapp2.WSGIApplication([
    ('/avisos/list', AvisosListHandler)
], debug=True)



