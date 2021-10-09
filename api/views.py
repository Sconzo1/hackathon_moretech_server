from rest_framework import viewsets

from .serializers import *


class SexView(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer


class MaritalStatusView(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer


class DifficultyView(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RarityView(viewsets.ModelViewSet):
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class GameTypeView(viewsets.ModelViewSet):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer


class LevelStatusView(viewsets.ModelViewSet):
    queryset = LevelStatus.objects.all()
    serializer_class = LevelStatusSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ThemeView(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class TheoryView(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer


class TheoryDatumView(viewsets.ModelViewSet):
    queryset = TheoryDatum.objects.all()
    serializer_class = TheoryDatumSerializer


class TheoryDatumTagView(viewsets.ModelViewSet):
    queryset = TheoryDatumTag.objects.all()
    serializer_class = TheoryDatumTagSerializer


class MiniGameView(viewsets.ModelViewSet):
    queryset = MiniGame.objects.all()
    serializer_class = MiniGameSerializer


class LevelView(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class RouteView(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class LevelTagView(viewsets.ModelViewSet):
    queryset = LevelTag.objects.all()
    serializer_class = LevelTagSerializer


class UserLevelView(viewsets.ModelViewSet):
    queryset = UserLevel.objects.all()
    serializer_class = UserLevelSerializer


class UserMiniGameRewardView(viewsets.ModelViewSet):
    queryset = UserMiniGameReward.objects.all()
    serializer_class = UserMiniGameRewardSerializer


class UserTheoryRewardView(viewsets.ModelViewSet):
    queryset = UserTheoryReward.objects.all()
    serializer_class = UserTheoryRewardSerializer
