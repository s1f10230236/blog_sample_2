from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
import random
from blog.models import Article,Comment

def index(request):
	if request.method=='POST':
		article=Article(title=request.POST['title'],body=request.POST['text'])
		article.save()
		return redirect(detail,article.id)
	context = {
        "articles":Article.objects.all()
    }
	return render(request, 'blog/index.html', context)

def redirect_test(redirect):
	return redirect(hello)

def detail(request,article_id):
	try:
		article=Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404('Article does not exist')
	if request.method=='POST':
		comment=Comment(article=article,text=request.POST['text'])
		comment.save()
	context={
		'article':article,
		'comment':article.comments.oder_by('-posted_at')
	}
	return render(request,'blog/detail.html',context)

def update(request, article_id):
	try:
		article=Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404('Article does not exist')
	if request.method=='POST':
		article.title=request.POST['title']
		article.body=request.POST['text']
		article.save()
		return redirect(detail,article_id)
	context={
		'article':article
	}
	return render(request,"blog/edit.html",context)

def delete(request,article_id):
	try:
		article=Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404('Article does not exist')
	article.delete()
	return redirect(index)

def hello(request):
	data={
		"name":"Alice",
		"weather_detail":["Temperature:23℃","Humidity:40%","Wind:5m/s"],
		"isGreatFortune":True,
		"fortune":"Great Fortune!"
	}
	return render(request, 'blog/hello.html',data)