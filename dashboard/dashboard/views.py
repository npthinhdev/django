from django.shortcuts import render, redirect
from datetime import datetime, timezone, timedelta
from django.conf import settings
from news.models import HeadLine, UserProfile
from notepad.forms import NoteModelForm
from notepad.models import Note

def home(request):
    user_p = UserProfile.objects.filter(user=request.user).first()
    time_diff = datetime.now(timezone.utc) - user_p.last_scrape
    if time_diff / timedelta(days=1) < 1:
        hide_me = True
    else:
        hide_me = False
    headlines = HeadLine.objects.all()
    notes = Note.objects.filter(user=request.user)
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/home/')
    context = {
        'form': form,
		'notes_list': notes,
		'object_list': headlines,
		'hide_me': hide_me,
        'next_scrape': round(24 - time_diff / timedelta(minutes=60))
    }
    return render(request, "news/home.html", context)
