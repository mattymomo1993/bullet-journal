"""jouralbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import home, animation, index, register, logout_view
from profilejournal.views import JournalPageView, AddAssignmentView, AssignmentDetailView, LessonAssignmentView, ActivityAssignmentView, QuizAssignmentView, AssessmentAssignmentView, CompletedAssignmentView, DeleteAssignmentView, AddReflectionView, DeleteReflectionView
from blog import views
from django.conf.urls import url
from django.views.static import serve 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', animation),
    path('home/', home, name="home"),
    path('login/', index, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('journal/', JournalPageView.as_view(), name='journal'),
    path('add_assignment/', AddAssignmentView.as_view(), name='add_assignment'),
    path('add_reflection/', AddReflectionView.as_view(), name='add_reflection'),
    path('assignment_detail/<int:assignment_id>/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('lesson_assignment/<int:assignment_id>/', LessonAssignmentView.as_view(), name='lesson_assignment'),
    path('activity_assignment/<int:assignment_id>/', ActivityAssignmentView.as_view(), name='activity_assignment'),
    path('quiz_assignment/<int:assignment_id>/', QuizAssignmentView.as_view(), name='quiz_assignment'),
    path('assessment_assignment/<int:assignment_id>/', AssessmentAssignmentView.as_view(), name='assessment_assignment'),
    path('completed_assignment/<int:assignment_id>/', CompletedAssignmentView.as_view(), name='completed_assignment'),
    path('delete_assignment/<int:assignment_id>/', DeleteAssignmentView.as_view(), name='delete_assignment'),
    path('delete_reflection/<int:reflection_id>/', DeleteReflectionView.as_view(), name='delete_reflection'),
    path('blog/', views.blog_index, name="blog"),
    path('create_post/', views.create_post, name="create_post"),
    path('search/', views.search, name="search"),
    path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('comment/<int:id>/', views.comment, name="comment"),
    path('article/<int:id>/', views.article, name="article"),
    path('upvote/<int:id>/', views.up_vote, name="upvote"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
