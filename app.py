from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import threading
import time
import subprocess
import uuid

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def fine_tune_model(file_path, job_id):
    # Placeholder for the modified fine-tune.py execution
    # Simulate fine-tuning progress
    for progress in range(1, 101):
        time.sleep(0.1)  # Simulate work being done
        socketio.emit('progress', {'job_id': job_id, 'progress': progress}, namespace='/fine-tuning')
    # Here you would call subprocess to run fine-tune.py and track progress

@app.route('/start-fine-tuning', methods=['POST'])
def start_fine_tuning():
    file = request.files['file']
    # Ensure the uploads directory exists or create it
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)
    job_id = str(uuid.uuid4())  # Generate a truly unique job ID
    threading.Thread(target=fine_tune_model, args=(file_path, job_id)).start()
    return jsonify({"message": "Fine-tuning started", "job_id": job_id})

@socketio.on('connect', namespace='/fine-tuning')
def test_connect():
    emit('response', {'message': 'Connected to fine-tuning'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
