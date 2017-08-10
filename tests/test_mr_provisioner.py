import logging
import os
import pytest
import tempfile
from mr_provisioner import create_app, db

@pytest.fixture
def app(request):
    #db_fd, temp_db_location = tempfile.mkstemp()
    #print(temp_db_location)

    app = create_app(config_path="tests/config.ini")
    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        #init_db()
        #import pdb; pdb.set_trace()
        yield app
#    os.remove(temp_db_location)

#
@pytest.fixture
def client(request, app):

    client = app.test_client()

    def teardown():
        #os.close(app.config['DB_FD'])
        #os.unlink(app.config['DATABASE'])
        pass
    request.addfinalizer(teardown)

    return client

def test_slash(client):
    rv = client.get('/')
    assert rv._status == "302 FOUND"
    assert rv.location == "http://localhost/admin/"
    rv1 = client.get('/admin')
    assert rv1._status == "301 MOVED PERMANENTLY"
    assert rv1.location == 'http://localhost/admin/'
    rv2 = client.get('/admin/')
    assert rv2._status == '200 OK'
    assert b'mr-provisioner' in rv2.data




def login(client, username, password):
    return client.post('/admin/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/admin/logout', follow_redirects=True)

#def test_login_logout(client):
#    """Make sure login and logout works"""
#    username = "admin"
#    password = "default"
#    rv = login(client, username, password)
#    import pdb; pdb.set_trace()

#    import pdb; pdb.set_trace()
#    assert b'You were logged in' in rv.data
#    rv = logout(client)
#    assert b'You were logged out' in rv.data
#    rv = login(client, username + 'x',
#               password)
#    assert b'Invalid username' in rv.data
#    rv = login(client, username,
#               password + 'x')
#    assert b'Invalid password' in rv.data


#def test_messages(client, app):
#    """Test that messages work"""
#    login(client, app.config['USERNAME'],
#          app.config['PASSWORD'])
#    rv = client.post('/add', data=dict(
#        title='<Hello>',
#        text='<strong>HTML</strong> allowed here'
#    ), follow_redirects=True)
#    assert b'No entries here so far' not in rv.data
#    assert b'&lt;Hello&gt;' in rv.data
#    assert b'<strong>HTML</strong> allowed here' in rv.data
