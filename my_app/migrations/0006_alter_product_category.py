# Generated by Django 5.1.4 on 2024-12-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('shoes', 'Shoes'), ('shirts', 'Shirts'), ('pants', 'Pants'), ('jackets', 'Jackets'), ('accessories', 'Accessories'), ('sportswear', 'Sportswear'), ('bags', 'Bags'), ('watches', 'Watches')], default='shoes', max_length=500),
        ),
    ]