Authentication Setup and Testing for Mins - Movie Insights API
This guide outlines the steps to set up JSON Web Token (JWT) authentication in your Django REST Framework (DRF) project and provides instructions on how to test the authentication process.

1. Setting Up JWT Authentication
1.1. Install Required Packages
Ensure that the following packages are installed in your Django project:

bash
Copy code
pip install djangorestframework djangorestframework-simplejwt
1.2. Update settings.py
Add 'rest_framework' and 'rest_framework_simplejwt' to your INSTALLED_APPS:

python
Copy code
INSTALLED_APPS = [
    # Other installed apps
    'rest_framework',
    'rest_framework_simplejwt',
]
Configure the REST framework to use JWT authentication by updating the DEFAULT_AUTHENTICATION_CLASSES:

python
Copy code
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
Optionally, configure JWT settings to customize token lifetimes and behaviors:

python
Copy code
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    # Additional settings...
}
1.3. Update urls.py
Include the JWT views in your project's URL configuration:

python
Copy code
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Other URL patterns
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
2. Testing the Authentication Setup
2.1. Obtain JWT Tokens
To authenticate, users need to obtain an access and refresh token by providing their credentials.

Request:

http
Copy code
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
Response:

json
Copy code
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
2.2. Access Protected Endpoints
Use the obtained access token to access protected API endpoints by including it in the Authorization header.

Request:

http
Copy code
GET /api/protected-endpoint/
Authorization: Bearer your_access_token
Response:

http
Copy code
HTTP/1.1 200 OK
{
    "message": "Access granted to protected endpoint."
}
2.3. Refreshing the Access Token
When the access token expires, obtain a new one using the refresh token.

Request:

http
Copy code
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token"
}
Response:

json
Copy code
{
    "access": "new_access_token"
}
3. Testing with Tools
3.1. Using Postman
Obtain Tokens:

Create a POST request to /api/token/.
In the body, select raw and JSON, then provide the username and password.
Send the request to receive the tokens.
Access Protected Endpoint:

Create a GET request to a protected endpoint.
In the Headers tab, add Authorization with the value Bearer your_access_token.
Send the request to access the endpoint.
Refresh Token:

Create a POST request to /api/token/refresh/.
In the body, provide the refresh token.
Send the request to receive a new access token.
3.2. Using cURL
Obtain Tokens:

bash
Copy code
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'
Access Protected Endpoint:

bash
Copy code
curl -H "Authorization: Bearer your_access_token" \
http://localhost:8000/api/protected-endpoint/
Refresh Token:

bash
Copy code
curl -X POST http://localhost:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{"refresh": "your_refresh_token"}'
4. Additional Resources
For more detailed information, refer to the official documentation:

Django REST Framework Authentication
Simple JWT Documentation
By following these steps, you can set up JWT authentication in your Django REST Framework project and test its functionality using tools like Postman or cURL.

For a visual guide on implementing JWT authentication in Django REST Framework, you might find the following video helpful:

Complete Django Rest Framework JWT Authentication System