from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', userlogin, name='login'),
    path('login_admin/', login_admin, name='login_admin'),
    path('signup/', signup1, name='signup'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('upload_notes/', upload_notes, name='upload_notes'),
    path('', index, name='index')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
