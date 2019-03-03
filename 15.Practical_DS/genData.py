#!/usr/bin/env python

import random, math
import json, os

print("Generating data ..", end='', flush=True)
os.makedirs("data/return-data", exist_ok=True)


sentbackZip = [random.randint(math.pow(10, 3), 2*math.pow(10, 4)) for i in range(0, 1000)]
def zipCode(sentback):
#	if(sentback and random.randint(0, 10) < 5):
#		return sentbackZip[random.randint(0, 100-2)]
#	else:
	return random.randint(math.pow(10, 3), math.pow(10, 4))

def transactionId():
	return random.randint(math.pow(10,9), math.pow(10, 10))

def sentbackCategory():
	rand = random.randint(0, 10)
	if(rand > 5):
		return 4
	if(rand > 2):
		return 3
	return rand

def basket(sentback):
	size = max((int)(random.gauss(5, 3)),1)
	if(sentback):
		return [sentbackCategory() for i in range(0, size)]
	else:
		return [random.randint(0, 5) for i in range(0, size)]

def totalAmount(sentback, itemsInBasket):
	if(sentback):
		return itemsInBasket*max((int)(random.gauss(70, 30)),10)
	else:
		return itemsInBasket*max((int)(random.gauss(50, 30)),10)

def jsonLine():
	sentback = random.randint(0, 100) < 3
	basketItems = basket(sentback)
	return json.dumps({
		"transactionId": transactionId(),
		"basket": basketItems,
		"zipCode": zipCode(sentback),
		"totalAmount": totalAmount(sentback, len(basketItems)),
		"returnLabel": 1 if(sentback) else 0
		})

def createLog(day):
	textFile = open("data/return-data/"+day+".txt", 'w')
	for i in range(0, 1000):
		textFile.write(jsonLine() + "\n")
	textFile.close()

for i in range(1,32):
	print(".",end='', flush=True)
	createLog("2017-01-{0:02d}".format(i))
print("done!")