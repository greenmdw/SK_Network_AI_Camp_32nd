# path : loop\\while_mission.py
# module : loop.while_mission

# Global Variable
sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]


def sungjuk_process():
    prompt = """
            *** 원하는 메뉴 번호를 선택하세요. ***
            1. 추가
            2. 삭제
            3. 출력
            4. 끝내기
        """
    print(prompt)
    while True:
        no = int(input("메뉴 숫자만 입력: "))
        if no == 1:
            add()
        elif no == 2:
            delete()
        elif no == 3:
            dis()
        elif no == 4:
            print("성적관리 프로그램이 종료되었습니다.")
            break
        else:
          print("잘못된 접근입니다. 다시 입력하세요")


# 1. 추가
def add():
    sno = int(input("번호: "))
    sname = input('이름: ')
    score = int(input("점수: "))
    sungjuk_list.append([sno, sname, score])

    print("새로운 학생정보가 추가되었습니다.")
    print(sungjuk_list)

# 2. 삭제
def delete():
    print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
    
    while True:
        deln = int(input('제거할 아이템의 순번: '))
        if 0 < deln < len(sungjuk_list):
            sungjuk_list.pop(deln - 1)
            break
        else:
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
            break
 
    print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
    
# 3. 출력
def dis():
    print("저장된 리스트 정보 아이템별로 출력")
    for i in range(len(sungjuk_list)):
        print(f'{i} : {sungjuk_list[i]}')

