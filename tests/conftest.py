import mongoengine as me
import pytest
from mongomock.mongo_client import MongoClient


@pytest.fixture()
def get_db(request):
    me.disconnect('default')
    db = me.connect(
        'testdb',
        host='mongodb://localhost',
        alias='default',
        mongo_client_class=MongoClient,
    )
    yield db
    db.drop_database('testdb')
