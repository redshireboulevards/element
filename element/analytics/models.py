from django.db import models

from element.accounts.models import User


class AnalyticsActivity(models.Model):
    user = models.ForeignKey(User, related_name='analytics_activities')
    graph = models.CharField('Graph', max_length=255)
    accessed_via = models.PositiveSmallIntegerField('Accessed Via')
    time_spent = models.DurationField('Time Spent')
    score = models.IntegerField('Score')

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return "User #{} used graph: #{} for {}".format(self.user.id, self.graph, self.time_spent.seconds)
