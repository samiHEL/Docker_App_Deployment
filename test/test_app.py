import pytest
import requests
#from frontend.streamlit_app import API_ENDPOINT
API_ENDPOINT = 'http://localhost:5000/api/get_data'

def test_api_response_not_empty():
    # Faire l'appel à l'API
    response = requests.get(API_ENDPOINT)
    
    # Vérifier que la réponse a un code HTTP 200 (OK)
    assert response.status_code == 200
    
    # Vérifier que le JSON de la réponse n'est pas vide
    #assert response.json() != []
