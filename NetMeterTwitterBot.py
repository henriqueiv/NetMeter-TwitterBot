#!/usr/bin/python
# coding=utf-8
# Based on http://pastebin.com/WMEh802V
import os
import sys
import csv
import datetime
import time
import tweepy

def test():
        #Constants
        #Enter the corresponding information from your Twitter application:
        CONSUMER_KEY = 'YOUR CONSUMER KEY'
        CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
        ACCESS_KEY = 'YOUR ACCESS KEY'
        ACCESS_SECRET = 'YOUR ACCESS SECRET'

        #Internet information
        # YES STRING BECAUSE I'M LAZY
        INTERNET_EXPECTED_DOWN = "50"
        INTERNET_EXPECTED_UP = "5"
        INTERNET_LOWER_THRESHOLD = 40
        ISP_TWITTER_ACC = '@gvtoficial @gvt_suporte'

        #Run speedtest-cli
        print 'Running test...'
        result = os.popen("speedtest-cli --simple").read()
        print 'Ran!'

        #if speedtest could not connect set the speeds to 0
        if "Cannot" in result:
            ping = 9999
            down = 0
            up = 0

        #extract the values for ping down and up values
        else:
            #Split the 3 line result (ping,down,up)
            values = result.split('\n')
            ping = values[0][6:11]
            down = values[1][10:14]
            up = values[2][8:12]

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print date, ping, down, up

        #save the data to file for local network plotting
        out_file = open('data.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,ping,down,up))
        out_file.close()

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        #try to tweet if speedtest couldnt even connet. Probably wont work if the internet is down
        if "Cannot" in result:
                try:
                    tweet="Hey " + ISP_TWITTER_ACC + "why is my internet down? I pay for " + INTERNET_EXPECTED_DOWN + "down|" + INTERNET_EXPECTED_UP + "up? #NetMeterTwitterBot #SpeedTest"
                    api.update_status(tweet)
                    # print tweet

                except:
                    pass

        # tweet if down speed is less than whatever I set
        elif eval(down) < INTERNET_LOWER_THRESHOLD:
                print "Trying to tweet..."
                try:
                    tweet="Hey " + ISP_TWITTER_ACC + " why my speed is now " + down + "down|" + up + "up if I pay for " + INTERNET_EXPECTED_DOWN + "down|" + INTERNET_EXPECTED_UP + "up? #NetMeterTwitterBot #SpeedTest"
                    api.update_status(tweet)
                    # print tweet

                except Exception,e:
                        print str(e)
                        pass

        print 'Completed'
        return

if __name__ == '__main__':
        test()
