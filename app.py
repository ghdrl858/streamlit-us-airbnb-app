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
    
    menu = ['Home', 'Info', 'Chart', 'ML']

    choice = st.sidebar.radio('Choice Menu', menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_info()
    elif choice == menu[2] :
        run_chart()
    elif choice == menu[3] :
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