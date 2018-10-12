from django_filters import rest_framework as filters
from backend.models import KeyWord, KeyWordType


class KeyWordFilter(filters.FilterSet):
    class Meta:
        model = KeyWord
        # fields = ["id","name_cn","name_en","kw_type","source"]
        fields = "__all__"


class KeyWordTypeFilter(filters.FilterSet):
    class Meta:
        model = KeyWordType
        # fields = ["id","name_cn","name_en","kw_type","source"]
        fields = '__all__'