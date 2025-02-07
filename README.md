# Number-Facts-API
 An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Overview
The **Number Classification API** is a Django REST API that classifies a given number based on its mathematical properties. It determines whether a number is prime, perfect, or an Armstrong number, calculates the sum of its digits, and provides a fun fact if applicable.

## Features
- Accepts a number as a query parameter in a GET request.
- Returns JSON responses with:
  - Whether the number is **prime**.
  - Whether the number is **perfect**.
  - The **sum of its digits**.
  - Identifies **Armstrong numbers**.
  - Classifies the number as **even or odd**.
  - Provides a **fun fact** about the number (if applicable).
- Returns proper HTTP status codes for success and errors.

## Technologies Used
- **Django** (Backend Framework)
- **Django REST Framework (DRF)** (API Development)
- **Python 3**

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/classify-number`.

## API Documentation

### **Endpoint:** Classify a Number
#### **GET** `/api/classify-number?number=<integer>`

#### **Request Example**
```bash
GET http://127.0.0.1:8000/api/classify-number?number=371
```

#### **Successful Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "digit_sum": 11,
    "properties": ["armstrong", "odd"],
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request - Invalid Input)**
```json
{
    "number": "alphabet",
    "error": true
}
```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
