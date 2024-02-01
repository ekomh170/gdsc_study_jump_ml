import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

# -> Churn
# -> Tujuan Mencari Tau Penyebab Masalah Bedasarkan
# -> Orang Yang Keluat Dari Aplikasi Kalian
df = pd.read_csv("churn.csv")
df

# Melakukan Cek Data
df.info()

# Melakukan Cek Data Perbandingan (20% Nasabah Keluar Dari Aplikasi)
sns.countplot(x='Exited', data=df)
plt.title('Distribution of Churn (Exited)')
plt.show()


numeric_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
df[numeric_features].hist(bins=20, figsize=(15,10))
plt.suptitle('Distribution of Number Features')
plt.show()