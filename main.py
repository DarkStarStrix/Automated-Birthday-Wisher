
# Extra Hard Starting Project #

import smtplib
import datetime as dt
import random
import pandas
# 1. Update the birthdays.csv
with open("birthdays.csv") as file:
    data = file.readlines()
    print(data)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
print(now)
today = (now.month, now.day)
print(today)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
print(letter)
with open(letter) as file:
    letter_data = file.read()
    print(letter_data)
    letter_data = letter_data.replace("[NAME]", "Angela")
    print(letter_data)


# 4. Send the letter generated in step 3 to that person's email address.

my_email = "emailishere13@gmail.com"
password = "fflfykmycicmctni"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Happy Birthday!\n\n{letter_data}")
