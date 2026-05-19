# ComfyUI – On Complete Notifications

**한국어** | [English](./README.md)

> ComfyUI 생성이 끝나는 순간을 **이메일 / 사운드 / 웹훅** 으로 바로 알려드립니다.

긴 렌더링, 대량 배치, 밤샘 작업… 더 이상 탭을 새로고침하지 마세요. 워크플로우 끝에 노드 하나만 붙이면 ComfyUI가 알아서 알려줍니다.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/bobddadoo?style=social)](https://github.com/sponsors/bobddadoo)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/bobddadoo)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](./LICENSE.txt)

---

## ✨ 포함된 노드

| 노드 | 설명 |
|------|------|
| **OnCompleteEmailMe** | 생성 완료 시 Gmail 발송. 마지막 생성 이미지가 자동 첨부됩니다. |
| **OnCompletePlaySound** | 완료 시 사운드 알림 재생. |
| **OnCompleteWebhook** | HTTP 웹훅 발사. Discord, Slack, n8n, IFTTT, 자체 서버 등과 연동 가능. |

---

## 📦 설치

### 방법 A — ComfyUI Manager (권장)

1. **ComfyUI Manager** 열기
2. **Install via Git URL** 클릭
3. 다음 주소 붙여넣기: `https://github.com/bobddadoo/comfy-ui-on-complete-email-me`
4. ComfyUI 재시작

![설치 1](docs/images/install01.jpg)
![설치 2](docs/images/install02.jpg)

### 방법 B — 수동 설치

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/bobddadoo/comfy-ui-on-complete-email-me
```

이후 ComfyUI 재시작.

---

## 🚀 사용법

### OnCompleteEmailMe

![사용법 1](docs/images/usage01.jpg)

1. `sender_email` — 본인 Gmail 주소
2. `sender_password` — Gmail **앱 비밀번호** (계정 비밀번호 아님)
   생성 링크: [Google 앱 비밀번호](https://myaccount.google.com/apppasswords)
3. `recipient_emails` — 받을 사람 이메일 목록 (엔터로 구분)
4. `message` — 본문 메시지

마지막으로 생성된 이미지가 자동으로 첨부됩니다.

![사용법 2](docs/images/usage02.jpg)

### OnCompleteWebhook

1. 워크플로우 끝에 **OnCompleteWebhook** 노드 추가
2. `webhook_url` 에 알림 받을 엔드포인트 설정 (Discord 웹훅, Slack incoming webhook, 자체 서버 등)
3. 워크플로우 실행 — 생성 완료 시 자동으로 발사됩니다

### OnCompletePlaySound

워크플로우 끝에 노드를 추가하면 작업이 끝날 때 사운드를 재생합니다.

---

## ❓ FAQ

**Q. 앱 비밀번호를 입력해도 이메일이 전송되지 않습니다.**

보통 다음 에러로 나타납니다:

```
Failed to send email: 'ascii' codec can't encode character '\xa0' in position 25: ordinal not in range
```

붙여넣기 과정에서 `\xa0` (non-breaking space) 가 끼어든 경우입니다. 앱 비밀번호를 **직접 타이핑** 으로 다시 입력하거나, 공백을 꼼꼼히 제거한 뒤 다시 시도하세요.

---

## 🗓️ 업데이트

**2025-01-15**
- 📎 마지막으로 생성된 이미지를 이메일에 자동 첨부
- 🔊 **OnCompletePlaySound** 노드 추가

![이미지 첨부 예시](https://github.com/user-attachments/assets/84c1ef4a-2996-4a69-b7b9-e8c7416cc731)

---

## 💛 후원하기

이 노드들이 렌더링 지키느라 모니터 앞에 묶여있던 시간을 돌려줬다면, 후원을 고려해주세요. 더 많은 ComfyUI 도구 제작에 직접 쓰입니다.

- ❤️ [GitHub Sponsors](https://github.com/sponsors/bobddadoo)
- ☕ [Ko-fi](https://ko-fi.com/bobddadoo)

커피 한 잔도 큰 힘이 됩니다. 감사합니다 🙏

---

## 📄 라이선스

**GPL-3.0** 라이선스를 따릅니다. 자세한 내용은 [LICENSE.txt](./LICENSE.txt) 참조.
