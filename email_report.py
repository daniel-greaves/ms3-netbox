from datetime import datetime
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from jinja2 import Environment, FileSystemLoader
import os
import smtplib

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "8813868bcb942415b4acd20143deb784-4b670513-efd3e03e"),
		data={"from": "Daniel Greaves <daniel.greaves@ms-3.co.uk>",
			"to": ["daniel.greaves@ms-3.co.uk"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomeness!"})
