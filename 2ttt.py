import pandas as pd
ttt=pd.read_csv("tictactoe.data",delimiter=",")
print (ttt.columns)
cols=ttt.columns
condprobs=[]
for i in len(cols):
	condprobs.append([])
	condprobs[i].append([[0][0]][[0][0]][[0][0]])
	for j in len(ttt):
		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1
		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1

		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1
		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1
		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1
		if ttt[cols[j]]=="x" and ttt[cols[-1]][j]=="positive":
			condprobs[i][0][0]+=1





	

