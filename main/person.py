# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 16:27:06
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 17:11:22

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


relations = {}


if __name__ == "__main__":
	datafile = "compas-scores-two-years-violent.csv"
	df = pd.read_csv(datafile)
	for index, series in df.iterrows():
		crime = series["c_charge_desc"]
		race = series["race"]
		if race in relations:
			relations[race].add(crime)
		else:
			relations[race] = Race(race)

# print(relations["African-American"].crimes)
file = open("data.txt","w")
for key,value in relations.items():
	file.write(value.getData())
file.close()
