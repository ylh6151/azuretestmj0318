from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from post.models import Postit


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == 'POST':
        print(request.FILES)
        Postit.objects.create(
            message=request.POST.get('message', '') if request.POST.get('message', '') != '' else None,
            image=request.FILES.get('image') if request.FILES.get('image') else None
        )

    return render(request, 'postit.html', context={
        'postit_list': Postit.objects.order_by('-created_at')
    })
