from django.urls import path
from Employee import views

urlpatterns = [
    path('home/',views.home),
    path('empdet/',views.empdet),
    path('delete/<int:tid>',views.delete),
    path('update/<int:tid>',views.update)
]
