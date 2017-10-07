print "hello my name is Alexis"

four = 2 + 2
print "the result of 2 + 2 is ..."
print four

def average(a, b):
    result = (a + b) / 2
    return result

a = 7
b = 5
avg = average(a, b)
print "the average is..."
print avg

from sklearn import tree

my_classifier = tree.DecisionTreeClassifier()

# my data:
features = [[300, 2], [450, 2], [200, 8], [150, 9]]
labels = [0, 0, 1, 1]
my_classifier.fit(features, labels)
print "training on the data done!"

new_vehicle = [350, 2]
print "the predicted vehicle is..."
print my_classifier.predict([new_vehicle])

new_vehicle_2 = [190, 6]
print "the predicted vehicle is..."
print my_classifier.predict([new_vehicle_2])

from sklearn import datasets
my_dataset = datasets.load_boston()

print my_dataset.DESCR