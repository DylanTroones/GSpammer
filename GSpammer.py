# Coded By DylanTroones.

import smtplib, os, sys


print("""


 ██████╗ ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗
██╔════╝ ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║  ███╗███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║   ██║╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚██████╔╝███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝(By DylanTroones)


""")

username = input("[?] Enter Your Gmail: ")
passw = input("[?] Enter Your Password: ")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(username, passw)
    print("[-] Logged In Successfully!")

except smtplib.SMTPAuthenticationError:
    print("[!] Wrong Password! Try Again.")
    exit()

except:
    print("[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps")
    exit()

target = input("[?] Enter Target Gmail: ")
subject = input("[?] Subject: ")
body = input("[?] Message: ")
amount = input("[?] Amount: ")
msg = 'From: ' + username + '\nSubject: ' + subject + '\n' + body

i = 0
while i < int(amount):
    try:
        print(i)
        server.sendmail(username,target,msg)
        print("[-] Successfully Sent.")
        i = i+1
    except:
        print("[!] Can't send now. Please Try Again In A Few Minutes.")
print('\n[<3] Done! Thanks For Using GSpammer.')
