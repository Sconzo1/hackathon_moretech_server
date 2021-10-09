from rest_framework import serializers

from .models import *


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = '__all__'


class LevelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelStatus
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class TheorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Theory
        fields = '__all__'


class TheoryDatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheoryDatum
        fields = '__all__'


class TheoryDatumTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheoryDatumTag
        fields = '__all__'


class MiniGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniGame
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class LevelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelTag
        fields = '__all__'


class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = '__all__'


class UserMiniGameRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMiniGameReward
        fields = '__all__'


class UserTheoryRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTheoryReward
        fields = '__all__'
