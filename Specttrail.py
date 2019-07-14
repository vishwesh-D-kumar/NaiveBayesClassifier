import pandas as pd
train=pd.read_csv("SPECT.train",delimiter=",")
test=pd.read_csv("SPECT.test",delimiter=",")

cols=train.columns

