import smtplib
from VDA.Engine import StartUp
from VDA.TakeCommand import CommandTaker


class FileReader:
    """It reads a file containing email address and password of sender """
    def file_reader(self):
        with open("password.txt", "r") as f:
            id = eval(f.read())
            if id[0] == "None" or id[1] == "None":
                email_address = input("Enter you email address : ")
                password = input("Enter you email password : ")
                id = [email_address, password]
                with open("password.txt", "w") as g:
                    g.write(str(id))
        return id


class EmailReceiver:
    """It reads a contact file containing emails of receiver"""
    def email_receiver(self):
        with open('emailcontact.txt', "r") as file:
            receiver_file = file.read()
            list_file = receiver_file.split('\n')
            print("Give me the name of reciver!!!")
            StartUp().Speak("Give me the name of reciver!!!")

            def correction():  # to prevent program from finish when varible(reciver) got "None"
                receiver1 = CommandTaker().MicroPhone()
                if receiver1 == "None":
                    StartUp().Speak("Say the name of receiver again!!")
                    print("Say the name of receiver again!!")
                    correction()
                else:
                    return receiver1

            receiver = correction()
            print("User said:", receiver)
            for i in list_file:
                if receiver in i:
                    to = i
            print("Receiver:", to)
            return to


class EmailSender(FileReader, EmailReceiver):
    """It takes email address and password of sender and sent it to email address selected"""

    def __init__(self, Content):
        self.content = Content
        self.file_reader()
        self.email_receiver()

    def file_reader(self):
        self.ID = super().file_reader()

    def email_receiver(self):
        self.emailReceiver = super().email_receiver()

    def SendEmail(self):  # It send email to a selected contact
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.ID[0], self.ID[1])  # ID[0]=Email address  ID[1]=PASSWORD
        server.sendmail(self.ID[0], self.emailReceiver, self.content)
        server.close()
