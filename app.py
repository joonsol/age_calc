import datetime
import streamlit as st

st.title("나이계산기")
st.write("출생정보를 입력하세요")


year = st.number_input("출생년도",min_value=1900, max_value=datetime.date.today().year, value=2000)
month = st.number_input("출생 월",min_value=1,max_value=12,value=1)
day=st.number_input("출생 일",min_value=1,max_value=31,value=1)




if st.button("나이계산"):
    try:
        birth_date=datetime.date(int(year),int(month),int(day))
        today=datetime.date.today()

        age= today.year - birth_date.year

        if(today.month, today.day)< (birth_date.month,birth_date.day):
            age-=1
        st.success(f"당신의 만나이는 {age}세입니다.")

        if(today.month,today.day)==(birth_date.month,birth_date.day):
            st.balloons()
            st.info("생일 축하합니다.@@@")

    except ValueError:
        st.error("유효하지 않은 날짜입니다.")
