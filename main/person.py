# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 16:27:06
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 23:02:17

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import indicoio as io
import pickle as pkl
import os
from collections import Counter, defaultdict

class Race:
	def __init__(self, race, crime):
		self.race = race
		self.total = 0
		self.crimes = {}
		self.add(crime)
	def add(self, crime):
		if crime in self.crimes:
			self.crimes[crime] += 1
		else:
			self.crimes[crime] = 1
		self.total += 1
	def print(self):
		print("Race: "+self.race)
		for key,value in self.crimes.items():
			print("%40s: %s" % (str(key), str(value)))
		print()

	def getData(self):
		data = ""
		data += "Race: "+self.race+"  "+"Total: "+str(self.getTotal())+"\n"
		for key,value in self.crimes.items():
			data += "%40s: %s\n" % (str(key), str(value))
		data += "\n"
		return data

	def getTotal(self):
		return self.total

class Crime:
	def __init__(self, crime, allRaces, danger):
		self.crime = crime
		self.races = {race: 0 for race in allRaces}
		self.danger = danger
	def add(self, race):
		self.races[race] += 1
	def print(self):
		print("Crime: "+self.crime)
		for key,value in self.races.items():
			print("%40s: %s" % (str(key), str(value)))
		print()

	def getData(self, rawRelations):
		data = ""
		data += "Crime: "+str(self.crime)+"	Danger: "+str(self.danger)+"\n"
		for key,value in self.races.items():
			data += "%40s: %f\n" % (str(key), value/rawRelations[key].getTotal())
		data += "\n"
		return data

	def getRawData(self,rawRelations):
		data = {}
		for key,value in self.races.items():
			data[key] = value/rawRelations[key].getTotal()
		return data

class BigData:
	def __init__(self, race):
		self.race = race
		self.crimes = {}
		self.x = []
		self.y = []
		self.vals = []
	def addCrime(self, crime, danger, frequency):
		self.crimes[crime] = (1-danger,frequency)
		self.x += [1-danger]
		self.y += [frequency]
		self.vals += [(1-danger, frequency, crime)]


if __name__ == "__main__":
	io.config.api_key = "9bc524ad52580fbbc308b2b136777ef9"
	plotly.tools.set_credentials_file(username="navravi", api_key="uYbUJOZ3VYmK0YILm3Gq")

	allRaces = ["caucasian", "african-american", "asian", "native american", "hispanic", "other"]

	rawRelations = {}
	crimeRelations = {}
	crimesByGroup = {}
	crimeToGroups = defaultdict(list)
	counterByGroup = Counter()
	counterByCrime = Counter()
	groupDangers = {}
	# crimeSentiments = {}
	bigData = {}

	file = open("unique-crimes.txt", "r")

	group = ""
	line = "1"
	while True:
		line = file.readline().strip().lower()
		if not line:
			break
		if line[:2] == "- ":
			group = line[2:]
		else:
			# crimeSentiments[line] = io.sentiment_hq(line)
			crimesByGroup[line] = group
			crimeToGroups[group].append(line)
			counterByCrime[line] += 1
			counterByGroup[group] += 1
	file.close()

	groupDangersPkl = "groupDangers.pkl"
	if os.path.exists(groupDangersPkl):
		with open(groupDangersPkl, 'rb') as pklfile:
			groupDangers = pkl.load(pklfile)
	else:	
		with open(groupDangersPkl, 'wb') as pklfile:
			for key, value in crimeToGroups.items():
				danger = 0
				for crime in value:
					print(crime)
					danger += counterByCrime[crime]*io.sentiment_hq(crime)
				danger /= counterByGroup[key]
				groupDangers[key] = danger
			pkl.dump(groupDangers, pklfile)


	datafile = "compas-scores-two-years.csv"
	df = pd.read_csv(datafile)
	for index, series in df.iterrows():
		crime = str(series["c_charge_desc"]).lower()
		race = str(series["race"]).lower()
		if crime == "nan":
			continue

		crime = crimesByGroup[crime]
		danger = groupDangers[crime]

		# keywords = Counter(io.keywords(crime, version=2))
		# top_words = keywords.most_common(2)
		# keyword = " ".join(x[0] for x in top_words)
		# danger = io.sentiment_hq(crime)
	
		if race in rawRelations:
			rawRelations[race].add(crime)
		else:
			rawRelations[race] = Race(race, crime)
		if crime in crimeRelations:
			crimeRelations[crime].add(race)
		else:
			crimeRelations[crime] = Crime(crime, allRaces, danger)
			crimeRelations[crime].add(race)

	for key, value in crimeRelations.items():
		crime = key
		danger = value.danger
		data = value.getRawData(rawRelations)
		for race, frequency in data.items():
			if race in bigData:
				bigData[race].addCrime(crime, danger, frequency)
			else:
				bigData[race] = BigData(race)
				bigData[race].addCrime(crime, danger, frequency)

	caucasian = sorted(bigData["caucasian"].vals, key=lambda x: x[0])
	trace_caucasian = go.Scatter(
	    x = [val[0] for val in caucasian],
	    y = [val[1] for val in caucasian],
	    text = [val[2] for val in caucasian],
	    name = 'Caucasian',
	   	marker = dict(
	        size = 10,
	        color = 'rgba(39, 174, 96,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(39, 174, 96,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)
	)

	african_american = sorted(bigData["african-american"].vals, key=lambda x: x[0])
	trace_african_american = go.Scatter(
	    x = [val[0] for val in african_american],
	    y = [val[1] for val in african_american],
	   	text = [val[2] for val in african_american],
	    name = 'African-American',
	   	marker = dict(
	        size = 10,
	        color = 'rgba(41, 128, 185,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(41, 128, 185,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)
	)

	hispanic = sorted(bigData["hispanic"].vals, key=lambda x: x[0])
	trace_hispanic = go.Scatter(
	    x = [val[0] for val in hispanic],
	    y = [val[1] for val in hispanic],
		text = [val[2] for val in hispanic],
	    name = 'Hispanic',
	   	marker = dict(
	        size = 10,
	        color = 'rgba(142, 68, 173,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(142, 68, 173,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)

	)

	native_american = sorted(bigData["native american"].vals, key=lambda x: x[0])
	trace_native_american = go.Scatter(
	    x = [val[0] for val in native_american],
	    y = [val[1] for val in native_american],
		text = [val[2] for val in native_american],
	    name = 'Native American',
	   	marker = dict(
	        size = 10,
	        color = 'rgba(230, 126, 34,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(230, 126, 34,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)
	)

	asian = sorted(bigData["asian"].vals, key=lambda x: x[0])
	trace_asian = go.Scatter(
	    x = [val[0] for val in asian],
	    y = [val[1] for val in asian],
		text = [val[2] for val in asian],
	    name = 'Asian',
	    marker = dict(
	        size = 10,
	        color = 'rgba(231, 76, 60,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(231, 76, 60,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)
	)

	other = sorted(bigData["other"].vals, key=lambda x: x[0])
	trace_other = go.Scatter(
	    x = [val[0] for val in other],
	    y = [val[1] for val in other],
		text = [val[2] for val in other],
	    name = 'Other',
	   	marker = dict(
	        size = 10,
	        color = 'rgba(52, 73, 94,1.0)',
	    ),
	    line = dict(
	    	color = 'rgba(52, 73, 94,1.0)',
	    	width = 1,
	    	dash = "dash"
	    	)
	)

	data = [trace_caucasian, trace_african_american, trace_hispanic, trace_native_american, trace_asian, trace_other]

	layout = dict(title = 'Criminal Activity by Race',
	              yaxis = dict(zeroline = False, title = "Percent Criminal Activity within Race", fixedrange = True),
	              xaxis = dict(zeroline = False, title = "Danger Sentiment", fixedrange = True)
	             )

	fig = dict(data=data, layout=layout)
	py.iplot(fig, filename='styled-scatter')

file = open("raceData.txt","w")
for key,value in rawRelations.items():
	file.write(value.getData())
file.close()

file = open("crimeData.txt","w")
for key in sorted(crimeRelations, key=lambda crime: crimeRelations[crime].danger):
	value = crimeRelations[key]
	file.write(value.getData(rawRelations))
file.close()