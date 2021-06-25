# Association Rules
# Recommending books with support
# Compute support for Hunger and Potter
supportHP = np.logical_and(books['Hunger'], books['Potter']).mean()

# Compute support for Hunger and Twilight
supportHT = np.logical_and(books['Hunger'], books['Twilight']).mean()

# Compute support for Potter and Twilight
supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()

# Print support values
print("Hunger Games and Harry Potter: %.2f" % supportHP)
print("Hunger Games and Twilight: %.2f" % supportHT)

# Refining support with confidence
# Compute support for Potter and Twilight
supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()

# Compute support for Potter
supportP = books['Potter'].mean()

# Compute support for Twilight
supportT = books['Twilight'].mean()

# Compute confidence for both rules
confidencePT = supportPT / supportP
confidenceTP = supportPT / supportT

# Print results
print('{0:.2f}, {1:.2f}'.format(confidencePT, confidenceTP))

# Further refinement with lift
# Compute support for Potter and Twilight
supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()

# Compute support for Potter
supportP = books['Potter'].mean()

# Compute support for Twilight
supportT = books['Twilight'].mean()

# Compute lift
lift = supportPT / (supportP * supportT)

# Print lift
print("Lift: %.2f" % lift)

# Computing conviction
# Compute support for Potter AND Hunger
supportPH = np.logical_and(books['Potter'], books['Hunger']).mean()

# Compute support for Potter
supportP = books['Potter'].mean()

# Compute support for NOT Hunger
supportnH = 1.0 - books['Hunger'].mean()

# Compute support for Potter and NOT Hunger
supportPnH = supportP - supportPH

# Compute and print conviction for Potter -> Hunger
conviction = supportP * supportnH / supportPnH
print("Conviction: %.2f" % conviction)

# Computing conviction with a function
def conviction(antecedent, consequent):
	# Compute support for antecedent AND consequent
	supportAC = np.logical_and(antecedent, consequent).mean()

	# Compute support for antecedent
	supportA = antecedent.mean()

	# Compute support for NOT consequent
	supportnC = 1.0 - consequent.mean()

	# Compute support for antecedent and NOT consequent
	supportAnC = supportA - supportAC

    # Return conviction
	return supportA * supportnC / supportAnC
# Promoting ebooks with conviction
# Compute conviction for twilight -> potter and potter -> twilight
convictionTP = conviction(twilight, potter)
convictionPT = conviction(potter, twilight)

# Compute conviction for twilight -> hunger and hunger -> twilight
convictionTH = conviction(twilight, hunger)
convictionHT = conviction(hunger, twilight)

# Compute conviction for potter -> hunger and hunger -> potter
convictionPH = conviction(potter, hunger)
convictionHP = conviction(hunger,potter)

# Print results
print('Harry Potter -> Twilight: ', convictionHT)
print('Twilight -> Potter: ', convictionTP)

# Computing association and dissociation
# Compute the support of Twilight and Harry Potter
supportT = books['Twilight'].mean()
supportP = books['Potter'].mean()

# Compute the support of both books
supportTP = np.logical_and(books['Twilight'], books['Potter']).mean()

# Complete the expressions for the numerator and denominator
numerator = supportTP - supportT*supportP
denominator = max(supportTP*(1-supportT), supportT*(supportP-supportTP))

# Compute and print Zhang's metric
zhang = numerator / denominator
print(zhang)

# Defining Zhang's metric
# Define a function to compute Zhang's metric
def zhang(antecedent, consequent):
	# Compute the support of each book
	supportA = antecedent.mean()
	supportC = consequent.mean()

	# Compute the support of both books
	supportAC = np.logical_and(antecedent, consequent).mean()

	# Complete the expressions for the numerator and denominator
	numerator = supportAC - supportA*supportC
	denominator = max(supportAC*(1-supportA), supportA*(supportC-supportAC))

	# Return Zhang's metric
	return numerator / denominator
# Applying Zhang's metric
# Define an empty list for Zhang's metric
zhangs_metric = []

# Loop over lists in itemsets
for itemset in itemsets:
    # Extract the antecedent and consequent columns
	antecedent = books[itemset[0]]
	consequent = books[itemset[1]]
    
    # Complete Zhang's metric and append it to the list
	zhangs_metric.append(zhang(antecedent, consequent))
    
# Print results
rules['zhang'] = zhangs_metric
print(rules)

# Filtering with support and conviction
# Preview the rules DataFrame using the .head() method
print(rules.head())

# Select the subset of rules with antecedent support greater than 0.05
rules = rules[rules['antecedent support'] > 0.05]

# Select the subset of rules with a consequent support greater than 0.01
rules = rules[rules['consequent support'] > 0.01]

# Select the subset of rules with a conviction greater than 1.01
rules = rules[rules['conviction'] > 1.01]

# Print remaining rules
print(rules)

# Using multi-metric filtering to cross-promote books
# Set the lift threshold to 1.5
rules = rules[rules['lift'] > 1.5]

# Set the conviction threshold to 1.0
rules = rules[rules['conviction']>1.0]

# Set the threshold for Zhang's rule to 0.65
rules = rules[rules['zhang']>0.65]

# Print rule
print(rules[['antecedents','consequents']])


print("Harry Potter and Twilight: %.2f" % supportPT)