from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models.category import (
    Category,
)

from .models.product import (
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType
)

admin.site.register(Category, MPTTModelAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
        ProductImageInline
    ]
