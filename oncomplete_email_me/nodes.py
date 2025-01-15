import requests
import numpy as np  # NumPy를 가져옵니다
import smtplib
import os
import comfy.utils
import re
import pygame
from PIL import Image  # Pillow의 Image 모듈 가져오기
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

data = b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86'  # 일본어 유니코드 문자열의 바이너리


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))


def send_gmail(sender_email, sender_password, recipient_emails, subject, body, attachments=None, text_type='plain'):
    try:
        # Convert recipient emails to a list
        recipient_list = [email.strip() for email in recipient_emails.split(',') if email.strip()]

        # Create email message with multipart
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_list)

        # Attach the email body
        msg.attach(MIMEText(body, text_type, 'utf-8'))

        # Add attachments if any
        if attachments:
            for attachment in attachments:
                if os.path.isfile(attachment):
                    with open(attachment, 'rb') as file:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(file.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename="{os.path.basename(attachment)}"'
                        )
                        msg.attach(part)
                else:
                    print(f"Attachment not found: {attachment}")

        # Connect to SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_list, msg.as_string())

        print("Email sent successfully!")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


class OnCompleteEmailMe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", ),
                "sender_email": ("STRING", {
                    "multiline": False,
                    "default": "sender_email_address@gmail.com"
                }),
                "sender_password": ("STRING", {
                    "multiline": False,
                    "input_type": "PASSWORD",
                    "default": "password"
                }),
                "recipient_emails": ("STRING", {
                    "multiline": True,
                    "default": "recipient_email1@gmail.com\nrecipient_email2@gmail.com",
                }),
                "message": ("STRING", {
                    "multiline": True,
                    "default": "Hello, this is a test email from ComfyUI!",
                })
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "on_complete_email_me"
    OUTPUT_NODE = True
    CATEGORY = "utils"
    

    def on_complete_email_me(self, images, sender_email, sender_password, recipient_emails, message):
        attachments = []

        # 마지막 이미지를 첨부할지 여부를 확인        
        print("Attatching the last processed image...")

        # ComfyUI 이미지 데이터를 NumPy 배열로 변환
        image_data = images[-1]
        if isinstance(image_data, np.ndarray):
            image_array = image_data
        else:
            image_array = np.asarray(image_data)

        # NumPy 배열을 uint8로 변환
        if image_array.dtype != np.uint8:
            # 데이터가 [0, 1] 범위라면 255를 곱하고 uint8로 변환
            if image_array.max() <= 1.0:
                image_array = (image_array * 255).astype(np.uint8)
            else:
                raise ValueError("Unsupported data range. Ensure values are in the range [0, 1] or uint8.")

        # NumPy 배열이 RGB인지 확인
        if len(image_array.shape) == 3 and image_array.shape[2] in [3, 4]:
            pil_image = Image.fromarray(image_array[:, :, :3])  # 알파 채널 제거
        elif len(image_array.shape) == 2:  # Grayscale 이미지
            pil_image = Image.fromarray(image_array)
        else:
            raise ValueError("Unsupported image array format")

            # 파일 경로와 디렉토리 설정
        tmp_dir = "C:\\tmp"
        last_image_path = os.path.join(tmp_dir, "last_processed_image.jpg")

        # 디렉토리가 존재하지 않으면 생성
        os.makedirs(tmp_dir, exist_ok=True)

        # PIL 이미지를 파일로 저장
        pil_image.save(last_image_path, "JPEG")
        attachments.append(last_image_path)

        subject = "ComfyUI OnComplete Email"
        body = message

        # 이메일 전송 로직
        success = send_gmail(sender_email, sender_password, recipient_emails, subject, body, attachments=attachments)

        print(f"Email sending success: {success}")
        return {}
    
# Integration with ComfyUI
class OnCompleteWebhook:
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):        
        return {
            "required": {
                "images": ("IMAGE", ),
                "sender_email": ("STRING", {
                    "default": "sender_email_address@gmail.com"
                }),
                "sender_password": ("STRING", {
                    "multiline": False,
                    "input_type": "PASSWORD",
                    "default": "password"
                }),
                "recipient_emails": ("STRING", {
                    "multiline": True,
                    "default": "recipient_email1@gmail.com\nrecipient_email2@gmail.com",
                }),
                "message": ("STRING", {
                    "multiline": True,
                    "default": "Hello, this is a test message from ComfyUI!"
                })
            },
            "optional": {
                "": ("LABEL", "Gmail ONLY SEND EMAIL")
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "on_complete_webhook"
    OUTPUT_NODE = True
    CATEGORY = "notify"

    def on_complete_webhook(self, images, webhook_type, webhook_url, message):
        pbar = comfy.utils.ProgressBar(images.shape[0])
        step = 0
        for image in images:
            pbar.update_absolute(step, images.shape[0])
            #when last image is processed, send email
            if step == images.shape[0]-1:
                if webhook_type == "GET":
                    response = requests.get(webhook_url, params={"message": message})
                else:
                    response = requests.post(webhook_url, json={"message": message})

                # Print the status code of the response
                print('Status Code:', response.status_code)
                # Print the response headers
                print('Headers:', response.headers)
                # Print the response body
                print('Response Body:', response.text)        
            step += 1
        return { "response": response.text }
    


class OnCompletePlaySound:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):        
        return {
            "required": {
                "images": ("IMAGE", )
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "on_complete_playsound"
    OUTPUT_NODE = True
    CATEGORY = "notify"

    def on_complete_playsound(self, images):
        # Play sound
        currentFolder = os.path.dirname(os.path.abspath(__file__))
        assetFolder = os.path.join(currentFolder, "assets")

        pygame.init()
        pygame.mixer.music.load(os.path.join(assetFolder, "finished.mp3"))
        pygame.mixer.music.play()
        return { }
    

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OnCompleteEmailMe": OnCompleteEmailMe,
    "OnCompleteWebhook": OnCompleteWebhook,
    "OnCompletePlaySound": OnCompletePlaySound
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OnCompleteEmailMe": "OnCompleteEmailMe Prompts",
    "OnCompleteWebhook": "OnCompleteWebhook Prompts",
    "OnCompletePlaySound": "OnCompletePlaySound Prompts"
}
