import matplotlib.pyplot as plt

from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and display the categorical plot
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')
plt.show()

# Generate and display the heat map
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')
plt.show()