# from app import app

# def test_index():
#     # Crée une instance de l'application Flask de test
#     client = app.test_client()

#     # Effectue une requête GET vers la page d'accueil
#     response = client.get('/')

#     # Vérifie si la réponse a un code HTTP 200 (OK)
#     assert response.status_code == 200


import pytest
import requests
#from frontend.streamlit_app import API_ENDPOINT
API_ENDPOINT = 'http://127.0.0.1:5000'
def test_api_response_not_empty():
    # Faire l'appel à l'API
    response = requests.get(API_ENDPOINT)
    
    # Vérifier que la réponse a un code HTTP 200 (OK)
    assert response.status_code == 200
    
    # Vérifier que le JSON de la réponse n'est pas vide
    #assert response.json() != []
