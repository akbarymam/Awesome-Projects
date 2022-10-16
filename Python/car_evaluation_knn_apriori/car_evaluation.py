import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import arules as ar
from arules.utils import top_10_variant_variables
import json
from flask import Flask, render_template, request
from selenium_testing import Testing
from unit_testing import tester

app = Flask(__name__)

df = pd.read_csv('car_evaluation.csv')

def lowmedhigh(row, column):
	if row[column] == 'low':
		return 0
	if row[column] == 'med':
		return 1
	if row[column] == 'high':
		return 2
	if row[column] == 'vhigh':
		return 3
	
def boot(row):
	if row['lug_boot'] == 'small':
		return 0
	if row['lug_boot'] == 'med':
		return 1
	if row['lug_boot'] == 'big':
		return 2
	
def decision(row):
	if row['decision'] == 'unacc':
		return 0
	if row['decision'] == 'acc':
		return 1
	if row['decision'] == 'good':
		return 2
	if row['decision'] == 'vgood':
		return 3

df['buying'] = df.apply(lambda row: lowmedhigh(row, 'buying'), axis=1)
df['maint'] = df.apply(lambda row: lowmedhigh(row, 'maint'), axis=1)
df['doors'] = df['doors'].replace('5more', '5')
df['persons'] = df['persons'].replace('more', '5')
df['lug_boot'] = df.apply(lambda row: boot(row), axis=1)
df['safety'] = df.apply(lambda row: lowmedhigh(row, 'safety'), axis=1)

class KNN:
	def __init__(self, df):
		X = df.drop(columns='decision')
		Y = df['decision']
		X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
		self.knn = KNeighborsClassifier()
		self.knn.fit(X_train, Y_train)
		self.score = round(self.knn.score(X_test, Y_test)*100, 2)
	
	def predict(self, x_data):
		X = np.array(x_data).reshape(1, -1)
		return self.knn.predict(X)

def apriori(df):
	rules, supp_dict = ar.create_association_rules(df, max_cols=2)
	rules_sorted = rules.sort_values(by='confidence', ascending=False)
	# UNACC
	rules_unacc, titles_unacc = ar.present_rules_per_consequent(rules_sorted,consequent={'decision':'unacc'}, selection_function=top_10_variant_variables, drop_dups=True)
	unacc = { title:[] for title in titles_unacc }
	for index, i in enumerate(rules_unacc):
		for j in i['antecedent'].values[:len(i['antecedent'].values)//2]:
			unacc[titles_unacc[index]].append(j[titles_unacc[index]])
	# ACC
	rules_acc, titles_acc = ar.present_rules_per_consequent(rules_sorted,consequent={'decision':'acc'}, selection_function=top_10_variant_variables, drop_dups=True)
	acc = { title:[] for title in titles_acc }
	for index, i in enumerate(rules_acc):
		for j in i['antecedent'].values[:len(i['antecedent'].values)//2]:
			acc[titles_acc[index]].append(j[titles_acc[index]])
	# GOOD
	rules_good, titles_good = ar.present_rules_per_consequent(rules_sorted,consequent={'decision':'good'}, selection_function=top_10_variant_variables, drop_dups=True)
	good = { title:[] for title in titles_good }
	for index, i in enumerate(rules_good):
		for j in i['antecedent'].values:
			good[titles_good[index]].append(j[titles_good[index]])
	# VGOOD
	rules_vgood, titles_vgood = ar.present_rules_per_consequent(rules_sorted,consequent={'decision':'vgood'}, selection_function=top_10_variant_variables, drop_dups=True)
	vgood = { title:[] for title in titles_vgood }
	for index, i in enumerate(rules_vgood):
		for j in i['antecedent'].values:
			vgood[titles_vgood[index]].append(j[titles_vgood[index]])
	return unacc, acc, good, vgood

unacc,  acc, good, vgood = apriori(df)
prediction = KNN(df)

@app.route('/')
def home():
	return render_template('home.html', score=prediction.score)

@app.route('/predict', methods=['POST'])
def predict():
	return str(prediction.predict(json.loads(request.data))[0])

@app.route('/classification')
def classification():
	data = { 'unacc': unacc, 'acc': acc, 'good': good, 'vgood': vgood, }
	return render_template('apriori.html', data=data)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/testing', methods=['GET', 'POST'])
def testing():
	if request.method == 'POST':
		if json.loads(request.data)['type']:
			test = Testing()
			## Prediction Page
			# Valid Accuracy
			test.accuracy_test()
			# Unacc
			test.prediction_test('Very High', 'High', '2', '2', 'Small', 'Low', 'Unacceptable')
			# Acc
			test.prediction_test('High', 'Medium', '3', '5+', 'Medium', 'Medium', 'Acceptable')
			# Good
			test.prediction_test('Medium', 'Medium', '4', '4', 'Medium', 'Medium', 'Preferred')
			# Vgood
			test.prediction_test('Low', 'Medium', '4', '5+', 'Large', 'High', 'Optimal')
			## Classification Page
			test.classification_test()
			## Testing Page
			test.unit_test()
			return json.dumps(test.quit())
		else:
			return json.dumps('\n'.join(tester(__import__(__name__)).split('\n')[2:]))
	return render_template('testing.html')

if __name__ == "__main__":
	app.run(debug=True)
