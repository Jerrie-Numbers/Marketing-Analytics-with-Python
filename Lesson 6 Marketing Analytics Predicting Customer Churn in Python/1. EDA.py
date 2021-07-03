# Predicting Customer Churn 

# EDA
# Summary statistics for both classes
# Adapt your code to compute the standard deviation
print(telco.groupby(['Churn']).mean())

# Count the number of churners and non-churners by State
print(telco.groupby('State')['Churn'].value_counts())

# Exploring feature distributions
# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the distribution of 'Day_Mins'
sns.distplot(telco['Day_Mins'])

# Display the plot
plt.show()

# Customer service calls and churn
# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Remove outliers
sns.boxplot(x = 'Churn',
            y = 'CustServ_Calls',
            data = telco,
            sym = "")

# Display the plot
plt.show()

# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add "Intl_Plan" as a third variable
sns.boxplot(x = 'Churn',
            y = 'CustServ_Calls',
            data = telco,
            sym = "",
            hue = "Intl_Plan")

# Display the plot
plt.show()

