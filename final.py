import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
dataset = pd.read_csv('C:/Users/胡少琰/desktop/2020年Covid-19数据集.csv',engine='python')
dataset = dataset.drop('test_indication', axis=1)
dataset=dataset[~dataset['corona_result'].isin(["negative"])]
dataset1 = pd.read_csv('C:/Users/胡少琰/desktop/2020年Covid-19数据集_new.csv',engine='python')
dataset1 = dataset
dataset1.to_csv('C:/Users/胡少琰/desktop/2020年Covid-19数据集_new.csv')
##绘制性别与感染人数的柱状图
male=0
female=0
for i in range(220975):
    if dataset.iloc[i]["gender"]=='male':
        male+=1
    else:
        female+=1
data = [male,female]
labels = ['male','female']
plt.xticks(range(len(data)),labels)
plt.xlabel('gender')
plt.ylabel('Amounts')
plt.bar(range(len(data)), data)
plt.show()
##绘制年龄与感染人数的柱状图
over60=0
under60=0
for i in range(220975):
    if dataset.iloc[i]["age_60_and_above"]=='Yes':
        over60+=1
    else:
        under60+=1
data = [over60,under60]
labels = ['over60','under60']
plt.xticks(range(len(data)),labels)
plt.xlabel('age')
plt.ylabel('Amounts')
plt.bar(range(len(data)), data)
plt.show()
##绘制60岁及以上人群中性别与感染人数的柱状图
male=0
female=0
for i in range(220975):
    if dataset.iloc[i]['age_60_and_above']=='Yes':
        if dataset.iloc[i]["gender"] == 'male':
            male += 1
        else:
            female += 1
data = [male,female]
labels = ['male','female']
plt.xticks(range(len(data)),labels)
plt.xlabel('gender')
plt.ylabel('Amounts')
plt.bar(range(len(data)), data)
plt.show()
##绘制不到60岁的人群中性别与感染人数的柱状图
male=0
female=0
for i in range(220975):
    if dataset.iloc[i]['age_60_and_above']=='No':
        if dataset.iloc[i]["gender"] == 'male':
            male += 1
        else:
            female += 1
data = [male,female]
labels = ['male','female']
plt.xticks(range(len(data)),labels)
plt.xlabel('gender')
plt.ylabel('Amounts')
plt.bar(range(len(data)), data)
plt.show()
##绘制感染人群中不同症状出现频数的柱状图
cough=0
fever=0
sore_throat=0
shortness_of_breath=0
head_ache=0
for i in range(220975):
    if dataset.iloc[i]["cough"]==1:
        cough+=1
    if dataset.iloc[i]["fever"] == 1:
        fever+=1
    if dataset.iloc[i]["sore_throat"] == 1:
        sore_throat += 1
    if dataset.iloc[i]["shortness_of_breath"] == 1:
        shortness_of_breath+=1
    if dataset.iloc[i]["head_ache"] == 1:
        head_ache+=1
data = [cough,fever,sore_throat,shortness_of_breath,head_ache]
labels = ['cough','fever','sore_throat','shortness_of_breath','head_ache']
plt.xticks(range(len(data)),labels)
plt.xlabel('symptom')
plt.ylabel('Amounts')
plt.bar(range(len(data)), data)
plt.show()
