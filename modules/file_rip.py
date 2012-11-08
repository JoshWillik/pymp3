class Ripper(object):
	def __init__(self, m_file):
		import mutagen.easyid3 as foobar
		import mutagen.id3 as error_mut #to catch ID3BadUnsynchData error. Unknown reason for error
		import re #used in strip_dashes
		self.re = re
		self.mp3 = foobar.EasyID3 #short name for required module
		self.m_file = m_file #make module wide accessable

		try:
			self.editable = self.mp3(m_file)
			self.main()
		except error_mut.ID3BadUnsynchData:
			print m_file, "could not be opened, mutagen library had unknown internal error" 
		except:
			print self.m_file, "is not an mp3, or an unknown error has occured"
		finally:
			self.song_data = {'-':'-','artist':'Unknown Artist','title':"Unknown Track","discnumber":"0","tracknumber":'00','album':"Unknown Album"}
	
	def main(self):
		try:
			f_artist   = self.strip_dashes("artist")
		except KeyError:
			f_artist   = "Unknown Artist"
		try:
			f_title    = self.strip_dashes("title")
		except KeyError:
			f_title    = "Unknown Track"
		try: 
			f_cd_num   = self.strip_dashes("discnumber")
		except KeyError:
			f_cd_num   = "0"
		try:
			f_song_num = self.strip_dashes("tracknumber")
		except KeyError:
			f_song_num = "00"
		try:
			f_album    = self.strip_dashes("album")
		except:
			f_album    = "Unknown Album"

		if f_cd_num:
			f_cd_num=f_cd_num[0]
		if f_song_num:
			f_song_num=f_song_num[0]
		if len(f_song_num)+len(f_cd_num) < 3:
			f_song_num = '0'+f_song_num

		song_data = {'title':f_title,'artist':f_artist,'discnumber':f_cd_num,'tracknumber':f_song_num, 'album':f_album, '-':'-'}
		self.song_data = song_data

	def strip_dashes(self, item): #dashes interfere with parsing the title data into metadata later
		to_strip = self.editable[item][0].encode('utf-8')
		item_list = self.re.split("-", to_strip)
		paste_back = "".join(item_list)
		return paste_back


if __name__ == "__main__":
	#for debugging, not intended for solitary use
	from sys import argv
	base_args = argv
	try: 
		modified = base_args[1]
	except:
		raise Exception('\033[1;38mNo target file specified\033[1;m') #formatt error to grab attention
	script = base_args[0]
	try:
		dat = Ripper(modified)
	except:
		raise Exception("File does not exist, is not an mp3, or is corrupted.")
	else:
		#print dat #for debugging
		#print dat.song_data #for debugging
		pass