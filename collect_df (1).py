import pandas as pd
import os


df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR-ti6Su94955DZ4Tky8EbwifpgZf_dTjpBdiVH0Ukhsq94jZdqoHuUytZsFZKfwpXEUCKRFteJRc9P/pub?gid=889004448&single=true&output=csv')

df_grp = df.groupby(['date', 'event'], as_index=False).agg({'time': 'count'})

df_grp_pivot = df_grp.pivot(index='date', columns='event', values='time').reset_index()

df_grp_pivot['ctr'] = df_grp_pivot['click'] / df_grp_pivot['view']

df_click_percent_var = (df_grp_pivot.loc[df_grp_pivot.index == 1,'click'].values[0] - df_grp_pivot.loc[df_grp_pivot.index == 0,'click'].values[0]) / df_grp_pivot.loc[df_grp_pivot.index == 0,'click'].values[0] * 100

df_view_percent_var = (df_grp_pivot.loc[df_grp_pivot.index == 1,'view'].values[0] - df_grp_pivot.loc[df_grp_pivot.index == 0,'view'].values[0]) / df_grp_pivot.loc[df_grp_pivot.index == 0,'view'].values[0] * 100

df_ctr_percent_var = (df_grp_pivot.loc[df_grp_pivot.index == 1,'ctr'].values[0] - df_grp_pivot.loc[df_grp_pivot.index == 0,'ctr'].values[0]) / df_grp_pivot.loc[df_grp_pivot.index == 0,'ctr'].values[0] * 100

df_cost = df.groupby(['date', 'event']).agg({'ad_cost': 'sum', 'event': 'count'}).rename(columns={'event' : 'event_count'}).reset_index()

df_cost['general_cost'] = df_cost['ad_cost'] / 1000 * df_cost['event_count']

df_cost_var = (df_cost.loc[df_cost.index == 3,'general_cost'].values[0] - df_cost.loc[df_cost.index == 1,'general_cost'].values[0]) / df_cost.loc[df_cost.index == 1,'general_cost'].values[0] * 100

string_to_file = 'Отчет по объявлению 121288 за 2 апреля\nТраты: {} рублей ({}%)\nПоказы: {} ({}%)\nКлики: {} ({}%)\nCTR: {} ({}%)'

file_loc = open('/home/jupyter-m.mandrik-1/MMandrik/20_3_miniproject_metrics.txt', 'w')

file_loc.write(string_to_file.format(df_cost.loc[df_cost.index == 3,'general_cost'].values[0].round(0), df_cost_var.round(0), df_cost.loc[df_cost.index == 3,'event_count'].values[0].round(0), df_view_percent_var.round(0), df_cost.loc[df_cost.index == 2,'event_count'].values[0].round(0), df_click_percent_var.round(0), df_grp_pivot.loc[df_grp_pivot.index == 1,'ctr'].values[0], df_ctr_percent_var.round(0)))

file_loc.close()
