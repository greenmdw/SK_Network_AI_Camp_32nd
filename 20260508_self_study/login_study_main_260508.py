# path: streamlit_login_csv_260508\\app\\login_study_main_260508.py

"""
기능:
1. data/users.csv 파일에서 로그인 계쩡 정보를 읽어옴
2. 사용자가 입력한 이메일과 비밀번호가 csv 값과 일치한다면 로그인 성공
3. 로그인 실패시 오류메시지
4. 성공 후, csv 파일 업로드 하면 통계 그래프 표시
"""

from pathlib import Path        # 안전한 파일경로 처리
import matplotlib.pyplot as plt     # 그래프 생성
import pandas as pd                 # csv 읽기, 통계
import streamlit as st              # 화면

# 현 dir
BASE_DIR = Path(__file__).resolve().parents[1]      # Path 객체로 BASE_DIR 생성
# print('path: ', Path)                   # Path: 경로를 단순 str이 아닌 윈도우나 맥에 맞춘 경로 데이터로 변경하는 class
# print('Path(__file__)', Path(__file__))   # C:\Python_workspace\streamlit_login_csv_260508\app\login_study_main_260508.py
print('현 dir 루트 주소: ', BASE_DIR)            # C:\Python_workspace\streamlit_login_csv_260508

# 사용자 계정 정보가 저장된 csv 파일 경로
USER_CSV_PATH = BASE_DIR/'data'/'users.csv'
print('데이터 저장 위치: ', USER_CSV_PATH)      # BASE_DIR에서 절대경로 Path로 지정해서 중복해서 설정 필요 없음

# 1. 기본 페이지 설정
st.set_page_config(
    page_title="login 및 csv 파일 분석",
    page_icon="",
    layout="wide",
)

# 2. 세션 상태(로그인 상태 관리요)
def init_session_state()-> None:
    "streamlit은 버튼 클릭하거나 값 입력하면 스크립트 전체 다시 실행해 session 값 저장 필요"
    # if 여러개 쓰면, 모든 if 다 확인하고 지나감. 
    # if -> elif -> else 는 중간에 하나라도 맞으면 뒤에구문 스킵 
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False      # 현 로그인 여부(로그아웃)
    if 'user_email' not in st.session_state:
        st.session_state.user_email = ""        # 로그인 한 사용자 이메일 저장 공간
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ''         # 로그인한 사용자 이름 저장

    if 'show_login_error' not in st.session_state:
        st.session_state.show_login_error = False   # 로그인 실패 팝업 표시 여부
    return

# 3. 사용자 csv 읽기 함수
# csv 파일은 매번 새로 읽을 필요가 없기 때문에 cash 처리
@st.cache_data                # 이 함수를 실행해서 얻은 data frame을 메모리에 캐시로 저장
def load_users() ->pd.DataFrame:
    'data/users.csv 파일에서 로그인 계정 정보 읽어오는 함수'
    if not USER_CSV_PATH.exists():      # 파일 없으면
        st.error(f'사용자 csv 파일 없습니다. : {USER_CSV_PATH}')
        st.stop()                       # 서버 정지

    user_df = pd.read_csv(USER_CSV_PATH)

    # 필수 커럼 존재 여부 확인(이메일, 비밀번호 컬럼)
    require_columns = {'email', 'password', 'name'}         # set 함수 씀(중복 방지)
    if not require_columns.issubset(user_df.columns):           # issubset: A가 b의 부분집합인지
        st.error('users.csv 파일에는 email, password, name 컬럼이 존재해야 합니다.')
        st.stop()

    
    # 비교를 위해 문자열 타입으로 변환
    user_df['email'] = user_df['email'].astype(str)
    user_df['password'] = user_df['password'].astype(str)
    user_df['name'] = user_df['name'].astype(str)

    return user_df

# 4. 로그인 검증 함수
def check_login(email: str, password: str) ->tuple[bool, str]:  # 이메일과 비밀번호 받아서 (참/거짓, 정보)를 돌려주는 함수
    """
    입력한 이메일/비밀번호가 users.csv 에 있는지 확인
    반환값:
    - (true, 사용자 이름): 로그인 성공
    - (false, ""): 로그인 실패
    """
    users_df = load_users()

    # 입력값 앞뒤 공백 제거
    email = email.strip()
    password = password.strip()

    # email과 password가 모두 일치하는지 검사
    matched = users_df[(users_df['email'] == email) & (users_df['password'] == password)]

    if not matched.empty:       # matched 가 안비어 있으면(적합 데이터 찾음)
        # 일치하는 값이 있다면, 사용자 이름 반환
        return True, matched.iloc[0]['name']        # .iloc은 index location 줄임말로 데이터 물리적 위치 접근
    return False, ""            # 로그인 실패


# 5. 로그인 실패 팝업창
@st.dialog('로그인 실패')
def login_error_dialog() ->None:
    '로그인 실패 메시지를 팝업창으로 출력하는 함수'
    st.error('아이디와 암호가 일치하지 않습니다.')

    # 닫기 버튼 클릭시 팝업 상태를 False로 바꾸고 화면을 다시 실행
    if st.button('닫기'):
        st.session_state.show_login_error = False
        st.rerun()

