#!/usr/bin/env python2

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.Aviso import Aviso
import time

class AvisosDeleteHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['id']
        except KeyError:
            self.redirect("/")
            return

        try:
            aviso = ndb.Key(urlsafe=id).get()
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


        aviso.key.delete()
        avisos = Aviso.query()
        time.sleep(0.1)

        values = {
            "usuario": usuario,
            "avisos": avisos,
            "logout": log,
            "admin": admin
        }

        self.response.write(jinja.render_template("aviso_list.html", **values))

app = webapp2.WSGIApplication([
    ('/avisos/delete', AvisosDeleteHandler)
], debug=True)



