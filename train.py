import pandas
import tensorflow
from sklearn.model_selection import train_test_split

# Modify input file removing unused data
df = pandas.read_csv('data_modified.csv', index_col=False)
df = df.drop(columns= ['Winner', 'Result'])

# Split data into training and prediction sets
training_set = df[['Season', 'Home Team', 'Away Team']]
prediction_set = df['Diff']

# Split the train and prediction sets into test and train sets
x_train, x_test, y_train, y_test = train_test_split(training_set, prediction_set, test_size=0.2)
y_train = pandas.DataFrame(y_train)
training_set = pandas.DataFrame(x_train).merge(y_train, left_index = True, right_index = True)
y_test = pandas.DataFrame(y_test)
testing_set = pandas.DataFrame(x_test).merge(y_test, left_index = True, right_index = True)


engineered_features = []
for continuous_feature in list(training_set.columns):
    engineered_features.append(tensorflow.contrib.layers.real_valued_column(continuous_feature))


# Builds the Model Framework
regressor = tensorflow.contrib.learn.DNNRegressor(feature_columns = engineered_features, activation_fn = tensorflow.nn.relu, hidden_units=[250, 100, 50])


regressor.fit(input_fn = (training_set) , steps=10000)

#print(regressor)