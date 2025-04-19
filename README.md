# Achare Authentication Service

A robust and secure authentication service built with Django and Django REST Framework, providing comprehensive user management and authentication features.

## 🚀 Features

-   **Custom User Model**

    -   Phone number-based authentication (Iranian phone numbers)
    -   Optional email support
    -   UUID-based user identification
    -   First name and last name support

-   **Authentication System**

    -   OTP (One-Time Password) authentication
    -   Session management
    -   Token-based authentication
    -   Secure password validation

-   **API Features**
    -   RESTful API endpoints
    -   CORS support
    -   Debug toolbar for development
    -   Comprehensive API documentation (Postman collection included)

## 🛠️ Tech Stack

-   **Framework**: Django 5.2
-   **API Framework**: Django REST Framework 3.16.0
-   **Database**: SQLite3 (easily configurable for other databases)
-   **Additional Tools**:
    -   django-cors-headers
    -   django-debug-toolbar
    -   python-dotenv

## 📋 Prerequisites

-   Python 3.x
-   pip (Python package manager)
-   Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/pouria-drd/achare_auth.git
    cd achare_auth
    ```

2. **Create and activate virtual environment**

    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On Unix or MacOS
    source .venv/bin/activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the project root and add the following:

    ```ini
    # ---------------------------------------------------------------
    # Base URL and Admin URL Configuration
    # ---------------------------------------------------------------

    # Base URL for the API
    BASE_URL="achare-api/"

    # Admin URL for the API (Typically used to access Django's admin panel)
    ADMIN_URL="admin/"

    # ---------------------------------------------------------------
    # Debugging and Secret Key Configuration
    # ---------------------------------------------------------------

    # Debug mode (True for development, False for production)
    # Set to "True" during development for detailed error messages, and "False" in production for security and performance
    DEBUG="True"

    # Secret key for Django (keep this secure!)
    # This is a critical setting, keep it secret and never expose it publicly
    SECRET_KEY="your_secret_key"

    # Enable Django's debug toolbar (optional)
    # Set to "True" to enable the Django Debug Toolbar for easier debugging during development
    ENABLE_DEBUG_TOOLBAR="True"

    # ---------------------------------------------------------------
    # Static and Media File Configuration
    # ---------------------------------------------------------------

    # Static files URL and root directory
    # URL where static files will be served from, relative to the site root
    STATIC_URL=static/
    # Path where static files will be stored after collection (useful when deploying)
    STATIC_ROOT=static

    # Media files URL and root directory
    # URL where media files (uploads) will be served from
    MEDIA_URL=/media/
    # Path where media files (uploads) will be stored on the server
    MEDIA_ROOT=media

    # ---------------------------------------------------------------
    # Host and Debugging IPs Configuration
    # ---------------------------------------------------------------

    # Allowed hosts for development (keep it simple)
    # These are the domains or IP addresses that Django will allow requests from
    ALLOWED_HOSTS=localhost,127.0.0.1

    # Internal IPs for Django Debug Toolbar and debugging
    # Defines which IPs can access the debug toolbar
    INTERNAL_IPS=127.0.0.1

    # ---------------------------------------------------------------
    # CORS (Cross-Origin Resource Sharing) Configuration
    # ---------------------------------------------------------------

    # Allow credentials (cookies, HTTP authentication, etc.) in CORS requests
    # Set to "True" if you want to allow credentials (e.g., cookies, HTTP headers) in CORS requests
    CORS_ALLOW_CREDENTIALS=True

    # List of allowed origins (comma-separated) that can make CORS requests to your API
    # CORS_ALLOWED_ORIGINS=https://example.com,https://another-example.com

    # List of allowed origins (comma-separated) that can make CORS requests to your API
    # Set this to the URLs of your frontend application(s)
    CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
    ```

5. **Database Setup**

    ```bash
    python manage.py migrate
    ```

6. **Create superuser (optional)**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```bash
    python manage.py runserver
    ```

## 🔐 Environment Variables

| Variable             | Description          | Default   |
| -------------------- | -------------------- | --------- |
| SECRET_KEY           | Django secret key    | Required  |
| DEBUG                | Debug mode flag      | False     |
| ALLOWED_HOSTS        | Allowed hosts list   | localhost |
| CORS_ALLOWED_ORIGINS | CORS allowed origins | None      |
| ENABLE_DEBUG_TOOLBAR | Enable debug toolbar | False     |
| STATIC_URL           | Static files URL     | static/   |
| MEDIA_URL            | Media files URL      | /media/   |

## 📚 API Documentation

A complete Postman collection is included in the repository (`Achare Auth API.postman_collection.json`). Import this collection into Postman to explore all available endpoints and their functionality.

### Main Endpoints

-   User Registration
-   Phone Number Verification
-   User Authentication
-   Profile Management
-   Password Management

## 🔒 Security Features

-   Phone number validation
-   Password validation rules
-   CORS protection
-   CSRF protection
-   Session security
-   Debug mode control

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

-   Initial work - [Your Name]

## 🙏 Acknowledgments

-   Django documentation
-   Django REST Framework documentation
-   Python community
