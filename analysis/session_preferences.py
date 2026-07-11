test = clients_grouped[clients_grouped['had_session'] == 1 ]
session_preference_stats = test.groupby('SESSION_PREFERENCE')['direct'].mean().reset_index()
session_preference_stats = session_preference_stats[session_preference_stats['SESSION_PREFERENCE'].isin(['inPerson', 'video'])]

session_preference_stats['direct'] = session_preference_stats['direct'] * 100

plt.figure(figsize=(8, 6))
plt.bar(session_preference_stats['SESSION_PREFERENCE'], session_preference_stats['direct'], color='blue')

plt.xlabel('Session Preference')
plt.ylabel('Scheduling Rate (%)')
plt.title('Scheduling Rate by Session Preference')
plt.ylim(0, 25)  # Set y-axis limits to percentage range (0 to 100)
plt.gca().yaxis.set_major_formatter(PercentFormatter())

plt.grid(True, axis='y')

plt.tight_layout()
plt.show()

test = clients_grouped[clients_grouped['accepted'] == 1]
session_preference_stats = test.groupby('SESSION_PREFERENCE')['had_session'].mean().reset_index()
session_preference_stats = session_preference_stats[session_preference_stats['SESSION_PREFERENCE'].isin(['inPerson', 'video'])]

session_preference_stats['had_session'] = session_preference_stats['had_session'] * 100

plt.figure(figsize=(8, 6))
plt.bar(session_preference_stats['SESSION_PREFERENCE'], session_preference_stats['had_session'], color='blue')

plt.xlabel('Session Preference')
plt.ylabel('Conversion Rate (%)')
plt.title('Conversion Rate Given They Are Accepted')
plt.ylim(0, 25)  # Set y-axis limits to percentage range (0 to 100)
plt.gca().yaxis.set_major_formatter(PercentFormatter())

plt.grid(True, axis='y')

plt.tight_layout()
plt.show()

session_preference_stats = clients_grouped.groupby('SESSION_PREFERENCE')['had_session'].mean().reset_index()
session_preference_stats = session_preference_stats[session_preference_stats['SESSION_PREFERENCE'].isin(['inPerson', 'video'])]

session_preference_stats['had_session'] = session_preference_stats['had_session'] * 100

plt.figure(figsize=(8, 6))
plt.bar(session_preference_stats['SESSION_PREFERENCE'], session_preference_stats['had_session'], color='blue')

plt.xlabel('Session Preference')
plt.ylabel('Conversion Rate (%)')
plt.title('Conversion Rate by Session Preference')
plt.ylim(0, 25)  # Set y-axis limits to percentage range (0 to 100)
plt.gca().yaxis.set_major_formatter(PercentFormatter())

plt.grid(True, axis='y')

plt.tight_layout()
plt.show()
