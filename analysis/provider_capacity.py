df = matches.merge(providers, on = 'PERSONA_PROVIDER_ID', how = 'left')
gender_stats = df.groupby('EDUCATION_LEVEL')['has_session'].mean().reset_index()
gender_stats = gender_stats[gender_stats['EDUCATION_LEVEL'].isin(['Masters', 'Psychologist'])]


# Step 2: Convert had_session rate to percentage
gender_stats['has_session'] = gender_stats['has_session'] * 100

# Step 3: Plot the data
plt.figure(figsize=(8, 6))
plt.bar(gender_stats['EDUCATION_LEVEL'], gender_stats['has_session'], color='blue')

# Step 4: Add labels and title
plt.xlabel('Education Level')
plt.ylabel('Conversion Rate (%)')
plt.title('Provider Conversion Rate by Education Level')
plt.ylim(0, 8)  # Set y-axis limits to percentage range

# Step 5: Format the y-axis to show percentages
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Step 6: Add grid for better readability
plt.grid(True, axis='y')

# Step 7: Display the plot
plt.tight_layout()
plt.show()

df = df.sort_values('MATCH_REQUEST_CREATED_AT')
df['clients_at_time_of_match'] = df.groupby(['PERSONA_PROVIDER_ID'])['has_session'].cumsum()

# Assuming your DataFrame is named 'df'

# Step 1: Create buckets for provider_capacity
bins = [0, 9, 19, 29,100]  # Define the bucket ranges
labels = ['0-9', '10-19', '20-29', '30+']  # Define labels for the buckets
df['capacity_bucket'] = pd.cut(df['clients_at_time_of_match'], bins=bins, labels=labels, right=False)

# Step 2: Group by the provider_capacity buckets and calculate the mean had_session rate
capacity_stats = df.groupby('capacity_bucket', observed=True)['has_session'].mean().reset_index()

# Step 3: Convert had_session rate to percentage
capacity_stats['has_session'] = capacity_stats['has_session'] * 100

# Step 4: Plot the data
plt.figure(figsize=(8, 6))
plt.bar(capacity_stats['capacity_bucket'], capacity_stats['has_session'], color='blue')

# Step 5: Add labels and title
plt.xlabel('Number of Clients a Provider Has At Time of Match')
plt.ylabel('Conversion Rate (%)')
plt.title('Conversion Rate by Current Provider Capacity')
plt.ylim(0, 10)  # Set y-axis limits to percentage range

# Step 6: Format the y-axis to show percentages
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Step 7: Add grid for better readability
plt.grid(True, axis='y')

# Step 8: Display the plot
plt.tight_layout()
plt.show()
