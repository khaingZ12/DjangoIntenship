from django.shortcuts import render
from .models import *

# Create your views here.
def postdata(request):
    post_data = Post.objects.all()
    context = {'post_data':post_data}
    return render(request, 'posts.html', context)


def myfriends(request):
    friends = Myfriend.objects.all()
    mylist = [1,2,3,4]
    context = {'friends':friends, 'mylist':mylist}
    return render(request, 'myfriend.html', context)
