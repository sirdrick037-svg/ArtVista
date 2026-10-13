from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="photos",
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PhotoReaction(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"

    REACTION_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name="reactions",
    )
    reaction = models.CharField(
        max_length=10,
        choices=REACTION_CHOICES,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "photo"],
                name="unique_user_photo_reaction",
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.photo.title}"