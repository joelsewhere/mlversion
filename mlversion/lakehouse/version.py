import dill
from urllib.parse import urlparse

class ObjIO:

    def write(self, filename):
        with open(filename, 'wb') as file:
            return dill.dump(self, file)
    
    def load(self, filename):
        with open(filename, 'rb') as file:
            dill.load(file)
        
class ObjectVersion(ObjIO):

    def __init__(self, table, database="objects", version=None, id=None, object=None):

        # if both version & id throw error
        
        # if id query for version id

        # if version query for version

        # if neither version or id create new version
        self.generate_new_version(object)

        pass

    def commit(self):

        # generate path for object, partitioned by version

        # use dill to write to object path

        # write iceberg table containing version, write_timestamp, id, path to stored object, and self.metadata()

        # returns Version(self.table, self.version)

        pass


    def generate_new_version(self, object):
        """
        Should support whatever versioning schema is appropriate
        
        :param self: Description
        """
        self._object = object
        
        # determine version
        version = None

        #
        pass

    def generate_metadata(self, object):
        pass
    
    @property
    def metadata_schema(self):
        pass

    @property
    def data(self):
        
        if hasattr(self, '_data'):
            return self._data
        
        # return query to record using table name and version number or id

    @property
    def object_path(self):
        return ''

    @property
    def object(self):

        if hasattr(self, '_object'):
            return self._object
        
        if self.storage_scheme == 's3':
            # pull from s3
            pass
        elif self.storage_schema == 'file':
            # read from file system
            pass

    @property
    def storage_scheme(self):

        return urlparse(self.object_path).scheme
    


"""
old_version = ObjectVersion(database="models", version="HEAD")

new_model = LinearRegression().fit(X, y)
new_version = ObjectVersion(database='models', table='kpi_model', object=new_model).commit()

old_predictions = old_version.object.predict(X, y)
new_predictions = new_version.object.predict(X, y)

"""
    
