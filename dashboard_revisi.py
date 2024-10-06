import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
data = pd.read_csv('C:\\Users\\REGI\\OneDrive - Universitas Diponegoro\\Dokumen\\UNDIP\\Semester 7\\Bangkit Academy\\Bike\\all_data.csv')

# Judul dashboard
st.title("Dashboard Penyewaan Sepeda")

# Menampilkian Dataframe
st.write("Dataset Penyewaan Sepeda")
st.dataframe(data.head())

# Menambahkan Sidebar untuk Filter Data
st.sidebar.header('Filter Data')

#Pilihan untuk filter suhu
temp_range = st.sidebar.slider('Range Suhu', float(data['temp'].min()), float(data['temp'].max()), (0.2, 0.8))

# Pilihan untuk filter kelembapan
hum_range = st.sidebar.slider('Range Kelembapan', float(data['hum'].min()), float(data['hum'].max()), (0.3, 0.7))

# Filter data berdasarkan pilihan suhu dan kelembapan
filtered_data = data[(data['temp'] >= temp_range[0]) & (data['temp'] <= temp_range[1]) & (data['hum'] >= hum_range[0]) & (data['hum'] <= hum_range[1])]

st.write(f"Data Tersaring dengan Suhu: {temp_range} dan Kelembapan: {hum_range}")
st.dataframe(filtered_data)

# Visualisasi Pengaruh Suhu Terhadap Penyewaan Sepeda
st.subheader('Pengaruh Suhu Terhadap Penyewaan Sepeda')
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=filtered_data, ax=ax, label='Total Penyewaan')
sns.scatterplot(x='temp', y='casual', data=filtered_data, ax=ax, label='Pengguna Biasa', color='blue')
sns.scatterplot(x='temp', y='registered', data=filtered_data, ax=ax, label='Pengguna Terdaftar', color='green')
plt.title('Pengaruh Suhu Terhadap Penyewaan Sepeda')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Visualisasi Pengaruh Kelembapan Terhadap Penyewaan Sepeda
st.subheader('Pengaruh Kelembapan Terhadap Penyewaan Sepeda')
fig, ax = plt.subplots()
sns.scatterplot(x='hum', y='cnt', data=filtered_data, ax=ax, label='Total Penyewaan')
sns.scatterplot(x='hum', y='casual', data=filtered_data, ax=ax, label='Pengguna Biasa', color='blue')
sns.scatterplot(x='hum', y='registered', data=filtered_data, ax=ax, label='Pengguna Terdaftar', color='green')
plt.title('Pengaruh Kelembapan Terhadap Penyewaan Sepeda')
plt.xlabel('Kelembapan')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Analisis Hari Libur
st.subheader('Pengaruh Hari Libur Terhadap Penyewaan Sepeda')
holiday_data = data.groupby('holiday').agg({'cnt':'sum'}).reset_index()

fig, ax = plt.subplots()
sns.barplot(x='holiday', y='cnt', data=holiday_data, ax=ax)
plt.title('Pengaruh Hari Libur Terhadap Total Penyewaan Sepeda')
plt.xlabel('Hari Libur')
plt.ylabel('Total Penyewaan')
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
- Conclution pertanyaan 1: Berdasarkan scatterplott yang telah dibuat, terlihat bahwa kenaikan temperature berkorelasi positif dengan jumlah sepeda yang disewa baik oleh casual user maupun registered user. Artinya temperature dapat mempengaruhi keinginan seseorang untuk menyewa sepeda, semakin naik temperature, maka jumlah penyewa sepeda akan semakin banyak, begitu juga sebaliknya. Pada scatterplot juga ditunjukkan bahwa humidity tidak memiliki korelasi terhadap jumlah penyewa sepeda. Artinya, tingkat humidity tidak akan mempengaruhi keinginan seseorang untuk menyewa sepeda.
- Conclution pertanyaan 2: Berdasarkan Barplot tersebut, terlihat bahwa bar yang menunjukkan jumlah penyewa sepeda pada hari libur lebih sedikit daripada selain hari libur. Artinya, orang-orang lebih banyak menyewa sepeda di hari selain hari libur dibandingkan hari libur. Hal ini bisa jadi disebabkan karena banyak orang yang menyewa sepeda untuk kebutuhan bekerja, sekolah atau aktivitas lainnya pada hari selain hari libur dan lebih memilih di rumah atau berlibur dengan transportasi lain pada hari libur.
""")