import  google.appengine.ext.ndb as ndb

class Comentario_Lugar(ndb.Model):
    autor = ndb.StringProperty()
    comentario = ndb.TextProperty()
    fecha = ndb.DateTimeProperty()
    id_lugar = ndb.StringProperty()