import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image


def run_info() :
    st.header('💬 US_AirBNB - Info')
    st.write('''##### ✔️ 각 컬럼 중 알아야하는 컬럼들에 정보를 간결하게 전달하고자 만든 페이지입니다.''')

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
    df_columns = df.columns[ : 5]

    # selectbox를 이용해 컬럼 선택
    my_choice = st.selectbox('Choice the Columns', df_columns)
    if my_choice == df.columns[0] :
        st.write('''###### ✔️ '***neighbourhood_group***' 은 번역하면 이웃그룹이지만, 데이터에서는 미국에 '주' 라고 생각하면된다.
            
        ''')
        # 이미지 영여 설정 후 넣기
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/brooklyn.jpg", caption = '< Brooklyn >')

        with col2:
            st.image("image/honolulu.jpg", caption = '< Honolulu >')

    if my_choice == df.columns[1] :
        st.write('')
        st.write('''###### ✔️ '***neighbourhood***' 는 이웃이라는 뜻이지만, 데이터 표시로는 '방문한 장소' 라고 생각하면 된다.

###### ✔️ 위 226029번째 '***neighbourhood***' 를 보면 Edgewood, Bloomingdale, Truxton Circle, Eckington라고 보입니다.
###### ✔️ 여기서 ***Bloomingdale***은 백화점, ***Eckington***은 유명한 시장 마을입니다.
        ''')
        st.write('')

        # 이미지 영역 설정 후 넣기
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/bloomingdales.png", caption = '< blooming >')

        with col2:
            st.image("image/eckington.png", caption = '< eckington >')

    if my_choice == df.columns[2] :
        st.write('')
        st.write('''###### ✔️ '***latitude***' 는 위도를 뜻하며, 해당 컬럼의 데이터들은 위도의 좌표가 입력되어있습니다.
                
###### ✔️ 위도 하나만으로 찾고자하는 장소에 위치를 알 수 없고 다음 컬럼에 경도와 같이 사용해야합니다.
                
                ''')

    if my_choice == df.columns[3] :
        st.write('')
        st.write('''###### ✔️ '***longitude***' 는 경도를 뜻하며, 위도처럼 경도에 데이터들이 입력되어있습니다.
                
###### ✔️ 앞서 위도 컬럼에서 말한 것처럼 단독 사용은 불가능, 위도에 좌표와 같이 사용해서 장소를 확인할 수 있습니다.
                
                ''')

    if my_choice == df.columns[4] :
        st.write('')
        st.write('''###### ✔️ 방 종류에 데이터들이 입력된 컬럼입니다.

###### ✔️ '***room_type***' 에 종류에는 '***Private room***', '***Entire home/apt***', '***Hotel room***', '***Shared room***' 이 있습니다.

###### ✔️ 여기서 '***Shared room***' 는 '***Dormitory***', '기숙사형' 이라 하며, 침대 단위의 객실을 제공하는 객실을 의미합니다.
                ''')

        # 이미지 영역 설정 후 넣기
        image = Image.open('image/hotel_room.png')
        st.image(image, use_column_width=True, caption = '< Room type - Hotel room >')