from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from mysite.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts':posts}
    return render(request,'mysite/index.html',context)