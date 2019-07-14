import pandas as pd
from random import randint as randi
ttt=pd.read_csv("shuttle-landing-control.data",delimiter=",")
ttt.mask(ttt=="*",1)
print (ttt)

cols=ttt.columns
c=0
for i in ttt.outcome.tolist():
	if i==1:
		c+=1
print(c,len(ttt.outcome.tolist()))
s=0
for i in ttt.outcome.tolist():
	if i==1:
		s+=1
positiveprob=s/(len(ttt))
negativeprob=1-positiveprob

predicted=[]
for i in range(len(ttt.outcome.tolist())):
	test=i
	train=list(range(len(ttt)))
	train.pop(i)
	testingparameters=[ttt[k].tolist()[i] for k in ttt.columns]
	testingparameters.pop(0)
	conditionalwin=[]
	conditionallose=[]
	for j in range(len(testingparameters)):
		win=0
		lose=0
		for k in train:
			z=cols[j]
			if ttt[z][k]=="*":
				ttt[z][k]=2
			if (testingparameters[j]==ttt[z][k]) and ttt.outcome[k]==1:
				win+=1
			if (testingparameters[j]==ttt[z][k]) and ttt.outcome[k]==2 :
				# print("dshjkfsdhjk",j,i)
				lose+=1

		if win==0:
			win=1
		if lose==0:
			lose=1
		win=win/(len(ttt)-1)
		lose=lose/(len(ttt)-1)
		if lose==0:
			print("bkaka",j)

		# print(win,lose,positiveprob,negativeprob)
		# break;
	
		conditionalwin.append(win/positiveprob)
		conditionallose.append(lose/negativeprob)

	# print(conditionalwin,conditionallose)

	w=positiveprob
	l=negativeprob

	for b in range(len(conditionalwin)):
		w*=conditionalwin[b]
		l*=conditionallose[b]
	print(w,l,i)

	if w>l:
		predicted.append(1)
	else:
		predicted.append(2)
	print(predicted[i],ttt.outcome[i],i)

print(ttt)
s=0
for i in range(len(predicted)):
	if predicted[i]==ttt.outcome[i]:
		s+=1

print(s/len(ttt)*100,"%")






			






	

