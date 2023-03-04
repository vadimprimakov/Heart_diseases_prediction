import streamlit as st

import pickle
from pickle import dump, load
st.image('heart.jpeg')
st.title('Рассчитайте вероятность риска развития сердечно-сосудистого заболевания')
st.subheader('Введите данные о вашем образе жизни')
age = st.slider('Возраст, лет', 0, 100, key='age') 
height = st.slider('Рост, см', 100, 220, key='height')
weight = st.slider('Вес, кг', 30, 400, key='weight')
ap_hi = st.slider('Верхнее давление', 70, 300, key='ap_hi')
ap_lo = st.slider('Верхнее давление', 20, 180, key='ap_lo')
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


#age *365
#imt вес//(рост/100)^2.int
#gender 1 и 2
#smoke 1 и 0
#alco 1 и 0
#active 1 и 0

if st.button("Рассчитать вероятность"):
        y_pr = model.predict_proba([[age, imt, ap_hi, ap_lo, gender, gluc, cholesterol, smoke, alco, active]])[:,1]
    st.success('The output is {}'.format(y_pr))


st.markdown("Больше проектов в профиле [GitHub](https://github.com/vadimprimakov)")