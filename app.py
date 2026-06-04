from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json
from datetime import datetime

app = Flask(__name__)

CLASS_NAMES_3 = {
    0: "Polusi Tinggi",
    1: "Polusi Rendah",
    2: "Polusi Sedang"
}

# Load the model
model_path = 'model/model_air.h5'
model = None
total_layers = 0
total_params = 0

# Try loading the model globally if it exists
if os.path.exists(model_path):
    try:
        model = load_model(model_path)
        # Dynamically fetch layer count and parameter count from the model file
        total_layers = len(model.layers)
        total_params = model.count_params()
    except Exception as e:
        print("Error loading model initially:", e)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DB_FILE = 'predictions.json'
METADATA_FILE = 'model/model_metadata.json'

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def migrate_history(history):
    updated = False
    for record in history:
        if record.get('prediction') == "Air Bersih":
            record['prediction'] = "Polusi Rendah"
            updated = True
        elif record.get('prediction') == "Air Kotor":
            record['prediction'] = "Polusi Tinggi"
            updated = True
    if updated:
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(history, f, indent=4)
        except Exception as e:
            print("Error saving migrated history:", e)
    return history

def get_history():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return migrate_history(data)
        except Exception as e:
            print("Error loading history:", e)
            return []
    return []

def get_model_metadata():
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("Error loading metadata:", e)
    return {}

def save_prediction(filename, prediction, confidence):
    history = get_history()
    new_record = {
        'filename': filename,
        'prediction': prediction,
        'confidence': float(confidence),
        'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }
    history.append(new_record)
    if len(history) > 100:
        history = history[-100:]
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print("Error saving prediction:", e)

@app.route('/')
def index():
    metadata = get_model_metadata()
    model_loaded = (model is not None)
    return render_template(
        'index.html',
        total_layers=total_layers,
        total_params=total_params,
        model_metadata=metadata,
        model_loaded=model_loaded
    )

@app.route('/analisis', methods=['GET', 'POST'])
def analisis():
    prediction = None
    confidence = None
    uploaded_filename = None
    model_loaded = (model is not None)

    if request.method == 'POST' and model_loaded:
        file = request.files.get('image')
        if file and file.filename != '':
            filepath = os.path.join(
                app.config['UPLOAD_FOLDER'],
                file.filename
            )
            file.save(filepath)
            uploaded_filename = file.filename

            img = image.load_img(
                filepath,
                target_size=(299,299)
            )

            img_array = image.img_to_array(img)
            img_array = img_array / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            pred = model.predict(img_array)

            if pred.shape[1] == 3:
                class_idx = np.argmax(pred[0])
                prediction = CLASS_NAMES_3.get(class_idx, "Tidak Diketahui")
                confidence = float(pred[0][class_idx] * 100)
            else:
                if pred[0][0] > 0.5:
                    prediction = "Polusi Tinggi"
                    confidence = float(pred[0][0] * 100)
                else:
                    prediction = "Polusi Rendah"
                    confidence = float((1 - pred[0][0]) * 100)
            
            save_prediction(file.filename, prediction, confidence)

    # Get predictions and model metrics
    history = get_history()
    metadata = get_model_metadata()

    # User prediction stats
    total_predictions = len(history)
    total_low = sum(1 for r in history if r['prediction'] == 'Polusi Rendah')
    total_mid = sum(1 for r in history if r['prediction'] == 'Polusi Sedang')
    total_high = sum(1 for r in history if r['prediction'] == 'Polusi Tinggi')
    avg_confidence = np.mean([r['confidence'] for r in history]) if history else 0.0

    return render_template(
        'analisis.html',
        prediction=prediction,
        confidence=confidence,
        uploaded_filename=uploaded_filename,
        history=history,
        total_predictions=total_predictions,
        total_low=total_low,
        total_mid=total_mid,
        total_high=total_high,
        avg_confidence=round(avg_confidence, 2),
        total_layers=total_layers,
        total_params=total_params,
        model_metadata=metadata,
        model_loaded=model_loaded
    )

@app.route('/reset', methods=['POST'])
def reset():
    if os.path.exists(DB_FILE):
        try:
            os.remove(DB_FILE)
        except Exception as e:
            print("Error deleting history:", e)
    return redirect(url_for('analisis'))

@app.route('/performa')
def performa():
    metadata = get_model_metadata()
    model_loaded = (model is not None)
    return render_template(
        'performa.html',
        total_layers=total_layers,
        total_params=total_params,
        model_metadata=metadata,
        model_loaded=model_loaded
    )



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)