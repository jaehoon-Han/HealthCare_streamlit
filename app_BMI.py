import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def run_bmi() :
    st.radio('성별을 선택하세요.', ['남자','여자'])
    

    age = st.slider('나이', 1,100)
    weight = int(st.slider('몸무게',30, 150))
    height = int(st.slider('키',100,210))

   
    if  st.button('BMI 측정하기') :
        BMI = round((weight)/(height/100)**2,1)
        if BMI > 25 :
            st.text('비만입니다.')
        st.text(BMI)
   