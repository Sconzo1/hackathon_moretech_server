import uuid

from django.contrib.postgres import fields
from django.db import models


# Reference tables
class Sex(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'sex'
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'marital_statuses'
        verbose_name = 'Семейное положение'
        verbose_name_plural = 'Семейные положения'

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'difficulties'
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Content(models.Model):
    pass


class Rarity(models.Model):
    name = models.CharField('Название', max_length=200)
    max_count_shards = models.PositiveSmallIntegerField('Макс. кол-во шардов')
    color = models.CharField('Цвет HEX', max_length=7)

    class Meta:
        db_table = 'rarities'
        verbose_name = 'Редкость'
        verbose_name_plural = 'Редкости'

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField('Название', max_length=200)
    company_name = models.CharField('Название компании', max_length=200)
    id_rarity = models.ForeignKey(Rarity, verbose_name='Редкость', on_delete=models.CASCADE,
                                  db_column='id_rarity')

    class Meta:
        db_table = 'stocks'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField('Название', max_length=200)
    max_value = models.PositiveSmallIntegerField('Макс. уровень')

    class Meta:
        db_table = 'skills'
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class GameType(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'game_types'
        verbose_name = 'Тип игры'
        verbose_name_plural = 'Типы игр'

    def __str__(self):
        return self.name


class LevelStatus(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'level_statuses'
        verbose_name = 'Статус уровня'
        verbose_name_plural = 'Статусы уровня'

    def __str__(self):
        return self.name


# Operated models tables


class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    age = models.PositiveSmallIntegerField('Возраст')
    id_marital_status = models.ForeignKey(MaritalStatus, verbose_name='Семейное положение', on_delete=models.CASCADE,
                                          db_column='id_marital_status')
    id_sex = models.ForeignKey(Sex, verbose_name='Пол', on_delete=models.CASCADE,
                               db_column='id_sex')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.uuid


class Theme(models.Model):
    name = models.CharField('Название', max_length=200)
    id_difficulty = models.ForeignKey(Difficulty, verbose_name='Сложность', on_delete=models.CASCADE,
                                      db_column='id_difficulty')

    class Meta:
        db_table = 'themes'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Theory(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    id_content = models.OneToOneField(Content, on_delete=models.CASCADE, db_column='id_content')

    class Meta:
        db_table = 'theory'
        verbose_name = 'Раздел теории'
        verbose_name_plural = 'Разделы теории'

    def __str__(self):
        return self.title


class TheoryDatum(models.Model):
    id_theory = models.ForeignKey(Theory, verbose_name='Раздел теории', on_delete=models.CASCADE, db_column='id_theory')
    src = models.CharField('Изображение', max_length=200)
    body = models.TextField('Текст')

    class Meta:
        db_table = 'theory_data'
        verbose_name = 'Единица теории'
        verbose_name_plural = 'Единицы теории'

    def __str__(self):
        return f"{self.id_theory}"


class TheoryDatumTag(models.Model):
    id_theory_datum = models.ForeignKey(TheoryDatum, verbose_name='Единица теории', on_delete=models.CASCADE,
                                        db_column='id_theory_datum')
    id_tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE, db_column='id_tag')

    class Meta:
        db_table = 'theory_datum_tags'
        verbose_name = 'Уровень-Тег'
        verbose_name_plural = 'Уровни-Теги'

    def __str__(self):
        return f"Datum: {self.id_theory_datum} || tag: {self.id_tag}"


class MiniGame(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    src = models.CharField('Изображение', max_length=200)
    body = models.TextField('Текст')
    right_answer = models.CharField('Правильный ответ', max_length=200)
    other_answers = fields.ArrayField(models.CharField(max_length=200), verbose_name='Неправильные ответы')
    src_right = models.CharField('Изображение при правильном ответе', max_length=200)
    body_right = models.TextField('Текст при правильном ответе')
    src_wrong = models.CharField('Изображение при неправильном ответе', max_length=200)
    body_wrong = models.TextField('Текст при неправильном ответе')
    id_type_game = models.ForeignKey(GameType, verbose_name='Тип игры', on_delete=models.CASCADE,
                                     db_column='id_type_game')
    id_content = models.OneToOneField(Content, on_delete=models.CASCADE, db_column='id_content')

    class Meta:
        db_table = 'minigames'
        verbose_name = 'Мини-игра'
        verbose_name_plural = 'Мини-игры'

    def __str__(self):
        return self.title


class Level(models.Model):
    id_theme = models.ForeignKey(Theme, verbose_name='Тема', on_delete=models.CASCADE,
                                 db_column='id_theme')
    id_difficulty = models.ForeignKey(Difficulty, verbose_name='Сложность', on_delete=models.CASCADE,
                                      db_column='id_difficulty')
    id_content = models.ForeignKey(Content, verbose_name='Контент', on_delete=models.CASCADE, db_column='id_content')
    is_optional = models.BooleanField('Опционально?', default=False)

    class Meta:
        db_table = 'levels'
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return f"{self.id_theme} || {self.pk}"


class Route(models.Model):
    id_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                db_column='id_user')
    id_theme = models.ForeignKey(Theme, verbose_name='Тема', on_delete=models.CASCADE,
                                 db_column='id_theme')
    serial_number = models.PositiveSmallIntegerField('Порядковый номер')

    class Meta:
        db_table = 'routes'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return f"{self.id_user} || {self.serial_number} : {self.id_theme}"


# Relationship tables


class LevelTag(models.Model):
    id_level = models.ForeignKey(Level, verbose_name='Уровень', on_delete=models.CASCADE, db_column='id_level')
    id_tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE, db_column='id_tag')

    class Meta:
        db_table = 'level_tags'
        verbose_name = 'Уровень-Тег'
        verbose_name_plural = 'Уровни-Теги'

    def __str__(self):
        return f"Lvl: {self.id_level} || tag: {self.id_tag}"


class UserLevel(models.Model):
    id_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                db_column='id_user')
    id_level = models.ForeignKey(Level, verbose_name='Уровень', on_delete=models.CASCADE, db_column='id_level')
    id_status = models.ForeignKey(LevelStatus, verbose_name='Статус', on_delete=models.CASCADE,
                                  db_column='id_status')
    count_errors = models.PositiveSmallIntegerField('Кол-во ошибок', default=0)
    active_time = models.PositiveIntegerField('Кол-во потраченных секунд', default=0)

    class Meta:
        db_table = 'user_levels'
        verbose_name = 'Пользователь-Уровень'
        verbose_name_plural = 'Пользователи-Уровни'

    def __str__(self):
        return f"{self.id_user} || {self.id_level}"


class UserMiniGameReward(models.Model):
    id_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                db_column='id_user')
    id_stock = models.ForeignKey(Stock, verbose_name='Акция', on_delete=models.CASCADE,
                                 db_column='id_stock')
    count_shards = models.PositiveSmallIntegerField('Кол-во шардов')
    created_at = models.DateField('Время получения', auto_now=True)

    class Meta:
        db_table = 'user_minigame_rewards'
        verbose_name = 'Пользователь-Награда игры'
        verbose_name_plural = 'Пользователи-Награды игры'

    def __str__(self):
        return f"{self.created_at} || {self.id_stock} x {self.count_shards} => {self.id_user}"


class UserTheoryReward(models.Model):
    id_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                db_column='id_user')
    id_skill = models.ForeignKey(Skill, verbose_name='Навык', on_delete=models.CASCADE,
                                 db_column='id_skill')
    value = models.FloatField('Прирост навыка')
    created_at = models.DateField('Время получения', auto_now=True)

    class Meta:
        db_table = 'user_theory_rewards'
        verbose_name = 'Пользователь-Награда обучения'
        verbose_name_plural = 'Пользователи-Награды обучения'

    def __str__(self):
        return f"{self.created_at} || {self.id_skill} + {self.value} => {self.id_user}"
