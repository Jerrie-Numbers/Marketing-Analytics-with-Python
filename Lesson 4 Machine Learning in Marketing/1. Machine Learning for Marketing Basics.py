# Machine Learning for Market Basics
# Supervised vs. unsupervised learning

# Print header of telco dataset
print(telco.head())

# Investigate the data (import pandas)
# Print the data types of telco_raw dataset
print(telco_raw.dtypes)

# Print the header of telco_raw dataset
print(telco_raw.head())

# Print the number of unique values in each telco_raw column
print(telco_raw.nunique())
# Separate numerical and categorical columns
# Store customerID and Churn column names
custid = ['customerID']
target = ['Churn']

# Store categorical column names
categorical = telco_raw.nunique()[telco_raw.nunique() < 5].keys().tolist()

# Remove target from the list of categorical variables
categorical.remove(target[0])

# Store numerical column names
numerical = [x for x in telco_raw.columns if x not in custid + target + categorical]

# Encode categorical and scale numerical variables
# Perform one-hot encoding to categorical variables 
telco_raw = pd.get_dummies(data = telco_raw, columns = categorical, drop_first=True)

# Initialize StandardScaler instance
scaler = StandardScaler()

# Fit and transform the scaler on numerical columns
scaled_numerical = scaler.fit_transform(telco_raw[numerical])

# Build a DataFrame from scaled_numerical
scaled_numerical = pd.DataFrame(scaled_numerical, columns=numerical)

# Split data to training and testing
# Split X and Y into training and testing datasets
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.25)

# Ensure training dataset has only 75% of original X data
print(train_X.shape[0] / X.shape[0])

# Ensure testing dataset has only 25% of original X data
print(test_X.shape[0] / X.shape[0])

# Fit a decision tree
# Initialize the model with max_depth set at 5
mytree = tree.DecisionTreeClassifier(max_depth = 5)

# Fit the model on the training data
treemodel = mytree.fit(train_X, train_Y)

# Predict values on the testing data
pred_Y = treemodel.predict(test_X)

# Measure model performance on testing data
accuracy_score(test_Y, pred_Y)

# Predict churn with decision tree
# Initialize the Decision Tree
clf = tree.DecisionTreeClassifier(max_depth = 7, 
               criterion = 'gini', 
               splitter  = 'best')

# Fit the model to the training data
clf = clf.fit(train_X, train_Y)

# Predict the values on test dataset
pred_Y = clf.predict(test_X)

# Print accuracy values
print("Training accuracy: ", np.round(clf.score(train_X, train_Y), 3)) 
print("Test accuracy: ", np.round(accuracy_score(test_Y, pred_Y), 3))

print(telco_raw.nunique())