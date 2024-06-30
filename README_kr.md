# Comfy-UI on-complete-email-me

[English](/) | [한국어](./README_kr.md)
---

Comfy-ui 에서 이미지 생성이 완료되면 Gmail로 이메일을 발송하는 기능입니다.

## 목차
- [설치](#설치)
- [사용법](#사용법)
- [라이선스](#라이선스)

## 설치

1. Git 주소 복사
![Image 1](docs/images/install01.jpg)
2. Comfy-UI-Manager 클릭
3. Install via GIT URL 클릭
![Image 2](docs/images/install02.jpg)
4. Git 주소 붙여넣기
5. Comfy-UI 재시작

## 사용법

![Image 3](docs/images/usage01.jpg)
1. `sender_email`에 자신의 Gmail 이메일 주소를 입력합니다.
2. `sender_password`에 Gmail 앱 비밀번호를 생성하여 입력합니다 (Gmail 계정 비밀번호를 입력하지 마세요).
   - 앱 비밀번호 생성 방법 링크: [Google 앱 비밀번호](https://myaccount.google.com/apppasswords)
3. 이메일 받을 주소 목록을 입력합니다 (엔터로 구분).
4. 전달받을 메세지를 입력합니다.

![Image 4](docs/images/usage02.jpg)
OnCompleteWebhook 노드
새로운 노드인 OnCompleteWebhook를 추가했습니다. 이 노드는 특정 작업이나 이벤트가 완료되면 웹훅 알림을 보낼 수 있도록 해줍니다.

**사용법**

1. OnCompleteWebhook 노드 생성:

워크플로우에서 OnCompleteWebhook 노드를 생성하는 지침을 따르세요.

2. 웹훅 URL 구성:

알림을 받을 엔드포인트로 웹훅 URL을 설정하세요.

3. 노드 트리거:

원하는 작업이나 이벤트가 완료되면 이 노드가 트리거되도록 설정하세요.
OnCompleteWebhook 노드를 사용하면 외부 서비스와 통합하여 다양한 프로세스의 완료에 대한 알림을 받을 수 있습니다.

워크플로우를 업데이트하고 새로운 기능을 확인해보세요.

## 라이선스

이 프로젝트는 GPL-3.0 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.

