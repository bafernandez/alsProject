import  google.appengine.ext.ndb as ndb

class Aviso(ndb.Model):
    asunto = ndb.StringProperty()
    descripcion = ndb.TextProperty()
    fecha = ndb.DateTimeProperty()

    @ndb.transactional
    def update(aviso):
        """Updates a section.
            :param par: The ticket to update.
            :return: The key of the record.
        """
        return aviso.put()