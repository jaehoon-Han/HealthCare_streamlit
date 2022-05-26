import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from app_BMI import run_bmi
from app_map import run_map

def main():

    st.title('체력 자가진단 및 운동 추천 시스템')
    menu = ['Home', 'BMI', 'Recommend']
    
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        st.balloons()
    elif choice == menu[1] :
        run_bmi()
    elif choice == menu[2] :
        run_map()



if __name__=='__main__' :
    main()
