import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from app_BMI import run_bmi
from app_map import run_map
from app_workout import run_workout
st.set_page_config(layout="wide")

def main():

    st.title('체력 자가진단 및 운동 추천 시스템')
    menu = ['Home', 'BMI', 'Recommend', "Today's Workout"]
    
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        pass
    elif choice == menu[1] :
        run_bmi()
    elif choice == menu[2] :
        run_map()
    elif choice == menu[3] :
        run_workout()



if __name__=='__main__' :
    main()
