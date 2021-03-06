from django.db import models

class Topic(models.Model):
    name = models.CharField("トピック名", max_length=20)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.CharField("内容", max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日時", auto_now_add=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField("内容", max_length=200)
    created_at = models.DateTimeField("投稿日時", auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField("タグ名", max_length=20)
    message = models.ManyToManyField(Message, null=True, blank=True, related_name="tag")

    def __str__(self):
        return self.name