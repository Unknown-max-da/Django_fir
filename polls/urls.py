from django.urls import path
from polls.views import javob

urlpatterns = [
    path('sorov/', javob)
]