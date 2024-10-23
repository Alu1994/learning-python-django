from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<topic_id>/', views.topic, name='topic'),
    path('new-topic/', views.new_topic, name='new-topic'),
    path('new-entry/<topic_id>', views.new_entry, name='new-entry'),
    path('edit-entry/<entry_id>', views.edit_entry, name='edit-entry'),
]
