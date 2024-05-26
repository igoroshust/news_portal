from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
from django.db.models import Sum

class Author(models.Model):
    """Автор"""
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE) # связь «один к одному» со встроенной моделью User
    ratingAuthor = models.SmallIntegerField(default=0) # рейтинг автора

    def update_rating(self):
        """Обновление рейтинга"""
        postRat = self.post_set.aggregate(postRating=Sum('rating')) # к модели Post применяется функция .aggregate(), которая применят функцию Sum() к полю rating
        pRat = 0 # промежуточная переменная
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    """Категории"""
    categoryName = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    """Публикации (новости, статьи)"""

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_LIST= (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE) # связь «один ко многим» с моделью Author
    categoryType = models.CharField(max_length=2, choices=CATEGORY_LIST, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True) # запоминаем время создания поста в БД
    postCategory = models.ManyToManyField(Category, through='PostCategory') # связь «многие ко многим» с моделью Category через промежуточную таблицу PostCategory
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[0:128]}..."


class Comment(models.Model):
    """Комментарии"""

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE) # связь «один ко многим» с моделью Post
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE) # связь «один ко многим» с моделью User
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True) # запоминаем время создания комментария в БД
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    """Промежуточная таблица для связи Post-Category"""
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE) # связь «один ко многим» с моделью Post
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE) # связь «один ко многим» с моделью Category