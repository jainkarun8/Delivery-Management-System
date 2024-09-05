# Delivery Management System

## Description

A Django-based Delivery Management System that handles vehicle and issue management, including calculation of final prices based on vehicle issues.

## Features

- Manage vehicles and components
- Track issues and their costs
- Calculate the final price based on issues associated with a vehicle

## Installation

### Prerequisites

- Python 3.12 or later
- Django 5.1 or later

### Steps to Set Up

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/jainkarun8/Delivery-Management-System.git
   ```

2. **Create a Virtual Environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**

   ```sh
   python manage.py migrate
   ```

6. **Run the Development Server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the Application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage

### API Endpoints

- **Calculate Final Price**

  - **URL:** `/calculate-price/<vehicle_id>/`
  - **Method:** `GET`

### Admin Interface

You can access the Django admin interface at `http://127.0.0.1:8000/admin/` to manage vehicles, components, and issues.
In my case
username asus
password karun

## Testing
Running Tests
To ensure everything is working correctly, run the tests using the following command:

python manage.py test

Test Cases
Test Vehicle Price Calculation: Validates the calculation of the total price based on issues associated with a vehicle.
Test Issue Management: Ensures that issues can be created, updated, and associated with vehicles and components correctly.

## Screenshots

![Screenshot (684)](https://github.com/user-attachments/assets/d0ecfe97-2ffb-487a-8c5a-b00660635ae5)
![Screenshot (685)](https://github.com/user-attachments/assets/59a3f7e5-5bce-4537-9f2f-0b15521e5604)
![Screenshot (686)](https://github.com/user-attachments/assets/04d07393-0812-4b56-bb3b-e2a37cd5f864)
![Screenshot (687)](https://github.com/user-attachments/assets/0d733c81-ef47-4f02-938c-e6198881392e)
![Screenshot (688)](https://github.com/user-attachments/assets/922fec91-ca63-4825-a5a4-48959f0a22ca)
![Screenshot (689)](https://github.com/user-attachments/assets/be19a556-d981-4d9f-bd1b-19d8772a9adf)

