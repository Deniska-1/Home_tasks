import uuid
import fileinput
import os
import argparse
import json


class Team:

    def __init__(self, name, players=None):
        self.id = str(uuid.uuid4())
        self.name = name
        if not players:
            self.players = []
        else:
            ...
        self.add_team_in_list()

    def add_team_in_list(self):
        with open('Teams.txt', 'a') as file:
            file.write(str(self.id) + ':' + self.name + ':')
            file.write(json.dumps(self.players))
            file.write('\n')


class Player:

    def __init__(self, name, team):
        self.id = str(uuid.uuid4())
        self.name = name
        self.team = team
        self.find_team(team)
        self.add_player_in_list()
        self.add_team_player()

    def add_player_in_list(self):
        with open('Players.txt', 'a') as file:
            file.write(str(self.id) + ':' + self.name + ':' + str(self.team) + '\n')

    def delete_player_from_list(self):
        old = str(self.id) + ':' + self.name + ':' + str(self.team)
        with fileinput.FileInput('Players.txt', inplace=True, backup='.bak') as file:
            for line in file:
                line = line.strip()
                sep = '' if line == old else '\n'
                print('' if line == old else line, sep=sep)
        os.unlink('Players.txt' + '.bak')

    def add_team_player(self):
        name, players = self.find_team()
        new = players[:]
        new.append(self.id)
        self.team_replace(name, new)

    def team_replace(self, name, players):
        old = [str(self.team), name]
        with fileinput.FileInput('Teams.txt', inplace=True, backup='.bak') as file:
            for line in file:
                line = line.strip()
                lst = line.split(':')[:-1]
                print(str(self.team) + ':' + name + ':' + json.dumps(players) if lst == old else line)
        os.unlink('Teams.txt' + '.bak')

    def find_team(self, name=None):
        if not name:
            with open("Teams.txt") as file:
                for i in file.readlines():
                    lst = i.strip().split(':')
                    if lst[0] == self.team:
                        a = lst[2]
                        return lst[1], json.loads(lst[2])
        else:
            with open('Teams.txt') as file:
                for i in file.readlines():
                    lst = i.strip().split(':')
                    if lst[1] == name:
                        self.team = lst[0]


"""
Расширенный функционал, но его нужно переработать, что бы работал с информацией из файла, а не 
с экземплярами класса Player.
 
    def delete_team_player(self, player_id, name, players):
        if player_id in players:
            new = players[:]
            new.remove(player)
            self.team_replace(name, new)
        else:
            print("There aren't this player in this team.")   
    
    def change_club(self, new_team):
        self.delete_player_from_list()
        self.find_team(new_team)
        self.add_team_player()
"""


class Match:

    def __init__(self, date, location, result, team1, team2):
        self.id = str(uuid.uuid4())
        self.date = date
        self.location = location
        self.result = result
        self.team1 = self.find(team1, choice='team')
        self.team2 = self.find(team2, choice='team')
        self.players = {}
        self.players.update(self.find(team1, choice='team and players'))
        self.players.update(self.find(team2, choice='team and players'))
        self.write_match_info()

    def find(self, team, choice):
        with open('Teams.txt') as file:
            for i in file.readlines():
                lst = i.strip().split(':')
                if lst[1] == team:
                    if choice == 'team':
                        return lst[0]
                    if choice == 'team and players':
                        return {lst[0]:json.dumps(lst[2])}

    def write_match_info(self):
        with open('Match.txt', 'a') as file:
            file.write(self.id + '_' + self.date + '_' + self.location + '_')
            file.write(self.result + '_' + json.dumps([self.team1, self.team2]) + '_' + json.dumps(self.players) + '\n')


def find_match(date1=(0, 0, 0), date2=(3000, 0, 0)):
    list_of_matches = []
    date1 = date1[0] * 365 + date1[1] * 30 + date1[2]
    date2 = date2[0] * 365 + date2[1] * 30 + date2[2]
    with open('Match.txt') as file:
        for i in file.readlines():
            j = i.split('_')[1].split('-')
            value_of_date = int(j[0]) * 365 + int(j[1]) * 30 + int(j[2])
            if date1 <= value_of_date <= date2:
                list_of_matches.append(i.split('_')[1:])
    print_results_of_finding(list_of_matches)


def print_results_of_finding(list_of_matches):
    for i in list_of_matches:
        if i:
            print(i[0], i[1], '\n', end='')
            teams = json.loads(i[3])
            list_of_teams = find_team(*teams)
            print(list_of_teams[0], i[2], list_of_teams[1])
            players = json.loads(i[4])
            print(list_of_teams[0], '- ', end='')
            lst1 = json.loads(json.loads(players[teams[0]]))
            str1 = ''
            for i in find_players(*lst1):
                str1 += i + ', '
            print(str1[:-2] + '.')
            print(list_of_teams[1], '- ', end='')
            lst2 = json.loads(json.loads(players[teams[1]]))
            str2 = ''
            for i in find_players(*lst2):
                str2 += i + ', '
            print(str2[:-2] + '.')


def find_team(*args):
    list_of_team = []
    with open('Teams.txt') as file:
        for i in file.readlines():
            for j in args:
                lst = i.split(':')
                if j == lst[0]: list_of_team.append(lst[1])
    return list_of_team


def find_players(*args):
    list_of_players = []
    with open('Players.txt') as file:
        for i in file.readlines():
            for j in args:
                lst = i.split(':')
                if j == lst[0]: list_of_players.append(lst[1])
    return list_of_players


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--teams', nargs='+', dest='teams', default=[('Manchester', []), ('Olimpic', [])])
    parser.add_argument('--players', nargs='+', dest='players', default=[('Diego', 'Manchester'),
                                                                         ('Vasia', 'Manchester'),
                                                                         ('Maradonna', 'Olimpic'),
                                                                         ('Hleb', 'Olimpic')])
    parser.add_argument('--match', nargs='+', dest='match', default=[('2019-01-31', 'Manchester-city', '3-2', 'Manchester','Olimpic'),
                                                                     ('2019-02-16', 'Valencia', '1-1', 'Olimpic', 'Manchester')])

    pars = parser.parse_args()
    for i in pars.teams:
        team = Team(i[0], i[1])
    for j in pars.players:
        player = Player(j[0], j[1])
    for k in pars.match:
        match = Match(*k)
    find_match()
    find_match(date1=[2019, 1, 1])
    find_match(date2=[2019, 1, 1])
    find_match((2019, 1, 1), (2019, 2, 1))
    find_match((2019, 1, 1), (2019, 3, 1))
    find_match([2019, 2, 1], [2019, 3, 1])
