# Generated by Django 3.0.7 on 2020-06-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intrest_category',
            name='Category_Image',
            field=models.ImageField(upload_to='images/category'),
        ),
        migrations.AlterField(
            model_name='intrest_sub_category',
            name='Sub_Category_Image',
            field=models.ImageField(upload_to='images/subcategory'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='Videos',
            field=models.FileField(upload_to='videos'),
        ),
    ]
