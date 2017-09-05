from django.conf.urls import url
import example2.views

urlpatterns = [
    url(r'^$', example2.views.formset_view),
]
