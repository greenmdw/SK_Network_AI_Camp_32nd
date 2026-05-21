# path: ./20260508_self_study/app_self_study.py

"""
GUI(Graphic User Interface)

"""

# ?app.py 복습
# import streamlit as st

# st.title("locatest")
# st.header('test')
# st.subheader('일반 텍스트')
# st.write('출력')

# # 입력 요소:
# name = st.text_input('이름: ')
# age = st.number_input('나이: ')
# gender = st.selectbox('성별', ['남', '여'])
# agree = st.checkbox('동의')
# btn = st.button('확인')

# # 출력 요소:
# st.success('성공')
# st.warning('경고')
# st.error('오류')

# ?app1.py 복습
# import streamlit as st

# st.set_page_config(
#     page_title='GUI 예제', 
#     page_icon='📊',
#     layout="centered"
#     )
# st.title('파이썬 streamlit gui')
# st.write('gui 테스트중')
# name = st.text_input('이름: ')
# age = st.number_input('나이: ')
# gender = st.selectbox('성', ['남자', '여자', '밝히지 않음'])
# memo = st.text_area('자소서')

# if st.button('확인'):           # 버튼 실행시
#     if name.strip() == "":
#         st.warning('이름 적어')
#     else:
#         st.success('입력이 완료되었습니다.')
#         st.write('### 입력 결과')
#         st.write(f'이름: {name}')
#         st.write(f'나이: {age}')
#         st.write(f'성: {gender}')
#         st.write(f'memo: {memo}')


# # ?app2.py 복습
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(page_title='데이터 시각화', page_icon='📊', layout='wide')
# st.title('Streamlit 데이터 시각화')

# data = {
#     'subject': ['python', 'sql', 'spring Boot', 'react', 'AI'],
#     'score': [85, 78, 92, 21, 45]
# }

# df = pd.DataFrame(data)     # data 사전을 데이터 프레임으로 만듬
# st.subheader('1. 데이터 표')
# st.dataframe(df, use_container_width=True)

# st.subheader('2. 요약')
# st.dataframe(df.describe(include='all'))

# st.subheader('3. 막대그래프')
# fig, ax = plt.subplots()
# ax.bar(df['subject'], df['score'])
# ax.set_xlabel('sub')
# ax.set_ylabel('score')
# ax.set_title('engli')
# st.pyplot(fig)


# # ?app3.py 복습
# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title='csv 업로드')
# st.title("csv 파일 업로드")
# upload_file = st.file_uploader('csv 파일 업로드 해', type=['csv'])

# if upload_file is not None:
#     df = pd.read_csv(upload_file)
#     st.success('파일 업로드 성공')
#     st.write('##data show##')
#     st.dataframe(df, use_container_width=True)
#     st.write("## 기본 통계 ##")
#     st.write(df.describe())
# else:
#     st.info('데이터 업로드 없음.')
#     st.warning('미업로드')


# ?app4.py 복습
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(
#     page_title="AI 직업훈련 관리",
#     page_icon="",
#     layout='wide',
# )
# st.title("ai 직업훈련")
# st.write('streamlit 예제')
# st.sidebar.header('학습자 정보')

# # sidebar쪽
# student_name = st.sidebar.text_input('이름')
# course = st.sidebar.selectbox('과정 선택', ['python 기초', '웹 개발', 'AI 연구'])
# attendance = st.sidebar.slider('출석률', 0, 100, 85)

# # Main
# st.header('과목 점수 입력')
# col1, col2, col3 = st.columns(3)

# with col1:
#     python_score = st.number_input('python 점수', min_value=0, max_value=100, value=85)
# with col2:
#     sql_score = st.number_input('sql 점수', min_value=0, max_value=100, value=23)
# with col3:
#     ai_score = st.number_input('ai 점수', min_value=0, max_value=100, value=55)

# if st.button('학습결과 분석'):
#     scores = {
#         'subject': ['Python', 'sql', 'ai'],
#         'score': [python_score, sql_score, ai_score]
#     }
#     df = pd.DataFrame(scores)
#     avg_score = df['score'].mean()

#     st.subheader("1. 학습자 정보")
#     st.write(f'이름: {student_name if student_name else '미입력'}')
#     st.write(f'수강 과목: {course}')
#     st.write(f'출석률: {attendance}%')

#     st.subheader('2. 점수 데이터')
#     st.dataframe(df, use_container_width=True)

#     st.subheader('3. 평균 점수')
#     st.write(f'평균 점수: {df['score'].mean():.2f}')

#     st.subheader('4. 점수 분석 요약')
#     st.dataframe(df.describe())

#     st.subheader('5. 점수 그래프')
#     fig, ax = plt.subplots()            # fig 라는 객체 생성, 
#     ax.bar(df['subject'], df['score'])
#     ax.set_xlabel('subject')
#     ax.set_ylabel('score')
#     ax.set_title('score graph')
#     st.pyplot(fig)                  # 메모리에 만든 정보를 웹 페이지에 표시
    
#     st.subheader('6. 학습 피드백')
#     if avg_score >= 90:
#         st.success('우수 학생')
#     elif avg_score >= 75:
#         st.info('양호')
#     else:
#         st.warning('공부 필요')
# else:
#     st.info('분석 결과 버튼 클릭')