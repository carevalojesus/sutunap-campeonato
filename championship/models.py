from django.db import models


# Create your models here.
class Edition(models.Model):
    title = models.CharField(max_length=255)
    season = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.season}'


class DepartamentCollege(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.short_name}'


class Departament(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    departament_college = models.ForeignKey(DepartamentCollege, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.departament_college} - {self.name} - {self.short_name}'


class Team(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    logo = models.ImageField(upload_to='teams/', null=True, blank=True)
    departament_college = models.ForeignKey(DepartamentCollege, on_delete=models.CASCADE)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    ROLES = [
        ('DOCENTE', 'Docente'),
        ('ADMINISTRATIVO', 'Administrativo'),
        ('CAS', 'CAS'),
        ('RxH', 'Recibo por Honorarios'),
    ]
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    document = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='players/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_expelled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.lastname} - {self.document} - {self.team.short_name}'


class Delegate(models.Model):
    team = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='delegate_as_team')
    player = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='delegate_as_player')

    def __str__(self):
        return f'{self.team.team.short_name} - {self.player.name} {self.player.lastname}'


class Phase(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(help_text="Orden de la fase en el campeonato")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    teams = models.ManyToManyField(Team)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MatchDay(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.group.name} - {self.name} - {self.date}'


class Match(models.Model):
    match_day = models.ForeignKey(MatchDay, on_delete=models.CASCADE, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(default=30)
    start_time = models.TimeField(null=True, blank=True)
    home_team = models.ForeignKey(Team, related_name='matches_as_home', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='matches_as_away', on_delete=models.CASCADE)
    home_goals = models.PositiveIntegerField(default=0)
    away_goals = models.PositiveIntegerField(default=0)
    is_played = models.BooleanField(default=False)
    is_reprogrammed = models.BooleanField(default=False)
    OUTCOMES = [
        ('GANO_LOCAL', 'Ganó Local'),
        ('GANO_VISITANTE', 'Ganó Visitante'),
        ('EMPATE', 'Empate')
    ]
    outcome = models.CharField(choices=OUTCOMES, max_length=30, blank=True, null=True)
    is_validated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}  - {self.time}'


class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    time = models.TimeField(null=True, blank=True)
    is_validated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.player.name} - {self.player} - {self.team} - {self.match} - {self.match.away_goals}'


class Card(models.Model):
    TYPES = [
        ('AMARILLA', 'Amarilla'),
        ('ROJA', 'Roja')
    ]
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card_type = models.CharField(choices=TYPES, max_length=10)
    minute = models.PositiveIntegerField()
    is_validated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.player.name} {self.player.lastname} - {self.match.home_team.short_name} - {self.match.away_team.short_name} - {self.card_type}'


class Substitution(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_out = models.ForeignKey(Player, related_name='subs_out', on_delete=models.CASCADE)
    player_in = models.ForeignKey(Player, related_name='subs_in', on_delete=models.CASCADE)
    minute = models.PositiveIntegerField()
    is_validated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.player_out.name} {self.player_out.lastname} - {self.player_in.name} {self.player_in.lastname} - {self.match.home_team.short_name} - {self.match.away_team.short_name}'


class Expulsion(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.PositiveIntegerField()
    reason = models.TextField()
    is_validated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.player.name} {self.player.lastname} - {self.match.home_team.short_name} - {self.match.away_team.short_name} - {self.reason}'


class Reprogramming(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_validated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.match.home_team.short_name} vs {self.match.away_team.short_name} - {self.date} - {self.time}'
