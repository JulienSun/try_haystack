from drf_haystack.serializers import HaystackSerializer
from rest_framework.serializers import ModelSerializer

from knowledge.models import Article
from knowledge.search_indexes import ArticleIndex


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ArticleIndex]
        fields = ["text", "title"]
