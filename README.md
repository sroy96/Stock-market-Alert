# STOCK - PRO 

This software can be used to provide alert to the 
users who forget to set target, stop loss or margin percentage while buying 
the stock.

## How to Setup ?

- Install the requirements
````
pip install -r requirement.txt 
````

- Run cache_server_up.sh 
- Run src/main.py
- Run utils/jobber.py

----
* Jobber is a scheduled task, the logs are on jobber_logs.txt
* Observer Pattern is used to observe stock price variations and notify the
 changes to the user.
* In order to receive email notification create file confidential.py and add your Email(SUPPORT_MAIL) and Password (SUPPORT_MAIL_PASS)
