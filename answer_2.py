import string
import pandas as pd
import csv


################################################
            # Answer - 2 : Part 1
################################################

pd.options.display.max_rows = 9999

#Read CSV FIle   
data = pd.read_csv('input.csv', header=None, names=['hostname', 'value'])
new = data['hostname'].str.split(".", n = 3, expand = True)

#Creating Dataframes for hostname format
data["host_number"]= new[0]
data["region"]=new[1]
data["environment"]=new[2]
data["domain"]=new[3]

data.drop(columns =["hostname", "value"], inplace = True)

count = 0
region = data["region"][0]
env = data["environment"][0]

print("Answer-2 Part 1: \n\n")

for ind in data.index:
    if(data['region'][ind]== region and data['environment'][ind]==env):
        count += 1
    else:
        print(region, ", ", env, ", ", count)
        region = data["region"][ind]
        env = data["environment"][ind]
        count = 1

print(region, ", ", env, ", ", count)


################################################
            # Answer - 2 : Part 2
################################################

data["host_int"] = 0
for ind in data.index:
    df = data["host_number"].str.slice(4,6)
    data["host_int"]=df

# print(data)

print("\n\n Answer-2 Part 2: \n\n")

bucket = [0]*41
print("Type the region Name\n\n")
usr_region = input()
print("Type the Environment Name\n\n")
usr_env = input()

prefix="host"
cluter_id="1001"
domain="internal.example.com"

for ind in data.index:
    if(data["region"][ind]==usr_region and data["environment"][ind]==usr_env):
        i = data["host_int"][ind]
        i = int(i)
        bucket[i-10]=1

# print(bucket)

counter = 0
for i in bucket:
    if(i==0):
        index = counter+10
        print(prefix, index, "-", cluter_id, ".", usr_region, ".", usr_env, ".", domain)
    counter += 1