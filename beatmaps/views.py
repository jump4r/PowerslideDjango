from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Submission, Beatmap

def index(request):
    submission_list = Submission.objects.order_by('date')
    context = {'submission_list': submission_list}
    return render(request, 'beatmaps/index.html', context)

def details(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)

    return render(request, 'beatmaps/detail.html', {'submission': submission})

def submit(request):
    return render(request, 'beatmaps/submit.html', {
        'message': ''
    })
    
def handle_submit(request):
    try:
        s_user = request.POST['user']
        s_name = request.POST['title']

        print(s_user + ' ' + s_name)
    except (KeyError):
        print("Error Uplading")
        return render(request, "beatmaps/submit.html", 
        {
            'message': "Error Uploading Beatmap"
        })

    return HttpResponseRedirect(reverse('beatmaps:index'))
    
