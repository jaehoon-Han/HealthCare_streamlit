import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app_BMI import run_bmi
from app_map import run_map
from app_workout import run_workout

## URL 사용하여 이미지 띄우는 라이브러리
import requests
from io import BytesIO
from PIL import Image



def main():
 

    st.title('체력 자가진단 및 운동 추천 시스템')
    menu = ['Home', 'BMI', 'Recommend', "Today's Workout"]
    ##

 
    col1, col2 = st.columns(2)

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
                st.text('산책 및 스트레칭')
            elif age >= 40 : 
                st.text('간단한 운동')
            elif age >= 20 :
                st.text('고강도 운동')
            else :
                st.text('반복적인 활동')
   
            if age >= 65 :
                st.image('https://cdn.pixabay.com/photo/2018/07/22/05/16/person-3553814__340.jpg')
            elif age >= 40 :
                st.image('https://media.yourtrustrochdale.co.uk/wp-content/uploads/2020/09/15144104/iStock-1192307192-scaled-523x310.jpg')
            elif age >= 18 :
                st.image('https://cdn.pixabay.com/photo/2018/04/05/17/21/kettlebell-3293478__340.jpg')
            else :
                st.image('https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199__340.jpg')
   
    st.image('data/BMI_chart.jpg')

 
    df = pd.read_csv('data/exercise_dataset.csv')
    
    df.columns= ['운동종목', '60kg 이하', '60~70kg', '70~80kg','80kg 이상','시간당 칼로리 소모량' ]


    col3, col4 = st.columns(2)
    with col3 :
        st.dataframe(df)

    with col4 :
            excer_inter = st.text_input('관심있는 종목을 입력하세요')
            if excer_inter is not None :
                st.markdown('https://www.youtube.com/results?search_query={}'.format(excer_inter.replace(' ','+')))


   
    
    
    options = st.selectbox('운동 부위',['가슴','등','복근','팔','하체'])
    if options == '가슴' :
        st.image('data/part_workout_jpg/Chest.jpg')
    elif options == '등' :
        st.image('data/part_workout_jpg/Back.jpg')
    elif options == '복근' :
        st.image('data/part_workout_jpg/Abdominal.jpg')
    elif options == '팔' :
        st.image('data/part_workout_jpg/Triceps.jpg')
    elif options == '하체' :
        st.image('data/part_workout_jpg/Leg.jpg')
  
    
    





if __name__=='__main__' :
    main()
