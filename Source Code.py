import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users/PROF.B.SHANAWAZ BAIG/Downloads/membership_groceries_userprofile.csv")
df=pd.DataFrame(data)
print(df)

#null value cheanck
print(df.isnull().sum())

##grup the gender customer
print(df.groupby("gender")["membership_tier"].value_counts())

##pie chat
x=df.groupby("gender")["membership_tier"].value_counts()
plt.pie(x,labels=x.index,autopct="%1.1f%%",startangle=90)
plt.title("MEMBERSHIP USER")
plt.show()

##bar chart
a=df.groupby("gender")["reward_points_used"].count()
i=["MALE","FEMALE"]
plt.bar(a.index,a.values,label=i,color=["blue","red"],width=0.4)
plt.title("REWARD POINTS USED")
plt.xlabel("CATAGERY")
plt.ylabel("COUNT VALUES")
plt.legend(loc="upper right")
plt.show()


h=df["gender"].value_counts()
plt.pie(h.index,h.values())
plt.show()

