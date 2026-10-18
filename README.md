# Student Performance Preprocessing and Modeling

Repositori ini memuat implementasi *end-to-end machine learning pipeline* untuk memprediksi nilai ujian siswa (*student exam score prediction*). Proyek ini berfokus pada tahapan komprehensif penyiapan data (*data cleaning*, penanganan pencilan, standardisasi, dan *encoding*), analisis eksploratif (EDA & ExDA), perbandingan performa algoritma regresi (LARS, Linear Regression, dan Gradient Boosting Regressor), hingga pembuatan simulasi REST API sederhana menggunakan Flask untuk *deployment* model.

## Ringkasan Proyek

* **Tipe Masalah:** Regresi Nilai Kontinu (*Tabular Data*)
* **Dataset:** Student Performance Factors (~6.600 baris total)
* **Target Variabel:** `Exam_Score`
* **Algoritma yang Diuji:** 
  * Least Angle Regression (LARS)
  * Linear Regression (OLS)
  * Gradient Boosting Regressor (GBR)
* **Metrik Evaluasi:** Mean Absolute Error (MAE), Mean Squared Error (MSE), R² Score
* **Format Penyimpanan Model:** `.joblib` & `.pkl`

## Pustaka & Lingkungan Komputasi

* **Bahasa:** Python 3.x
* **Lingkungan Kerja:** Jupyter Notebook (VS Code)
* **Pengolahan & Analisis Data:** Pandas, NumPy
* **Visualisasi:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn
* **Serialisasi Objek & Deployment:** Joblib, Pickle, Flask

## Struktur Repositori

```text
student-performance-factors/
├── dataset/
│   └── StudentPerformanceFactors.csv   # Data mentah
├── models/
│   ├── gbr_model.joblib                # Serialisasi model GBR (Joblib)
│   └── gbr_model.pkl                   # Serialisasi model GBR (Pickle)
├── deployment/
│   ├── gbr_model.joblib                # Model siap pakai untuk API
│   ├── testing_deploy.py               # Script server Flask API
│   └── data.json                       # Contoh data input untuk prediksi
├── praktikum.ipynb                     # Notebook alur kerja lengkap
└── README.md
