import streamlit as st
import datetime
from openai import OpenAI

SOLAR_API_KEY='up_kVlyczu4sWoHKPKXxz3iZPxvn7urP'
BASE_URL = "https://api.upstage.ai/v1"

client = OpenAI(
    api_key=SOLAR_API_KEY,
    base_url=BASE_URL
)

def chat(system_prompt, user_prompt, temperature=0):
    response = client.chat.completions.create(
        model="solar-pro2",
        messages=[
             {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=temperature
    )
    return response.choices[0].message.content

st.title('여행 계획 비교 🧳')

col1, col2 = st.columns(2)
with col1:
    mylocation1 = st.selectbox('현재 위치 선택',
                              ('서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도',
                               '강원특별자치도', '충청북도', '충청남도', '전북특별자치도', '전라남도', '경상북도', '경상남도', '제주특별자치도'))

    want1 = st.text_input('가고 싶은 나라 이름')

    theme1 = st.text_input('여행 테마 입력   예시) 역사, 문화, 미식, 자연, 예술, 레저 등')

    question11 = (f'{want1}에서 주요 관광지를 3개로 알려줘. 단, 관광지 명칭 : 20자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
    result11 = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question11)


    st.text(f'{want1}의 주요 관광지 :\n{result11}' )


    if theme1 !="" :
        question12 = (
            f'{want1}에서 {theme1}과 관련된 주요 관광지를 3개로 알려줘. 단, 관광지 명칭 : 20자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
        result12 = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question12)
        st.text(f'{want1}의 {theme1}과 관련된 주요 관광지 : \n{result12}' )

    place1 = st.text_input('특별히 가고 싶은 장소')

    col11, col12 = st.columns(2)
    with col11:
        today = datetime.date.today()
        sdate = st.date_input("시작일", today)

    with col12:
        today = datetime.date.today()
        fdate = st.date_input("종료일", today)



with col2:
    mylocation2 = st.selectbox('현재 위치 선택2',('서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전북특별자치도','전라남도','경상북도','경상남도','제주특별자치도'))

    want2 = st.text_input('가고 싶은 나라 이름')




    theme2 = st.text_input('여행 테마 입력2   예시) 역사, 문화, 미식, 자연, 예술, 레저 등')

    question2 = (f'{want2}에서 주요 관광지를 3개로 알려줘. 단, 관광지 명칭 : 20자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
    result2 = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question2)

    st.text(f'{want2}의 주요 관광지 :\n{result2}')

    if theme2 != "":
        question2 = (
            f'{want2}에서 {theme2}과 관련된 주요 관광지를 3개로 알려줘. 단, 관광지 명칭 : 20자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
        result12 = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question2)
        st.text(f'{want2}의 {theme2}과 관련된 주요 관광지 : \n{result2}')

    place2 = st.text_input('특별히 가고 싶은 장소2')


    col1, col2 = st.columns(2)
    with col1:
        today2 = datetime.date.today()
        sdate2 = st.date_input("시작일2", today2)

    with col2:
        fdate2 = st.date_input("종료일2", today2)




if st.button('획인'):
    col1, col2 = st.columns(2)
    with col1:
        question13 = (
            f'{mylocation1}에서 출발해{want1}가 목적지야 여행테마는{theme1}이야 특별히 가고 싶은 장소는{place1}야 나는{sdate}에 시작해 {fdate}에 여행을 끝낼거야 거야')
        print(question13)
        iteration = "계획중~"
        st.success(iteration)
        iteration = chat('너는 일정을 짜는 ai야', question13)
        st.snow()
        st.success(iteration)


    with col2:
        question2 = (
            f'{mylocation2}에서 출발해{want2}가 목적지야 여행테마는{theme2}이야 특별히 가고 싶은 장소는{place2}야 나는{sdate2}에 시작해 {fdate2}에 여행을 끝낼거야 거야')
        print(question2)
        iteration2 = "계획중~"
        st.success(iteration2)
        iteration2 = chat('너는 일정을 짜는 ai야', question2)
        st.snow()
        st.success(iteration2)

    if st.button('다시하기'):
        st.rerun