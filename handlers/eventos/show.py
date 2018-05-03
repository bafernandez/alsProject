#!/usr/bin/env python2

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.Evento import Evento
import datetime
from model.Comentario_Evento import Comentario_Evento
import time


class EventoShowHandler(webapp2.RequestHandler):
    def get(self):
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

        user = users.get_current_user()
        admin = users.is_current_user_admin()
        comentarios = Comentario_Evento.query(Comentario_Evento.id_evento == id).order(Comentario_Evento.fecha)

        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/eventos/show?id=' + evento.key.urlsafe())
        else:
            usuario = "none"
            log = users.create_login_url('/eventos/show?id=' + evento.key.urlsafe())

        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "nombre": evento.nombre,
            "descripcion": evento.descripcion,
            "pagweb": evento.pagweb,
            "nombre_lugar": evento.nombre_lugar,
            "fecha": evento.fecha,
            "hora": evento.hora,
            "lugar_id": evento.lugar_id,
            "precio": evento.precio,
            "foto": evento.foto,
            "usuario": usuario,
            "log": log,
            "admin": admin,
            "id": id,
            "comentarios": comentarios
        }

        self.response.write(jinja.render_template("evento_show.html", **values))

    def post(self):

        evento_id = self.request.get("id", "").strip()

        try:
            evento = ndb.Key(urlsafe=evento_id).get()
        except:
            self.redirect("/")
            return

        user = users.get_current_user()
        admin = users.is_current_user_admin()

        if user:
            usuario = user.nickname()
            log = users.create_logout_url('/eventos/show?id=' + evento.key.urlsafe())
        else:
            usuario = "none"
            log = users.create_login_url('/eventos/show?id=' + evento.key.urlsafe())

        comentarios = Comentario_Evento.query(Comentario_Evento.id_evento == evento_id).order(Comentario_Evento.fecha)
        jinja = jinja2.get_jinja2(app=self.app)

        values = {
            "nombre": evento.nombre,
            "descripcion": evento.descripcion,
            "pagweb": evento.pagweb,
            "nombre_lugar": evento.nombre_lugar,
            "fecha": evento.fecha,
            "hora": evento.hora,
            "lugar_id": evento.lugar_id,
            "precio": evento.precio,
            "foto": evento.foto,
            "usuario": usuario,
            "log": log,
            "admin": admin,
            "id": evento_id,
            "comentarios": comentarios
        }

        usuario_comento = self.request.get("usuario", "").strip()
        comentario = self.request.get("comentario", "").strip()
        fecha = datetime.datetime.now()

        if (len(evento_id) == 0 or len(usuario_comento) == 0 or len(comentario) == 0):
            self.response.write("Error")
            return

        comentario_evento = Comentario_Evento(autor=usuario_comento, comentario=comentario, fecha=fecha,
                                              id_evento=evento_id)
        comentario_evento.put()
        time.sleep(0.1)
        self.redirect("/eventos/show?id=" + evento_id)


app = webapp2.WSGIApplication([
    ('/eventos/show', EventoShowHandler)
], debug=True)
