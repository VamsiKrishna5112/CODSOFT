from flask import Flask, request, jsonify, render_template, send_file
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename
import base64
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load pre-trained Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_faces(image):
    """Detect faces in an image"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces with optimized parameters
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        maxSize=(500, 500)
    )
    
    return faces, gray, image

def draw_faces(image, faces):
    """Draw rectangles around detected faces"""
    image_with_faces = image.copy()
    
    for (x, y, w, h) in faces:
        # Draw rectangle
        cv2.rectangle(image_with_faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Add label
        cv2.putText(
            image_with_faces,
            'Face',
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )
    
    return image_with_faces

def image_to_base64(image):
    """Convert OpenCV image to base64 string"""
    _, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer).decode()
    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    """Detect faces in uploaded image or base64 data"""
    try:
        data = request.json
        
        if 'image' not in data:
            return jsonify({'error': 'No image provided'}), 400
        
        # Decode base64 image
        image_data = data['image'].split(',')[1] if ',' in data['image'] else data['image']
        nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({'error': 'Invalid image'}), 400
        
        # Detect faces
        faces, gray, original = detect_faces(image)
        
        # Draw faces
        result_image = draw_faces(image, faces)
        
        # Convert to base64
        result_base64 = image_to_base64(result_image)
        
        return jsonify({
            'success': True,
            'faces_detected': len(faces),
            'image': f'data:image/jpeg;base64,{result_base64}',
            'face_count': len(faces),
            'message': f'Detected {len(faces)} face(s)!' if len(faces) > 0 else 'No faces detected'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload for face detection"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file:
            # Read file
            file_bytes = np.frombuffer(file.read(), np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            
            if image is None:
                return jsonify({'error': 'Invalid image file'}), 400
            
            # Detect faces
            faces, gray, original = detect_faces(image)
            
            # Draw faces
            result_image = draw_faces(image, faces)
            
            # Convert to base64
            result_base64 = image_to_base64(result_image)
            
            return jsonify({
                'success': True,
                'faces_detected': len(faces),
                'image': f'data:image/jpeg;base64,{result_base64}',
                'face_count': len(faces),
                'message': f'Detected {len(faces)} face(s)!' if len(faces) > 0 else 'No faces detected'
            })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/webcam', methods=['POST'])
def webcam_detect():
    """Handle webcam frame for face detection"""
    try:
        data = request.json
        
        if 'frame' not in data:
            return jsonify({'error': 'No frame provided'}), 400
        
        # Decode base64 frame
        frame_data = data['frame'].split(',')[1] if ',' in data['frame'] else data['frame']
        nparr = np.frombuffer(base64.b64decode(frame_data), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return jsonify({'error': 'Invalid frame'}), 400
        
        # Detect faces
        faces, gray, original = detect_faces(frame)
        
        # Draw faces
        result_frame = draw_faces(frame, faces)
        
        # Convert to base64
        result_base64 = image_to_base64(result_frame)
        
        return jsonify({
            'success': True,
            'faces_detected': len(faces),
            'frame': f'data:image/jpeg;base64,{result_base64}',
            'face_count': len(faces)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'face_cascade': face_cascade.empty() == False
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
