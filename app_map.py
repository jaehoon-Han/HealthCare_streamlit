import streamlit as st
import pandas as pd
import numpy as np

def run_map() :
    df = pd.read_csv('data/exercise_dataset.csv')
    
    df.columns= ['운동종목', '60kg 이하', '60~70kg', '70~80kg','80kg 이상','시간당 칼로리 소모량' ]

    st.dataframe(df)

    
    excer_inter = st.text_input('관심있는 종목을 입력하세요')
    if excer_inter is not None :
            st.markdown('https://www.youtube.com/results?search_query={}'.format(excer_inter.replace(' ','+')))