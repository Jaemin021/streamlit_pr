import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.header("Task 2: 데이터 표시하기")
st.subheader("데이터프레임")
df = pd.DataFrame(
    rng(0).standard_normal((50,20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df)

st.subheader("지표 정보")

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("온도", "-1 °C", -2, border=True)
b.metric("바람", "2 m/s", 8, border=True)
c.metric("습도", "47%",  -9, border=True)
d.metric("강수량", "0 mm", 0, border=True)