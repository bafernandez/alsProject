import  google.appengine.ext.ndb as ndb

class Lugar(ndb.Model):
    nombre = ndb.StringProperty()
    descripcion = ndb.TextProperty()
    num_telefono = ndb.StringProperty()
    pagweb = ndb.StringProperty()
    lugar = ndb.StringProperty()
    categoria = ndb.StringProperty()
    foto = ndb.BlobProperty()

    @ndb.transactional
    def update(lugar):
        """Updates a section.
            :param par: The ticket to update.
            :return: The key of the record.
        """
        return lugar.put()