from django.urls import path
from . import views
app_name="cafe"
urlpatterns = [    
    path('', views.index_view, name='cafe_home'),
    path('menu_list_url/', views.menu_list, name="menu_list_page"),
    path('menu_add_url/',views.menu_add, name="menu_add_page"), # 메뉴 추가 페이지
    path('add_menu_data/', views.add_menu_data, name='add_menu_data'),
    # 메뉴 디테일 페이지 추가
    path('detail/<int:menu_id>/', views.menu_detail, name="menu_detail"),
    path('add_option/<int:menu_id>/', views.add_option, name='add_option'),
    path('add_option_data/', views.add_option_data, name='add_option_data'),
    path('create/', views.create, name="menu_create"),
    path('<int:pk>/update/', views.update, name="menu_update"),
    path('<int:pk>/delete/', views.delete, name="menu_delete"),
]