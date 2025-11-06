import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def sign_up(email, password):
    """Create a new user account with email/password."""
    return supabase.auth.sign_up({"email": email, "password": password})

def sign_in(email, password):
    """Sign in an existing user with email/password."""
    return supabase.auth.sign_in_with_password({"email": email, "password": password})

def sign_in_with_google():
    """Initiate a Google OAuth login flow."""
    return supabase.auth.sign_in_with_oauth({"provider": "google"})

def get_user():
    """Return the currently logged-in user, or None if no active session."""
    user = supabase.auth.get_user()
    if user and user.user:
        return user.user
    return None

def sign_out():
    """Sign the current user out."""
    supabase.auth.sign_out()
