# ComfyUI – On Complete Notifications

[한국어](./README_kr.md) | **English**

> Get notified the moment your ComfyUI generation finishes — by **email**, **sound**, or **webhook**.

Long renders, queued batches, or overnight jobs: stop refreshing the tab. Drop one node at the end of your workflow and ComfyUI will tell you when it's done.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/bobddadoo?style=social)](https://github.com/sponsors/bobddadoo)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/bobddadoo)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](./LICENSE.txt)

---

## ✨ Nodes Included

| Node | What it does |
|------|--------------|
| **OnCompleteEmailMe** | Sends a Gmail when generation finishes. Attaches the last generated image. |
| **OnCompletePlaySound** | Plays a sound notification on completion. |
| **OnCompleteWebhook** | Fires an HTTP webhook so you can integrate with Discord, Slack, n8n, IFTTT, your own server, etc. |

---

## 📦 Installation

### Option A — ComfyUI Manager (recommended)

1. Open **ComfyUI Manager**
2. Click **Install via Git URL**
3. Paste: `https://github.com/bobddadoo/comfy-ui-on-complete-email-me`
4. Restart ComfyUI

![Install step 1](docs/images/install01.jpg)
![Install step 2](docs/images/install02.jpg)

### Option B — Manual

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/bobddadoo/comfy-ui-on-complete-email-me
```

Then restart ComfyUI.

---

## 🚀 Usage

### OnCompleteEmailMe

![Usage step 1](docs/images/usage01.jpg)

1. `sender_email` — your Gmail address.
2. `sender_password` — a **Gmail App Password** (not your account password).
   Create one at [Google App Passwords](https://myaccount.google.com/apppasswords).
3. `recipient_emails` — list of recipients (one per line, separated by Enter).
4. `message` — body text for the email.

The last generated image is attached automatically.

![Usage step 2](docs/images/usage02.jpg)

### OnCompleteWebhook

1. Add the **OnCompleteWebhook** node at the end of your workflow.
2. Set `webhook_url` to your endpoint (Discord webhook, Slack incoming webhook, your own server, …).
3. Run the workflow — the node fires once generation completes.

### OnCompletePlaySound

Add the node at the end of your workflow to play a sound when the run finishes.

---

## ❓ FAQ

**Q. I entered the app password but emails aren't sending.**

The error usually looks like:

```
Failed to send email: 'ascii' codec can't encode character '\xa0' in position 25: ordinal not in range
```

This means a non-breaking space (`\xa0`) snuck into the app password when you pasted it. Re-type the app password manually (no copy/paste) or carefully strip the spaces, and try again.

---

## 🗓️ Changelog

**2025-01-15**
- 📎 Attach the last generated image to the email.
- 🔊 Added **OnCompletePlaySound** node.

![Image attachment example](https://github.com/user-attachments/assets/427d945a-10da-41eb-9579-416952885c85)

---

## 💛 Support this project

If these nodes saved you from babysitting renders, consider sponsoring — it directly funds more ComfyUI tooling.

- ❤️ [GitHub Sponsors](https://github.com/sponsors/bobddadoo)
- ☕ [Ko-fi](https://ko-fi.com/bobddadoo)

Even a one-time coffee helps. Thanks 🙏

---

## 📄 License

Licensed under **GPL-3.0**. See [LICENSE.txt](./LICENSE.txt) for details.
