from django.urls import path, include #including list of urls

from rest_framework.routers import DefaultRouter
#from dj_rest_auth.registration.views import RegisterView

from profiles_api import views


router = DefaultRouter()
#router.register('hello-viewset', views.HelloViewSet)
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('datapoint', views.DataPointViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    #path('datapoint/', views.SessionDataView.as_view(), name='sessiondata'),
    path('', include(router.urls))

]
