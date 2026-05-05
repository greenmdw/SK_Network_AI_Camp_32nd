# app 만드는 종류
#   - CLI(command line interface): 터미널로 실행
#   - GUI(graphic user interface): 메뉴/툴바 클릭해서 실행

import fileio_study.fileio_module_study as fms


# Cli 방식의 메뉴 출력용 함수
def menu():
    print("-------------INITIATE----------------")
    prompt = """
    실행할 메뉴에 맞는 번호 클릭하세요.
    1. 파일에 저장하기 테스트
    2. 정해진 경로에 파일 생성
    3. 파일에 append 
    4. 파일 read
    5. while 문 테스트
    6. while 문 + unicode
    7. 디렉토리 다루기
    10. 리스트에 내용 저장(freadlines)
    9. 메뉴 종료
    11. 컬렉션 아이템들을 파일에 저장
    12. 바이너리 파일 저장 pickle.dump
    13. 바이너리 파일 로드 pickle.load
    """

    while True:
        print(prompt)
        no = int(input("실행 원하는 메뉴 번호 입력: "))
        
        if no == 1:
            fms.test_fwrite()
        if no == 2:
            fms.test_fwrite2()
        if no == 3: 
            fms.test_fwrite3()
        if no == 4:
            fms.test_fread()
        if no == 5:
            fms.test_while()
        if no == 6:
            fms.test_while_unicode()
        if no == 7:
            fms.test_osmodule()
        if no == 10:
            fms.test_readlines()
        if no == 11:
            fms.test_writelines()
        if no == 12: 
            fms.test_binary()
        if no == 13:
            fms.test_binary2()
        if no == 9:
            break
    
    print("------------------END-----------------")
    return



if __name__ == '__main__':
    menu()
    print('program end')