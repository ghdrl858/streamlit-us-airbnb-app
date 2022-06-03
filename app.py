import streamlit as st
import pandas as pd
from PIL import Image
from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from app_home import run_home
from app_info import run_info
from app_chart import run_chart
from app_ml import run_ml

def main() :

    st.title('')

    menu = ['Home', 'info', 'Chart', 'ML']
    
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == 'Home' :
        run_home()
    elif choice == 'Info':
        run_info()
    elif choice == 'Chart':
        run_chart()
    elif choice == 'ML':
        run_ml()
        
    # 이미지 구현
    # with st.sidebar :
    #     st.write('')
    #     st.write('')
    #     st.write('')
    #     st.write('')
    #     image = Image.open('image/dia.png')
    #     st.image(image, use_column_width=True)
    # 

if __name__ == '__main__' :
    main()