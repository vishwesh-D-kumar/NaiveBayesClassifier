import pandas as pd
ttt=pd.read_csv("soybean-small.data",delimiter=",")
print (ttt.columns)
cols=ttt.columns
c=0
d=0
e=0
f=0

for i in ttt.outcome.tolist():
	if i=="D1":
		c+=1
	if i=="D2":
		d+=1
	if i=="D3":
		e+=1
	if i=="D4":
		f+=1
# print(c,len(ttt.outcome.tolist()))

D1prob=c/(len(ttt))
D2prob=d/(len(ttt))
D3prob=e/(len(ttt))
D4prob=f/(len(ttt))


predicted=[]
for i in range(len(ttt)):
	test=i
	train=list(range(len(ttt)))
	train.pop(i)
	testingparameters=[ttt[k].tolist()[i] for k in ttt.columns]
	testingparameters.pop(-1)
	conditionalD1=[]
	conditionalD2=[]
	conditionalD3=[]
	conditionalD4=[]

	
	for j in range(len(testingparameters)):
		D1=0
		D2=0
		D3=0
		D4=0
		for k in train:
			z=cols[j]
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="D1":
				D1+=1
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="D2":
				D2+=1
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="D3":
				D3+=1
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="D4":
				D4+=1


		# if lose==0:
		# 	print("bkaka",j)

		# print(win,lose,positiveprob,negativeprob)
		# break;
	
		conditionalD1.append(D1/D1prob)

		conditionalD2.append(D2/D2prob)
		conditionalD3.append(D3/D3prob)
		conditionalD4.append(D4/D4prob)

	# print(conditionalwin,conditionallose)

	l,m,n,o=D1prob,D2prob,D3prob,D4prob


	for b in range(len(conditionalD1)):
		l*=conditionalD1[b]
		m*=conditionalD2[b]
		n*=conditionalD3[b]
		o*=conditionalD4[b]
	p=max(l,m,n,o)
	if p==l:
		predicted.append("D1")
	elif p==m:
		predicted.append("D2")
	elif p==n:
		predicted.append("D3")
	else:
		predicted.append("D4")

	print(predicted[i],ttt.outcome[i],i)

print(len(predicted),len(ttt))
s=0
for i in range(len(predicted)):
	if predicted[i]==ttt.outcome[i]:
		s+=1

print(s/len(ttt)*100,"%")






			






	

