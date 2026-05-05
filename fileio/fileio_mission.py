# path : fileio\\fileio_mission.py
# module : fileio.fileio_misson

# 파일입출력, 반복문, 리스트, 딕셔너리 사용 실습문제 요구사항
'''
while 문을 사용해서 prompt 가 반복해서 출력되도록 함
입력된 번호에 따라서 emp_list 에 아이템 추가, 삭제, 출력 처리하도록 함

prompt = 
        *** 직원 정보 관리 서비스 ***
        1. 새 직원정보 추가
        2. 직원정보 삭제
        3. 전체 출력
        4. 파일에 저장
        5. 파일로 부터 직원정보 읽어오기
        9. 서비스 끝내기
        
1 이 입력되면 리스트에 추가할 아이템 정보를 키보드로 입력받아서 추가함
  사번 : 200 (empid : str)
  이름 : 홍길순 (empname : str)
  주민번호 : 851225-1234567 (empno : str)
  이메일 : hong77@test.com (email : str)
  전화번호 : 010-1234-5678 (phone : str)
  급여 : 3800000 (salary : int)
  직급 : 대리 (job : str)
  부서 : 개발부 (dept : str)
  => 사번은 키로 해서 딕셔너리에 직원정보를 리스트로 저장함
     사번 : [사번, 이름, 주민번호, 이메일, 전화번호, 급여, 직급, 부서]
2 입력시 :
    삭제할 사번 : 200
    => 딕셔너리에서 해당 사번의 아이템 제거함
    => '200 번 사번의 직원 정보가 삭제되었습니다.' 출력함
3 입력시 :
    딕셔너리의 각 아이템의 정보를 한줄씩 출력되게 함
    사번 : [리스트 정보]
    사번 : [리스트 정보]
    ....
4 입력시 :
    딕셔너리 상태 그대로 파일에 저장되도록 함
    저장할 파일명 : employees.dat
    ==> 'employees.dat 파일에 성공적으로 저장되었습니다.' 출력됨
5 입력시 :
    읽을 파일명 : employees.dat
    => 파일의 내용을 읽어서 딕셔너리(emp_dict)에 저장하고 출력되게 함
9 입력시 :
    while 문 끝내면서 프로그램 종료되게 함
    => 종료시 '직원 관리 프로그램을 종료합니다.' 출력함

함수명 : emp_process()
'''
import pickle

emp_dict = {}

def start():
    prompt = """
        *** 직원 정보 관리 서비스 ***
        1. 새 직원정보 추가
        2. 직원정보 삭제
        3. 전체 출력
        4. 파일에 저장
        5. 파일로 부터 직원정보 읽어오기
        9. 서비스 끝내기
        """    

    while True:
        print(prompt)
        num = int(input("메뉴 순번 입력: "))
        if num == 1:
            add()
        elif num == 2:
            dele_emp()
        elif num == 3:
            disp_emp()
        elif num == 4:
            save_emp()
        elif num == 5:
            read_emp()
        elif num == 9:
            print("직원 관리 프로그램을 종료합니다.")
            break

# 1. 새 직원 정보 추가
def add():
    empid = input('사번: ')
    empname = input('이름: ')
    empno = input('주민번호: ')
    email = input('이메일: ')
    phone = input('전화번호: ')
    salary = int(input('급여: '))
    job = input('직급: ')
    dept = input('부서: ')

    emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]
    print(f"{empname}의 정보가 저장되었습니다.")


# 2. 직원정보 삭제
def dele_emp():
    dele = input('삭제할 사번: ')
    if dele in emp_dict:
        del emp_dict[dele]
        print(f'{dele} 번 사번의 직원 정보가 삭제되었습니다.')
    else:
        print('해당 사번을 찾을 수 없습니다.')


# 3. 전체 출력
def disp_emp():
    if not emp_dict:
        print('등록된 정보 없음')
    else:
        for key, value in emp_dict.items():
            print(f'{key} : {value}\n')


# 4. 저장
def save_emp():
    with open('employees.dat', 'wb') as f:
        pickle.dump(emp_dict, f)
    print("employees.dat 파일에 성공적으로 저장되었습니다.")


# 5. 파일로 부터 일어오기
def read_emp():
    global emp_dict 
    try:
        with open('employees.dat', 'rb') as f:
            emp_dict = pickle.load(f)
        print('성공적으로 데이터 불러왔습니다.')
        disp_emp()
    except FileNotFoundError:
        print("읽어올 파일이 없습니다.")
