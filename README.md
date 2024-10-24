
# **Novaji Introserve**

## **Overview**

This is an assessment from Novaji Introserve

## **Prerequisites**

- `Python 3.11.3`
- `Django 5.1.1`
- `Django Rest Framework (DRF) 3.15.2`
- `SQLite or any other preferred database`


## **Installation**
Clone the Repository


git clone https://github.com/GbolahanAlaba/novaji

cd novaji


## **Create Virtual Environment**

It's recommended to use a virtual environment to manage dependencies:


`python -m venv venv`

## **Activate Virtual Environment**

MAC `source venv/bin/activate`

Windows `venv/Scripts/activate`

## **Install Dependencies**

Install the required dependencies using pip:

`pip install -r requirements.txt`


## **Run Migrations**

Apply the migrations to set up your database schema:

`python manage.py makemigrations`

`python manage.py migrate`


## **Run the Development Server**
Start the development server to verify everything is set up correctly:

`python manage.py runserver`
You should now be able to access the application at http://127.0.0.1:8000

## **API Endpoints**
Base URL - `http://127.0.0.1:8000`

- `POST /reg/register/`
- `GET /reg/get-registrations/`
- `POST /reg/update-registration/<str:reg_id>/`


## **API Implementation**

#### POST /register/

- **Request Body**:

  ```json
  {
    "phone_number": "09084848838",
    "mobile_network": "Airtel",
    "message": "Good network"
  }

- **Response**:

  ```json
  {
    "status": "success",
    "message": "Data registered successfully",
    "data": {
        "reg_id": "fd4241df-f185-4dac-98b6-1da38e5570ec",
        "phone_number": "090848488383",
        "mobile_network": "MTN",
        "ref_code": "q2YXI7Gs8sTvCk4a"
    }
  }

`201 Created` on registration.

`509 Internal Server Error` on server error.


#### GET /get-registrations/

- **Response**:

  ```json
  {
    "status": "success",
    "message": "Registered records",
    "data": [
        {
            "reg_id": "8ccb2d48-381c-4269-b7f2-8a0304b88302",
            "phone_number": "090848488383",
            "mobile_network": "MTN",
            "ref_code": "rakDDFA9OUr95zf0"
        },
        {
            "reg_id": "25349651-3a9d-47e8-a370-ed1951f127ce",
            "phone_number": "090848488383",
            "mobile_network": "MTN",
            "ref_code": "rakZDFA9OUr95zf4"
        },
    ]
  }

`200 Ok` on listing registrations.

`509 Internal Server Error` on server error.


#### PUT /update-registrations/

- **Request Body**:

  ```json
  {
    "phone_number": "09084848838",
    "mobile_network": "Airtel",
    "message": "Good network"
  }

- **Response**:

  ```json
  {
    "status": "success",
    "message": "Record updated",
    "data": {
        "reg_id": "8ccb2d48-381c-4269-b7f2-8a0304b88302",
        "phone_number": "090848488383",
        "mobile_network": "Airtel",
        "ref_code": "rakZDFA9OUr95zf0"
    }
  }

`200 Ok` on registration.

`509 Internal Server Error` on server error.

## **Testing**
Run a tests to ensure the API endpoints work as expected.

`py manage.py test`