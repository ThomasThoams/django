# Generated by Django 5.1.2 on 2024-10-25 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PanierArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.article')),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.panier')),
            ],
        ),
        migrations.AddField(
            model_name='panier',
            name='articles',
            field=models.ManyToManyField(through='boutique.PanierArticle', to='boutique.article'),
        ),
    ]