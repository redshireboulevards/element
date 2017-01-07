from django.db import models


class Item(models.Model):
    MOVIE_TYPE = 0
    MUSIC_TYPE = 1
    TARGET_TYPES = (
        (MOVIE_TYPE, 'Movie'),
        (MUSIC_TYPE, 'Music'),
    )
    item_type = models.PositiveSmallIntegerField(blank=False, choices=TARGET_TYPES, default=MOVIE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
