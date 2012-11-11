class Location:
	def __init__(self):
		self.current = 4
		self.compass = dict({"north": -2,
							"south": +2,
							"east": -1,
							"west": +1})
		self.descr = dict({1: "You are in a forrest",
						2: "You are now in a desert",
						3: "You have suddenly stumbled into what appears to be a haunted house, in front of you is a large door",
						4: "You wake up, what was that you thought as you feel the wind rushing around you.",
						5: "Suddenly you hear a song, WHAT ON EARTH ARE THOSE?! They look like g...giant muffins?!",
						6: "",
						7: "DESCRIPTION"})
		self.rooms = dict({"items": {
							1:[True],
							2:[True],
							3:[True],
							4:[True],
							5:[True],
							6:[True],
							7:[True]}})
	#Keeps track of the players location
	def move(self, direction):
		#Input Validation
		if direction.lower() in ["north","south","east","west","exit"]:
			if direction.lower() == "exit":
				return 0
			#set temp to where we would be if we followed the directions
			temp = self.current + self.compass[direction.lower()]
			#if we'd still within the amount of rooms we have, carry on + move
			if not (temp < 1 or temp > 7):
				self.current = temp
				return self.current
		#If the input is invalid, or the room is out of bounds, return -1
		return -1
	
	def ask_move(self):
		#Question to ask when deciding about moving
		question = self.move(raw_input("Which direction would you like to move in: "))
		#While the result is invalid
		while question == -1:
			#Tell the user
			print "That direction is not valid, please try again!"
			#Get their answer again
			question = self.move(raw_input("Which direction would you like to move in: "))
		#If the result is to exit
		if question == 0:
			#allow the main loop to know to stop
			return False
		#otherwise describe the room
		self.room(self.current)
		#and carry on the game loop
		return True
		
	def room(self, room):
		print self.descr[room]
	
	def has_item(self, room):
		if True in self.rooms["items"][room]:
			if self.rooms["items"][room][0] == True:
				#there is a key in the room
				return True,"key"
						
class Action:
	def fight(self, foe):
		print foe
	def investigate(self, location, room, inventory):
		has_item, item = location.has_item(room)
		if has_item:
			print "You have found a", item
			inventory.add_item(item)
class Inventory:
	#Keep track of the players inventory
	def __init__(self):
		current_item = None
	def add_item(self, item):
		#Do stuff
		print "Item '%s' added" % item
		self.current_item = item
		