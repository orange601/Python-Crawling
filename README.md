# Python-Crawling
파이썬을 이용한 텍스트 이미지 크롤링

## 설치 ##
1. 파이썬을 직접 PC에 설치하기에는 버전 충돌 및 관리가 불편하다.
2. gooormide를 이용한 개발환경을 구성한다.

## goormide 사용 ##
- https://ide.goorm.io/ 접속, 무료

- 회원가입, 카카오톡 아이디 사용

- 컨테이너생성 및 실행 ( 파이썬 환경으로 실행됨 )

- BeautifulSoup 설치, 크롤링 라이브러리
  + pip install bs4

- google iamge download 라이브러리 다운로드받기
  + https://pypi.org/project/google_images_download/
  + pip install google_images_download

- Google image download 라이브러리 샘플 코드 ( https://google-images-download.readthedocs.io/en/latest/examples.html# )
````python
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
````

