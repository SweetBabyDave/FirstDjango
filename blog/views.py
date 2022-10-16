from time import strftime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Blog, Comments
from django.urls import reverse

from django.utils import timezone

# Create your views here.
def index(request):
	commentsList = list(Comments.objects.all())
	blogList = list(Blog.objects.all())
	newBlogList = []

	for blogPost in blogList[-3:]:
		newBlogList.insert(0, blogPost)

	return render(request, 'blog/index.html', {'now': strftime('%c'), 'newBlogList': newBlogList, 'commentsList' : commentsList})

def archive(request):
	commentsList = list(Comments.objects.all())
	print(len(commentsList))

	blogList = list(Blog.objects.all())
	newBlogList = []

	for blogPost in blogList:
		newBlogList.insert(0, blogPost)

	return render(request, 'blog/archive.html', {'now': strftime('%c'), 'newBlogList': newBlogList, 'commentsList' : commentsList})
	
def entry(request, blog_id):
	# blog = get_object_or_404(Blog, pk=blog_id)
	# commentsList = list(Comments.objects.all())
	# newCommentList = []
	# blogList = list(Blog.objects.all())

	# for comment in commentsList:
	# 	newCommentList.insert(0, comment)

	blogPost = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/entry.html', {'now': strftime('%c'), 'blogPost': blogPost})

def comment(request, blog_id):
    blogPost = get_object_or_404(Blog, pk=blog_id)
    try:
        comment = blogPost.set(pk=request.POST['comment'])
    except (KeyError, Comments.DoesNotExist):
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