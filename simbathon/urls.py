import imp
from django.contrib import admin
from django.urls import include, path
from projectapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('postcreate', views.postcreate, name='postcreate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
    path('postupdate/<int:post_id>', views.postupdate, name='postupdate'),

    path('detail/<int:post_id>',views.detail, name='detail'),
    path('new_comment/<int:post_id>',views.new_comment, name='new_comment'),
    path('commentdelete/<int:comment_id>', views.commentdelete, name='commentdelete'),
    path('commentupdate/<int:comment_id>', views.commentupdate, name='commentupdate'),

    # path('login/<int:post_id>',accounts_views.login, name='login'),
    # path('logout/<int:post_id>',accounts_views.logout, name='logout'),

    path('freehome/', views.freehome, name='freehome'),
    path('freepostcreate', views.freepostcreate, name='freepostcreate'),
    path('freepostdelete/<int:post_id>', views.freepostdelete, name='freepostdelete'),
    path('freepostupdate/<int:post_id>', views.freepostupdate, name='freepostupdate'),

    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),
    path('freecommentdelete/<int:comment_id>', views.freecommentdelete, name='freecommentdelete'),
    path('freecommentupdate/<int:comment_id>', views.freecommentupdate, name='freecommentupdate'),

    path('filterfreepost/', views.filterfreepost, name='filterfreepost'),
    path('filterpost/', views.filterpost, name='filterpost'),

    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
