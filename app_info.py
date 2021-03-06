import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image


def run_info() :
    st.header('๐ฌ US_AirBNB - Info')
    st.write('''##### โ๏ธ ๊ฐ ์ปฌ๋ผ ์ค ์์์ผํ๋ ์ปฌ๋ผ๋ค์ ์ ๋ณด๋ฅผ ๊ฐ๊ฒฐํ๊ฒ ์ ๋ฌํ๊ณ ์ ๋ง๋  ํ์ด์ง์๋๋ค.''')

    # 'AB_US_2020' ๋ถ๋ฌ์ค๊ธฐ
    df = pd.read_csv('data/AB_US_2020.csv')

    # info๋ฅผ ํตํด NaN๊ฐ์ด ์๋ ๊ฐ ์ปฌ๋ผ๋ค์ ๊ฐ ์ฑ์ฐ๊ธฐ ์์
    df['neighbourhood_group'].fillna('Others',inplace=True)
    df.drop(['name','host_name'],axis=1,inplace=True)
    df['last_review'] = pd.to_datetime(df['last_review'],infer_datetime_format=True)
    df['reviews_per_month'].fillna(df['reviews_per_month'].mean(),inplace=True)
    df["last_review"] = df["last_review"].replace(np.nan, df["last_review"].mode().iloc[0])

    # ํ์์๋ ์ปฌ๋ผ drop์ ํตํด ์ ๊ฑฐ
    df.drop(['id','host_id'],axis=1,inplace=True)

    # ๋ฐ์ดํฐ ํํํ๊ธฐ
    st.dataframe(df.tail(15))

    # ํ์ํ ์ปฌ๋ผ๋ง ๋ถ๋ฌ์ค๊ธฐ
    st.write('')
    df_columns = df.columns[ : 5]

    # selectbox๋ฅผ ์ด์ฉํด ์ปฌ๋ผ ์ ํ
    my_choice = st.selectbox('Choice the Columns', df_columns)
    if my_choice == df.columns[0] :
        st.write('''###### โ๏ธ '***neighbourhood_group***' ์ ๋ฒ์ญํ๋ฉด ์ด์๊ทธ๋ฃน์ด์ง๋ง, ๋ฐ์ดํฐ์์๋ ๋ฏธ๊ตญ์ '์ฃผ' ๋ผ๊ณ  ์๊ฐํ๋ฉด๋๋ค.
            
        ''')
        # ์ด๋ฏธ์ง ์์ฌ ์ค์  ํ ๋ฃ๊ธฐ
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/brooklyn.jpg", caption = '< Brooklyn >')

        with col2:
            st.image("image/honolulu.jpg", caption = '< Honolulu >')

    if my_choice == df.columns[1] :
        st.write('')
        st.write('''###### โ๏ธ '***neighbourhood***' ๋ ์ด์์ด๋ผ๋ ๋ป์ด์ง๋ง, ๋ฐ์ดํฐ ํ์๋ก๋ '๋ฐฉ๋ฌธํ ์ฅ์' ๋ผ๊ณ  ์๊ฐํ๋ฉด ๋๋ค.

###### โ๏ธ ์ 226029๋ฒ์งธ '***neighbourhood***' ๋ฅผ ๋ณด๋ฉด Edgewood, Bloomingdale, Truxton Circle, Eckington๋ผ๊ณ  ๋ณด์๋๋ค.
###### โ๏ธ ์ฌ๊ธฐ์ ***Bloomingdale***์ ๋ฐฑํ์ , ***Eckington***์ ์ ๋ชํ ์์ฅ ๋ง์์๋๋ค.
        ''')
        st.write('')

        # ์ด๋ฏธ์ง ์์ญ ์ค์  ํ ๋ฃ๊ธฐ
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/bloomingdales.png", caption = '< blooming >')

        with col2:
            st.image("image/eckington.png", caption = '< eckington >')

    if my_choice == df.columns[2] :
        st.write('')
        st.write('''###### โ๏ธ '***latitude***' ๋ ์๋๋ฅผ ๋ปํ๋ฉฐ, ํด๋น ์ปฌ๋ผ์ ๋ฐ์ดํฐ๋ค์ ์๋์ ์ขํ๊ฐ ์๋ ฅ๋์ด์์ต๋๋ค.
                
###### โ๏ธ ์๋ ํ๋๋ง์ผ๋ก ์ฐพ๊ณ ์ํ๋ ์ฅ์์ ์์น๋ฅผ ์ ์ ์๊ณ  ๋ค์ ์ปฌ๋ผ์ ๊ฒฝ๋์ ๊ฐ์ด ์ฌ์ฉํด์ผํฉ๋๋ค.
                
                ''')

    if my_choice == df.columns[3] :
        st.write('')
        st.write('''###### โ๏ธ '***longitude***' ๋ ๊ฒฝ๋๋ฅผ ๋ปํ๋ฉฐ, ์๋์ฒ๋ผ ๊ฒฝ๋์ ๋ฐ์ดํฐ๋ค์ด ์๋ ฅ๋์ด์์ต๋๋ค.
                
###### โ๏ธ ์์ ์๋ ์ปฌ๋ผ์์ ๋งํ ๊ฒ์ฒ๋ผ ๋จ๋ ์ฌ์ฉ์ ๋ถ๊ฐ๋ฅ, ์๋์ ์ขํ์ ๊ฐ์ด ์ฌ์ฉํด์ ์ฅ์๋ฅผ ํ์ธํ  ์ ์์ต๋๋ค.
                
                ''')

    if my_choice == df.columns[4] :
        st.write('')
        st.write('''###### โ๏ธ ๋ฐฉ ์ข๋ฅ์ ๋ฐ์ดํฐ๋ค์ด ์๋ ฅ๋ ์ปฌ๋ผ์๋๋ค.

###### โ๏ธ '***room_type***' ์ ์ข๋ฅ์๋ '***Private room***', '***Entire home/apt***', '***Hotel room***', '***Shared room***' ์ด ์์ต๋๋ค.

###### โ๏ธ ์ฌ๊ธฐ์ '***Shared room***' ๋ '***Dormitory***', '๊ธฐ์์ฌํ' ์ด๋ผ ํ๋ฉฐ, ์นจ๋ ๋จ์์ ๊ฐ์ค์ ์ ๊ณตํ๋ ๊ฐ์ค์ ์๋ฏธํฉ๋๋ค.
                ''')

        # ์ด๋ฏธ์ง ์์ญ ์ค์  ํ ๋ฃ๊ธฐ
        image = Image.open('image/hotel_room.png')
        st.image(image, use_column_width=True, caption = '< Room type - Hotel room >')