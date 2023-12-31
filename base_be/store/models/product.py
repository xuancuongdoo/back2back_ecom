from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from store.abstract.base.timestamps import TimestampModel
from .category import Category


class ProductType(models.Model):
    name = models.CharField(
        verbose_name=_('Product Type'),
        help_text=_("Required"),
        max_length=255
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(
        ProductType, on_delete=models.RESTRICT
    )
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_("Required"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(TimestampModel):
    """
    The Product table counts all the products.
    """

    product_type = models.ForeignKey(
        ProductType, on_delete=models.RESTRICT
    )
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        help_text=_("Required")
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_("Not Required"),
        blank=True
    )
    slug = models.SlugField(
        max_length=255,
    )
    regular_price = models.DecimalField(
        verbose_name=_('Regular Price'),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_('Discounted Price'),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("Change product visibility"),
        verbose_name=_("Product visibility"),
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table contains all the values of the product specifications
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    specification = models.ForeignKey(
        ProductSpecification,
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        verbose_name=_('Value'),
        max_length=255,
        help_text=_("Product Specification Value (maximum of 255 words)"),
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(TimestampModel):
    """
    The Product Image table
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name=_(
            "image"
        ),
        help_text=_(
            "Upload a product image"
        ),
        upload_to="images/",
        default="images/default.jpg",
    )
    alt_text = models.CharField(
        verbose_name=_('Alt Text'),
        max_length=255,
        blank=True,
        null=True
    )
    is_feature = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
