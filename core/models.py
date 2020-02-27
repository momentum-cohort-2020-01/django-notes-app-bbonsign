from django.db import models


class Note(models.Model):
    """A model for a note"""
    title = models.CharField(max_length=256, help_text="Title of the note")
    body = models.TextField(help_text="The body of the note")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Note object (in Admin site etc.)."""
        return self.title

    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(id)])
