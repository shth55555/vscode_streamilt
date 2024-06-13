import streamlit as st
from PIL import Image
import pandas as pd

st.title("사용자 지정 화면 분할")

#2로 세로단 분할
import pandas as pd
df2=pd.read_csv("data\공장별_생산현황2.csv",index_col='year')

[col1, col2] = st.columns(2)  #열(너비)로 2개 분할, 동일너비

with col1:
    st.subheader("DF data")
    st.dataframe(df2)
with col2:
    st.subheader("꺾꺾은 선 차트")
    st.line_chart(df2)

## 3개로 세로단 분할
columns = st.columns([1.2,1.0,0.8])

image_files=['dog.png','cat.png','bird.png']
image_captions=['강아지','고양이','새']

for k in range(len(columns)):
    with columns[k]:
         st.subheader(image_captions[k])
         img_call=Image.open(r"D:/LDH/visual_2024/20240613/data/"+image_files[k])
         st.image(img_call,caption=image_captions[k])