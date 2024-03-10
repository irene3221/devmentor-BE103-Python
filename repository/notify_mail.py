import smtplib #用於連接SMTP服務器並發送郵件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #MIMEMultipart類別能夠讓電子郵件的格式包含純文字或HTML的內容

class EmailNotification:
    def send_notification(self, recipient, message):
        # 設置郵件內容
        msg = MIMEMultipart()
        msg['From'] = "123@example.com"
        msg['To'] = recipient
        msg['Subject'] = "Notification"

        body = message
        msg.attach(MIMEText(body, 'plain'))

        # 連接SMTP服務器並發送郵件
        try:
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()  # 建立加密傳輸
            server.login("your_email@example.com", "your_password") # 登入寄件者gmail
            text = msg.as_string()  #轉換為str，以便於發送
            server.sendmail("your_email@example.com", recipient, text)
            server.quit()
            print("Email notification sent successfully")
        except Exception as e:
            print("Failed to send email notification:", str(e))

