from flask import Flask, render_template
import bs4 as bs
import urllib.request
from time import sleep
import smtplib

link= input('Input your link: ')
keywords= input('Input your keywords: ').lower().split()
remail = input('Input your email: ')

def make_soup(link):
    sauce = urllib.request.urlopen(link)
    soup = bs.BeautifulSoup(sauce,'lxml')
    body = soup.find('body').get_text().lower().split()

def send_email(link, matches, remail):
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls()
    email.ehlo()
    email.login('jobagent.matcher@gmail.com','yqoczgfebvsgwjia')
    subject = f'Job {matches} Found'
    body = f'Your Job Agent has found a match on the website: {link}'
    msg = f"Subject: {subject} \n\n {body}"
    email.sendmail('jobagent.matcher@gmail.com', remail, msg)
    email.quit()

def main():
    match=False
    matches=[]
    make_soup(link)
    for word in body:
        if word in keywords:
            match=True
            matches.append(word)
    if match:
        send_email(link, set(matches))

while True:
    main()
    sleep(86400)
