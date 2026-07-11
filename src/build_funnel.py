"""Construct client-level acceptance and first-session funnel metrics."""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.ticker import PercentFormatter


matches = pd.read_excel('Match_Data_for_Case_Study_Final_(2).xlsx', sheet_name = 1)
clients = pd.read_excel('Match_Data_for_Case_Study_Final_(2).xlsx', sheet_name = 2)
providers = pd.read_excel('Match_Data_for_Case_Study_Final_(2).xlsx', sheet_name = 3)

matches = matches[matches['MATCH_REQUEST_CREATED_AT'] > '2021-06-30'].copy()
matches['accepted_no_decline'] = np.where((~matches['ACCEPTED_AT'].isna()) & (matches['DECLINED_AT'].isna()), 1, 0)


matches['has_session'] = np.where(matches['CLIENT_PROVIDER_FIRST_DATE_OF_SERVICE'].isna(), 0 , 1)

clients_grouped = matches.groupby(['PERSONA_CLIENT_ID', 'MATCH_REQUEST_CREATED_AT'],
                                  as_index = False).agg(had_session = ('has_session', 'max'), accepted = ('accepted_no_decline', 'max'), direct = ('IS_DIRECT_SCHEDULED_BY_CLIENT', 'max') )

clients_grouped = clients_grouped.merge(clients, on = 'PERSONA_CLIENT_ID', how = 'left')
