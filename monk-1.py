import pandas as pd
ttt=pd.read_csv("monks-1.train",delimiter=" ")
print (ttt.columns)
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
testing=pd.read_csv("monks-1.test",delimiter=" ")
print(len(testing))
print(len(ttt))
# ttt=pd.concat([ttt,testing])
# print(ttt)
for i in range(len(testing)):
	# test=i
	print(i,"slksdjskldjasldsalkjdjslkdjkl",len(testing))

	train=list(range(len(ttt)))
	testingparameters=[testing[k].tolist()[i] for k in testing.columns]

	# testingparameters.pop(0)
	conditionalwin=[]
	conditionallose=[]
	testingparameters.pop(-1)
	for j in range(1,len(testingparameters)):
		win=0
		lose=0
		for k in train:
			z=cols[j]
			# print(testingparameters[j],ttt[z][k])
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]==1:
				win+=1
			if testingparameters[j]==ttt[z][k] and ttt.outcome[k]==0 :
				# print("dshjkfsdhjk")
				lose+=1

		win=win/(len(train))
		lose=lose/(len(train))
		if lose==0:
			print("bkaka",j)
			lose=1
		if win==0:
			win=1


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
	print(w,l)

	if w>l:
		predicted.append(1)
	else:
		predicted.append(0)
	print(len(predicted),i)
	print(predicted[i],testing.outcome[i],i)

s=0
for i in range(len(predicted)):
	if predicted[i]==testing.outcome[i]:
		s+=1

print(s/len(predicted)*100,"%")




