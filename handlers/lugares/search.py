
import webapp2
from google.appengine.api import users
from model.Lugar import Lugar
from webapp2_extras import jinja2
from google.appengine.ext import ndb
import time

class SearchLugar(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/')
        else:
            usuario = "none"
            log = users.create_login_url('/')

        search = self.request.get("search", "").strip()

        try:
            lugares = Lugar
        except:
            self.redirect("/")
            return

        jinja = jinja2.get_jinja2(app=self.app)



        values = {
            "lugares": lugares,
            "usuario": usuario,
            "logout": log
        }
        jinja = jinja2.get_jinja2(app = self.app)

        self.response.write(jinja.render_template("main.html",**values))



app = webapp2.WSGIApplication([
    ("/lugares/search", SearchLugar),
], debug=True)
