from django.shortcuts import render

# Create your views here.
def post_list(request):
    text = "Hello user"
    context = {'title':text}
    return render(request,'mysite/index.html',context)