import matplotlib.pyplot as plt
from data_loader import load_data
import seaborn as sns

file_path = '/Users/isiomailoh/Desktop/datasets/shopping_trends_project/data/shopping_trends_dataset.csv'
df = load_data(file_path)
colors = ["#89CFF0", "#FF69B4", "#FFD700", "#7B68EE", "#FF4500",
          "#9370DB", "#32CD32", "#8A2BE2", "#FF6347", "#20B2AA",
          "#FF69B4", "#00CED1", "#FF7F50", "#7FFF00", "#DA70D6"]

# What is the distribution of customers by age and gender?
# Set the color palette
sns.set_palette(sns.color_palette(colors))

# DEMOGRAPHIC ANALYSIS:
# 1. What is the distribution of customers by age and gender?


# Set plot title and axis labels
# def plot_age_gender_distribution(df):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data=df, x='Age', hue='Gender', bins=30, kde=True)
#     plt.title('Distribution of Customers by Age and Gender')
#     plt.xlabel('Age')
#     plt.ylabel('Count of Customers')
#     genders = df['Gender'].unique()
#     plt.legend(title='Gender', labels=genders)
#     plt.show()


# 2. Correlation between Age, Gender, and Purchase Amount:
# How does age and gender correlate with the purchase amount?

# Using a box plot to visualize the distribution of purchase amount by
# df['Age_Group'] = pd.cut(df['Age'], bins=range(10, 81, 10), labels=['{}s'.format(i) for i in range(10, 80, 10)])
#
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df, x='Age_Group', y='Purchase Amount (USD)', hue='Gender')
#
# # Set plot title and axis labels
# plt.title('Distribution of Purchase Amount by Age Group and Gender')
# plt.xlabel('Age Group')
# plt.ylabel('Purchase Amount (USD)')
# plt.legend(title='Gender')
# plt.show()

# Calculate Correlation Coefficient
# pearson_corr = df[['Age', 'Purchase Amount (USD)']].corr().iloc[0, 1]
# print("Pearson Correlation Coefficient:", pearson_corr)


# 3. Differences in Shopping Behavior between Male and Female Customers:
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df, x= 'Gender', y='Purchase Amount (USD)', palette=colors)
# plt.title('Differences in Shopping Behavior between Male and Female Customers')
# plt.xlabel('Gender')
# plt.ylabel('Purchase Amount (USD)')
# plt.show()

# Using t-test to determine if there are significant differences in
# purchase amount between different age groups and genders
# t_stat, p_val = stats.ttest_ind(df[df['Gender'] == 'Male']['Purchase Amount (USD)'],
#                                 df[df['Gender'] == 'Female']['Purchase Amount (USD)'])
# print("T-Statistic:", t_stat)
# print("P-Value:", p_val)

# PRODUCT ANALYSIS:
# 1. Which items are the most frequently purchased by customers?
# item_count = df['Item Purchased'].value_counts().sort_values(ascending=False)
# most_frequent_items = item_count.head(10)
# print("Top 10 most frequently purchased items:")
# print(most_frequent_items)
#
# # Create a Bar plot to visualize the most frequently purchased items
# plt.figure(figsize=(10, 6))
# most_frequent_items.plot(kind= 'bar', color='blue')
# plt.title('Top 10 Most Frequently Purchased Items')
# plt.xlabel('Item Purchased')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# 2. What are the most popular catogories of items purchased by customers?

# Extract the category of each item
# categories = df['Category']
# # Count the frequency of each category
# top_categories = categories.value_counts().sort_values(ascending=False)
# print(f'Top category items purchased: {top_categories}')
#
# # Create a bar plot to visualize the most popular categories of items purchased
# plt.figure(figsize=(10, 6))
# top_categories.plot(kind='bar', color=colors)
# plt.title('Top Categories of Items Purchased by customers')
# plt.xlabel('Category')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()
#
# # Create a Pie Chart showing the percentage of categories of items purchased
# plt.figure(figsize=(10, 6))
# plt.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%', startangle=140)
# plt.title('Percentage of Items in Top 10 Most Popular Categories')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

# 3. What is the average purchase amount for each category of items?
# Calculate the average purchase amount for each category
# avg_purchase_amount = df.groupby('Category')['Purchase Amount (USD)'].mean().sort_values(ascending=False)
# print(f'Average purchase amount for each category: {avg_purchase_amount}')

# 4. Do certain seasons affect the types of items purchased?
# Group data by season and item category
# seasonal_category_count = df.groupby(['Season', 'Category']).size().unstack(fill_value=0)
# print(f'Seasonal category count: {seasonal_category_count}')
# # Create a bar plot to visualize the count of items purchased in each season
# seasonal_category_count.plot(kind='bar', stacked=True, figsize=(10, 6))
# plt.title('Count of Items Purchased by Season')
# plt.xlabel('Season')
# plt.ylabel('Count of Items Purchased')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# CUSTOMER ANALYSIS:
# How does the purchase amount vary based on the review rating?

# Calculate the average purchase by rating
average_purchase_by_rating = df.groupby('Review Rating')['Purchase Amount (USD)'].mean()
print(f'Average purchase amount by review rating: {average_purchase_by_rating}')

# Create a line plot to visualize the average purchase amount by review rating
plt.figure(figsize=(10, 6))
average_purchase_by_rating.plot(kind='bar', color=colors)
plt.title('Average Purchase Amount by Review Rating')
plt.xlabel('Review Rating')
plt.ylabel('Average Purchase Amount (USD)')
plt.xticks(rotation=0)
# , ha='center')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
