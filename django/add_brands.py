import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson2.settings')
django.setup()

from user.models import Brand

brands_data = [
    {'name': 'Nike', 'country': 'США', 'description': 'Американський бренд спортивного одягу та взуття'},
    {'name': 'Samsung', 'country': 'Південна Корея', 'description': 'Південнокорейська компанія електроніки'},
    {'name': 'Adidas', 'country': 'Німеччина', 'description': 'Німецький виробник спортивних товарів'},
    {'name': 'Sony', 'country': 'Японія', 'description': 'Японська корпорація електроніки та розваг'},
    {'name': 'Apple', 'country': 'США', 'description': 'Американська технологічна компанія'},
]

for data in brands_data:
    Brand.objects.create(**data)
    print(f'Створено бренд: {data["name"]}')

print('Всі бренди успішно додані!')