# 6. 로그인 화면 구성
def show_login_page() ->None:
    '로그인 화면 출력 함수'
    st.title('로그인 하세요.')
    st.write('이메일과 비밀번호를 입력하세요')

    # 로그인 폼 영역
    with st.form('login_form'):
        email = st.text_input('이메일: ', placeholder='text@eample.com')
        password = st.text_input('비밀번호: ', type='password', placeholder="1234")
        submited = st.form_submit_button('로그인')

        # 로그인 버튼 클릭시 검증
        if submited:
            success, user_name = check_login(email, password)

            if success:
                # 로그인 성공 정보 저장 => session_State
                success, user_name = check_login(email, password)
                
                if success:
                    # 로그인 성공 정보 저장
                    st.session_state.logged_in = True
                    st.session_state.user_name = user_name
                    st.session_state.user_email = email.strip()
                    st.session_state.show_login_error = False
                    st.rerun()
                else:
                    # 로그인 실패 파법
                    st.session_state.show_login_error = True
    if st.session_state.show_login_error:
        login_error_dialog()
    with st.expander('테스트 계정 보기'):
        st.code('admin@example.com/1234\nstudent@example.com/pass123\nteacher@example.com/teach123,강사\n')


# 7. 업로드 csv 데이터 파일 읽기 함수
def read_upload_csv(upload_file) ->pd.DataFrame:
    '사용자가 업로드한 csv 데이터 파일을 읽어서 pandas의 DataFrame으로 만들어 return'
    try:
        return pd.read_csv(upload_file)
    except UnicodeDecodeError:
        # 한글 window csv가 cp94로 저장된 경우에 대비
        upload_file.seek(0) # 파일 포인터를 처음으로 이동
        return pd.read_csv(upload_file, encoding='cp949')   # 949 인코딩으로 파일 읽어오기


# 8. 데이터 분석 화면 구성
def show_dashboard_page() ->None:
    '로그인 성공 후 표시되는 데이터 분석 페이지'
    st.title('로그인 성공 - csv 데이터 분석')

    # 상단에 사용자 정보와 로그아웃 버튼
    col1, col2 = st.columns([4, 1])     # 항목 4개 표시
    with col1:
        st.success(f'{st.session_state.user_name}님 로그인 성공: {st.session_state.user_email}')
    with col2: 
        if st.button('로그아웃'):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.session_state.user_name = ''
            st.session_state.show_login_error = False
            st.rerun()
    
    st.divider()        # 화면 나누는 함수

    # 파일 업로드 위젯
    upload_file = st.file_uploader(
        "csv 파일 선택",
        type=['csv'],
        help="예: 'data/sample.sales.csv 업로드"
    ) 
    
    if upload_file is None:
        st.info('csv 파일을 업로드 하면 통계 자료 볼 수 있따')
        st.write('프로젝트에 포함된 예제 데이터 파일')
        return
    
    # 업로드한 파일 읽기
    df = read_upload_csv(upload_file)

    st.subheader('1. 읽어온 데이터 테입ㄹ')
    st.dataframe(df, use_container_width=True)

    st.subheader('2. 기본 데이터 정보')
    col1, col2, col3 = st.columns(3)
    col1.metric('행 겟수: ', len(df))
    col2.metric('열 겟수: ', len(df.columns))
    col3.metric('결측치 겟수: ', int(df.isna().sum().sum()))

    st.subheader('3. 숫자 컬럼 통계 요약')
    numeric_df = df.select_dtypes(include='number')

    if numeric_df.empty:
        st.warning('숫자형 컬럼이 없어서 통계 못 그려')
        return
    
    # 숫자형 컬럼의 통계값 표시
    st.dataframe(numeric_df.describe(), use_container_width=True)

    st.subheader('4. 통계 그래프')
    
    # 그래프로 표시할 숫자 컬럼 선택
    select_column = st.selectbox(
        '그래프로 표시할 숫자 컬럼 선택',
        numeric_df.columns,
    )

    chart_type = st.radio(
        '그래프 종류 선택: ',
        ['선 그래프', '막대 그래프', '히스토그램'],
        horizontal=True, 
    )

    if chart_type == '선 그래프':
        st.line_chart(numeric_df[select_column])
    elif chart_type == '막대그래프':
        st.bar_chart(numeric_df[select_column])
    else:
        fig, ax = plt.subplots()
        ax.hist(numeric_df[select_column].dropna(), bins=10)
        ax.set_title(f'{select_column} histogram')
        ax.set_xlabel(select_column)
        ax.set_ylabel('frequency')
        st.pyplot(fig)
        

# 9. 메인 실행 흐름
def main() ->None:
    '앱의 시작 함수'
    init_session_state()

    # 로그인 여부에 따라 다른 화면 표시
    if st.session_state.logged_in:
        show_dashboard_page()
    else:
        show_login_page()

# 10. 이 파일을 직접 실행할 때 main() 함수 실행
if __name__ == '__main__':
    main()