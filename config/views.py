from django.views import generic


#--- TemplateView
class HomeView(generic.TemplateView):
    template_name = 'home.html'



