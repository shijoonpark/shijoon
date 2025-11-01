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

st.title('여행 계힉 🧳')



mylocation = st.selectbox('출발 위치 선택',('서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전북특별자치도','전라남도','경상북도','경상남도','제주특별자치도'))

want = st.selectbox('가고 싶은 지역',('서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전북특별자치도','전라남도','경상북도','경상남도','제주특별자치도','전국'), index=1)

theme = st.text_input('여행 테마 입력')
st.text('예시) 역사, 문화, 미식, 자연, 예술, 레저 등')

question = (f'{want}에서 주요 관광지를 5개로 알려줘. 단, 관광지 명칭 : 30자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
result = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question)
question2 = (f'{want}에서 {theme}과 관련된 주요 관광지를 5개로 알려줘. 단, 관광지 명칭 : 30자 이내의 간략한 설명으로 관광지 별 1줄 대답해주고 ** 이런 표시는 하지 말아줘.')
result2 = chat('너는 사람들이 많이 찾는 관광지를 잘 아는 ai야', question2)
place = st.text_input('특별히 가고 싶은 장소')

col1, col2 = st.columns(2)
with col1:
    st.text(f'{want}의 주요 관광지 : ')
    st.text(result)

with col2:
    st.text(f'{want}의 {theme}과 관련된 주요 관광지 : ')
    st.text(result2)


col1, col2 = st.columns(2)
with col1:
    today = datetime.date.today()
    sdate = st.date_input("시작일", today)

with col2:
    today = datetime.date.today()
    fdate = st.date_input("종료일", today)

if st.button('확인'):
    question = ( f'{mylocation}에서 출발해{want}가 목적지야 여행테마는{theme}이야 특별히 가고 싶은 장소는{place}야 나는{sdate}에 시작해 {fdate}에 여행을 끝낼거야 거야')
    print(question)
    iteration = "계획중~"
    st.success(iteration)
    iteration = chat('너는 일정을 짜는 ai야',question)
    st.snow()
    st.success(iteration)
    url = ""

    if want=='전국':
        st.write(f"가고 싶은 지역 관광정보 알아보기 : [한국관광공사](%s)" % 'https://knto.or.kr/index#')
    else:
        if want=='서울특별시':
            url = 'https://news.seoul.go.kr/culture/'

        if want =='부산광역시':
            url = 'https://www.visitbusan.net/kr/index.do'

        if want=='대구광역시시':
            url = 'https://tour.daegu.go.kr/'

        if want=='인천광역시':
            url = 'https://itour.incheon.go.kr/'

        if want=='광주광역시':
            url = 'https://tour.gwangju.go.kr/home/main.cs'

        if want=='대전광역시':
            url = 'https://www.djto.kr/kor/index.do'

        if want=='울산광역시':
            url = 'https://www.ulsan.go.kr/tour/kor/main.ulsan'

        if want=='세종특별자치시':
            url = 'https://www.sejong.go.kr/tour.do'

        if want=='경기도':
            url = 'https://ggtour.or.kr/'

        if want=='강원특별자치도':
            url = 'https://www.gangwon.to/gwtour'

        if want=='충청북도':
            url = 'https://tour.chungbuk.go.kr/www/index.do'

        if want=='충청남도':
            url = 'https://tour.chungnam.go.kr/kor.do'

        if want=='전북특별자치도':
            url = 'https://tour.jb.go.kr/index.do'

        if want=='전라남도':
            url = 'https://www.namdokorea.com/'

        if want=='경상북도':
            url = 'https://www.namdokorea.com/'

        if want=='경상남도':
            url = 'https://tour.gyeongnam.go.kr/index.gyeong'

        if want=='제주특별자치도':
            url = 'https://www.visitjeju.net/kr/'

        st.write(f"가고 싶은 지역 관광정보 알아보기 : [{want} 관광공사](%s)" % url)

        if st.button('다시하기'):
            st.rerun