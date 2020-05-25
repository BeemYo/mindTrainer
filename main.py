import time, random, os

reg = []
counter = 0
run = True

while run:
	counter += 1
	for i in range(counter):
		rnd = random.randint(0, 4)
		reg.append(rnd)

		print(rnd)
		time.sleep(0.5)

	time.sleep(2)
	os.system("clear")

	for i in range(counter):
		inp = int(input(str(i + 1) + ":"))
		if inp == reg[0]:
			reg.remove(reg[0])
		else:
			print("Wrong")
			run = False
			break

	reg = []
