import csv
with open (r"D:\PROGRAMS\PYTHON\C102\SOCR-HeightWeight.csv",newline = '')as f:
        reader = csv.reader(f)
        file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n=file_data[i][1]
    new_data.append(float(n))
n = len(new_data)
total=0
for x in new_data:
    total=total+x
median = n/2
print ("median",median)
mean = total/n
print("mean",mean)
mod = 3*median-2*mean
print("mod",mod)