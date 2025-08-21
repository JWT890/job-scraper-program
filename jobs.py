import feedparser
from flask import Flask, render_template
from bs4 import BeautifulSoup
import threading
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
jobs_listings = []

RSS_URLS = {
    "Blue Origin": "www.indeed.com/jobs?q=blue+origin&l=huntsville%2C+al&from=subwaywebapp&radius=25"
}

def get_jobs(RSS_URLS):
    global jobs_listings

def update_job_listings():


def schedule_fetch():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_job_listings, 'interval', hours=3)
    scheduler.start()


@app.route('/')
def index():
    return render_template('index.html', job_listings=jobs_listings)

if __name__ == "__main__":
    threading.Thread(target=schedule_fetch, daemon=True).start()
    app.run(debug=True)