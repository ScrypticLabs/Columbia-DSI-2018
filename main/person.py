# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 16:27:06
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 17:21:05

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 

class Race:
	def __init__(self, race):
		self.race = race
		self.crimes = {}
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
	def __init__(self, crime):
		self.crime = crime
		self.races = {}
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

rawRelations = {}
crimeRelations = {}

if __name__ == "__main__":
	datafile = "compas-scores-two-years-violent.csv"
	df = pd.read_csv(datafile)
	for index, series in df.iterrows():
		crime = series["c_charge_desc"]
		race = series["race"]
		if race in rawRelations:
			rawRelations[race].add(crime)
		else:
			rawRelations[race] = Race(race)

		if crime in crimeRelations:
			crimeRelations[crime].add(race)
		else:
			crimeRelations[crime] = Crime(crime)

# print(relations["African-American"].crimes)
file = open("rawData.txt","w")
for key,value in rawRelations.items():
	file.write(value.getData())
file.close()

file = open("crimeData.txt","w")
for key,value in crimeRelations.items():
	file.write(value.getData())
file.close()