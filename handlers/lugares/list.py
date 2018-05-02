#!/usr/bin/env python2
#
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.Lugar import Lugar

class MainHandler(webapp2.RequestHandler):
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
        lugares = Lugar.query()

        values = {
            "lugares": lugares,
            "usuario": usuario,
            "log": log,
            "admin": admin
        }

        self.response.write(jinja.render_template("lugar_list.html", **values))

app = webapp2.WSGIApplication([
    ('/lugares/list', MainHandler)
], debug=True)



