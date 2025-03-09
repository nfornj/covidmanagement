# COVID Management System

A comprehensive Django application for managing COVID-19 resources and vaccination information.

## Features

- **Resource Management**: Track and manage requests for plasma, oxygen, hospital beds, and other resources
- **Vaccination Centers**: Find vaccination centers and check vaccine availability
- **Real-time Updates**: Automated data fetching from CoWIN API
- **Filtering and Search**: Filter resources by type, location, and status

## Tech Stack

- **Backend**: Django 3.2
- **Database**: PostgreSQL
- **Task Queue**: Celery with Redis
- **API Integration**: CoWIN API for vaccination data
- **Containerization**: Docker and Docker Compose

## Setup and Installation

### Prerequisites

- Docker and Docker Compose
- Git

### Installation Steps

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/covidmanagement.git
   cd covidmanagement
   ```

2. Create a `.env` file from the example:
   ```
   cp .env.example .env
   ```
3. Update the `.env` file with your settings.

4. Build and start the containers:

   ```
   docker-compose up -d --build
   ```

5. Create a superuser:

   ```
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access the application:
   - Web interface: http://localhost:8000
   - Admin interface: http://localhost:8000/admin

## Project Structure

- `covidfeed/`: App for managing resource requests (plasma, oxygen, beds)
- `vaccination/`: App for vaccination center information
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `covidcryindia/`: Main project settings

## API Endpoints

- `/covidfeed/`: Resource requests dashboard
- `/vaccination/`: Vaccination centers dashboard
- `/vaccination/api/districts/<state_id>/`: Get districts for a state

## Development

### Running Migrations

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Running Tests

```
docker-compose exec web python manage.py test
```

### Celery Tasks

The application uses Celery for background tasks:

- `populate_states_and_districts`: Populates states and districts from CoWIN API
- `download_vaccination_data`: Downloads vaccination center data

## Deployment

For production deployment:

1. Update the `.env` file with production settings:

   - Set `DJANGO_DEBUG=False`
   - Set a strong `DJANGO_SECRET_KEY`
   - Update `DJANGO_ALLOWED_HOSTS` with your domain

2. Build and start the containers:
   ```
   docker-compose -f docker-compose.prod.yml up -d --build
   ```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- CoWIN API for vaccination data
- Django community for the excellent framework
