#!/usr/bin/env python2

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.Lugar import Lugar
import datetime
from model.Comentario_Lugar import Comentario_Lugar
import time

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
        admin = users.is_current_user_admin()
        comentarios = Comentario_Lugar.query(Comentario_Lugar.id_lugar == id).order(Comentario_Lugar.fecha)

        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/lugares/show?id='+ lugar.key.urlsafe())
        else:
            usuario = "none"
            log = users.create_login_url('/lugares/show?id='+ lugar.key.urlsafe())

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
            "log": log,
            "admin": admin,
            "id": id,
            "comentarios" : comentarios
        }

        self.response.write(jinja.render_template("lugar_show.html", **values))

    def post(self):


        lugar_id = self.request.get("id", "").strip()

        try:
            lugar = ndb.Key(urlsafe=lugar_id).get()
        except:
            self.redirect("/")
            return

        user = users.get_current_user()
        admin = users.is_current_user_admin()

        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/lugares/show?id='+ lugar.key.urlsafe())
        else:
            usuario = "none"
            log = users.create_login_url('/lugares/show?id='+ lugar.key.urlsafe())

        comentarios = Comentario_Lugar.query(Comentario_Lugar.id_lugar == lugar_id).order(Comentario_Lugar.fecha)
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
            "log": log,
            "admin": admin,
            "id": lugar_id,
            "comentarios": comentarios
        }


        usuario_comento = self.request.get("usuario", "").strip()
        comentario = self.request.get("comentario", "").strip()
        fecha = datetime.datetime.now()

        if (len(lugar_id) == 0 or len(usuario_comento) == 0 or len(comentario) == 0):
            self.response.write("Error")
            return

        comentario_lugar = Comentario_Lugar(autor = usuario_comento, comentario=comentario, fecha = fecha, id_lugar = lugar_id)
        comentario_lugar.put()
        time.sleep(0.1)
        self.redirect("/lugares/show?id="+ lugar_id)

app = webapp2.WSGIApplication([
    ('/lugares/show', ShowHandler)
], debug=True)



