from haystack.generic_views import SearchView
from drf_haystack.viewsets import HaystackViewSet

from knowledge.models import Article
from knowledge.serializers import ArticleSearchSerializer


class MySearchView(SearchView):
    """My custom search view."""

    def get_queryset(self):
        print(self.request)
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        print("test")
        return queryset.all()

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        print("come here")
        return context


class ArticleSearchView(HaystackViewSet):
    index_models = [Article]
    serializer_class = ArticleSearchSerializer
