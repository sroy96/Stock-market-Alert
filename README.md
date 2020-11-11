# STOCK - PRO 

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
[![Build Status](https://travis-ci.com/anuragsarkar97/msgs.svg?branch=master)](https://travis-ci.com/anuragsarkar97/msgs)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/anuragsarkar97/msgs/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/anuragsarkar97/msgs)
[![GitHub version](https://badge.fury.io/gh/anuragsarkar97%2Fmsgs.svg)](https://github.com/anuragsarkar97/msgs)


[![ForTheBadge built-with-swag](http://ForTheBadge.com/images/badges/built-with-swag.svg)](https://GitHub.com/anuragsarakr97/)
[![forthebadge](https://forthebadge.com/images/badges/winter-is-coming.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

This software can be used to provide alert to the 
users who forget to set target, stop loss or margin percentage while buying 
the stock. Generally companies like Zerodha, Yahoo finance, Morning Star has made it available at 
a subscription cost. 

I think for a growth in market it require all of us to invest and it is my small contribution towards that as 
a software developer. Keep Building for the Growth :) 

## How to Setup ?

- Install the requirements
````
pip install -r requirement.txt 
````

- Run cache_server_up.sh 
- Run src/main.py
![add stock](https://github.com/sroy96/Stock_Price_Notification/blob/main/add_stock.png)

- Run utils/jobber.py

![jobber](https://github.com/sroy96/Stock_Price_Notification/blob/main/jobber.png)

----
* Jobber is a scheduled task, the logs are on jobber_logs.txt
* Observer Pattern is used to observe stock price variations and notify the
 changes to the user.
* In order to receive email notification create file confidential.py and add your Email(SUPPORT_MAIL) and Password (SUPPORT_MAIL_PASS)
