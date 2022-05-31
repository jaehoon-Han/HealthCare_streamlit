import streamlit as st
import pandas as pd
import numpy as np



def run_workout() :   
   

    options = st.selectbox('운동 부위',['가슴','어깨','등','복근','팔','하체','엉덩이','전신','유산소'])
    if options == '가슴' :
        st.image('data/part_color/chest.png')
    elif options == '어깨' :
        st.image('data/part_color/shoulder.png')
    elif options == '등' :
        pass
    elif options == '복근' :
        pass
    elif options == '팔' :
        pass
    elif options == '하체' :
        pass
    elif options == '엉덩이' :
        pass
    elif options == '전신' :
        pass
    
    st.write('운동 부위', options)
    if options == '가슴' :
        st.image('https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199__340.jpg')
    elif options == '어깨' :
        pass
    elif options == '등' :
        pass
    elif options == '복근' :
        pass
    elif options == '팔' :
        pass
    elif options == '하체' :
        pass
    elif options == '엉덩이' :
        pass
    elif options == '전신' :
        pass
    
    