import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
from pickle import dump, load
st.image('heart.jpeg')
st.title('Рассчитайте вероятность риска развития сердечно-сосудистого заболевания')
st.subheader('Введите данные о вашем образе жизни')
age = st.number_input('Возраст, лет', 0, 100, key='age') 
height = st.number_input('Рост, см', 100, 220, key='height')
weight = st.number_input('Вес, кг', 30, 400, key='weight')
ap_hi = st.number_input('Верхнее давление', 70, 300, key='ap_hi')
ap_lo = st.number_input('Нижнее давление', 20, 180, key='ap_lo')
gender = st.radio("Выберите ваш пол", options=("М", "Ж"), key='gender')
gluc = st.radio("Ваш уровень сахара", options=("1", "2", "3"), key='gluc')
cholesterol = st.radio("Ваш уровень холестерина", options=("1", "2", "3"), key='cholesterol')
smoke = st.radio("Вы курите", options=("Да", "Нет"), key='smoke')
alco = st.radio("Вы алкоголик", options=("Да", "Нет"), key='alco')
active = st.radio("Вы занимаетесь спортом", options=("Да", "Нет"), key='active')


def load():
    with open('/Users/vadimprimakov/Documents/Yandex_practicum/Heart_diseases_prediction/model_rfс.pkl', 'rb') as fid:
        return pickle.load(fid)
model = load()


age = age * 365
imt = weight // (height/100)**2
if gender == "М":
    gender = 1
else:
    gender = 2
if smoke == 'Да':
    smoke = 1
else: 
    smoke = 0
if alco == 'Да':
    alco = 1
else:
    alco = 0
if active == 'Да':
    active = 1
else:
    active = '0'
#data = [{'age': age, 'gender': gender, 'ap_hi': ap_hi, 'ap_lo': ap_lo, 'cholesterol': cholesterol, 'gluc':  gluc, 'smoke': smoke, 'alco': alco, 'active': active, 'imt': imt}]
#df = st.dataframe(data)
#df_scale = pd.DataFrame(data)
#numeric = ['age', 'gender', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'imt']
#scaler = StandardScaler()
#scaler.fit(df_scale[numeric])
#df_scale[numeric] = scaler.transform(df_scale[numeric])

if st.button("Рассчитать вероятность"):
    y_pr = model.predict_proba([[age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, imt]])[:,1]
    #y_pr = model.predict_proba(df_scale)[:,1]
    y_pr = y_pr[0]
    st.success(f'Вероятность риска развития сердечно-сосудистого заболевания составляет {y_pr : 0.0%}')
    st.image('output.png')
    st.subheader('Ваши результаты могут улушиться, если вы обратите внимание на ваше давление, уровень холестерина и индекс массы тела')


st.markdown("Больше проектов в профиле [GitHub](https://github.com/vadimprimakov)")