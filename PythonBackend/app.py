import bs4 as bs
import urllib.request
from time import sleep
from pymongo import MongoClient
import smtplib

URI = "mongodb+srv://petarsam:"+process.env.PASSWORD+"@cluster0-gp7st.gcp.mongodb.net/test?retryWrites=true&w=majority"

def send_email(link, matches, remail):
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls() 
    email.ehlo()
    email.login('jobagent.matcher@gmail.com','yqoczgfebvsgwjia')
    subject = f"Job {matches} Found"
    body = f"Your Job Agent has found a match on the website: {link}"
    msg = f"Subject: {subject} \n\n {body}"
    email.sendmail('jobagent.matcher@gmail.com', remail, msg)
    email.quit()

def main():
    client = MongoClient(URI)
    db = client['JobAgent']
    agents = db.agents
    all_agents = list(agents.find())
    for agent in all_agents:
        sauce = urllib.request.urlopen(agent['link'])
        soup = bs.BeautifulSoup(sauce,'lxml')
        body = soup.find('body').get_text().lower()
        keyword = agent['position'].lower()
        match = False
        matches = []

        if keyword[0] in body:
            match = True
            matches.append(keyword)

        if match:
            send_email(agent['link'], ' '.join(set(matches)), agent['email'])
            agents.delete_one({"_id":agent['_id']})
            print('success2')


while True:
    main()
    sleep(86400)
