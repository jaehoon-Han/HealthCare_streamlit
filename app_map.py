import streamlit as st
import pandas as pd
import numpy as np
import googlemaps
def run_map() :
    df = pd.DataFrame(
        np.random.randn(1000,2) / [50, 50] + [37.76, -122.4],
        columns = ['lat', 'lon'])

    gmaps_key = 'AIzaSyAC9bK-fOBY_JcKs9uhH4hiCiIv0O9aEJY'
    gmaps = googlemaps.Client(key=gmaps_key)
    gg = gmaps.geocode('헬스장', language='ko')
    st.dataframe(gg)    