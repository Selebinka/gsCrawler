# gsCrawler


Scrapy Project can scan Google search results and show your position by keyword. Using the web interface, you can launch the spider and see the results of the execution.


# Setup
1 - Install requirements

    $ pip install -r requirements.txt


# Start the project
In order to start this project you will need to have running Django and Scrapyd at the same time.

In order to run Django

    $ python manage.py runserver

In order to run Scrapyd

    $ cd scrapy_app
    $ scrapyd

Open localhost:8000


# limitation
The project doesn't provide any workaround to the anti-spider measure like CAPTCHA, IP ban list, etc.

But to reduce these measures, recommand to set DOWNLOAD_DELAY=5 in settings.py file to add a temporisation (in second) between the crawl of two pages, see details in Scrapy Setting.