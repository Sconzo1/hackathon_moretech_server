from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'sexes', SexView)
router.register(r'marital_statuses', MaritalStatusView)
router.register(r'difficulties', DifficultyView)
router.register(r'tags', TagView)
router.register(r'rarities', RarityView)
router.register(r'stocks', StockView)
router.register(r'skills', SkillView)
router.register(r'game_types', GameTypeView)
router.register(r'level_statuses', LevelStatusView)
router.register(r'users', UserView)
router.register(r'themes', ThemeView)
router.register(r'theories', TheoryView)
router.register(r'theory_data', TheoryDatumView)
router.register(r'theory_datum_tags', TheoryDatumTagView)
router.register(r'minigames', MiniGameView)
router.register(r'levels', LevelView)
router.register(r'routes', RouteView)
router.register(r'level_tags', LevelTagView)
router.register(r'user_levels', UserLevelView)
router.register(r'user_minigame_rewards', UserMiniGameRewardView)
router.register(r'user_theory_rewards', UserTheoryRewardView)

urlpatterns = router.urls
