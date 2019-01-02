from rest_framework import serializers

from polls.models import Question, Choice


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
