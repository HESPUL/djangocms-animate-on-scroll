# Generated by Django 3.2.16 on 2023-03-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_animate_on_scroll', '0003_animateonscroll_element_aos_mirror'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animateonscroll_element',
            name='aos_once',
            field=models.BooleanField(help_text='Choose whether animation should fire once, or every time you scroll down to element', null=True, verbose_name='Once'),
        ),
    ]
