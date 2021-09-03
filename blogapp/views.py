from django.contrib.auth.backends import UserModel
from django.contrib import messages
from django.http import request
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from . models import Blog, Comment, User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from blogapp.forms import  Edit_Blog, New_Blog, CommentForm, EditCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import get_user_model


class ShowPostsView(UserPassesTestMixin,LoginRequiredMixin,DetailView):
    template_name = 'showposts.html'
    model = User
    def test_func(self):
        
        return  self.request.user.is_superuser
      

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.get_object()
        ctx['posts'] = Blog.objects.filter(user_id = obj)
        return ctx 


class User_ListView(UserPassesTestMixin,LoginRequiredMixin,ListView):
    template_name = 'user_list.html'
    model = User
    def test_func(self):
       
        return  self.request.user.is_superuser
    # user_posts = User.objects.annotate(total_posts = Count('id'))

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     qs = self.get_queryset()
    #     total = 0
    #     for key in  qs:
    #         posts = Blog.objects.filter(user_id = key)
    #         total = len(posts)
    #         print(len(posts))
    #         ctx['total_posts'] = total
    #     # print(User.objects.count())
    #     return ctx 


class DashBoardView(TemplateView):
    template_name = 'dashboard.html'
    
   
    
    

class EditCommentView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    template_name = 'editcomment.html'
    form_class = EditCommentForm
    model = Comment
 
    def test_func(self):
        obj = self.get_object()
        print(type(obj.name))
        print(type(self.request.user.username))
        return  obj.name == self.request.user.username

    def get_success_url(self):
        obj = self.get_object()
        print()
        return reverse_lazy('blog_detail',kwargs={'pk':obj.post.id})
    
    
    # return  obj.user_id == self.request.user
    


class AddCommentView(LoginRequiredMixin, CreateView):
    template_name = 'add_comment.html'
    form_class = CommentForm
    model = Comment
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('blog_detail',kwargs={'pk':self.kwargs['pk']})
    
    

    
   


class Home(ListView):
    template_name = 'home.html'
    # model = Blog
    queryset = Blog.objects.filter(checkbox=True)

# def home(request):
#     blog = Blog.objects.all()
#     context ={'blogs':blog}
#     return render (request, 'home.html' , context)

class UserRegister(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = UserModel
    # success_url = reverse_lazy('login')
    def get_success_url(self):
        messages.success(self.request, 'Registerd')
        return reverse_lazy('login')


# def user_register(request):
#     if request.method == "POST":
#         fname= request.POST.get('firstname')
#         lname= request.POST.get('lastname')
#         uname= request.POST.get('username')
#         email= request.POST.get('email')
#         pass1= request.POST.get('pass1')
#         pass2= request.POST.get('pass2')
#         if pass1!=pass2:
#             messages.warning(request, "Password Does Not Match")
#             return redirect('register')
#         elif User.objects.filter(username=uname).exists():
#             messages.warning(request, "This UserName Already Exist!")
#             return redirect('register')
#         elif  User.objects.filter(email=email).exists():
#             messages.warning(request, "This Email Already Exist!")
#             return redirect('register')
#         else:
#             user = User.objects.create_user(first_name=fname, last_name=lname, 
#             username=uname, email=email, password=pass1)
#             user.save()
#             messages.success(request, 'You are Registerd Successfully!')
#             return redirect('login')
#     return render (request, 'register.html')


# def user_login(request):
#     if request.method == "POST":
#         username= request.POST.get('username')
#         password= request.POST.get('pass1')
#         user = authenticate(request, username=username , password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#         else:
#             messages.error(request,"Register YourSelf Or Check Password!")
#             return redirect('login')   

#     return render (request, 'login.html')


# def user_logout(request):

#     logout(request)
#     return redirect('/')

class PostCreate(LoginRequiredMixin, CreateView):
    template_name= 'post_blog.html'
    model = Blog
    form_class = New_Blog 
    success_url = reverse_lazy('home')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['user_id'] = self.request.user
        print(initial)
        return initial
    
    

# def post_blog(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         desc = request.POST.get('Description') 
#         blog = Blog(title=title , dsc= desc , user_id=request.user)
#         print(blog)
#         blog.save()
#         messages.success(request , 'Post Uploaded Sucessfully!')
#         return redirect('post_blog')
#     return render(request, 'post_blog.html')

class Blog_Detail(DetailView):
    template_name = 'blog_detail.html'
    model = Blog
    

class PublishView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    template_name = 'blog_detail.html'
    model = Blog
    fields = ('checkbox',)
    success_url = reverse_lazy('home')
    def test_func(self):
       
        return  self.request.user.is_superuser
    # def get_object(self, queryset):
    #     self.query_pk_and_slug
    #     return super().get_object(queryset=queryset)

    def post(self, request, *args, **kwargs):
        print(super().post(request, *args, **kwargs))
        return super().post(request, *args, **kwargs)
    
    
    

        




# def blog_detail(request, id):
#     blog = Blog.objects.get(id=id)
#     context = {'blog':blog}
#     return render(request, 'blog_detail.html', context)


class Delete(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model =Blog
    success_url = reverse_lazy('home')
    def test_func(self):
        obj = self.get_object()
        print(obj.user_id) 
        return  obj.user_id == self.request.user
         # if User.is_authenticated and User.id == Blog.user_id_id:
            # messages.success(self.request, 'Post Deleted')
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and User.id == Blog.user_id_id:
    #         return reverse_lazy('blog_detail',kwargs={'pk':self.kwargs['pk']})
    
    # def get_success_url(self):
    #     if User.is_authenticated and User.id == Blog.user_id_id:
    #         messages.success(self.request, 'Post Deleted')
    #     return reverse_lazy('home')

# def delete(request, id):
#     blog = Blog.objects.get(id=id)
#     blog.delete()
#     messages.success(request, 'Blog Deleted')
#     return redirect('/')


class Edit( UserPassesTestMixin, LoginRequiredMixin,  UpdateView):
    template_name= 'edit_blog.html'
    model = Blog
    form_class = Edit_Blog
    success_url = reverse_lazy('home')
    def test_func(self):
        
        obj = self.get_object()
        
        return  obj.user_id == self.request.user

            # if User.is_authenticated and User.id == Blog.user_id_id:
            # messages.success(self.request, 'Post Deleted')
            # .get_object(obj)
            # return reverse_lazy('edit')
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and User.id == Blog.user_id_id:
    #         return redirect('edit',kwargs={'pk':self.kwargs['pk']})
    #     else:
    #         return reverse_lazy('blog_detail',kwargs={'pk':self.kwargs['pk']})
    # def get_object(self, *args, **kwargs):
    #     user = get_object_or_404(Blog, pk=self.kwargs['pk'])
    #     return user
    
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({'instance':self.object})
    #     return kwargs

    # def form_valid(self, form):
    #     form.instance.title = self.kwargs['title']
    #     return super().form_valid(form)
    # success_url = reverse_lazy('home')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['title'] = self.object.title
    #     initial['dsc'] = self.object.dsc
    #     print(initial)
    #     return initial
    
  

# def edit(request, id):
#     blog = Blog.objects.get(id=id)
#     editblog = Edit_Blog(instance=blog)
#     if request.method == 'POST':
#         form =Edit_Blog(request.POST, instance=blog)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Updated Successfully!')
#             return redirect('/')
#     return render (request,'edit_blog.html', {'edit_blog':editblog})
