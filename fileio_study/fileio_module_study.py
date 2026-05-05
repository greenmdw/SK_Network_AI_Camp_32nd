# 20260504 review 
# path: self_study\\fileio_study\\fileio_module_study.py
# module: self_study.fileio_study.fileio_module_study

# ?----------fileio : 입출력 처리-------------
"""
프로그램 기본 입출력 단계: open() -> write() | read() -> close()
파일 입출력의 기본 확장자는 txt. (=메모장)
열기모드 종류:
- w(=wt):
    - 새로 쓰기 모드
    - 대상 파일 없으면 새로 만들고 씀
    - 대상 파일 있으면 덮어씀
- x(=xt):
    - 새로 쓰기 모드
    - 대상 파일 없으면 새로 만들고 씀
    - 대상 파일 있으면 에러 난다. 
- a(=at):
    - 추가 쓰기 모드
    - 대상 파일 없으면 새로 만들고 씀
    - 대상 파일 있으면 append
- r(=rt):
    - 읽기 전용 모드
    - 대상 파일 없으면 error
"""
# 1. 파일 새로 만들고 값 기록
import os
import pickle

def test_fwrite():
    f = open('study.txt', 'w', encoding='utf-8')      # encoding 필요
    f.write('testing write on txt.\n')
    f.write('실험\n')
    f.close()

    print(os.getcwd())      # 현 작업 dir 확인
    return
# --------------------------------------------

# 2. 원하는 dirt에 저장하는 방법
# \ 는 이스케이프 문자로 경로 표시 때 반드시 두 번 \\
def test_fwrite2():
    # f = open('C:\\Python_workspace\\python_fileio_260504\\self_study\\testb.txt', 'x', encoding='utf-8')
    f = open('C:\\Python_workspace\\python_fileio_260504\\self_study\\testb.txt', 'w', encoding='utf-8')
    f.write('Creating test file at sertain path\n')
    f.write('fwrite2: 경로에 저장')
    f.write("20260504")
    f.close()
# --------------------------------------------

# 3. a 모드: append
def test_fwrite3():
    f = open('testc.txt', 'a', encoding = 'utf-8')
    f.write("append testing \n")
    f.write('20250504')
    f.write('at''testing++++++++++\n')
    f.close()
# --------------------------------------------

# 4. r 모드
# 읽을 대상 있어야 함. 없으면 error
# read(): 전체 내용 한번에 읽음
# readline(): 한 줄씩 읽음. 더이상 없으면 none 리턴
# readlines(): 줄 단위(아이템)로 모두 읽고 list로 리턴
def test_fread():
    print(os.getcwd())
    f = open('testc.txt', 'r', encoding = 'utf-8')
    # print(f.read())         # 전체 내용 read

    # 파일 내용 한 줄씩
    line_number = 1
    while True:
        line = f.readline()
        if not line:
            break
        print(line_number, ':', line.strip())
        line_number += 1

    f.close()

# ?-----------------while 문 -----------------------
""" 
while 반복에 대한 조건식:
    반복 실행할 구문

비고, 논리 연산자 써서 true, false 나와야 함
"""

# 5. while 문
def test_while():
    num = 5
    while num > 0:
        print(f'num: ', num)
        num -= 1
    return

# 6. while 문: 문자 uni_code 출력
# while 문은 주로 몇 번 반복할지 정해지지 않을 때 사용
def test_while_unicode():
    ch = input('문자 하나 입력(0 입력시 종료): ')

    while ch != '0':
        print(f'{ch} is unicode of {ord(ch)}')
        ch = input('문자 하나 입력(0 입력시 종료): ')
    return

# ?-----------------complete -----------------------

