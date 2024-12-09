'''
This is the testing file for the database module.
In order to run the operation, it's required to set up AWS crentials configuration in advance.
'''
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Database import DB_operation

#read the data from the database
def test_read():
    db = DB_operation()
    data = db.read("top_news", "1")
    assert type(data) == dict
    assert data['Item']['id'] == "1"