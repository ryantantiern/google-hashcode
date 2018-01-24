"""
V E R C X 
contains V numbers representing size of individal videos
Ld K
Next K lines: c Lc 
Rv	Re Rn
"""
from pprint import pprint as pprint

def get_data():
	"""
	Do fancy calculations but just dump into std output for now. 
	"""
	filename = 'me_at_the_zoo.in'
	with open(filename, 'r') as f:
		# First Line
		line = f.readline().rstrip()
		first_line = line.split()
		nvideos = first_line[0]
		nendpoints = first_line[1]
		nrequests = first_line[2]
		nservers = first_line[3]
		server_cap = first_line[4]
		# Second Line
		line = f.readline()
		videos = line.rstrip().split()
		data_center, ep_cs, requests = {}, {}, []

		for i in range(int(nendpoints)):
			# Set data center latency for endpoint i
			line = f.readline().rstrip().split()
			data_center[i] = line[0]
			k = int(line[1])
			for j in range(k):
				# There are k cache servers connected to enpoint i
				next_line = f.readline().rstrip().split()
				ep_cs[(i, next_line[0])] = next_line[1]

		for i in range(int(nrequests)):
			line = f.readline().rstrip().split()
			requests.append((line[0], line[1], line[2]))

	return {
		"nvids" : nvideos,
		"nep" : nendpoints,
		"nreqs" : nrequests,
		"ncs" : nservers,
		"scap" : server_cap,
		"dcent" : data_center,
		"ep_cs" : ep_cs,
		"reqs" : requests 
	}


if __name__ == "__main__":
	data = get_data()

	print('Number of Videos\t', data['nvids'])
	print('Number of Endpoints\t', data['nep'])
	print('Number of Requests\t',data['nreqs'])
	print('Number of Cache Servers\t',data['ncs'])
	print('Server Capacity\t\t',data['scap'])
	print('Data Center\t',data['dcent'])
	print('Endpoints, Cache Servers\t',data['ep_cs'])
	print('Requests Data\t',data['reqs'])





