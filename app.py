# 파일명 예시: app.py

import streamlit as st

st.title("숫자 계산기")

# 사용자 입력 받기
number = st.number_input("숫자를 입력하세요", value=1)

# 계산
square = number ** 2
cube = number ** 3

# 출력
st.write(f"입력한 숫자: {number}")
st.write(f"{number}의 제곱: {square}")
st.write(f"{number}의 세제곱: {cube}")
