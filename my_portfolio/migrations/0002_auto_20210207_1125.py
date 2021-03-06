# Generated by Django 3.1.6 on 2021-02-07 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='is_thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='my_portfolio.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(blank=True, null=True, related_name='Project_technology', to='my_portfolio.Technology'),
        ),
        migrations.AlterField(
            model_name='project',
            name='visit_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
