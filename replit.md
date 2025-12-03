# Bread Van App - Replit Setup

## Project Overview
This is a Flask-based API application for managing bread delivery routes with three user roles: Admin, Driver, and Resident. The application is API-only (no UI) and implements the Observer design pattern for notifications.

## Architecture
- **Backend**: Flask framework with Python 3.11
- **Database**: SQLite (development) with SQLAlchemy ORM
- **API Only**: No frontend templates, designed for API consumption
- **Authentication**: Flask-JWT-Extended with token-based auth
- **Design Pattern**: Observer pattern (Driver=Subject, Resident=Observer) for notifications

## Design Patterns
### Observer Pattern Implementation
- **Subject**: Driver model - notifies observers when drives are scheduled/cancelled
- **Observer**: Resident model - receives notifications about drive changes
- **Models contain**: Data definitions + Observer pattern implementation only
- **Controllers contain**: All business logic

## Current Configuration

### Development Environment
- **Host**: 0.0.0.0 (configured for Replit proxy)
- **Port**: 5000 
- **Database**: SQLite (temp-database.db)
- **Debug Mode**: Enabled in development
- **Workflow**: Flask development server configured and running

### Deployment Configuration
- **Target**: Autoscale deployment
- **Production Server**: Gunicorn with reuse-port
- **Command**: `gunicorn --bind=0.0.0.0:5000 --reuse-port wsgi:app`

## User Roles & Features

### Admin
- Create and delete drivers
- View all areas and streets
- Manage inventory items

### Driver
- Schedule and cancel drives
- View and manage stops
- Start and end drives
- Update stock/inventory

### Resident
- Request and cancel stops
- View driver stats and stock
- Receive notifications (via Observer pattern)
- View inbox

## API Endpoints
- `/api/auth/` - Authentication endpoints (login, logout)
- `/api/admin/` - Admin management endpoints
- `/api/driver/` - Driver route management
- `/api/resident/` - Resident stop requests
- `/areas` - View all areas
- `/streets` - View streets (optional filter by area_id)
- `/streets/<id>/drives` - View drives for a street

## Project Structure
- `App/` - Main application package
  - `controllers/` - Business logic (user, admin, driver, resident)
  - `models/` - Data models + Observer pattern (User, Admin, Driver, Resident, Area, Street, Drive, Stop)
  - `views/` - API route definitions
  - `api/` - Security utilities
- `wsgi.py` - WSGI application entry point
- `requirements.txt` - Python dependencies

## Available Commands
- `flask init` - Initialize database
- `flask run --host 0.0.0.0 --port 5000` - Start development server
- `flask user create <username> <password>` - Create user
- `flask user list` - List users

## Status
✅ All dependencies installed
✅ Database initialized
✅ Flask configured for Replit environment
✅ Workflow running on port 5000
✅ Deployment configuration set
✅ API-only application (no UI)
✅ Observer pattern preserved in models
✅ Business logic separated into controllers

## Recent Changes (December 3, 2025)
- Converted to API-only application (removed templates/static folders)
- Refactored business logic from models to controllers:
  - User controller: login, logout functionality
  - Admin controller: driver management, area/street viewing
  - Driver controller: drive scheduling, stock management, stop viewing
  - Resident controller: stop requests, notifications, inbox
- Preserved Observer pattern in models (Driver=Subject, Resident=Observer)
- Removed empty controller files (area.py, street.py, drive.py, stop.py)
- Updated common_views.py to use admin controller imports
- Updated controllers __init__.py with all exports

## User Preferences
- API-only application, no UI components
- Observer pattern must remain in models
- Business logic should be in controllers, not models
- Clean separation of concerns
