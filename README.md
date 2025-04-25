# Bookstore Management System

A full-stack Django application for managing a bookstore, including user authentication, book management, and shopping cart functionality.

## Features

- User authentication (login, registration, profile management)
- Book management (CRUD operations)
- Shopping cart functionality
- Responsive design with Bootstrap 5
- Docker support for easy deployment
- Jenkins integration for CI/CD

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL
- Redis (for caching)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bookstore.git
cd bookstore
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Docker Deployment

1. Build and run the containers:
```bash
docker-compose up --build
```

2. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

3. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Project Structure

```
bookstore/
├── books/              # Book management app
├── cart/               # Shopping cart app
├── users/              # User authentication app
├── bookstore/          # Project settings
├── static/             # Static files
│   ├── css/
│   └── js/
├── templates/          # HTML templates
├── media/              # User uploaded files
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker configuration
└── README.md          # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 