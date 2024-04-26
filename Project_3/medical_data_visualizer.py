import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# 3
def normalize(x):
    if x == 1:
        return 0
    else:
        return 1

df['cholesterol'] = df['cholesterol'].apply(normalize)
df['gluc'] = df['gluc'].apply(normalize)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().to_frame('total').reset_index()
    

    # 7



    # 8
    fig = sns.catplot(data=df_cat, x='variable', hue='value' , col="cardio",kind="count")
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 9))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    fig.tight_layout()
    plt.show()


    # 16
    fig.savefig('heatmap.png')
    return fig
