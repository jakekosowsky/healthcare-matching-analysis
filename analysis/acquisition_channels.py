client_source_stats = clients_grouped.groupby('CLIENT_SOURCE')['had_session'].mean().reset_index()
client_source_stats['had_session'] = client_source_stats['had_session'] * 100

client_source_stats = client_source_stats.sort_values('had_session')

plt.figure(figsize=(8, 6))
plt.bar(client_source_stats['CLIENT_SOURCE'], client_source_stats['had_session'], color='blue')

plt.xlabel('Client Source')
plt.ylabel('Conversion Rate (%)')
plt.title('Conversion Rate by Client Source')
plt.ylim(0, 50)

plt.gca().yaxis.set_major_formatter(PercentFormatter())
plt.grid(True, axis='y')

plt.tight_layout()
plt.show()
