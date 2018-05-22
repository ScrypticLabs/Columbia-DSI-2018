# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 16:27:06
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 19:25:19

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 

class Race:
	def __init__(self, race, crime):
		self.race = race
		self.crimes = {}
		self.add(crime)
	def add(self, crime):
		if crime in self.crimes:
			self.crimes[crime] += 1
		else:
			self.crimes[crime] = 1
	def print(self):
		print("Race: "+self.race)
		for key,value in self.crimes.items():
			print("%40s: %s" % (str(key), str(value)))
		print()

	def getData(self):
		data = ""
		data += "Race: "+self.race+"\n"
		for key,value in self.crimes.items():
			data += "%40s: %s\n" % (str(key), str(value))
		data += "\n"
		return data

class Crime:
	def __init__(self, crime, race):
		self.crime = crime
		self.races = {}
		self.add(race)
	def add(self, race):
		if race in self.races:
			self.races[race] += 1
		else:
			self.races[race] = 1
	def print(self):
		print("Crime: "+self.crime)
		for key,value in self.races.items():
			print("%40s: %s" % (str(key), str(value)))
		print()

	def getData(self):
		data = ""
		data += "Crime: "+str(self.crime)+"\n"
		for key,value in self.races.items():
			data += "%40s: %s\n" % (str(key), str(value))
		data += "\n"
		return data


if __name__ == "__main__":
	rawRelations = {}
	crimeRelations = {}
	crimesByGroup = {}

	file = open("unique-crimes.txt", "r")

	group = ""
	line = "1"
	while line != "":
		line = file.readline().strip().lower()
		if line[:2] == "- ":
			group = line[2:]
		else:
			crimesByGroup[line] = group
	file.close()


	datafile = "compas-scores-two-years.csv"
	df = pd.read_csv(datafile)
	for index, series in df.iterrows():
		crime = str(series["c_charge_desc"]).lower()
		race = str(series["race"]).lower()
		if crime == "nan":
			continue
		crime = crimesByGroup[crime]
	
		if race in rawRelations:
			rawRelations[race].add(crime)
		else:
			rawRelations[race] = Race(race, crime)
		if crime in crimeRelations:
			crimeRelations[crime].add(race)
		else:
			crimeRelations[crime] = Crime(crime, race)

file = open("rawData.txt","w")
for key,value in rawRelations.items():
	file.write(value.getData())
file.close()

file = open("crimeData.txt","w")
for key,value in crimeRelations.items():
	file.write(value.getData())
file.close()