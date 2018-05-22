# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 18:07:24
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 18:19:27

import indicoio as io
from collections import Counter
io.config.api_key = "9bc524ad52580fbbc308b2b136777ef9"

file = open("unique-crimes.txt","r")
i = 0
for crime in file.readlines():
	i += 1
	keywords = Counter(io.keywords(crime, version=2))
	top_words = keywords.most_common(2)
	keyword = " ".join(x[0] for x in top_words)
	print(crime)
	# print(keywords)
	print(keyword)
	print(io.sentiment_hq(keyword))
	print()
	if i == 30:
		break
