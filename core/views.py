from django.shortcuts import render
from .models import Post, Contact, Aboutme #,Comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import CommentForm, ContactModelForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    template_name='core/home.html'
    context={}
    return render(request, template_name, context)


def blog(request):
    template_name = 'core/blog.html'
    post = Post.objects.order_by("-timestamp")
    paginator = Paginator(post, 37) 
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts}
    return render(request, template_name, context)




def post_detail_view(request, slug):
    template_name = 'core/post_detail.html'
    instance = get_object_or_404(Post, slug=slug)
    commentss= instance.comments.order_by("-created_date")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = instance
            comment.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = CommentForm()
    context = {'post': instance,'form': form,'commentss': commentss}
    return render(request, template_name, context)



def about_me(request):
    template_name = 'core/about_me.html'
    abm = Aboutme.objects.all()
    context = {
        'abm' : abm
    }
    return render(request, template_name, context)

def contact(request):
    form = ContactModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        #obj.user = request.user
        obj.save()
        return redirect('/contact')
        form = ContactModelForm()
    template_name = 'core/contact.html'
    context = {'form': form}
    return render(request, template_name, context)    



def gallery(request):
    template_name = 'core/gallery.html'
    pics = Post.objects.all()
    context = {
        'pics': pics
    } 
    return render(request, template_name, context)   