![logo](https://raw.github.com/ibek/music-library/master/mlib-web/src/main/webapp/resources/logo.png)
=============

#Help

	$ ./client.py -h
	usage: client.py [-h] [-m {GET,POST,DELETE}] -e {artist,genre} [-i ID]
		         [-o OBJECT] [-u USERNAME] [-p PASSWORD]

	optional arguments:
	  -h, --help            show this help message and exit
	  -m {GET,POST,DELETE}, --method {GET,POST,DELETE}
		                Type of HTTP request
	  -e {artist,genre}, --entity {artist,genre}
		                Database entity
	  -i ID, --identifier ID
		                Identifier of the entity (song artist's name, name of
		                genre)
	  -o OBJECT, --object OBJECT
		                JSON object with object data
	  -u USERNAME, --username USERNAME
		                Username (default: admin)
	  -p PASSWORD, --password PASSWORD
		                Password

#Examples
	1. Show all artists
		./client.py -e artist
	2. Show artist "Roger Waters"
		./client.py -e artist -i "Roger Waters"
	3. Create artist "Roger Lavas"
		./client.py -e artist -m POST -o '{"name":"Roger Lavas"}' -p admin
	4. Update artist "Roger Lavas" to "Roger Beers"
		./client.py -e artist -m POST -i "Roger Lavas" -o '{"name":"Roger Beers"}' -p admin
	5. Delete artist "Roger Beers"
		./client.py -e artist -m DELETE -i "Roger Beers" -p admin

