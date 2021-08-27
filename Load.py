def Load():
	import sys, time
	try:
		aa = 33
		bb = 0
		while (0 < aa):
			aa -= 1
			bb += 1
			sys.stdout.write("\r Loading [{}{}] ".format("#"*bb,"-"*aa))
			sys.stdout.flush()
			time.sleep(0.5)
	except KeyboardInterrupt:
		sys.exit()
Load()