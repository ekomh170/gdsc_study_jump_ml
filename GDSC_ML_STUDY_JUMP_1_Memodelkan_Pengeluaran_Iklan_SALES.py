# Study Jam Bisiness Case : Kita Mencoba Memodelkan Hubungan Antara Pengeluaran Iklan (Advertising Spend) dengan
# penjualan (Sales) suatu produk atau produk atau layanan. tujuannya adalah untuk menggunakan model regresi linear untuk
# memprediksi nilai penjualan berdasarkan besarnya pengeluaran iklan.

# import library yang di perlukan
# how to install sklearn
# Untuk Melakukan Regress
# Pengecekan Variabel

# Import library untuk regresi linear dan metrik evaluasi
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Import library untuk manipulasi data
import pandas as pd
import numpy as np

# Import library untuk statistik
from scipy import stats

# Import library untuk manipulasi data
sales = pd.Series([200000, 150000, 100000, 50000, 0, -50000])
ads_spend = pd.Series([8000, 12000, 16000, 20000, 24000, 28000])
sales

# Cek Data
ads_spend

# Cek Data
sales

# Persiapkan Data untuk Model: Bingung
# Berhubungan Dengan Statika
# Linear Regression Buat
# Pengeluaran pipfitter

# 1. Tahap Modelling
x = ads_spend.values.reshape(-1, 1)
y = sales.values.reshape(-1, 1)

# Inisialisasi dan Latih Model Regresi Linear:
model = LinearRegression()
model.fit(x, y)


# 2. Tahap Modelling
# Prediksi Penjualan Menggunakan Model:
predicted_sales = model.predict(x)

# 3. Tahap Modelling
mse = mean_squared_error(y, predicted_sales)
r2 = r2_score(y, predicted_sales)

print(f'Mean Squared Error (MSE) : {mse:.2f}')
print(f'R-Squared (Coefficient of Determination) : {r2:.2f}')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))
plt.scatter(x, y, color='red', label='Actual Sales')
plt.plot(x, predicted_sales, color='blue', label='Predicted Sales')
plt.xlabel('Advertising Spend')
plt.ylabel('Sales')
plt.title('Sales vs Advertising')
plt.legend()
plt.show()

# Study Jam Bisiness Case : Kita Mencoba Memodelkan Hubungan Antara Pengeluaran Iklan (Advertising Spend) dengan
# penjualan (Sales) suatu produk atau produk atau layanan. tujuannya adalah untuk menggunakan model regresi linear untuk
# memprediksi nilai penjualan berdasarkan besarnya pengeluaran iklan.