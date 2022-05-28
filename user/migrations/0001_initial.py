# Generated by Django 4.0.4 on 2022-05-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CharacterName', models.CharField(default='None', max_length=150, unique=True)),
                ('AllianceID', models.BigIntegerField(blank=True, null=True)),
                ('CorporationID', models.BigIntegerField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, max_length=3000, null=True)),
                ('SecurityStatus', models.FloatField(blank=True, null=True)),
                ('AccessToken', models.CharField(blank=True, max_length=500, null=True)),
                ('TokenType', models.CharField(blank=True, max_length=25, null=True)),
                ('ExpiresIn', models.IntegerField(blank=True, null=True)),
                ('RefreshToken', models.CharField(blank=True, max_length=150, null=True)),
                ('Avatar', models.CharField(max_length=150)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '#Users',
            },
        ),
    ]