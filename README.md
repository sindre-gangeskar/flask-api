# Simple Flask API
This is a simple Flask API that provides api paths for authentication, and incredibly basic mathematical solutions.

I've learned the basics of middleware for Flask, and I've implemented an auth middleware that protects the mathematical routes, which requires a Bearer jwt token in the Authorization header to gain access.
The simplicity in adding a route's **"before request"** function to call my auth-check function gave me pure joy. 

Flask to me seems quite similar to Express.js in terms of how you can build your API routes, and I was able to recognize quite a bit even though I'm still not that great at Python and Flask. It's been a fun small project; I've learned a lot and I'll continue to develop projects with Flask to further improve my skills and knowledge.

## Authentication
The project reads from a super basic *users.json* file and if it finds a match; the password is compared between the one provided in the body and the user's password. A token is signed if it matches. I did it this way so I wouldn't have to hook up a database for such a simple API meant for learning purposes.

## Documentation
I was able to learn how to generate Swagger-based documentation with the **flasgger** package, The documentations were modeled with yml files, and the actual documentation can be reached at **/apidocs**. 

## Dependencies used
- **Flask**
- **PyJWT**
- **flasgger**
- **dotenv**

## Quickstart
This project utilizes **Python v3.14**  

### Clone project to local folder
Open an empty folder  
Clone the repo with ``` git clone https://github.com/sindre-gangeskar/flask-api.git .```

### Setup virtual environment
Create a virtual environment with ``` python -m venv venv```  
Activate the virtual environment with ``` venv\Scripts\activate ```

### Setup Environment Variable
Create a .env file in the root of the project, and add a JWT_SECRET variable. Use a strong random value; for example at least 16 random bytes (32 hex characters).  
If the **JWT_SECRET** variable isn't present in the .env file, the project will throw an error specifying such.

```JWT_SECRET=super_secret```

### Install dependencies
```pip install -r requirements.txt```

### Run dev server
```flask run --debug ```
