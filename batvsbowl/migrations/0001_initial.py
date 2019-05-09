# Generated by Django 2.1.5 on 2019-05-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IplMatch',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_date', models.DateTimeField(blank=True, null=True)),
                ('team_name_id', models.IntegerField(blank=True, null=True)),
                ('opponent_team_id', models.IntegerField(blank=True, null=True)),
                ('season_id', models.IntegerField(blank=True, null=True)),
                ('venue_name', models.TextField(blank=True, null=True)),
                ('toss_winner_id', models.IntegerField(blank=True, null=True)),
                ('toss_decision', models.TextField(blank=True, null=True)),
                ('is_superover', models.IntegerField(blank=True, null=True)),
                ('is_result', models.IntegerField(blank=True, null=True)),
                ('is_duckworthlewis', models.IntegerField(blank=True, null=True)),
                ('win_type', models.TextField(blank=True, null=True)),
                ('won_by', models.TextField(blank=True, null=True)),
                ('match_winner_id', models.IntegerField(blank=True, null=True)),
                ('man_of_the_match_id', models.IntegerField(blank=True, null=True)),
                ('first_umpire_id', models.IntegerField(blank=True, null=True)),
                ('second_umpire_id', models.IntegerField(blank=True, null=True)),
                ('city_name', models.TextField(blank=True, null=True)),
                ('host_country', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ipl_match',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerIpl',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.TextField()),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('batting_hand', models.TextField(blank=True, null=True)),
                ('bowling_skill', models.TextField(blank=True, null=True)),
                ('country', models.TextField()),
                ('is_umpire', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'player_ipl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('player_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('is_keeper', models.IntegerField()),
                ('is_captain', models.IntegerField()),
            ],
            options={
                'db_table': 'player_match',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season_id', models.IntegerField(primary_key=True, serialize=False)),
                ('season_year', models.IntegerField(blank=True, null=True)),
                ('orange_cap_id', models.IntegerField(blank=True, null=True)),
                ('purple_cap_id', models.IntegerField(blank=True, db_column='purple_cap_Id', null=True)),
                ('man_of_the_series_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeamIpl',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.TextField(blank=True, null=True)),
                ('team_short_code', models.TextField(blank=True, null=True)),
                ('team_logo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'team_ipl',
                'managed': False,
            },
        ),
    ]