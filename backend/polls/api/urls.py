from django.urls import path

from .views import PollListView, PollRetrieveView

urlpatterns = [
    path('', PollListView.as_view()),
    path('<pk>', PollRetrieveView.as_view())
]
