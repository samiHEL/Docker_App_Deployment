import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    # Test avec des fausses données
    response = client.post('/login', data={'username': 'fake_user', 'password': 'fake_password'})
    assert b'Invalid Credentials. Please try again.' in response.data

    # Test avec de vraies données
    response = client.post('/login', data={'username': 'admin', 'password': 'admin'})
    assert b'Logged in as: admin' in response.data
