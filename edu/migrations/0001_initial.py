# Generated by Django 4.0.10 on 2023-12-02 09:55

from django.db import migrations, models
import edu.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EDU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('descriptions', models.TextField()),
                ('thumbnail', models.ImageField(upload_to=edu.models.get_thumbnail_file_path)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('video', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]