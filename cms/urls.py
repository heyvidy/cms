
from django.contrib import admin
from django.urls import path

from blog.views import home, create_post, post_page, signin, signup, signout

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home),
	path('create/', create_post),
	path('post/<int:post_id>/', post_page),
	path('login/', signin),
	path('signup/', signup),
	path('logout/', signout)
]
