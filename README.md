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
    git clone [repository-url]
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

4. **Environment Setup**

    - Copy `.env.example` to `.env`
    - Configure your environment variables:
        - `SECRET_KEY`
        - `DEBUG`
        - `ALLOWED_HOSTS`
        - `CORS_ALLOWED_ORIGINS`
        - Other optional settings

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
