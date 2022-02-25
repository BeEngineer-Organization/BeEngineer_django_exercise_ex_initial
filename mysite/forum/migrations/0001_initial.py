# Generated by Django 4.0.2 on 2022-02-25 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='トピック名')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='タグ名')),
                ('message', models.ManyToManyField(blank=True, null=True, related_name='tag', to='forum.Message')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topic'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='forum.message')),
            ],
        ),
    ]