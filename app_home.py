import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_home() :
    st.header('🛫 US_AirBNB')
    st.write('''###### ✔️ 이 페이지는 미국에 AirBNB 통계에 대해서 정보 전달을 위한 페이지입니다.
    
###### ✔️ 'info' 에서는 각 컬럼이 뭘 의미하는지에 대해 간단히 설명할 것입니다.
###### ✔️ 'Chart' 에서는 간단한 설명과 몇 개의 그래프를 보여줄 것입니다.
###### ✔️ 'ML' 에서는 인공지능학습을 통해 구한 예측값과 실제값을 비교한 그래프를 보여줄 것입니다.
    ''')
    st.write('')
    st.write('')
    image = Image.open('image/airplane.png')
    st.image(image, use_column_width=True)