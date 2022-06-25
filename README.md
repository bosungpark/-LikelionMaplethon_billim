# 멋쟁이 사자처럼 단풍톤 - [빌림(林)의 숲]

## 실행 프로그램

📙🍁 https://billimsoop.herokuapp.com/ 🍁📙<br />

    🖐 서비스 소개

빌림(林)은 <b>전공책 대여 및 솔루션 공유 서비스</b>를 제공하는 플랫폼입니다.<br />
<img width="80%" src="https://user-images.githubusercontent.com/81094055/140632040-5992cd20-8c69-4312-b4c3-f119ee6a5f7c.jpg"/>
<br />

    🖐 개발자 소개 (오프라인 1팀)
<img width="80%" src="https://user-images.githubusercontent.com/81094055/140632077-087f7680-d3d2-4432-ada0-01f941d28f10.jpg"/>

## 주요 기능

* 코인 관련 기능

* 도서 등록 및 대여하기

* 필요한 도서를 관리자 메일을 통해 요청하기

* 전공문제 솔루션 공유 및 검색기능

* 마이페이지(유저의 코인, 도서 등록 및 대여 등의 정보를 관리하는 페이지)

* 계정 관련 기능

* 이미지가 없는 도서의 경우 크롤링을 통해 적절한 이미지를 등록해주는 기능

## 설치 방법

IDE는 VS Code를 기준으로 합니다.

깃에서 초기 파일을 내려 받는 방법 (VS code에서 빈 폴더 생성 후)

```
$ git clone https://github.com/bosungpark/LikelionMaplethon_billim.git
```

가상환경 생성하기 및 켜기

```
$ cd Likelion_Maplethon
$ python3 -m venv myvenv
$ source myvenv/bin/activate      //Mac
$ source myvenv/scripts/activate  // Windows
```

#### 프로젝트에 필요한 패키지 다운로드
```
$ pip install -r requirements.txt
```
#### .env 파일 생성 
  - 프로젝트 루트 디렉토리 (`/Likelion_Maplethon`)에 작성
```
$ touch .env
```
  - .env 파일 안에 SECRET_KEY='본인의 SECRET_KEY'를 추가해준다.
  - .env 파일 안에 EMAIL_HOST_USER ='도서 요청이 가게될 관리자용 메일 주소'를 추가해준다.
  - .env 파일 안에 EMAIL_HOST_PASSWORD ='도서 요청이 가게 될 관리자용 메일 비밀번호'를 추가해준다.

```
$ python manage.py migrate --run-syncdb
$ python manage.py makemigrations
$ python manage.py migrate
```

확인 및 실행

```
$ cd Likelion_Maplethon
$ python manage.py runserver
```

크롤링을 위한 웹드라이버 설치

  * 처음 사용하는 유저는 구글 크롬 버전에 맞는 webdriver를 설치해야 한다.
  * url창에 ‘chrome://version’를 입력하면 구글 크롬 버전을 확인할 수 있다. 
  * webdriver의 설치를 마쳤다면 book/views.py의 crawlor()함수에서 driver의 주소를 자신의 webdriver가 설치된 주소로 수정해준다.

## 사용 예제

1.자유롭게 도서 대출 및 솔루션 공유를 할 수 있다.


## 업데이트 내역

* 0.1.1(21.12.19~)
    
    
    버그 수정: 
    * 글을 마구 올리면, 그에 따라 코인이 무분별하게 생기는 오류 수정
    * 기존의 책 등록과 동시에 충전되는 방식을, 대여가 이루어지면 동록한 계정에 코인을 충전해주는 방식으로 수정
    * 코인이 0이하면 충전이 안 되는 오류 수정
    * 출간일 형식이 맞지 않을 시, 책이 등록되지 않는 오류 수정
    * 자신이 등록한 책을 스스로 대여할 수 있는 오류 수정
    
    추가 기능 구현:
    * 유저가 이미지를 추가하지 않고 책을 동록할 때, 크롤링 적용해서 이미지 불러오게끔 기능 수정

* 0.1.0
    * 개발완료(21.11.06)
    * Heroku를 이용한 첫 배포

* 0.0.1
    * 작업 진행 중(21.10.30)

## 아쉬운 점

* Selenium을 통해 크롤링을 하면, wed-driver를 설치하고 주소를 수정해야하는 번거로움이 있다. 다음에 비슷한 기능을 구현하게된다면 Beautifulsoup를 이용해 차이점을 느껴보고 싶다.

## 정보

블로그에서 영상 확인하기[@click](https://blog.naver.com/qkrqhtjd0806/222560916695) 

이메일: qkrqhtjd0806@naver.com

## 기여 방법

1. (<https://github.com/yourname/yourproject/fork>)을 포크합니다.
2. (`git checkout -b feature/fooBar`) 명령어로 새 브랜치를 만드세요.
3. (`git commit -am 'Add some fooBar'`) 명령어로 커밋하세요.
4. (`git push origin feature/fooBar`) 명령어로 브랜치에 푸시하세요. 
5. 풀 리퀘스트를 보내주세요.
