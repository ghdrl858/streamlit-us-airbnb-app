import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_home() :
    st.header('π« US_AirBNB')
    st.write('''###### βοΈ μ΄ νμ΄μ§λ λ―Έκ΅­μ AirBNB ν΅κ³μ λν΄μ μ λ³΄ μ λ¬μ μν νμ΄μ§μλλ€.
    
###### βοΈ 'info' μμλ κ° μ»¬λΌμ΄ λ­ μλ―Ένλμ§μ λν΄ κ°λ¨ν μ€λͺν  κ²μλλ€.
###### βοΈ 'Chart' μμλ κ°λ¨ν μ€λͺκ³Ό λͺ κ°μ κ·Έλνλ₯Ό λ³΄μ¬μ€ κ²μλλ€.
###### βοΈ 'ML' μμλ μΈκ³΅μ§λ₯νμ΅μ ν΅ν΄ κ΅¬ν μμΈ‘κ°κ³Ό μ€μ κ°μ λΉκ΅ν κ·Έλνλ₯Ό λ³΄μ¬μ€ κ²μλλ€.
    ''')
    st.write('')
    st.write('')
    image = Image.open('image/airplane.png')
    st.image(image, use_column_width=True)