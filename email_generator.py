import csv
import email_sender
import re
import os


def email_creator(sender_email,password,email_subject,filename):
    path = os.getcwd()
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        f = open("email.txt", "r")
        content = f.read()
        namereg = re.compile(r'John Doe')
        a = namereg.search(content)
        for cname, pname,email in reader:
            print(pname)
            if (pname != '' and cname != ''):
                print(f"Sending email to {pname} at {email} from {cname}")
                result = re.sub(r'John Doe', str(pname), str(content))
                result = re.sub(r'XYZ Inc', str(cname), str(result))
                #filename = "./emails/file_{}_{}.txt".format(pname,email)
                receiver_email = email
                message = result
                if(email_sender.send_email(sender_email,receiver_email,password,email_subject,message)):
                    try:
                        f = open(f'{path}/logs.txt', 'a')
                        f.write(f"Successfully sent email to {pname} from {cname} at {email}\n ")
                        f.close()
                    except FileNotFoundError:
                        pass
                else:
                    try:
                        f = open(f'{path}/logs.txt', 'a')
                        f.write(f"Could not send email to {pname} from {cname} at {email}\n ")
                        f.close()
                        f = open(f'{path}/updated_file.csv', 'a')
                        f.write(f'{cname},{pname},{email} \n')
                        f.close()
                    except FileNotFoundError:
                        pass


if __name__ == '__main__':
    path = os.getcwd()
    sender_email = input("Enter email address you wish to use: ")  # Enter your address
    password = input("Type your password and press enter: ")
    email_subject = input("Please Enter your subject line: ")
    print("Note, the csv format should be the following: Company Name,Contact Name,Contact Information")
    filename = input("Please enter the name of the csv.(Insert path if the csv does not exist in the same directory as the program): ")
    f = open(f'{path}/updated_file.csv', 'w')
    f.write(f'Company Name,Contact Name,Contact Information \n')
    f.close()
    email_creator(sender_email,password,email_subject,filename)
    print("The updated csv file only consits of the details of people to which the email was not successfully delivered to.")