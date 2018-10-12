from rest_framework import serializers
from backend.models import KeyWord, KeyWordType

"""关键词管理类型"""


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = '__all__'
        # fields = ["id", "name_cn", "name_en", "source", "kw_type"]


class KeyWordListSerializer(serializers.ModelSerializer):
    # kw_type = serializers.StringRelatedField(many=False)
    class Meta:
        model = KeyWord
        # fields = '__all__'
        fields = ["id", "name_cn", "name_en", "source", "kw_type"]


"""关键词管理类型"""


class KeyWordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWordType
        fields = '__all__'