import re
import webbrowser
import smtplib, ssl
class automation:
    list_urls = []
    def extractsurls(self):


        name = input('Enter file name : ')
        with open(name, 'r') as f:
            content = f.read()
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                              content.lower())
            print("This are the list : ")
            for i in urls:
                self.list_urls.append(i)
            print(self.list_urls)

            for i in self.list_urls:
                webbrowser.open_new_tab(i)


    def sendemail(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "fakesweta.12@gmail.com"
        receiver_email = input("enter a Receiver email : ")
        password = input("Type your password and press enter: ")
        message = """\
        Subject: Please check your email
        Hello this is aditya
        from a fake account please approved
        after  completing today task we can
        go home
        its really urgent ."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email Sent !!! ")


if __name__ == '__main__':
    obj = automation()
    print('1. Fetch URL\n2. Send Email')
    choice = input("Enter your choice :")

    if choice == '1':
        obj.extractsurls()
    if choice == '2':
        obj.sendemail()
