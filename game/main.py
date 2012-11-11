import sys
import player
location = player.Location()
inventory = player.Inventory()
game = True
try:
	while game:
		game = location.ask_move()
		player.Action().investigate(location, location.current, inventory)

except KeyboardInterrupt:
	print "\nError: Interrupted by user."
#except:
#	print "\nError: Unknown Error."