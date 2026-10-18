from flask import Flask, request, jsonify
import joblib

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat model Gradient Boosting yang telah disimpan
joblib_model = joblib.load('gbr_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil data dari request JSON
    data = request.json['data'] 
    
    # Melakukan prediksi (harus dalam bentuk 2D array)
    prediction = joblib_model.predict(data) 
    
    # Mengembalikan hasil prediksi dalam bentuk JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)