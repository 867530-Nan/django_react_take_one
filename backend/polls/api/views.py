# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )
# from polls.models import Question
# from .serializers import PollSerializer

# class PollListView(ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = PollSerializer


# class PollCreateView(CreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = PollSerializer


# class PollRetrieveView(RetrieveAPIView):
#     queryset = Question.objects.all()
#     serializer_class = PollSerializer


# class PollDestroyView(DestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = PollSerializer


# class PollUpdateView(UpdateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = PollSerializer

from rest_framework import viewsets

from .serializers import PollSerializer
from polls.models import Question


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Question.objects.all()
