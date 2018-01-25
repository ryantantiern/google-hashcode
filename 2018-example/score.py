from pprint import pprint
import traceback, sys
class FileLineWrapper(object):
    def __init__(self, f):
        self.f = f
        self.line = 0
    def close(self):
        return self.f.close()
    def readline(self):
        self.line += 1
        return self.f.readline()
    # to allow using in 'with' statements 
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()	

def check_answer(filename, RCLH, pizza):
	R,C,L,H = RCLH
	with FileLineWrapper(open(filename, 'r')) as f:
		line = f.readline().rstrip()
		nslices = int(line)
		score = 0
		for i in range(nslices):
			line = list(map(int, f.readline().rstrip().split()))
			r1, c1, r2, c2 = line[0], line[1], line[2], line[3]
			if r1 > r2:
				t = r1
				r1 = r2
				r2 = t
			if c1 > c2:
				t = c1
				c1 = c2
				c2 = t

			if r1 < 0: 
				print("Row is not a non-negative integer at line {}".format(f.line))
				return 
			if c1 < 0: 
				print("Column is not a non-negative integer at line {}".format(f.line))
				return
			if r2 > R: 
				print("Row is greater than maximum row, R at line {}".format(f.line))
				return
			if c2 > C: 
				print("Column is greater than maximum column, C at line {}".format(f.line))
				return

			# one slice
			sl = [pizza[i][c1:c2+1] for i in range(r1, r2+1)]
			ntmt, nmsh = 0, 0
			count = 0
			for i in range(len(sl)):
				for j in range(len(sl[0])):
					try:
						if sl[i][j] == 'T': ntmt += 1
						else: nmsh += 1
					except Exception as e:
						print("r1:\t {}".format(r1))
						print("r2:\t {}".format(r2))
						print("c1:\t {}".format(c1))
						print("c2:\t {}".format(c2))
						print(i, j)
						print(traceback.print_exc(file=sys.stdout))
						return None

			if ntmt < L:
				print("Number of Tomatos: {} is less than {} at line {}".format(ntmt, L, f.line))
				return 
			if nmsh < L: 
				print("Number of Mushrooms: {} is less than {} at line {}".format(nmsh, L, f.line))
				return 
			if ntmt + nmsh > H:
				print("Total number of toppings: {} is greater than {} at line {}".format(ntmt + nmsh, H, f.line))
				return 
			score += len(sl) * len(sl[0])
	return score

if __name__ == "__main__":
	input_file, answers = 'example.in', 'answers_example.txt'
	pizza, RCLH = [], ()
	with open(input_file) as f:
		line = f.readline().rstrip().split()
		RCLH = (int(line[0]),int(line[1]),int(line[2]),int(line[3]))
		for i in range(RCLH[0]):
			line = list(f.readline().rstrip())
			pizza.append(line)
	score = check_answer(answers, RCLH, pizza)
	print(score)
