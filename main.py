import requests
import feedparser
from datetime import timedelta, datetime
from dateutil import parser
from pprint import pprint
from time import sleep
BOT_TOKEN='1349889773:AAGDiGrrt3hEZVj7672kHSXbmDfp5Z8bKkE'
CHANNEL_ID='@AnimeReleaseAlert'
FEED_URL="http://animeschedule.net/subrss.xml"
#FEED_URL='https://honeysanime.com/feed/'
i=1
def send_msg(title,msg):
    print("Detected a new release!")
    headers={'Connection':'close'}
    requests.Session().post(f'https://api.telegram.org/bot'+BOT_TOKEN+'/sendMessage?chat_id='+CHANNEL_ID+'&text='+title+'%0A'+msg, headers=headers, verify=False)
    
def main():
    print("running..."+str(i), end='\r')
    news=feedparser.parse(FEED_URL)
    for entry in news.entries:
        parsed_date = parser.parse(entry.published).replace(tzinfo=None)
        #parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None)
        now_date = datetime.utcnow()

        published_3_minutes_ago = now_date - parsed_date < timedelta(minutes=3)
        #print(published_5_minutes_ago)
        if published_3_minutes_ago:
            send_msg(entry.title,entry.links[0].href)
            print(entry.links[0].href)    
            sleep(60)
if __name__=="__main__":
    i=1
    while(True):
        main()
        sleep(2*60)
        i+=1