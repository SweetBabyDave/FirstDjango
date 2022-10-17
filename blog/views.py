from time import strftime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from django.shortcuts import redirect

from django.utils import timezone

# Create your views here.
def index(request):
	blogList = Blog.objects.order_by("-posted").all()[:3]
	return render(request, 'blog/index.html', {'now': strftime('%c'), 'blogList': blogList})

def archive(request):
	blogList = Blog.objects.order_by("-posted").all()
	return render(request, 'blog/archive.html', {'now': strftime('%c'), 'blogList': blogList})
	
def entry(request, blog_id):
	blogPost = get_object_or_404(Blog, pk=blog_id)
	comments = Comment.objects.filter(blog=blogPost).order_by("-posted").all()
	return render(request, 'blog/entry.html', {'now': strftime('%c'), 'blogPost': blogPost, 'comments': comments})

def comment(request, blog_id):
	blogPost = get_object_or_404(Blog, pk=blog_id)

	# Redisplay the entry.
	if not request.POST['commenter'] or not request.POST['email'] or not request.POST['content']: 
		return redirect('entry', blog_id=blogPost.pk)
		
	comment = Comment(blog=blogPost, commenter=request.POST['commenter'],
	email=request.POST['email'], content=request.POST['content'],
	posted=timezone.now()
	)
	comment.save()

	return redirect('entry', blog_id=blogPost.pk)

def about(request):
	return render(request, 'blog/about.html', {'now': strftime('%c')})

def techtipsBad(request):
	return render(request, 'blog/techtips-css.html', {'now': strftime('%c')})

def techtipsGood(request):
	return render(request, 'blog/techtips+css.html', {'now': strftime('%c')})

def plan(request):
	return render(request, 'blog/plan.html', {'now': strftime('%c')})