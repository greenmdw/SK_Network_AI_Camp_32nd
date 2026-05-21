# mypackage
간단한 Python package 만들어 사용하기 예제

# 기능
sum()
sub()
mul()
div()
mod()
max()
min()
strlen()
hello()

# 프로젝트 구조
python_package/
|- REAME.md
|- setup.py
|- pyproject.toml
|- my_packages
    |- my_module.py
    |- message.py
    |- init.py

# 패키지 설치
pip install .

# 패키지 설치 확인
가상환경 폴더\Libs패키지명 설치 확인
pip list

pip show my_packages

# 배포용 wheel 파일 생성
...> python -m build
=> build/ 폴더 생성