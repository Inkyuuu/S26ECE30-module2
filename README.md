you know the drill-- create a venv (or don't, idgaf) and run `pip install -r requirements.txt` to install all packages

then you can run `python plot.py`.

this will create plots for each trial. for each trial, it'll produce:
1. total acceleration vs. time
2. acceleration vs. time for each axis (x, y, z) for each drop.

for the first type of plot, you will need to click two points on the graph. the first should be release time and the second should be impact time. these points will be recorded and the free fall duration and impact velocity will be calculated based on the chosen points. when you are done with all 9 plots, a table including all of the above info will be printed and saved to `drop_analysis_results.csv`. i already have a table based on the points i've selected, but if you want to choose your own, feel free to do so. 

anyways that's it have fun guys
