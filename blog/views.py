from math import ceil

from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blogs(request):
    posts = Blog.objects.order_by('-date')
    len_page = 4
    count_page = ceil(posts.count() / len_page)

    page = int(request.GET.get('page', 1))
    count_posts = posts.count()

    posts = posts[(page - 1) * len_page:page * len_page]

    prev = page - 1 if page != 1 else 1
    next = page + 1 if page != count_page else count_page
    if count_posts < 3:
        page_range = range(1, count_page + 1)
    else:
        page_range = range(prev, next+1)
    return render(request, 'blog/all_blog.html', {'posts': posts, 'page': page,
                                                  'count_page': count_page, 'count_posts': count_posts,
                                                  'prev': prev, 'next': next,
                                                  'page_range': page_range})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
