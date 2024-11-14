import streamlit as st
import pandas as pd

data = pd.read_csv("2022서울시미세먼지.csv")

st.title('때는 바야흐로2022년도 12월 31일 23시! 코로나시기 서울특별시의 미세먼지는 어땠을까? - 교수님 진짜 어려웠어요..... 해냈습니다 제가....')


data.loc[:,'size'] = 5*(data['미세먼지']+data['초미세먼지'])
data


color = {'초미세먼지':'#ff0000',
         '미세먼지':'#ffd700'}
data.loc[:,'color'] = data.copy().loc[:,'주된먼지'].map(color)


st.map(data, latitude="위도",
       longitude="경도",
       size="size",
       color="color")
