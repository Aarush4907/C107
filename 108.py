import pandas as pd
import plotly.graph_objects as go 
df = pd.read_csv(r"D:\PROGRAMS\PYTHON\C102\108Data.csv")
student_df = df.loc[df["student_id"]=="TRL_123"]
print (student_df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = student_df.groupby("level")["attempt"].mean(),y=['level1','level2','level3','level4'],orientation = 'h' ))
fig.show()
