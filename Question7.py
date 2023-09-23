# Q7. You are analyzing a dataset with two continuous variables, "Temperature" and "Humidity", and two
# categorical variables, "Weather Condition" (Sunny/Cloudy/Rainy) and "Wind Direction" (North/South/
# East/West). Calculate the covariance between each pair of variables and interpret the results.

# Answer - 

# Temperature and Humidity (Continuous - Continuous):

# Calculate the covariance between "Temperature" and "Humidity" to measure their joint variability. Positive covariance indicates that when one variable increases, the other tends to increase, and vice versa. Negative covariance indicates an inverse relationship.
# Interpretation: A positive covariance between temperature and humidity might suggest that higher temperatures are associated with higher humidity levels, while a negative covariance might suggest that higher temperatures are associated with lower humidity levels.
# Weather Condition and Wind Direction (Categorical - Categorical):

# Covariance is typically not calculated for categorical variables like "Weather Condition" and "Wind Direction" since they don't have a numeric scale or natural order.
# Instead, consider using techniques like chi-squared contingency tables or Cramer's V statistic to measure the association between these categorical variables.