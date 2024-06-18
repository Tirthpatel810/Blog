from django.contrib import admin
from django.urls import path,include
from blog import views as v1

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', v1.login_form, name='index'),
    path('login/', v1.home, name='login'),
    path('home/', v1.home,name='home'),
    path('my_posts/', v1.my_posts,name='my_posts'),
    path('accounts/profile/', v1.home),
    path('post/<int:pk>/', v1.post_detail, name='post-detail'),
    path('admin/', v1.admin_dashboard, name='admin-dashboard'),
    path('admin/post/<int:pk>/edit/', v1.edit_post, name='post-edit'),
    path('admin/post/<int:pk>/delete/', v1.delete_post, name='post-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', v1.registration, name='register'),
]