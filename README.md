# 코딩 유치원

## 개요

코딩 유치원에서는 약 5~6주동안 프로그래밍 언어에 대한 기초를 배운 후, 웹 애플리케이션의 원리 및 블로그 만들기, 실제로 배포하기 실습을 진행합니다. 배우실 언어는 다음과 같습니다:

- Python
- JavaScript
- HTML
- Django (✳︎언어는 아닙니다)

1. 개인 블로그를 제작하고 배포하는 것을 기본적인 목표로 합니다.

2. 디자인이나 전체적인 기획 등을 어느 정도 직접 해 주시면 좋을 것 같습니다. 디자인과 기획이 있다면 그것을 만드는 것을 도와드릴 수는 있지만, 디자인과 기획을 해 드리지는 않을 계획입니다.

3. 과정이 모두 끝난 후 Python과 JavaScript를 실생활에서 활용할 수 있고, 스스로 만든 블로그에 기능을 추가하거나, 스스로 만든 블로그를 편집할 수 있는 - 그리고 독학을 통해 새로운 독자적인 애플리케이션을 만들어나갈 수 있는 - 사람으로 거듭나게 되는 것을 목표로 하고 있습니다.

4. 저도 프로그래밍을 배운지 얼마 되지 않은 초보자이기에 같이 공부해나간다고 생각하시면 좋겠습니다. 실제로 아래의 내용들도 이미 다 알고 있는 것들이 아니라, 다시금 되짚어가면서 배운 것들을 공유하고자 하는 마음입니다. 그러니 수업이라기보다는 스터디라고 생각해주시고, 중간에 뭔가 막히거나 이상한 버그에 쩔쩔 매도 원래 저런 거구나 하고 이해해주시길 바랍니다 :)

## Meta

- 시간: 매주 화/목요일 오전 10시~12시(or 12시 30분)
- 장소: 서울대입구역 히든스페이스
- 개인 도메인(ex. jesse.kim)을 구매하여 실제로 배포해보는 것까지는 포함합니다.

## 목차

✳︎ 과제는 1~2주차까지는 직접, 3주차부터는 웬만하면 스터디 시간에 같이 진행할 예정입니다.
* 3주차 이후의 과정은 독립적인 강의 자료 없이 [my-first-blog](https://github.com/jessekim-ck/my-first-blog) 레포지토리에서 진행됩니다.

### 1주차: Python 및 JavaScript 기초

Python 및 JavaScript의 기본적인 기능성과 문법들에 대해 배웁니다. 두 언어를 동시에 배울 거예요.

- Installation & Introduction
- Basic Operations
- Data Type
- Conditional Statement
- Loop
- Function
- Class
- External Libraries
- 과제 1: 숫자 맞추기 게임
- 과제 2: Is Multiple?

### 2주차: Web Application 기초

웹 애플리케이션이 돌아가는 원리를 아주 간단하게 배우고, 프론트를 구성하는 언어인 HTML에 대해 배웁니다. 유튜브의 "생활코딩" 페이지에 관련 짧은 강의 영상들이 있으니, 심심할 때 한 번 보시면 아주 좋습니다.

- Client vs Server
- HTTP
- HTML: Head (Meta Information)
- HTML: Body (Tags)
- 과제 3: 자기 소개 페이지 만들기
- HTML: Script
- 과제 4: Todo Application 만들기

### 3주차: Django

서버를 구성하는 파이썬 기반의 프레임워크인 Django에 대해 배웁니다. 이제부터 실제 블로그를 만들어가기 시작합니다. [Django Girls Tutorial](https://tutorial.djangogirls.org/ko/)을 잔뜩 참고하여 진행할 예정입니다. 미리 둘러보고 오시면 아주 좋습니다.

- MVC (Model, View, Controller)
- Project Setup
- Models
- Views
- Templates
- Routing
- 과제 5: 메인 페이지 만들기

### 4주차: Django (2)

블로그의 나머지 부분을 완성합니다. 정확히 어떤 페이지가 생길지는 기획에 따라 다르겠습니다!

- 과제 6: 글 작성 페이지 만들기
- 과제 7: 글 편집 페이지 만들기
- 과제 8: 네비게이션 만들기
- 과제 9: 로그인/회원가입 기능 만들기

### 5주차: Deploy

기본적인 블로그가 완성되었습니다. 이제 누구나 웹을 통해 애플리케이션에 접근할 수 있도록 배포해보겠습니다. 아마존의 클라우드 서비스인 AWS를 이용합니다. 배포 과정은 저의 블로그에 정리해 놓았으니, 이 것을 따를 예정입니다. 모든 과정은 [저의 개인 블로그](https://blog.jesse.kim/category/6)에 정리되어 있습니다.

- EC2 Instance Setup
- Environment Setup
- RDS
- Nginx & uWSGI
- Route53
- ...

### 6주차~

업데이트하고 싶은 기능이 있거나, 추가적으로 전달드리고 싶은 것들이 있거나, 조금 더 배우고 싶은 것이 있으면 추가적으로 다루도록 하겠습니다.

후보들

- Python으로 엑셀 작업 자동화하기
- ...
