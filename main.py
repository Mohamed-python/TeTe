import flet as ft
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import json

# إعدادات OAuth 2.0 من Google Developer Console
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid']
REDIRECT_URI = "https://chatgpt.com/oauth2callback"

def main(page: ft.Page):
    page.title = "Google Sign-In with Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def login_with_google(e):
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        page.launch_url(authorization_url)

    def handle_oauth_callback(e):
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(authorization_response=page.url)
        credentials = flow.credentials

        # حفظ التوكن في ملف
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

        page.add(ft.Text("تم تسجيل الدخول بنجاح!"))

    login_button = ft.ElevatedButton("تسجيل الدخول باستخدام Google", on_click=login_with_google)
    page.add(login_button)

    if "code=" in page.url:
        handle_oauth_callback(None)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
