# Generated by Django 2.0.4 on 2018-04-24 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=5)),
                ('q_1', models.IntegerField(default=0)),
                ('q_2', models.IntegerField(default=0)),
                ('q_3', models.IntegerField(default=0)),
                ('q_4', models.IntegerField(default=0)),
                ('travel_cost', models.IntegerField(default=100)),
                ('stay_cost', models.IntegerField(default=500)),
                ('residual_income', models.IntegerField(default=500)),
                ('height', models.IntegerField(default=0.5)),
                ('neighborhood', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Name', max_length=25)),
                ('turn', models.IntegerField(default=0)),
                ('board_length', models.IntegerField(default=10)),
                ('num_players', models.IntegerField()),
                ('waiting_to_finish_turn', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=5)),
                ('turn', models.IntegerField(default=0)),
                ('account_balance', models.IntegerField()),
                ('action', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_profiles', to='users.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, unique=True)),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('sw', models.CharField(max_length=255)),
                ('pw', models.CharField(max_length=255)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='player_profile',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_profiles', to='users.User'),
        ),
        migrations.AddField(
            model_name='game',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_games', to='users.User'),
        ),
        migrations.AddField(
            model_name='cell',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cells', to='users.Game'),
        ),
        migrations.AddField(
            model_name='cell',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cells_owned', to='users.Player_Profile'),
        ),
    ]
