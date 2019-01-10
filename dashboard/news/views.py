import requests
import shutil
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
from django.conf import settings
from .models import HeadLine, UserProfile

requests.urllib3.disable_warnings()

def news_list(request):
    user_p = UserProfile.objects.filter(user=request.user).first()
    time_diff = datetime.now(timezone.utc) - user_p.last_scrape
    if time_diff / timedelta(days=1) < 1:
        hide_me = True
    else:
        hide_me = False
    headlines = HeadLine.objects.all()
    context = {
        'object_list': headlines,
        'hide_me': hide_me,
        'next_scrape': round(24 - time_diff / timedelta(minutes=60))
    }
    return render(request, 'news/home.html', context)

def scrape(request):
    user_p = UserProfile.objects.filter(user=request.user).first()
    user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()

    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url = 'https://www.theonion.com/'
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, 'html.parser')
    posts = soup.find_all('div', {'class': 'curation-module__item__wrapper'})

    for i in posts:
        link = i.find_all('a', {'class': 'js_curation-click'})[1]['href']
        title = i.find_all('a', {'class': 'js_curation-click'})[1].text
        image_source = i.find('img', {'class': 'featured-image'})['data-src']

        if not image_source.startswith(("data:image", "javascript")):
            local_filename = image_source.split('/')[-1]
            r = session.get(image_source, stream=True, verify=False)
            if r.status_code == 200:
                with open(local_filename, 'wb') as f:
                    f.write(r.content)
                shutil.move(local_filename, '/'.join([settings.MEDIA_ROOT, local_filename]))
        
        new_headline = HeadLine()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = local_filename
        new_headline.save()
    return redirect('/home/')
