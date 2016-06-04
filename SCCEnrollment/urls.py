"""SCCEnrollment URL Configuration

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
from reroute import handler404, handler500, patterns, url, include
from reroute.verbs import verb_url
from django.contrib import admin


profiling = patterns('profiling.views', 
    verb_url('GET', '^personal_information/?$', 'list_personal_information'),
    verb_url('GET', '^personal_information/(?P<pk>\d+)$', 'get_personal_information'),
    verb_url('POST', '^personal_information/?$', 'set_personal_information'),

    verb_url('GET', '^profile/(?P<pk>\d+)$', 'get_profile'),
    verb_url('POST', '^profile$', 'set_profile'),

    verb_url('GET', '^extended_profile/(?P<pk>\d+)$', 'get_extended_profile'),
    verb_url('POST', '^extended_profile$', 'set_extended_profile'),
)

health = patterns('health.views', 
    verb_url('GET', '^medical_history/(?P<pk>\d+)$', 'get_medical_history'),
    verb_url('POST', '^medical_history$', 'set_medical_history'),
)

urlpatterns = [
	url(r'^profiling/', include(profiling)),
	url(r'^health/', include(health)),
	url(r'^admin/', admin.site.urls),
]
