import pytest
from app import create_app, db
from app.model import Issue
from app.exceptions import ValidationError

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    db.create_all()
    yield
    db.drop_all()

def test_create_issue(client, init_database):
    response = client.post('/register', json={
        'title': 'Test Issue',
        'description': 'This is a test issue'
    })
    assert response.status_code == 200
    assert b'Issue created successfully!' in response.data

def test_get_issues(client, init_database):
    client.post('/register', json={
        'title': 'Test Issue',
        'description': 'This is a test issue'
    })
    response = client.get('/issues')
    assert response.status_code == 200
    assert b'Test Issue' in response.data

def test_get_issue_by_id(test_client):
    response = test_client.post('/register', json={
        'title': 'Another Issue',
        'description': 'This is another test issue'
    })
    assert response.status_code == 200
    response_json = response.get_json()
    assert 'id' in response_json  # Ensure 'id' is in the response
    issue_id = response_json['id']

    response = test_client.get(f'/issues/{issue_id}')
    assert response.status_code == 200
    assert response.get_json()['title'] == 'Another Issue'


def test_update_issue(client, init_database):
    response = client.post('/register', json={
        'title': 'Issue to Update',
        'description': 'Description before update'
    })
    issue_id = response.get_json()['id']
    response = client.put(f'/issues/{issue_id}', json={
        'title': 'Updated Issue',
        'description': 'Description after update'
    })
    assert response.status_code == 200
    assert b'Updated Issue' in response.data

def test_delete_issue(client, init_database):
    response = client.post('/register', json={
        'title': 'Issue to Delete',
        'description': 'Description before delete'
    })
    issue_id = response.get_json()['id']
    response = client.delete(f'/issues/{issue_id}')
    assert response.status_code == 200
    assert b'Issue deleted successfully!' in response.data

def test_404_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Page not found' in response.data

def test_500_error(client):
    with pytest.raises(Exception):
        client.get('/issues/invalid_id')

def test_validation_error(client, init_database):
    response = client.post('/register', json={})
    assert response.status_code == 400
    assert b'Validation Error' in response.data

