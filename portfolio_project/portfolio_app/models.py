from django.db import models


# Create a job project model
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_app/images/', blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


# Create a message model
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
