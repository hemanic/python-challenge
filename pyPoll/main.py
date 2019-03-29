import pandas as pd
file_one= "Resources/election_data.csv"
file_one_df=pd.read_csv(file_one)
file_one_df.head()
vote_count = len(file_one_df["Candidate"])
vote_count
candidates = (file_one_df["Candidate"].unique())
candidates
file_one_df["Candidate"].value_counts()
df_2=file_one_df["Candidate"].value_counts()
df_2
#total number of votes each candidate won
#percent votes per candidate
##manually put because I tried using the loc function but was unsuccesful in picking out each value
KhanPercentage= (2218231/vote_count)*100
CorreyPercentage=(704200/vote_count)*100
LiPercentage=(492940/vote_count)*100
OTooleyPercentage= (105630/vote_count)*100
print(KhanPercentage)
print(CorreyPercentage)
print(LiPercentage)
print(OTooleyPercentage)
#winner counts
winner_count = file_one_df['Candidate'].value_counts()
int(KhanPercentage)
print('Winner is Khan with ' + (str(int(KhanPercentage)))+' percent of votes')