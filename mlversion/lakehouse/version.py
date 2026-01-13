import dill
import pyarrow as pa
from urllib.parse import urlparse


class ObjectVersion:

    def __init__(self, table, database="objects", version=None, object=None):

        # if version query for version
        self._version = version

        # store 
        self._object = object
        self.table = table
        self.database = database

        pass

    def commit(self):

        # generate path for object, partitioned by version
        # https://stackoverflow.com/questions/78933802/how-to-create-a-partitioned-table-in-python-using-pyiceberg-with-pyarrow

        # use dill to write to object path


        # write iceberg table containing version, write_timestamp, id, path to stored object, and self.metadata()

        # returns Version(self.table, self.version)

        pass


    @property
    def version(self):
        """
        Should support whatever versioning schema is appropriate
        
        :param self: Description
        """
        if hasattr(self, '_version'):
            return self._version
        
        # determine version
        version = None

        return version

    
    @property
    def metadata(self, object):
        
        if hasattr(self, '_metadata'):
            return self._metadata
        
        self._metadata = self.generate_metadata()
        return self._metadata
    
    
    def generate_metadata(self):

        return pa.Table.from_pylist([])
  

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
    

