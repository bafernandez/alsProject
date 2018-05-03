import  google.appengine.ext.ndb as ndb

class Comentario_Evento(ndb.Model):
    autor = ndb.StringProperty()
    comentario = ndb.TextProperty()
    fecha = ndb.DateTimeProperty()
    id_evento = ndb.StringProperty()