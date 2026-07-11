clients_grouped.groupby(['SESSION_PREFERENCE']).agg(count = ('PERSONA_CLIENT_ID', 'nunique'))

import matplotlib.pyplot as plt
import pandas as pd

clients_grouped['MATCH_REQUEST_CREATED_AT'] = pd.to_datetime(clients_grouped['MATCH_REQUEST_CREATED_AT'])

clients_grouped['YearMonth'] = clients_grouped['MATCH_REQUEST_CREATED_AT'].dt.to_period('M')

had_session_rate_per_month = clients_grouped.groupby('YearMonth')['had_session'].mean().reset_index()
sessions_per_month = clients_grouped.groupby('YearMonth')['PERSONA_CLIENT_ID'].nunique().reset_index()

had_session_rate_per_month['YearMonth'] = had_session_rate_per_month['YearMonth'].dt.strftime('%b %Y')
sessions_per_month['YearMonth'] = sessions_per_month['YearMonth'].dt.strftime('%b %Y')
had_session_rate_per_month['had_session'] = had_session_rate_per_month['had_session'] * 100

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the Number of Sessions on the first y-axis
ax1.plot(sessions_per_month['YearMonth'], sessions_per_month['PERSONA_CLIENT_ID'], label='Number of Sessions', marker='s', color='red')
ax1.set_xlabel('Date')
ax1.set_ylabel('Number of NCRs', color='red')
ax1.set_ylim(0, 12000)  # Set appropriate limits for the session rate
ax1.tick_params(axis='y', labelcolor='red')

plt.xticks(rotation=45)

# Create a second y-axis for the Had Session Rate
ax2 = ax1.twinx()  
ax2.plot(had_session_rate_per_month['YearMonth'], had_session_rate_per_month['had_session'], label='Had Session Rate', marker='o', color='blue')
ax2.set_ylabel('Conversion Rate (%)', color='blue')  
ax2.tick_params(axis='y', labelcolor='blue')
ax2.yaxis.set_major_formatter(PercentFormatter())

ax2.set_ylim(0, 15)  # Set appropriate limits for the session rate

plt.title('Conversion Rate and Number of NCRs')
ax1.grid(True)

fig.tight_layout()  # Adjust layout to make room for the labels
plt.show()