# 7. 파일이나 디렉토리 다루기
# os 모듈에서 제공하는 함수 사용
def test_osmodule():
    # A. 사용자 컴퓨터 이름 조회
    print("사용자 컴퓨터 이름: \n", os.getlogin())
    # B. 현 작업 디렉토리 조회
    print("현 작업 dir: \n", os.getcwd())

    # C. 디렉토리 생성하기
    system_user = os.getlogin()
    work_dir = "C:\\Users\\green\\Downloads\\New_working"

    if not os.path.exists(work_dir):
        os.mkdir(work_dir)          # 이미 동일 경로에 동일 폴더 있으면 에러
        print(f'폴더 생성했습니다. {work_dir}')
    else:
        print('이미 폴더가 존재하여 다음 단계로 넘어갑니다.')

    # D. 생성한 디랙토리로 이동
    os.chdir(work_dir)
    print('작업할 dir 변경: ', os.getcwd())     # 확인

    # E. 변경한 dir에 파일 저장
    f = open('download pyt.txt', 'w', encoding = 'utf-8')
    f.write("파이썬으로 디렉토리 만들고, 만든 dir에 파일 저장\n")
    st = '''변경된 디렉토리에 파일 
    생성하고 유니코드로 확인 \n   
    ''' 
    f.write(st)
    f.close()
    print("변경된 dir에 txt 파일 생성/수정 완료")

    # F. 시스템 환경변수, dir, file 다루기
    #   listdir(): 현재 작업 디렉토리 안에 파일들과 하위 디렉토리 목록 조회
    print(os.listdir(os.getcwd()))
    print(os.listdir('.'))      # '.' : 현 디렉토리
    print(os.listdir('../'))    # '../': 상위 디렉토리 

    #   rename(): 디렉토리 이름 바꾸기

    #   path.exist(): 파일이나 디렉토리의 존재 여부 확인
    print('os.path.exists(download pyt.txt): ', os.path.exists('download pyt.txt'))
    print('os.path.exists(파파이스.txt): ', os.path.exists('파파이스.txt'))

    # path.abspath(): 파일이나 dir 절대 경로
    print('절대경로: ', os.path.abspath('dowload pyt.txt'))      # C:\Users\green\Downloads\New_working\dowload pyt.txt
    # path.basename(), path.dirname(), path.split()
    current_path = os.path.abspath('download pyt.txt')
    print('basename: ', os.path.basename(current_path))     # basename: 파일명, 확장자 값
    print('dirname: ', os.path.dirname(current_path))       # dir name: 경로만 추출
    print('split', os.path.split(current_path))             # (경로명, 파일명.확장자)
    # path.splitdrive(), splittext()
    print(os.path.splitdrive(current_path))             # tuple return, (드라이브명, 나머지 경로)
    print(os.path.splitext(current_path))               # tuple return, (경로명과 파일명, 확장자)
# --------------------------------------------

# 10. readlines: 한 줄씩 읽은 정보가 리스트에 저장
def test_readlines():
    f = open('testc.txt', 'r', encoding = 'utf-8')
    lst = f.readlines()
    print(lst)
# --------------------------------------------

# 11. writelines(): list, tuple, set, dictionary 등에 저장한 데이터들을 파일에 저장
def test_writelines():
    tp = ('a', 'b', 'c')
    ls = ["r", "e", "d"]
    f = open('list.txt', 'a')
    f.writelines(tp)
    f.write(': writelines\n')
    f.writelines(ls)
    f.write(': writelines\n')
    f.close()
# --------------------------------------------


"""
파이썬의 기본 파일 입출력은 txt 파일
텍스트가 아닌 자료형의 파일을 다룰 때 pickle 모듈 활용
바이너리(binary) 는 이진 데이터
파일 열기 모드 시, wb, rb, ab로 표기
"""

# 12. 이진 데이터 파일 저장
def test_binary():
    data = {1:'python', 2:'you need'}
    f = open('btest.dat', 'wb')
    # 텍스트 저장이 아니기 때문에 str 사용 불가, encoding 사용 불가
    # 이진 파일 저장 포맷은 dat.
    pickle.dump(data, f)        # 파이썬 객체를 바이너리 형태로 변환하여 저장
    f.close()
# --------------------------------------------
 
# 13. 파일로 부터 이진 데이터 읽어오기
def test_binary2():
    f = open('btest.dat', 'rb')
    read_data = pickle.load(f)  # 파일에 저장된 이진 데이터 읽어드림
    f.close()

    print(read_data)
    print(type(read_data))          # wb는 객체 타입 그대로 기록