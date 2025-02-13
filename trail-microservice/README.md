# Trail Microservice

This project is a microservice for managing trails, implemented in Python using Flask. It provides a RESTful API for performing CRUD operations on trails, which consist of a series of location points owned by users. The data is stored in a Microsoft SQL Server database.

## Project Structure

```
trail-microservice/
├── Dockerfile/
│   └── Docker
├── src/
│   ├── __pycache__/
│   ├── .dockerignore
│   ├── app.py
│   ├── controllers/
│   │   ├── __pycache__/
│   │   └── trail_controller.py
│   ├── database_test.py
│   ├── database.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── models/
│   │   ├── __pycache__/
│   │   ├── trail_model.py
│   │   └── user_model.py
│   ├── README.md
│   ├── requirements.txt
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   └── trail_routes.py
│   ├── services/
│   │   ├── __pycache__/
│   │   └── trail_service.py
│   ├── templates/
│   │   └── index.html
│   └── utils/
│       ├── __pycache__/
│       ├── auth.py
│       └── security.py
└── SQLQuery_1.sql                     # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/HBizzy/COMP2001-Report
   cd trail-microservice
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure the database connection:**
   Update the database connection settings in `src/app.py` to point to your Microsoft SQL Server instance.

4. **Run the microservice:**
   ```
   python src/app.py
   ```

5. **Using Docker:**
   To build and run the microservice using Docker, execute:
   ```
   docker-compose up --build
   docker run -p 5000:5000 my-flask-app
   ```
6. **Login Token**
   To get the token need to run this in command prompt 
   ```
   curl -X POST http://localhost:5000/login -u grace@plymouth.ac.uk:ISAD123!
   ```

## API Endpoints
- ""POST /login**: Login in and recieve token.
- **GET /trails**: Retrieve a list of all trails.
- **GET /trails/{id}**: Retrieve a specific trail by ID.
- **POST /trails**: Create a new trail.
- **PUT /trails/{id}**: Update an existing trail.
- **DELETE /trails/{id}**: Delete a trail by ID.

## Security Considerations

This microservice implements measures to mitigate common vulnerabilities as outlined by the OWASP Top 10. Ensure to validate inputs and handle authentication and authorization appropriately.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
