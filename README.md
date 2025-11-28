# Flight Routes System

## Project Overview

The Flight Routes System is a Django-based web application to manage airports and flight routes. It allows administrators to:

* Add and manage airports
* Add and manage flight routes with positions (Left/Right) and durations
* View shortest and longest routes
* Display the latest added routes
* Visualize key metrics on a dynamic dashboard

## Features

### Dashboard
* Total number of airports
* Total number of routes
* Longest route by duration
* Shortest route by duration
* Latest 5 added routes

### Airport Management
* Add and edit airports
* Unique airport codes (3-letter)

### Route Management
* Add and edit routes between airports
* Route positions (Left / Right)
* Track duration for each route

### Shortest/Longest Route
* Shortest route between two airports
* Longest direct route

## Installation & Setup

### Prerequisites
* Python 3.10+
* Django 4.x
* SQLite

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/amal-dev-01/flight_routes.git
cd flight_routes
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. **Access the dashboard**

Open http://127.0.0.1:8000/

## Views / Functionalities

* **Dashboard View**: Displays total airports, routes, longest and shortest routes, latest 5 routes
* **Shortest Route Finder**: Computes shortest path between two airports (direct)
* **Longest Route Finder**: Finds route with maximum duration
* **Airport & Route CRUD**: Manage airports and routes from Django Admin or custom views

## Technologies Used

* Python 3.10+
* Django 4.x
* Bootstrap 5 (frontend)
* SQLite
* Font Awesome (icons)

## Contact

**Developer**: Amal Dev  
**Email**: devmpamal@gmail.com 
**GitHub**: https://github.com/amal-dev-01/

---
