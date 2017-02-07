from django.shortcuts import render

from .models import Post


def post_list(request):
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request, 'blog/post-list.html', context)
