import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
from app_home import run_home
from app_info import run_info
from app_chart import run_chart
from app_ml import run_ml

def main() :
    st.set_page_config(
     page_title="US_AirBNB",
     page_icon="✈️",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/ghdrl858/streamlit-us-airbnb-app',
         'Report a bug': 'https://ai0418.tistory.com/',
     })

    st.title('')
    
   # 이미지 구현
    with st.sidebar :
        image = Image.open('image/air_travel.png')
        st.image(image, use_column_width=True)
        st.write('')
        st.write('')

    # 라디오버튼 - 메뉴 구성
    menu = ['Home', 'Info', 'Chart', 'ML']
    choice = st.sidebar.radio('Choice Menu', menu)

    if choice == menu[0] :
        if st.sidebar.checkbox('💬 Home 설명') :
            run_home()
    elif choice == menu[1] :
        if st.sidebar.checkbox('💡 각 컬럼 설명') :
            run_info()
    elif choice == menu[2] :
        if st.sidebar.checkbox('📋 그래프 확인') :
            run_chart()
    elif choice == menu[3] :
        run_ml()

if __name__ == '__main__' :
    main()