import sys, time
def Loads():
	a = 33
	b = 0
	while (0 < a):
		a -= 1
		b += 1
		sys.stdout.write("\r Loading [{}{}] ".format("•"*b," "*a))
		sys.stdout.flush()
		time.sleep(0.5)

Loads()