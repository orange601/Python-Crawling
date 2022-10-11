# 파이썬을 이용한 크롤링 #
파이썬으로 작성된 google_images_download 라이브러리를 통해 크롤링한다.
- pip install google_images_download
- https://pypi.org/project/google_images_download/

## 파이썬 설치 및 개발 환경 Setting ##
- 파이썬을 Local에 설치해도 상관없지만, goormIDE를 통해 개발환경을 갖춘다.
- goormIDE란 Cloud IDE이다. 브라우저를 통해 통합 개발환경을 설정하고 사용할 수 있다.
- https://ide.goorm.io/

## goormIDE를 이용한 Python 개발 환경 Setting ##
1. goormIDE 사이트 접속
2. 새 컨테이너를 생성하고, 생성시 python으로 설정
3. google_images_download를 설치한다.
````
pip install google_images_download
````

## google.py ##
1. pip을 통해 google_images_download를 다운 받으면, google.py이 생성이 된다.
2. 파일을 열어보면 아래와 같이 설정되어있다.
````python
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"원더걸스 유빈, 세븐틴 버논, 트와이스 사나"
             , "limit": 20
             , "print_urls": True
             , "format": "jpg"
            }   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
````
3. keywords에 원하는 검색어를 입력하고 만약 여러개의 검색어가 필요하다면 콤마(,)로 구문지어 입력한다.
4. limit에 다운로드를 원하는 개수를 지정할 수 있다.
5. format은 jpg만 다운로드한다.
6. 전체적인 내용은 https://google-images-download.readthedocs.io/en/latest/arguments.html arguments의 문서를 확인한다.
7. python google.py 실행하면 download 폴더가 생성되고, 크롤링 된 이미지 파일이 생성된다.
8. 완료

## 파이썬 더 알아보기 ##

### 1. 사용 ###

#### 1.1 다운로드 ####
* https://www.python.org/downloads/windows/  
* Windows x86-64 executable installer(Windows x86-64 실행 가능 설치 패키지 프로그램) 다운로드

#### 1.2 설치 ####
* Add Python 3.9 to Path 체크 후 Install Now  
> Path를 자동으로 설정

* 윈도우 재부팅 후 Path 설정됨

* 설치 확인
> CMD - python입력

### 2. 기본문법 ###

#### 2.1 들여쓰기  ( 스코프 결정 ) ####

* 문법적인 강제사항

* 코드 블럭을 구성하기 위해 if, for, class, def 등등 을 작성하면서 나오는 : 다음 아랫줄은 들여쓰기를 해야한다.

* 블록 내에서는 들여쓰기 칸 수가 같아야 한다. 공백과 탭을 섞어쓰면 안된다.

```python
for i in range(10):
     print(i)
     print(i + 1)
```

#### 2.2 주석 ####

```python
#이건주석입니다.
if i > 0:
     print("OK")
```

#### 2.3 세미콜론 ####

* 필수사항X

* 여러구문을 같은 줄에 쓸때 사용하기도 한다.

```python
print('Hello'); print('world')
```

#### 2.4 import ####

* 라이브러리 전체 import

```python
import math
math.sqrt(81) #제곱근
```

* 라이브러리 함수만 import

```python
from sqrt import math
sqrt(81)
```

* 함수 별칭 사용이 가능하다

```python
from sqrt import math as dou
dou(81)
```

#### 2.5 데이터타입 ####

##### 2.5.1 스칼라 데이터 타입 ####

* int 
```python
>>> int(3.5)
3
>>> int(-3.5)
-3
>>> int(True)
1
>>> int(False)
0
>>> int("500")
500
>>> int("1000",3)
27
```

* float
```python
>>> float(7)
7.0
>>> float("1.618")
1.618
>>> float(True)
1.0
>>> float(False)
0.0
```

* None
```python
>>> None
>>> 
>>> a = None
>>> a is None
True
```

* bool
```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True
>>> bool(-1)
True
>>> bool("")
False
>>> bool("abcde")
True
```
