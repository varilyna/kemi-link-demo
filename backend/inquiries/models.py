from django.db import models


class Inquiry(models.Model):
    name = models.CharField("Name", max_length=120)
    email = models.EmailField("Email")
    question = models.TextField("Question")
    is_answered = models.BooleanField("Answered", default=False, db_index=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "inquiry"
        verbose_name_plural = "inquiries"

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"
