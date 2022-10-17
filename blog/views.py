from time import strftime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from django.urls import reverse

from django.utils import timezone

# Create your views here.
def index(request):
	blogList = Blog.objects.order_by("-posted").all()[:3]
	return render(request, 'blog/index.html', {'now': strftime('%c'), 'blogList': blogList})

def archive(request):
	blogList = Blog.objects.order_by("-posted").all()
	return render(request, 'blog/archive.html', {'now': strftime('%c'), 'blogList': blogList})
	
def entry(request, blog_id):
	# blog = get_object_or_404(Blog, pk=blog_id)
	# commentsList = list(Comments.objects.all())
	# newCommentList = []
	# blogList = list(Blog.objects.all())

	# for comment in commentsList:
	# 	newCommentList.insert(0, comment)

	blogPost = get_object_or_404(Blog, pk=blog_id)
	comments = Comment.objects.filter(blog=blogPost).order_by("-posted").all()
	return render(request, 'blog/entry.html', {'now': strftime('%c'), 'blogPost': blogPost, 'comments': comments})

def comment(request, blog_id):
    blogPost = get_object_or_404(Blog, pk=blog_id)
    try:
        comment = blogPost.set(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the entry.
        return render(request, '/blog/entry/{blog_id}', {
            'blogPost': blogPost,
            'error_message': "You didn't select a choice.",
        })
    else:
        comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:entry', args=(blog_id,)))

def about(request):
	return render(request, 'blog/about.html', {'now': strftime('%c')})

def techtipsBad(request):
	return render(request, 'blog/techtips-css.html', {'now': strftime('%c')})

def techtipsGood(request):
	return render(request, 'blog/techtips+css.html', {'now': strftime('%c')})

def plan(request):
	return render(request, 'blog/plan.html', {'now': strftime('%c')})