from rest_framework import serializers
from ads.models import Post
from users.models import CustomUser


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        obj = self.Meta.model(**validated_data)
        if password is not None:
            obj.set_password(password)
        else:
            print('nope')
        obj.save()
        return obj


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'date_posted', 'author', 'image']
        read_only_fields = ['date_posted']

    """ Returns the username instead of user id in 'author' field """

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['author'] = instance.author.username
        return rep

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
