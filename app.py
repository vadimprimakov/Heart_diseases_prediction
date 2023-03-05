import streamlit as st

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
if gender == 'M':
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

if st.button("Рассчитать вероятность"):
    y_pr = model.predict_proba([[age, imt, ap_hi, ap_lo, gender, gluc, cholesterol, smoke, alco, active]])[:,1]
    st.success('Вероятность риска развития сердечно-сосудистого заболевания составляет {}'.format(y_pr))
    st.image('output.png')
    st.subheader('Ваши результаты могут улушиться, если вы обратите внимание на ваше давление, уровень холестерина и индекс массы тела')



st.markdown("Больше проектов в профиле [GitHub](https://github.com/vadimprimakov)")