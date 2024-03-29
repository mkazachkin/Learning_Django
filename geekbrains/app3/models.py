from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=128)
    author_email = models.EmailField()

    def __str__(self):
        return f'Name = {self.author_name}, email: {self.author_email}'


class Post(models.Model):
    post_title = models.CharField(max_length=128)
    post_content = models.TextField()
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'title is {self.post_title}'

    def get_summary(self):
        words = str(self.post_content).split()
        return f'{" ".join(words[:12])}...'
