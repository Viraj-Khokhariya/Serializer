from django.urls import path,include
from app import views

urlpatterns = [
    # path('snippets/', views.UserList),
    # path('snippets/all/', views.UserDetail.as_view()),
    # path('all/',UserList.as_view()),
    # path('snippets/all/', views.UserDetail.as_view()),
    # path('details/<pk>',Item.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    path('snippets/',views.snippet_list,name='Home'),
    
    path('snippost/',views.snippet_post,name='PostMethod'),
    
    path('snipdelete/<int:pk>/',views.snippet_delete,name='DeleteMethod'),
      
]

