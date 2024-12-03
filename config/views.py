from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


#--- TemplateView
#기본 홈페이지를 렌더링하는 뷰
#template_name = 'home.html' 홈.html을 반환한다
class HomeView(generic.TemplateView):
    template_name = 'home.html'
#장고에서 새로운 사용자를 등록하는 폼을 제공한다
class UserCreateView(generic.CreateView):
    template_name='registration/register.html'
    #회원가입을 위한 장고에서 제공하는 폼
    form_class=UserCreationForm
    #회원가입 후 이동한 url
    success_url=reverse_lazy('register_done')
#회원가입 후 렌더링하는 뷰
class UserCreateDoneTV(generic.TemplateView):
    template_name='registration/register_done.html'

