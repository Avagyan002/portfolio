from django.urls import path


from . import views


urlpatterns = [
    path("", views.programmer_list, name='programmer_list'),
    path("programmer/<int:programmer_id>/", views.programmer_detail, name='programmer_detail'),
    path("programmer/<int:programmer_id>/add_project/", views.add_project, name='add_project'),
]