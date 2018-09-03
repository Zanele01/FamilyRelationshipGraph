import random
import math

data = open('sample0.txt', 'r')
lines = data.readlines()
count = 0
infile = []
node1 = []
node2 = []
output = []
numbers=[]
people=[]
col1=[]
col2=[]
col3=[]
max_num=7519286
cnt=0
for line in lines:
	count = count+1
	    
	if count == 1:
		print("Data set being sampled...")

	else:
		u,v,w = line.strip('	').split()
		infile.append((u,v,w))
		col1.append(u)
		col2.append(v)
		col3.append(w)

random_pos=random.randint(1,20000)
for i in range(0,100):

	random_pos=math.ceil(random.uniform(1,max_num))
	while(float(infile[random_pos][2])<0.05 or (infile[random_pos][0]) in people):
		random_pos=math.ceil(random.uniform(1,max_num))
	people.append(infile[random_pos][0])

for j in range (0,len(col1)):
	if ((col1[j] in people) and (col2[j] in people)):
		numbers.append(j)
		cnt=cnt+1
	if (cnt>100):
		break


with open('dataset.txt','w') as f:
    for i in numbers:
        f.write(infile[i][0] + ' ' + infile[i][1] + ' ' + infile[i][2] + '\n')
        node1.append(infile[i][0])
        node2.append(infile[i][1])

for i in node1:
    if i not in output:
        output.append(i)

for n in node2:
    if n not in output:
        output.append(n)

with open('input2.txt','w') as f:
    for n in output:
        f.write(str(n) + ' ' + str(random.randint(0,100)) + '\n')

print("Data sampling complete!")
print("Loading the GUI...")
	
		



		
	






