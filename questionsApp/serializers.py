from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'metrics', 'tags', 'created_at', 'modified_at', 'url')