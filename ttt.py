import pandas as pd
ttt=pd.read_csv("tictactoe.data",delimiter=",")
print (ttt.columns)
cols=ttt.columns
c=0
for i in ttt.outcome.tolist():
	if i=="positive":
		c+=1
print(c,len(ttt.outcome.tolist()))
s=0
for i in ttt.outcome.tolist():
	if i=="positive":
		s+=1
positiveprob=s/(len(ttt))
negativeprob=1-positiveprob

predicted=[]
for i in range(len(ttt.outcome.tolist())):
	test=i
	train=list(range(len(ttt)))
	train.pop(i)
	testingparameters=[ttt[k].tolist()[i] for k in ttt.columns]
	testingparameters.pop(-1)
	conditionalwin=[]
	conditionallose=[]
	for j in range(len(testingparameters)):
		win=0
		lose=0
		for k in train:
			z=cols[j]
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="positive":
				win+=1
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]=="negative" :
				# print("dshjkfsdhjk")
				lose+=1

		win=win/(len(ttt)-1)
		lose=lose/(len(ttt)-1)
		if lose==0:
			print("bkaka",j)

		# print(win,lose,positiveprob,negativeprob)
		# break;
	
		conditionalwin.append(win/positiveprob)
		conditionallose.append(lose/negativeprob)

	print(conditionalwin,conditionallose)

	w=positiveprob
	l=negativeprob

	for b in range(len(conditionalwin)):
		w*=conditionalwin[b]
		l*=conditionallose[b]
	print(w,l)

	if w>l:
		predicted.append("positive")
	else:
		predicted.append("negative")
	print(predicted[i],ttt.outcome[i],i)

s=0
for i in range(len(predicted)):
	if predicted[i]==ttt.outcome[i]:
		s+=1

print(s/len(ttt))






			






	

