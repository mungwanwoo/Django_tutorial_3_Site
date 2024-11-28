from django.contrib import admin

#from polls import views
#from . import views
# from .views import index, detail
from . import views
from django.urls import path,include
from django.conf import settings

app_name = "polls"
urlpatterns = [   
        # ex: /polls/
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("create/", views.CreateQuestionView.as_view(), name="create_question"),
    path("<int:pk>/update/", views.UpdateQuestionView.as_view(), name="update_question"),
    path("<int:pk>/delete/", views.DeleteQuestionView.as_view(), name="delete_question"),
    path("<int:pk>/create_choice/", views.CreateChoiceView.as_view(), name="create_choice"),
    path('choice/<int:pk>/delete/', views.DeleteChoiceView.as_view(), name='choice_delete'),

    # path('', index),
    # path('<int:question_id>/', detail), # < 이 자료형이 들어오면 : 이 변수로 다음단계로 전달할게>
    # path('django/', index1),
    # path('new/', index2),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] + urlpatterns
