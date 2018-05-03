import  google.appengine.ext.ndb as ndb

class Evento(ndb.Model):
    nombre = ndb.StringProperty()
    descripcion = ndb.TextProperty()
    nombre_lugar = ndb.StringProperty()
    pagweb = ndb.StringProperty()
    lugar = ndb.StringProperty()
    fecha = ndb.DateTimeProperty()
    foto = ndb.BlobProperty()

    @ndb.transactional
    def update(evento):
        """Updates a section.
            :param par: The ticket to update.
            :return: The key of the record.
        """
        return evento.put()