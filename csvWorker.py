__author__ = 'eweil'
import csv
import json


def LoadHeroList():
    with open('HeroList.json') as f:
        HeroList = json.load()


with open(dota22_TI2018.csv) as csvfile:
