# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 18:42:50
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 18:56:20

file = open("unique-crimes.txt", "r")
crimesByGroup = {}

group = ""
line = "1"
while line != "":
	line = file.readline()
	if line[:2] == "- ":
		group = line[2:]
	else:
		crimesByGroup[line] = group

for key,value in crimesByGroup.items():
	print(key+"   "+value)

file.close()