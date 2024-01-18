from django import template
from ..models import Category, Product



register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()



@register.simple_tag
def get_new_products(count=5):
    return Product.objects.filter(available=True).order_by('-created')[:count]

    