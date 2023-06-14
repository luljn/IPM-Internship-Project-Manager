# Generated by Django 4.2.1 on 2023-06-07 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_document_fichier_alter_document_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='document',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='intern.phase'),
        ),
        migrations.AlterField(
            model_name='document',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='intern.project'),
        ),
        migrations.AlterField(
            model_name='document',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='intern.task'),
        ),
        migrations.AlterField(
            model_name='intership',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='durée du stage(en semaines)'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='durée de la phase(en jours)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='durée du projet(en semaines)'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='durée de la tâche(en jours)'),
        ),
    ]