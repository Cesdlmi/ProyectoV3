"""loginsocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""



from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout_then_login
from principal.views import MenuView, AlumnosView, DocentesView, MateriasView, IndexView, materias_list, docentes_list, alumnos_View, infoAlumno_View, eleccion
#urlpatterns = [#patterns('',


    
    #INICIO
    #url(r'^' , include('principal.urls')),
    #url(r'^admin/', admin.site.urls),

#]#)


urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^$' , login, {'template_name':'index.html'}, name= 'login' ),
        


    url(r'^cerrar/$' , logout_then_login,
         name= 'logout' ),


    #url(r'^$', IndexView.as_view()),
    #url(r'^logout/', LogOut, name="log"),
    url(r'^accounts/profile/', infoAlumno_View, name="menu"),
    #url('',include('social_django.urls', namespace ='social')),

    url(r'^Alumnos/', alumnos_View, name = "alum"),
    url(r'^Docentes/', docentes_list, name = "doc"),
    url(r'^Materias/', materias_list, name = "mat"),
    url(r'^eleccion/', eleccion, name = "ele"),
]


