from django.urls import path
from main.views import Error404, Error500, IndexView, AboutView, ContactsView

app_name = 'main'

handler404 = Error404.as_view()
handler500 = Error500.as_view()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
