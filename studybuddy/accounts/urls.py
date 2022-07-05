from django.contrib import admin
from django.urls import path,include
from django.urls import path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
router = routers.DefaultRouter()
urlpatterns = [
    path('api/', include(router.urls)),
   path('', views.redirecthome, name='home'),
    path('home/', views.home, name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('redirecthome/',views.redirecthome,name='availablecourse'),
    path('logout/', views.logoutUser, name="logout"), 
    path('javacourse/',views.javacourseview,name="javacourse"),
    path('cppcourse/',views.cppcourseview,name="cppcourse"),
    path('about/',views.aboutview,name="about"),
    path('pythoncourse/',views.pythoncourseview,name="pythoncourse"),
    path('quizjava/',views.quizjavaview,name="quizjava"),
    path('quizpython',views.quizpythonview,name="quizpython"),
    path('quizcpp',views.quizcppview,name="quizcpp"),
    path('availcourse/',views.availcourseview,name="availcourse"),
    path('viewbook/',views.viewbookspage,name="viewbook"),
    path('viewjavabook/',views.javabookview,name="viewjavabook"),
    path('viewpythonbook/',views.pythonbookview,name="viewpythonbook"),
    path('viewcppbook/',views.cppbookview,name="viewcppbook"),
    path('enrollc/',views.viewenrollpage,name="enrollc"),
    path('discussionforumview/',views.discussionforum,name="discussionforumview"),
    path('replyforumview/<int:myid>' ,views.replyforum,name="replyforumview"),
    path('editor/',views.editorview,name="editor"),
    path('delete_document/<int:docid>/',views.delete_document, name='delete_document'),
    path('feedback/',views.FormView,name="feedback"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()