# 5.1 Introduction to Matplotlib

### Overview

Today's class will introduce the basics of [Matplotlib](http://Matplotlib.org/), one of the most popular Python plotting libraries in use today.

### Instructor Priorities

* You should understand Matplotlib's pyplot interface.

* You should be able to create line; bar; scatter; and pie charts.

* You should be familiar with basic plot configuration options, such as `xlim` and `ylim`.
- - -

### Introduction to Matplotlib

* Today's class will introduce students to Matplotlib, one of the most popular Python charting libraries in use.

* Today's lesson will focus in on the basics of a module called PyPlot, which they can use to create simple charts quickly.

* The NumPy library is oftentimes used alongside PyPlot. This package contains plenty of built-in methods which allow for simple scientific computing.

* `np.arange(start, end, step)` creates a list of numbers from `start` to `end`, where each number in the list is `step` away from the next ones.

* List comprehensions allow lists to be created using mathematic formulae. For example, you could take the values of `x_axis` list one at a time, finds the exponential of them, and stores the response within a list.

![Numpy and List Comprehensions](Images/01-IntroToMatPlot_Lists.png)

* Matplotlib allows users to generate plots by setting one list as the x-axis and another as the y-axis. It really is as simple as calling `plt.plot()`, passing those two lists through as parameters, and then calling `plt.show()` afterwards to print the chart to the screen.

* Matplotlib handles the details of painting charts to the screen, but the programmer has full control over each stage of the drawing process if they really need it. By using `plt.xlabel()` and `plt.ylabel`, for example, users can easily add axis titles to their charts as well.

![Drawing a Line Chart](Images/01-IntroToMatPlot_MakeChart.png)

* Open and run [01-Ins_BasicLineGraphs/SinCos.ipynb](Activities/01-Ins_BasicLineGraphs/SinCos.ipynb) within Jupyter Notebook to show students how PyPlot can be used to create a plot with multiple lines as well.

* Point out how `np.arange()`, `np.sin()`, and `np.cos()` are all being used in order to create the lists for the application's charts.

* In order to chart multiple lines on the same chart, it is as simple as calling `plt.plot()` two times and providing PyPlot with different values.

![Sin and Cos](Images/01-IntroToMatPlot_SinCos.png)

* While this plot is very simple, it introduces all of the major tools required to build much "prettier" plots in the future.

* Visualizations of data are valuable for far more than aesthetics. Trends and "human" insights buried within complex data sets are often clearest when the data is visualized in some way.

* Open the [Austin Weather screenshot](Images/01-IntroToMatPlot_austin.png) and point out the obvious trend — that temperature rises from January to July, and falls off from July to December. That trend is clear from the graphic but would _not_ be obvious in a table.

![Austin Weather screenshot](Images/01-IntroToMatPlot_austin.png)

* Matplotlib offers considerable control over the details of our plots' appearances and the easiest way to change the way things look is to use **keyword arguments** to configure the behavior of `plot`.

* `plt.hlines()` is used to draw a horizontal line. This method takes in three parameters: the Y value across which the line will be drawn, the X value where the line will start, and the X value where the line will end.

* The transparency of the horizontal line can also be set using the `alpha=` keyword and passing a number between 0 and 1. This setting is possible with most MatplotLib plotting functions.

![Horizontal Line](Images/03-LineConfiguration_HLines.png)

* `plt.plot()` can take in more parameters than just the X and Y values for the line being charted. For example, the markers for a plot can be set using `marker=`, the color of a plot can be set using `color=`, and the label for a line can be set using `label=`.

![Tupled Plots](Images/03-LineConfiguration_Tupled.png)

* The `plt.legend()` method allows the user to create a legend for their chart. This method takes in two parameters, `handles` and `loc`. The `handles` parameter should be set to a list of the plots the user wishes to create while `loc` is used to set the location of the legend on the chart.

* While the `plt.show()` command has not changed, a new line called `plt.savefig()` has been added which will save a version of the chart to an external file. Simply pass the file path desired as a parameter to save the image.

![Adding Legends](Images/03-LineConfiguration_Legend.png)

* The different [markers](http://Matplotlib.org/api/markers_api.html) and [colors](http://Matplotlib.org/api/colors_api.html) are available in the documentation, which students are encouraged to peruse when building their own plots.

* [updated sine and cosine plot](Activities/05-Ins_Aesthetics/sin_cos_with_markers.png).

* Point out that this is not yet "attractive", but is more readable than the previous plots, thanks to the labels and changes being made to the x-axis.

* `plt.xlabel()`, `plt.ylabel()`, and `plt.title()` are fairly self-explanatory. Simply pass a string into them as a parameter and the labels and title will be drawn onto the chart.

* `plt.xlim()` and `plt.ylim()` are used to set where the axes for the chart should begin/end. MatplotLib will naturally create charts with a lot of empty space and these methods can help to limit that.

* `plt.grid()` is also fairly obvious. Through its usage, gridlines are added onto the chart.

![Basic Aesthetics](Images/05-Aesthetics_Output.png)


### Bar Charts

* When dealing with bar charts, it is necessary to provide the heights of each bar within an array.

* The x-axis will also be an array whose length must equal that of the list of heights.

* Instead of using `plt.plot()` bar charts are drawn using `plt.bar()`.

* The `align` parameter for `plt.bar()` initially set to "center" but this oftentimes leads to the first bar to be off the side of the chart. Using "edge" instead will fix this.

![Axes and Plotting](Images/07-BarCharts_Plot.png)

* Additional aesthetic challenge unique to bar charts is aligning the tick locations on the x-axis and providing textual, rather than numeric, labels.

* The `tick_locations` list that is being created within this application moves each tickmark on the X axis over 0.4 units. This ensures the ticks are located at the center of the bars as opposed to being on the left edge.

![Ticks](Images/07-BarCharts_Ticks.png)

* The `plt.xlim()` and `plt.ylim()` are being set so that there is some space between the bars and the edge of the chart. This makes the chart look a little better aesthetically.


### Pie Charts

* The sizes of each wedge are passed into `plt.pie()` as an array. Lists containing the labels for each wedge and the colors for each wedge are also passed in.

* The pie chart allows the user to choose a wedge to "explode", using the `explode` option. This will seperate one wedge from the rest so that it is easier to examine.

* Inside of the `plt.pie()` method, a parameter of `autopc="%1.1%%"` will automatically convert the values passed into percentages with one decimal place.

![Pie Plotting](Images/09-PieCharts_Plot.png)

* Matplotlib does not constrain pie charts to be circular — by default, they will be ovals if the window the plot lives in is not a square. This is why `plt.axis("equal")` is being passed.

![Pie Axis](Images/09-PieCharts_Axes.png)

* There are additional configuration options available for improving the appearance of Matplotlib's pie charts should students desire to look into them.


### Scatter Plots

* Generating scatter plots demands the simplest set of methods of all the charts so far. Simply take in two sets of data and pass them into `plt.scatter()`.

* Call attention to the fact that the code can change the size of each individual dot by passing the `s=<LIST>` parameter. In this case, the values stored within `x_axis` will determine the size of a dot.

![Scatter Plots](Images/11-scatter.png)

