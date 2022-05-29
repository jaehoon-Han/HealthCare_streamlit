import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def run_bmi() :
    col1, col2, col3 = st.columns(3)

    with col1 :
        gender = st.radio('성별을 선택하세요.', ['남자','여자'])
        

        age = st.slider('나이', 6,100,25)
        weight = int(st.slider('몸무게',30, 150, 60))
        height = int(st.slider('키',100,210, 170))

    with col2 :
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
   
            if age >= 65 :
                st.image('https://cdn.pixabay.com/photo/2018/07/22/05/16/person-3553814__340.jpg')
            elif age >= 18 :
                st.image('https://cdn.pixabay.com/photo/2018/04/05/17/21/kettlebell-3293478__340.jpg')
            else :
                st.image('https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199__340.jpg')
    with col3 :
        if age >= 60 :
            st.text('''60세 이상 노인은 여가시간과 이동시간을 활용한 운동이나 집안일, 스포츠 등을 매일 하는것이 좋습니다.
            운동을 통해 심폐능력, 근육, 뼈 등의 건강기능을 강화시킬 수 있으며
            비 전염성질병, 우울증, 인지력 하락도 방지됩니다.
            일주일에 적어도 150분 중간 강도의, 또는 75분 가량의 격렬한 강도의 유산소운동을 합니다.''')
    st.image('data/BMI_chart.jpg')
   