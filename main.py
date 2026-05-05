# main 함수


import fileio.fileio_mission as fi
import loop.while_mission as lw

def menu():
    prompt = '''
	*** 파이썬 과제 1 ***
	1. while 실습문제
	2. fileio 실습문제
	9. 과제 실행 테스트 끝내기
     '''
    print(prompt)

    while True:
        no = int(input('실행할 과제 선택(9번 테스트 끝내기): '))
        if no == 1:
            lw.sungjuk_process()
        elif no == 2:
            fi.start()
        elif no == 9:
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요")



if __name__ == '__main__':
    print('-----------------INITIATE SYSTEM--------------')
    menu()
    PRINT('-------------------END SYSTEM-----------------')