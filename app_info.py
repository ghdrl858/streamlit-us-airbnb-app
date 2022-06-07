import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image


def run_info() :
    st.header('💬 US_AirBNB - Info')
    st.write('''##### ✔️ 각 컬럼에 의미를 모를 수 있기에 간단히 정보를 전달하고자 만든 페이지입니다.''')

    # 'AB_US_2020' 불러오기
    df = pd.read_csv('data/AB_US_2020.csv')

    # info를 통해 NaN값이 있던 각 컬럼들에 값 채우기 작업
    df['neighbourhood_group'].fillna('Others',inplace=True)
    df.drop(['name','host_name'],axis=1,inplace=True)
    df['last_review'] = pd.to_datetime(df['last_review'],infer_datetime_format=True)
    df['reviews_per_month'].fillna(df['reviews_per_month'].mean(),inplace=True)
    df["last_review"] = df["last_review"].replace(np.nan, df["last_review"].mode().iloc[0])

    # 필요없는 컬럼 drop을 통해 제거
    df.drop(['id','host_id'],axis=1,inplace=True)

    # 데이터 표현하기
    st.dataframe(df.tail(15))

    # 필요한 컬럼만 불러오기
    st.write('')
    df_columns = df.columns[ : ]

    # selectbox를 이용해 컬럼 선택
    my_choice = st.selectbox('Choice the Columns', df_columns)
    if my_choice == df.columns[0] :
        st.write('''###### ✔️ 'neighbourhood_group' 은 번역하면 이웃그룹이지만, 데이터에서는 미국에 '주' 라고 생각하면된다.
            
        ''')
        # 이미지 영여 설정 후 넣기
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/brooklyn.jpg", caption = '< Brooklyn >')

        with col2:
            st.image("image/honolulu.jpg", caption = '< Honolulu >')

    if my_choice == df.columns[1] :
        st.write('')
        st.write('''###### ✔️ 'neighbourhood' 는 이웃이라는 뜻이지만, 데이터 표시로는 '방문한 장소' 라고 생각하면 된다.

###### ✔️ 위에 데이터들의 

        ''')
