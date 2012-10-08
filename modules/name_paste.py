class Paster(object):
	def __init__(self, song_data, parse_array):
		self.song_data = song_data
		self.parsed_config = parse_array
		print song_data
		print parse_array


if __name__ == "__main__":
	#NOTE: "__main__" for debugging purposes only, not meant to be used individually
	import os
	
	#get parsed configuration data to pass to name paster
	import parse_config
	parsed_config = parse_config.Parser()
	parse_format = parsed_config.parsed

	#get filename to pass to file renamer
	from sys import argv
	#target = argv[1]
	script = argv[0]

	#get song data to pass to file renamer
	import file_rip
	ripped = file_rip.Ripper('modules/test/foo.mp3').song_data
	start_paste = Paster(ripped, parse_format)