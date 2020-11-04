import os
import requests
import feedparser
from datetime import timedelta, datetime
from dateutil import parser
from pprint import pprint
from time import sleep
BOT_TOKEN=os.environ.get("BOT_TOKEN")
CHANNEL_ID='@AnimeReleaseAlert'
FEED_URL="http://animeschedule.net/subrss.xml"
prev=None
#FEED_URL='https://honeysanime.com/feed/'
#i=1
def send_msg(title,msg):
    print("Detected a new release!")
    headers={'Connection':'close'}
    requests.Session().post(f'https://api.telegram.org/bot'+BOT_TOKEN+'/sendMessage?chat_id='+CHANNEL_ID+'&text='+title+'%0A'+msg, headers=headers)
    
def main():
    #print("running..."+str(i), end='\r')
    news=feedparser.parse(FEED_URL)
    for entry in news.entries:
        parsed_date = parser.parse(entry.published).replace(tzinfo=None)
        #parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None)
        now_date = datetime.utcnow()

        published_3_minutes_ago = now_date - parsed_date < timedelta(minutes=2)
        #print(published_5_minutes_ago)
        if published_3_minutes_ago AND entry.title!=prev:
            if prev==None: prev=entry.title
            send_msg(entry.title,entry.links[0].href)
            print(entry.links[0].href)    
            #sleep(60)
if __name__=="__main__":
    #i=1
    while(True):
        prev=None
        main()
        sleep(2*60)
        #i+=1
