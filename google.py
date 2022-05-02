from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"원더걸스 유빈, 세븐틴 버논, 노을 전우성, 펜타곤 진호, 하석진, 홍대광, 홍진경, 프로미스나인 장규리, 우주소녀 연정"
             , "limit": 20
             , "print_urls": True
             , "format": "jpg"
            }   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images