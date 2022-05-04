# 크롤링 #
with python

## goormIDE를 이용한 Python 개발 환경 Setting ##
- https://ide.goorm.io/ 접속
- 컨테이너 생성시 python으로 설정
- https://pypi.org/project/google_images_download/ 파이썬을 이용한 크롤링 라이브러리
- 위 사이트 접속 후 설치방법 확인
````
pip install google_images_download
````

## google.py ##
````python
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"원더걸스 유빈, 세븐틴 버논, 노을 전우성, 펜타곤 진호, 하석진, 홍대광, 홍진경, 프로미스나인 장규리, 우주소녀 연정"
             , "limit": 20
             , "print_urls": True
             , "format": "jpg"
            }   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
````

1. https://google-images-download.readthedocs.io/en/latest/arguments.html arguments의 문서를 확인한다.
2. arguments의 원하는 keyword와 limit 개수를 정한다. format은 jpg만 다운로드한다.
3. python google.py 실행하면 download 폴더에 크롤링 된 이미지 파일이 생성된다.

```
┌───────────────────────────────────────────────┐
                                       _       
     __ _  ___   ___  _ __ _ __ ___   (_) ___  
    / _` |/ _ \ / _ \| '__| '_ ` _ \  | |/ _ \ 
   | (_| | (_) | (_) | |  | | | | | |_| | (_) |
    \__, |\___/ \___/|_|  |_| |_| |_(_)_|\___/ 
    |___/                                      
			     🌩 𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
└───────────────────────────────────────────────┘
```

# goormIDE
Welcome to goormIDE!

goormIDE is a powerful cloud IDE service to maximize productivity for developers and teams.  
**DEVELOP WITH EXCELLENCE**  

`Happy coding! The goormIDE team`


## 🔧 Tip & Guide

* Command feature
	* You can simply run your script using the shortcut icons on the top right.
	* Check out `PROJECT > Common/Build/Run/Test/Find Command` in the top menu.
	
* Get URL and Port
	* Click `PROJECT > URL/PORT` in top menu bar.
	* You can get default URL/Port and add URL/Port in the top menu.

* Useful shortcut
	
| Shortcuts name     | Command (Mac) | Command (Window) |
| ------------------ | :-----------: | :--------------: |
| Copy in Terminal   | ⌘ + C         | Ctrl + Shift + C |
| Paste in Terminal  | ⌘ + V         | Ctrl + Shift + V |
| Search File        | ⌥ + ⇧ + F     | Alt + Shift + F  |
| Terminal Toggle    | ⌥ + ⇧ + B     | Alt + Shift + B  |
| New Terminal       | ⌥ + ⇧ + T     | Alt + Shift + T  |
| Code Formatting    | ⌥ + ⇧ + P     | Alt + Shift + P  |
| Show All Shortcuts | ⌘ + H         | Ctrl + H         |

## 💬 Support & Documentation

Visit [https://ide.goorm.io](https://ide.goorm.io) to support and learn more about using goormIDE.  
To watch some usage guides, visit [https://help.goorm.io/en/goormide](https://help.goorm.io/en/goormide)
