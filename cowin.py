# importing the requests library
from twilio.rest import Client
import requests
import sys
import time
from datetime import date
import re
from datetime import timedelta
import smtplib


# https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python

#export TWILIO_AUTH_TOKEN=08645f5a1ce47d83c6dff64e16339c19
#export TWILIO_ACCOUNT_SID='AC544cd4ac21c73722f834b8fc2db10b2f'

def send_email(date):
	print("Sending Mail")
	s = smtplib.SMTP('smtp.gmail.com', 587)
	# start TLS for security
	s.starttls()
  
	# Authentication
	s.login("testcowin507@gmail.com", "Suri@123")
	  
	
	SUBJECT = "Cowin slot found!"
	TEXT = 'Hi, found slot for date, please hurry :) ' + str(date)
	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
	# message to be sent
	  
	# sending the mail
	s.sendmail("testcowin507@gmail.com", "palakj159@gmail.com", message)
	s.sendmail("testcowin507@gmail.com", "nikhilsuri507@gmail.com", message)
	  
	# terminating the session
	s.quit()
	print("Sent")

def sendMessage(date):
	print("Sending Whatsapp Message")
	from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
	to_whatsapp_number1='whatsapp:+918058405256'

	to_whatsapp_number2='whatsapp:+919461254427'

	client.messages.create(body='Hi, found slot for date, please hurry :) ' + str(date),
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number1)


	client.messages.create(body='Hi, found slot for date, please hurry :) ' + str(date),
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number2)
	print("Sent")

def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)


def session_present_18_centers(centers):
	for center in centers:
		if session_present_18_sessions(center['sessions']):
			return True;
	
	return False

def session_present_18_sessions(sessions):
	for session in  sessions:
		if session['min_age_limit'] == 18 & session['available_capacity'] > 0:
			if session['vaccine'] == 'COVISHIELD':
				print(session)
				#sendMessage(session['date'])
				#send_email(session['date'])
				return True
	return False

def getData(pincode, date):
	print("Checking for date: "+ str(date))
	URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date
	r = requests.get(url = URL)   
	# extracting data in json format
	data = r.json()
	return data

def get_slot_for_date(pincode, date):
	data = getData(pincode, date)
	if(data['centers']):
		return session_present_18_centers(data['centers'])
	return False

pincode = "122002"
client = Client()

while 1 == 1 :
	for x in range(0,10):
		try:
			queryDate = date.today() + timedelta(days=x)
			transformedDate = change_date_format(str(queryDate))
			if get_slot_for_date(pincode, transformedDate):
				break
		except Exception as e:
	  		print("I broke , sorry to disappoint you master :(")	
	  		print(e)
		time.sleep(60)
	print("Tired, going on sleep")
	time.sleep(1800)