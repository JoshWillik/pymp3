class Puller(object):
	def __init__(self):
		self.format = raw_input("Input parse pattern in format \%\item\%\item\%\item\n> ")
		print self.format #for debugging purposes


if __name__ == "__main__":
	Puller()