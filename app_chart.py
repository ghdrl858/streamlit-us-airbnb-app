import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart() :

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

    st.header('📊 US_AirBNB - Chart')
    st.write('''###### ✔️ 많은 데이터가 있지만 중요한건 우리가 원하는 ***방 종류*** 와 적절한 ***가격*** 이 아닌가 생각이 든다.
    

    
    ''')

    # 그래프에 해당하는 컬럼에 데이터 표시
    st.dataframe(df.loc[ : ,['room_type', 'price']])

    # 그래프 나타내기
    st.write('')
    st.write(''' ###### ✔️ 그래서 그래프는 간단하게 ***room_type*** 과 ***price*** 에 데이터만을 이용해서 그래프로 표현했다.
    
    ''')
    fig1 = plt.figure()
    sns.barplot(data = df, x = 'room_type', y = 'price', palette = 'spring')
    st.pyplot(fig1)