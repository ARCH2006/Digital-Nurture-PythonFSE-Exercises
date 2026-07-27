# 1. The journey of a GET /api/courses/ request

"""
User enters:
http://127.0.0.1:8000/api/courses/

Step 1:
 Browser sends an HTTP GET request.

Step 2:
Django receives the request.

Step 3:
urls.py checks which URL matches /api/courses/.

Step 4:
The matching View function is called.

Step 5:
The View requests data from the Model.

Step 6:
The Model queries the database.

Step 7:
Database returns the course records.

Step 8:
Model sends data back to the View.

Step 9:
View prepares an HTTP Response.

Step 10:
Browser receives and displays the response.


"""
"""
2. Middleware

Middleware executes before the request reaches the View
and after the View returns a response.

Examples:

1. SecurityMiddleware
 Adds security features like HTTPS redirect and security headers.

2. SessionMiddleware
 Manages user sessions so users remain logged in across requests.
"""
"""
3. WSGI vs ASGI
WSGI (Web Server Gateway Interface)
Handles synchronous requests.
jango uses WSGI by default.

ASGI (Asynchronous Server Gateway Interface)
Handles asynchronous requests.
Useful for WebSockets, chat applications,
live notifications, and long-running connections.

Switch to ASGI when building real-time applications.
"""
"""
4. MVC vs Django MVT
# MVC:
# Model -> Handles database operations.
# View -> Displays the user interface.
# Controller -> Handles business logic.

# Django MVT:
# Model -> Database layer.
# View -> Business logic (acts like Controller).
# Template -> User interface (acts like View in MVC).

# Mapping:
# MVC Model      -> Django Model
# MVC View       -> Django Template
# MVC Controller -> Django View
"""




