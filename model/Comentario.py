import  google.appengine.ext.ndb as ndb

class Comentario(ndb.Model):
    autor = ndb.StringProperty()
    comentario = ndb.TextProperty()
    fecha = ndb.DateTimeProperty()