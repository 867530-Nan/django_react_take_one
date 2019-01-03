from .views import PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PollViewSet, basename='polls')
urlpatterns = router.urls

# from django.urls import path

# from .views import (
#     PollListView,
#     PollRetrieveView,
#     PollCreateView,
#     PollDestroyView,
#     PollUpdateView
# )

# urlpatterns = [
#     path('', PollListView.as_view()),
#     path('create/', PollCreateView.as_view()),
#     path('<pk>', PollRetrieveView.as_view()),
#     path('<pk>/delete/', PollDestroyView.as_view()),
#     path('<pk>/update/', PollUpdateView.as_view())
# ]
