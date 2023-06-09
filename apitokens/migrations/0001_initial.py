# Generated by Django 3.2.18 on 2023-03-20 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('knox', '0008_remove_authtoken_salt'),
    ]
    
    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('authtoken_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='knox.authtoken')),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            bases=('knox.authtoken',),
        ),
        migrations.CreateModel(
            name='MyToken',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apitokens.token',),
        ),
    ]
