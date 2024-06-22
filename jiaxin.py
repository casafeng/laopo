import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import streamlit as st 
import time
import random 
from random import sample

# Main page configuration
st.set_page_config(
    page_title = '佳欣爱睡觉',
    page_icon = "🐰💤",
    layout = "wide",
    initial_sidebar_state = "collapsed",
    menu_items = {
        'Get Help': 'https://www.instagram.com/angelozhang_?igsh=cXd5eG1mNHgzeDFu&utm_source=qr',
        'Report a bug': "https://bere.al/casafeng",
        'About': "# 尊嘟假嘟!"
    }
)

st.title('_早上好老婆_ 🌹')
st.header('睡得好吗？')
st.subheader('一起玩游戏吧 👻', divider='grey')
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

st.markdown(

    """
    👈 Apri la barra laterale
    """
)

# Build Dashboard 
add_sidebar = st.sidebar.selectbox(
    'Scegli un gioco 🎮',
    (' ', '比大小 📊', '石头剪刀布 🆚', 'Quanto conosci bene 阿烽 🧐', 'Test della personalità 💭', '秘密'))



## Total Picture 

if add_sidebar == 'Quanto conosci bene 阿烽 🧐':

    st.title('Work in Progress 🚧')

elif add_sidebar == 'Test della personalità 💭':

    st.title('Work in Progress 🏗️')

elif add_sidebar == '比大小 📊':

    st.title('Work in Progress 🔜')

elif add_sidebar == '石头剪刀布 🆚':

    st.title('Work in Progress ⏳')

elif add_sidebar == '秘密':

    time.sleep(1)
    # st.write('READY!')
    time.sleep(1)
    # You can use a column just like st.sidebar:
    if st.button('Clicca'):
        st.write('你是傻逼 🐸')


    
