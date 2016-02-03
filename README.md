# NetMeter-TwitterBot #
The NetMeter-Twitter bot(as you can imagine) is a Twitter bot that measure your internet connection speed and tweet it to your ISP if is below a determined threshold. 

Some things to have in mind:

1. This bot is based on AlekseyP's bot from Reddit!
2. I am **NOT** a Python programmer so I'm sorry for this code :P improvements are welcome
3. Next step is to put it on a Raspberry Pi to get it running 24/7.


## Setup the environment ##
- Install Python
- ```brew install python``` or whatever cmd line you want
- Install tweepy
- ```sudo pip install tweepy``` or whatever cmd line you want, again
- Install speedtest-cli
- ```sudo pip install speedtest-cli``` or whatever cmd line you want, and again


## Using it

After you setup the environment just type ```python NetMeterTwitterBot.py``` in your terminal and press Enter.

Tested with:
- Python 2.7.10 (default, Oct 23 2015, 18:05:06) [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)]
- MacOS Version 10.11.3 (15D21)
