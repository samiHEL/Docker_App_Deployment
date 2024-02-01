import streamlit as st
import requests

# Endpoint de l'API pour obtenir les données
API_ENDPOINT = 'http://backend:5000/api/get_data'

# Function to initialize session state
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

def main():
    # Initialize session state
    init_session_state()

    st.title('Streamlit App')

    # Page 1: Login
    login_page()

    # Check if logged in
    if st.session_state.logged_in:
        # Page 2: Dashboard
        dashboard_page()

        # Page 3: Password Modification
        if password_modification_page():
            st.success('Password modified successfully!')
            st.session_state.logged_in = False  # Logout after modifying password
def login_page():
    st.header('Login Page')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # Validate credentials using API call
        response = requests.get(API_ENDPOINT)
        data = response.json()

        # Check if username and password combination exists in the data
        if any(entry['login'] == username and entry['mdp'] == password for entry in data):
            st.session_state.logged_in = True
        else:
            st.warning('Invalid Credentials. Please try again.')

def dashboard_page():
    st.header('Dashboard')

    # Display data from the API
    response = requests.get(API_ENDPOINT)
    data = response.json()
    st.write("Database Content:")
    st.table(data)

    # You can add additional content to the dashboard here

def password_modification_page():
    if not st.session_state.logged_in:
        st.warning('Please log in to modify your password.')
        return False

    st.header('Password Modification')

    old_password = st.text_input('Old Password', type='password')
    new_password = st.text_input('New Password', type='password')
    confirm_new_password = st.text_input('Confirm New Password', type='password')

    if st.button('Modify Password'):
        # You can add password modification logic here
        return True

if __name__ == '__main__':
    main()
