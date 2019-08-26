# custom_email_generator
This program parses your csv file which contains information of the people from companies you want to send emails to and replaces an email template with the custom information and sends out the email. 

To run the program, from the terminal while in project file type: python3 email_generator.py 

The inputs that will be asked for are:
1) Sender Email address.
2) Password. 
3) Email Subject. 
4) Name of CSV file or path if it is not in directory.

CSV file should contain the following details in the same order:
Company Name, Receiver Name(Along with salutations if needed), email address.


The output will contain a log file witrh details of emails sent and also and updated csv with only the details of the people to which the email was not successfully delivered to. 


* Note :  Before using this app you will have to enable your gmail account to allow apps with low security access.You can do that on this link: https://myaccount.google.com/lesssecureapps
