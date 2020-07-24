# Generated by Django 3.0.8 on 2020-07-24 17:08

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=190, null=True, unique=True, verbose_name='E-mail')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Apellido')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is site admin')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('locale', models.CharField(default='en-us', max_length=50, verbose_name='Language')),
                ('timezone', models.CharField(default='UTC', max_length=100, verbose_name='Timezone')),
                ('require_2fa', models.BooleanField(default=False, verbose_name='Two-factor authentication is required to log in')),
                ('notifications_send', models.BooleanField(default=True, help_text='If turned off, you will not get any notifications.', verbose_name='Receive notifications according to my settings below')),
                ('notifications_token', models.CharField(default=accounts.models.generate_notifications_token, max_length=255)),
                ('auth_backend', models.CharField(default='native', max_length=255)),
                ('session_token', models.CharField(default=accounts.models.generate_session_token, max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('email',),
            },
        ),
        migrations.CreateModel(
            name='ExamplePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
