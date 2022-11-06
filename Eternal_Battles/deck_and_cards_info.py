
"""
This is the full dict with the info of the cards!
All the cards are here, and all the necessary info for the images 2

CARDS_STATS_DICT has the info for the game to run, cards stats in general.
The CARDS_STATS_DICT has:
	'cost' : integer,
	'health' : integer,
	'damage' : integer,
	'card_id' : integer,
	'card_name' : string,

CARDS_IMAGES_DICT has the address and things for the images in Animation to draw
The Animations get a image file in the form of a image, and calculates the images
with the values of the size. For that, the image, if it is animated, must be:

* each line is a animation state (like idle, running , falling , jumping, so on)
* the lines don't need to have the same numbers of images. (first line, idle with 14 images, second line with running with 8 images).
* each line has a name state, while in that state, it will keep repeating the animation
* the active animations are the animations that will happen only once and will call a given action at the end of the animation.

The CARDS_IMAGES_DICT has:
	"adress": string object, or os.path object
	"size": [64 , 64], The size of each sprites. if it is a Image with no movement, this don't need to be given.
	"states" : ['idle'], a list with the names of the animation in each line. Must be the sime size of the lines of the images.
	"active animations": {'death': 'kill()'} # a dict with the name of the active animation and the action it takes after it finished. the key and value must be a string, with the parameters if any.

"""


CARDS_STATS_DICT = {

	1 : {
		'cost' : 2 ,
		'health' : 8 ,
		'damage' : 2 ,
		'card_name' : 'Test',
	} ,
	2 : {
		'cost' : 4 ,
		'health' : 100 ,
		'damage' : 3 ,
		'card_name' : 'Test2',
	},
    3: {
		'cost' : 4 ,
		'health' : 100 ,
		'damage' : 3 ,
		'card_name' : 'Test2',
	},
    4: {
		'cost' : 4 ,
		'health' : 100 ,
		'damage' : 3 ,
		'card_name' : 'Test2',
	}
}


CARDS_IMAGES_DICT = {
	'path': None, # Change the path of the images here!
	1: {
		"adress": None,
		"size": [64 , 64],
		"states" : ['idle'],
		"active animations": {}
	}
}
