# Aggregation and Pruning
# Performing aggregation
# Select the column headers for sign items
sign_headers = [i for i in onehot.columns if i.lower().find('sign')>=0]

# Select columns of sign items
sign_columns = onehot[sign_headers]

# Perform aggregation of sign items into sign category
signs = sign_columns.sum(axis = 1) >= 1.0

# Print support for signs
print('Share of Signs: %.2f' % signs.mean())

# Defining an aggregation function
def aggregate(item):
	# Select the column headers for sign items
	item_headers = [i for i in onehot.columns if i.lower().find(item)>=0]

	# Select columns of sign items
	item_columns = onehot[item_headers]

	# Return category of aggregated items
	return item_columns.sum(axis = 1) >= 1.0

# Aggregate items for the bags, boxes, and candles categories  
bags = aggregate('bag')
boxes = aggregate('box')
candles = aggregate('candle')

# identifying frequent itemsets with Apriori
# Import apriori from mlxtend
from mlxtend.frequent_patterns import apriori

# Compute frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(onehot, 
                            min_support = 0.006, 
                            max_len = 3, 
                            use_colnames = True)

# Print a preview of the frequent itemsets
print(frequent_itemsets.head())

# Selecting a support threshold
# Import apriori from mlxtend
from mlxtend.frequent_patterns import apriori

# Compute frequent itemsets using a support of 0.003 and length of 3
frequent_itemsets_1 = apriori(onehot, min_support = 0.003, 
                            max_len = 3, use_colnames = True)

# Compute frequent itemsets using a support of 0.001 and length of 3
frequent_itemsets_2 = apriori(onehot, min_support = 0.001, 
                          max_len =  3, use_colnames = True)

# Print the number of freqeuent itemsets
print(len(frequent_itemsets_1), len(frequent_itemsets_2))

# Generating association rules
# Import the association rule function from mlxtend
from mlxtend.frequent_patterns import association_rules

# Compute all association rules for frequent_itemsets_1
rules_1 = association_rules(frequent_itemsets_1, 
                            metric = "support", 
                         	min_threshold = 0.0015)

# Compute all association rules for frequent_itemsets_2
rules_2 = association_rules(frequent_itemsets_2, 
                            metric = "support", 
                        	min_threshold = 0.0015)

# Print the number of association rules generated
print(len(rules_1), len(rules_2))

# Pruning with lift
# Import the association rules function
from mlxtend.frequent_patterns import association_rules

# Compute frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(onehot, min_support = 0.001, 
                            max_len = 2, use_colnames = True)

# Compute all association rules for frequent_itemsets
rules = association_rules(frequent_itemsets, 
                            metric = "lift", 
                         	min_threshold = 1.0)

# Print association rules
print(rules)
# Pruning with confidence
# Import the association rules function
from mlxtend.frequent_patterns import apriori, association_rules

# Compute frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(onehot, min_support = 0.0015, 
                            max_len = 2, use_colnames = True)

# Compute all association rules using confidence
rules = association_rules(frequent_itemsets, 
                            metric = "confidence", 
                         	min_threshold = 0.5)

# Print association rules
print(rules)

# Aggregation and filtering
# Apply the apriori algorithm with a minimum support of 0.0001
frequent_itemsets = apriori(aggregated, min_support = 0.0001, use_colnames = True)

# Generate the initial set of rules using a minimum support of 0.0001
rules = association_rules(frequent_itemsets, 
                          metric = "support", min_threshold = 0.0001)

# Set minimum antecedent support to 0.35
rules = rules[rules['antecedent support'] > 0.35]

# Set maximum consequent support to 0.35
rules = rules[rules['consequent support'] < 0.35]

# Print the remaining rules
print(rules)

# Applying Zhang's rule
# Generate the initial set of rules using a minimum lift of 1.00
rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1.00)

# Set antecedent support to 0.005
rules = rules[rules['antecedent support'] > 0.005]

# Set consequent support to 0.005
rules = rules[rules['consequent support'] > 0.005]

# Compute Zhang's rule
rules['zhang'] = zhangs_rule(rules)

# Set the lower bound for Zhang's rule to 0.98
rules = rules[rules['zhang'] > 0.98]
print(rules[['antecedents', 'consequents']])

# Advanced filtering with multiple metrics
# Apply the Apriori algorithm with a minimum support threshold of 0.001
frequent_itemsets = apriori(onehot, min_support = 0.001, use_colnames = True)

# Recover association rules using a minium support threshold of 0.001
rules = association_rules(frequent_itemsets, metric = 'support', min_threshold = 0.001)

# Apply a 0.002 antecedent support threshold, 0.60 confidence threshold, and 2.50 lift threshold
filtered_rules = rules[(rules['antecedent support'] > 0.002) &
						(rules['consequent support'] > 0.01) &
						(rules['confidence'] > 0.60) &
						(rules['lift'] > 2.50)]

# Print remaining rule
print(filtered_rules[['antecedents','consequents']])