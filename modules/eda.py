import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visualizations(df, tag):
    output_path = f'static/outputs/{tag}_plot.png'

    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x='Date', y='PM2.5', label='PM2.5')
    sns.lineplot(data=df, x='Date', y='NO2', label='NO2')
    sns.lineplot(data=df, x='Date', y='O3', label='O3')
    plt.title(f'Air Quality Over Time - {tag}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path
