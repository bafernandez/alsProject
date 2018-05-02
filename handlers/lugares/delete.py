#!/usr/bin/env python2

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.Lugar import Lugar
import time

class DeleteHandler(webapp2.RequestHandler):
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

        lugar.delete()
        time.sleep(0.1)
        self.response.write(jinja.render_template("lugar_list.html", **values))

app = webapp2.WSGIApplication([
    ('/lugares/delete', DeleteHandler)
], debug=True)



