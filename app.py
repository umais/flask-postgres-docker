from flask import Flask, request, jsonify
import psycopg2
import bcrypt
import os
import socket

app = Flask(__name__)

# Database connection details (Update as needed)
DB_HOST = os.getenv("DB_HOST")  
DB_NAME = os.getenv("DB_NAME")  
DB_USER = os.getenv("DB_USER")  
DB_PASS = os.getenv("DB_PASS")  

# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# Regular root endpoint
@app.route('/')
def index():
    # Get the container's hostname
    container_name = socket.gethostname()
    
    # Return a welcome message with the container's name
    return f"Welcome! You are running Flask on Docker container: {container_name}"

@app.route('/register', methods=['POST'])
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
    
@app.route('/users', methods=['GET'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
