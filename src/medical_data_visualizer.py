import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('../data/medical_examination.csv')

# Add overweight column to the data
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Make 0 always good and 1 always bad.  If the value of cholesterol or gluc is 1, set the value to 0. 
# If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    """
    Creates a categorical plot showing counts of features split by 'cardio'.
    Returns the figure object.
    """
    # Create a Dataframe for the cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars = 'cardio',
        value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # Create the categorical plot
    g = sns.catplot(
        data = df_cat,
        x = 'variable',
        hue = 'value',
        col = 'cardio',
        kind = 'count',
        order = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    fig = g.figure

    return fig


# - Draw the Heat Map in the draw_heat_map function
# - Clean the data in the df_heat variable
# - Calculate the correlation matrix
# - Generate a mask for the upper triangle
# - Set up the matplotlib figure
# - Plot the correlation matrix

def draw_heat_map():
    """
    Creates a heat map of the correlation matrix after cleaning the data.
    Returns the figure object.
    """
    # Clean the data by filtering out incorrect segments
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Diastolic <= Systolic
        (df['height'] >= df['height'].quantile(0.025)) &  # Height >= 2.5th percentile
        (df['height'] <= df['height'].quantile(0.975)) &  # Height <= 97.5th percentile
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Weight >= 2.5th percentile
        (df['weight'] <= df['weight'].quantile(0.975))    # Weight <= 97.5th percentile
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # Plot the heat map
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        cmap='coolwarm',
        square=True,
        linewidths=0.5,
        ax=ax
    )
    
    return fig