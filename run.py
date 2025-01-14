import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders

def encode_filename(filename):
    return Header(filename, 'utf-8').encode()

def send_email(sender_email, sender_password, recipient_email, subject, body, attachments=None):
    try:
        # 이메일 메시지 생성
        msg = MIMEMultipart()
        msg['From'] = sender_email
        print(msg['From'])

        msg['To'] = recipient_email
        print(msg['To'])

        msg['Subject'] = Header(subject, 'utf-8')
        print(msg['Subject'])


        # 본문 추가 (UTF-8로 인코딩)
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        print(body)

        # SMTP 서버 연결 및 로그인
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # TLS 보안 시작

            print(1)

            print(sender_email)
            print(sender_password)

            server.login(sender_email, sender_password)  # 로그인
            print(2)

            # 이메일 전송
            server.send_message(msg)
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# 사용 예제
if __name__ == "__main__":

    sender_email = "hyunamy19@gmail.com"
    sender_password = "odmt hyyk ayjw nxwi"
    recipient_email = "hyunamy@naver.com"
    subject = "test"
    body = "testbody"

    send_email(sender_email, sender_password, recipient_email, subject, body)
