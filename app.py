#database connection
from flask import app
import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='local_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    return conn

#add member
@app.route('/members', methods=['POST'])
def add_member():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Members (name, age, gender) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['name'], data['age'], data['gender']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Member added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#retrieve member
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        member = cursor.fetchone()
        cursor.close()
        conn.close()
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#update member
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE Members SET name = %s, age = %s, gender = %s WHERE id = %s"
        cursor.execute(query, (data['name'], data['age'], data['gender'], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Member updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#delete member
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Member deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#task2
#schedule workout session
@app.route('/workouts', methods=['POST'])
def add_workout_session():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO WorkoutSessions (member_id, session_date, activity) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['member_id'], data['session_date'], data['activity']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Workout session added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#update workout sessions
@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout_session(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE WorkoutSessions SET session_date = %s, activity = %s WHERE id = %s"
        cursor.execute(query, (data['session_date'], data['activity'], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Workout session updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#view all workout sessions
@app.route('/members/<int:id>/workouts', methods=['GET'])
def get_member_workouts(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
        cursor.execute(query, (id,))
        sessions = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(sessions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


