from flask import Flask, request, jsonify,render_template
import psycopg2
import bcrypt
import os
import socket
import jwt
import base64
import datetime
app = Flask(__name__)

# Database connection details (Update as needed)
DB_HOST = os.getenv("DB_HOST")  
DB_NAME = os.getenv("DB_NAME")  
DB_USER = os.getenv("DB_USER")  
DB_PASS = os.getenv("DB_PASS")  

SECRET_KEY = os.getenv("SECRET_KEY") 


# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# Regular root endpoint
@app.route('/api', methods=['POST'])
def api():
    # Get the container's hostname
    container_name = socket.gethostname()
    
    # Return a welcome message with the container's name
    return f"Welcome! You are running Flask on Docker container: {container_name}"

@app.route('/api/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get("UserName")
        email = data.get("email")
        password = data.get("pwd")

        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        # Hash the password
        hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insert into PostgreSQL
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (UserName, pwd, email) VALUES (%s, %s, %s)", (username, hashed_pwd, email))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Fetch all users but exclude passwords for security
        cur.execute("SELECT id, UserName, email, date_created FROM users")
        users = cur.fetchall()

        cur.close()
        conn.close()

        # Convert query result into JSON format
        user_list = []
        for user in users:
            user_list.append({
                "id": user[0],
                "UserName": user[1],
                "email": user[2],
                "date_created": user[3].strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp
            })

        return jsonify(user_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/login', methods=['POST'])
def login():
    try:
        # Get the Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith("Basic "):
            return jsonify({"error": "Authorization header missing or invalid format"}), 400

        # Extract the base64-encoded username:password
        base64_credentials = auth_header.split(" ")[1]
        
        # Decode base64 to get username:password
        decoded_credentials = base64.b64decode(base64_credentials).decode('utf-8')
        username, password = decoded_credentials.split(":")

        # Case insensitive username match
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Check if user exists (username is case-insensitive)
        cur.execute("SELECT id, UserName, pwd FROM users WHERE LOWER(UserName) = LOWER(%s)", (username,))
        user = cur.fetchone()
        
        if not user:
            return jsonify({"error": "Invalid username or password"}), 401
        
        # Compare hashed password
        stored_hashed_password = user[2]
        if not bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            return jsonify({"error": "Invalid username or password"}), 401
        
        # Create JWT token if credentials are valid
        payload = {
            "user": username,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500    
@app.route('/')
def index():
    # Get the container's hostname
    container_name = socket.gethostname()

    # Render an HTML page
    return render_template('index.html', container_name=container_name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

@app.route('/users', methods=['GET'])
def users_page():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
