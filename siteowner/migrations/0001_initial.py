# Generated by Django 2.2.7 on 2019-11-15 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Luke', max_length=50)),
                ('family_name', models.CharField(default='Gao', max_length=50)),
                ('intro', models.CharField(max_length=255, null=True)),
                ('github', models.URLField(verbose_name='github account')),
                ('wechat', models.URLField(verbose_name='wechat id')),
                ('linkedin', models.URLField(verbose_name='linkedin account')),
                ('twitter', models.URLField(verbose_name='twitter account')),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]
