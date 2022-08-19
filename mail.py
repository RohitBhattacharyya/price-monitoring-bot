import smtplib as slib
from cfg import read_cfg


class Mailing:
    def __init__(self):
        hostInfo = read_cfg ('cfg.ini', 'mail')
        self.sender = hostInfo ['mailid']
        self.password = hostInfo ['password']

        self.receivers = read_cfg ('cfg.ini', 'recievers')

        self.server = slib.SMTP ('smtp.gmail.com', 587)

        self.server.starttls ()

        try:
            self.server.login (self.sender, self.password)
            print ('\033[92m' + f'[SUCCESS] Logged in to the mail server as {self.sender}' + '\033[0m')

        except slib.SMTPAuthenticationError as e:
            print ('\033[91m' + f'[ERROR] {e}' + '\033[0m')
            # print in bold red
            print ('\033[91m' + '[ERROR] Invalid credentials' + '\033[0m')
            exit ()

    def createMsg (self, objName: str, objPrice: str, priceLimit: str, delCost: str, sendMail: bool = False):
        # TODO: Create a message to be sent to the user
        Subject = 'Notification from the Price Monitoring Bot'
        Body = f'''
Hello,

This is a notification from the Price Monitoring Bot. The price of {objName} has dropped below the price limit ({priceLimit}). You can buy it now at {objPrice}. The delivery cost is {delCost}.

Regards,
Price Monitoring Bot'''

        if sendMail:
            self.sendMail (Subject, Body)

        return (Subject, Body)

    def sendMail (self, Subject: str, Body: str):
        self.msg = f'Subject:{Subject}\n\n{Body}'

        try:
            for rmail in self.receivers:
                self.server.sendmail (self.sender, rmail [1], self.msg)

                print ('\033[92m' + f'[SUCCESS] Mail sent to {rmail}' + '\033[0m')

        except Exception as e: # ERROR
            print ('\033[91m' + f'[ERROR] {e}' + '\033[0m')

        self.server.quit ()


def main ():
    inf = open ('init.txt', 'r').readlines () # [0] = Sender's email, [1] = password, [2] = Receiver's email
    mail = Mailing (inf [0], inf [1], inf [2])

    mail.createMsg ('Grey Women Sling Bag', 'Rs. 394', 'Rs. 400', 'Rs. 0', True)


if __name__ == '__main__':
    main ()


# THE END
