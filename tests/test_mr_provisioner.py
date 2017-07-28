import os
import pytest
import tempfile
from mr_provisioner import create_app, db

@pytest.fixture
def app(request):
    #db_fd, temp_db_location = tempfile.mkstemp()
    #print(temp_db_location)

    app = create_app(config_path="tests/config.ini")

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

def test_redirect(client):
    rv = client.get('/')
    assert rv._status == "302 FOUND"
    assert rv.location == "http://localhost/admin/"

#
#
#def login(client, username, password):
#    return client.post('/login', data=dict(
#        username=username,
#        password=password
#    ), follow_redirects=True)
#
#
#def logout(client):
#    return client.get('/logout', follow_redirects=True)
#
#
#def test_empty_db(client):
#    """Start with a blank database."""
#    rv = client.get('/')
#    assert b'No entries here so far' in rv.data
#
#
#def test_login_logout(client, app):
#    """Make sure login and logout works"""
#    rv = login(client, app.config['USERNAME'],
#               app.config['PASSWORD'])
#    assert b'You were logged in' in rv.data
#    rv = logout(client)
#    assert b'You were logged out' in rv.data
#    rv = login(client,app.config['USERNAME'] + 'x',
#               app.config['PASSWORD'])
#    assert b'Invalid username' in rv.data
#    rv = login(client, app.config['USERNAME'],
#               app.config['PASSWORD'] + 'x')
#    assert b'Invalid password' in rv.data
#
#
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
