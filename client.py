#!/usr/bin/env python

import sys
import argparse
import urllib
import urllib2
import json

REST_URL = "http://localhost:8080/pa165/rest/"

if __name__ == "__main__":
	# Let's find out what the user wants.
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--method', choices=['GET','POST','DELETE'], default='GET', dest='method',
				help="Type of HTTP request")
	parser.add_argument('-e', '--entity', choices=['artist', 'genre'], required=True, dest='entity',
				help="Database entity")
	parser.add_argument('-i', '--identifier', dest='id',
				help="Identifier of the entity (song artist's name, name of genre)")
	parser.add_argument('-o', '--object', dest='object',
				help = "JSON object with object data")
	args = parser.parse_args()

	# Set up REST URL
	url = REST_URL + args.entity + "/"
	if args.id != None:
		# Encode ID and add it to the URL
		args.id = urllib.quote_plus(args.id)
		args.id = args.id.replace("+", "%20")
		url += args.id


	# GET method
	if args.method == 'GET':
		try:
			# Send HTTP GET to the prepared URL
			response = urllib2.urlopen(url)
		except urllib2.URLError as e:
			print "URL Not Found!"
			print "Used URL: " + url
			sys.exit(1)
		if response.code == 404:
			print "Resource not found!"
			sys.exit(1)
		else:
			# Print HTTP header and incoming data
			print response.info()
			data = response.read()
			print data

	# POST method - for create and update
	if args.method == 'POST':
		# Prepare the data
		if args.object is None:
			print "JSON object needs to be provided."
			sys.exit(2)

		try:
			# Prepare JSON data
			jdata = json.dumps(json.loads(args.object))

			# Send HTTP POST to the prepared URL
			request = urllib2.Request(url, jdata, {'Content-Type': 'application/json'})
			response = urllib2.urlopen(request)
		except urllib2.HTTPError as e:
			if e.code == 404:
				print "Resource not found!"
			else:
				print e
			sys.exit(1)
		except urllib2.URLError as e:
			print "URL Not Found!"
			print "Used URL: " + url
			sys.exit(1)
		except ValueError as e:
			print "JSON object is not properly formatted."
			sys.exit(2)
		else:
			# Print HTTP header and announce success
			print response.info()
			if args.id != None:
				print "Update successful."
			else:
				print "Creation successful."

	# DELETE method
	if args.method == 'DELETE':
		if args.id is None:
			print "Identifier needs to be provided."
			sys.exit(2)
		
		# Send HTTP DELETE to the prepared URL
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url)
		request.add_header('Content-Type', 'application/json')
		request.get_method = lambda: 'DELETE'

		try:
			response = opener.open(request)
		except urllib2.HTTPError as e:
			if e.code == 404:
				print "Resource not found!"
			else:
				print e
			sys.exit(1)
		except urllib2.URLError as e:
			print "URL Not Found!"
			print "Used URL: " + url
			sys.exit(1)
		else:
			# Print HTTP header and announce success
			print response.info()
			if args.id != None:
				print "Entity removed successfully."

