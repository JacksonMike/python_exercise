from rest_framework import serializers
from first.models import Book


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


# 自定义验证
def my_validate(value):
    print("111")
    if "敏感信息" in value.lower():
        raise serializers.ValidationError("有敏感信息")
    return value


# class BookSerializer(serializers.Serializer):
#     # 不需要序列化
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate, ])
#     pub_time = serializers.DateField()
#     # 仅正序
#     category = serializers.CharField(source="get_category_display", read_only=True)
#     # 仅反序
#     post_category = serializers.IntegerField(write_only=True)
#     publisher = PublisherSerializer(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#     authors = AuthorSerializer(many=True, read_only=True)
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         book_obj = Book.objects.create(title=validated_data["title"],
#                                        pub_time=validated_data["pub_time"],
#                                        category=validated_data["post_category"],
#                                        publisher_id=validated_data["publisher_id"])
#         print(book_obj)
#         book_obj.authors.add(*validated_data["author_list"])
#         return book_obj
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.pub_time = validated_data.get("pub_time", instance.pub_time)
#         instance.category = validated_data.get("post_category", instance.category)
#         instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
#         if validated_data.get("author_list"):
#             instance.authors.set(validated_data["author_list"])
#         instance.save()
#         return instance
#
#     # 单个验证
#     def validate_title(self, value):
#         print("222")
#         if "python" not in value.lower():
#             raise serializers.ValidationError("标题必须含有python")
#         return value
#
#     # 多个验证
#     def validate(self, attrs):
#         print("333")
#         if "python" in attrs["title"].lower() or attrs["post_category"] == 1:
#             return attrs
#         else:
#             raise serializers.ValidationError("分类或者标题不符合")
#     # 权重由大到小为:自定义>单个>多个

class BookSerializer(serializers.ModelSerializer):
    publisher_info = serializers.SerializerMethodField(read_only=True)
    authors_info = serializers.SerializerMethodField(read_only=True)
    category_display = serializers.SerializerMethodField(read_only=True)

    def get_publisher_info(self, obj):
        publisher_obj = obj.publisher
        return {"id": publisher_obj.id, "title": publisher_obj.title}

    def get_authors_info(self, obj):
        authors_queryset = obj.authors.all()
        return [{"id": author.id, "name": author.name} for author in authors_queryset]

    def get_category_display(self, obj):
        return obj.get_category_display()

    class Meta:
        model = Book
        fields = "__all__"
        # 外键关系层数,会让所有的外键关系编程 read_only = True
        # depth = 1
        extra_kwargs = {"publisher": {"write_only": True},
                        "authors": {"write_only": True},
                        "category": {"write_only": True}}
