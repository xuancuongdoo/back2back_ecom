from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from store.abstract.base.timestamps import TimestampModel


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_('Category Name'),
        max_length=255,
        help_text=_("required and unique"),
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_('Category safe URL'),
        max_length=255,
        unique=True
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True, related_name="children")
    is_active = models.BooleanField(
        default=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name
