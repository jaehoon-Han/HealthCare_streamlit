import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def run_bmi() :
    gender = st.radio('성별을 선택하세요.', ['남자','여자'])
    

    age = st.slider('나이', 1,100)
    weight = int(st.slider('몸무게',30, 150))
    height = int(st.slider('키',100,210))

   
    if  st.button('BMI 측정하기') :
        BMI = round((weight)/(height/100)**2,1)
        if gender == '남자' :
            if BMI >= 30 :
                st.text('비만')
            elif BMI >= 25 :
                st.text('과체중')
            elif BMI >= 18.5 :
                st.text('정상')
            else :
                st.text('저체중')
        else :
            if BMI >= 25 :
                st.text('과체중')
            elif BMI >= 18.5 :
                st.text('정상')
            else :
                st.text('저체중')
        st.text(BMI)

        if age >= 60 :
            st.text('간단한 운동')
        elif age >= 40 : 
            st.text('배드민턴')
        elif age >= 15 :
            st.text('고강도 운동')
        else :
            st.text('놀아라')

   