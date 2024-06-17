import streamlit as st

# Initialize session state for user_data if not already present
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}


def home():
    """
    Renders the Home page.
    Greets and provides information about the app.
    """
    st.title("Simple Login App")
    st.header("Home")
    st.write("Welcome to Simple Login App. Please use the menu to log in or sign up.")


def signup():
    """
    Renders the sign-up page for the web application.
    Allows a new user to create an account by providing a username and password.
    Checks for existing username and password confirmation before adding the user.
    """

    st.title("Simple Login App")
    st.header("Create a New Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    # confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if username in st.session_state['user_data']:
            st.error("Username already exists. Please choose a different username.")
        # elif password != confirm_password:
        #     st.error("Passwords do not match.")
        else:
            st.session_state['user_data'][username] = password
            st.success("You have successfully signed up!")
            st.info("Please go to the Login page to log in.")


def login():
    """
    Renders the login page for the web application.
    Allows an existing user to log in by providing their username and password.
    Checks for the existence of the username and matches the password.
    """
    st.title("Simple Login App")
    st.header("Login Section")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username not in st.session_state['user_data']:
            st.error("Username does not exist. Please sign up first.")
        elif st.session_state['user_data'][username] != password:
            st.error("Incorrect password. Please try again.")
        else:
            st.success(f"Welcome {username.title()}!")
            st.write("You have successfully logged in.")
            st.header("Inner Page")
            st.write("This is a protected inner page that only logged in user can see.")


def main():
    """
    Main function to run the Streamlit app.
    Provides navigation between the sign-up and login pages using a sidebar dropdown menu list.
    """
    # st.sidebar.header("Menu")
    choice = (st.sidebar.selectbox("Menu", ["Home", "Login", "Sign Up"]))

    if choice == "Sign Up":
        signup()
    elif choice == "Login":
        login()
    elif choice == "Home":
        home()


if __name__ == "__main__":
    main()
