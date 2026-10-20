# Question-21 How many bins is Too many?
## Aim
These are the scores of 20 players on a game level. A teammate drew the histogram below and says the two plots are unreadable.
plt.hist(scores, bins=5)
plt.hist(scores, bins=10)
plt.show()
Explain what is wrong with this approach, then draw the two histograms side by side in two subplots with a shared x-range of 0–100, titles and axis labels. Add vertical lines for the mean and median. Interpret: what shape does the distribution have, and which bin width tells the story better?

## Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
scores = [12, 18, 22, 25, 28, 31, 33, 35, 38, 41, 44, 47, 52, 55, 58, 61, 67, 74, 88, 95]
# plt.hist(scores, bins=5)
# plt.hist(scores, bins=10)
# plt.show()
meanvalue=np.mean(scores)
medianvalue=np.median(scores)
fig,axes=plt.subplots(1,2,sharey=True)
axes[0].hist(scores,bins=5,range=(0,100), color='skyblue', edgecolor='black')
axes[0].axvline(meanvalue, color='red', linestyle='--', linewidth=2, label="mean {}".format(meanvalue))
axes[0].axvline(medianvalue, color='green', linestyle='-', linewidth=2, label="median {}".format(medianvalue))
axes[0].set_title("5 bin histogram")
axes[0].set_xlabel('Scores')
axes[0].set_ylabel('Number of Players')
axes[0].set_xlim(0,100)
axes[0].legend()
axes[0].grid()

axes[1].hist(scores,bins=10,range=(0,100), color='red', edgecolor='black')
axes[1].axvline(meanvalue, color='red', linestyle='--', linewidth=2, label="mean {}".format(meanvalue))
axes[1].axvline(medianvalue, color='green', linestyle='-', linewidth=2, label="median {}".format(medianvalue))
axes[1].set_title("10 bin histogram")
axes[1].set_xlabel('Scores')
axes[1].set_ylabel('Number of Players')
axes[1].set_xlim(0,100)
axes[1].legend()
axes[1].grid()
plt.tight_layout()
plt.show()
```

## Output
```text
(image in figures section)
```

## Explanation
Here is the line-by-line explanation of the code, which calculates basic statistics and visualizes a dataset of scores side-by-side using two different histogram configurations.

## Data Preparation and Setup
scores = [...]: Creates a list of numerical player scores to be analyzed and plotted.
plt.hist(...) & # plt.show(): Commes out initial basic plot test lines so they do not run.
meanvalue = np.mean(scores): Calculates the average value of all scores in the list.
medianvalue = np.median(scores): Finds the middle value of the sorted list of scores.
fig, axes = plt.subplots(1, 2, sharey=True): Creates a layout with 1 row and 2 side-by-side plots that share the same vertical y-axis.
axes[0].hist(...): Draws a sky-blue histogram with 5 blocks spanning from 0 to 100 on the first plot.
axes[0].axvline(meanvalue, ...): Draws a dashed red vertical line at the calculated mean value location.
axes[0].axvline(medianvalue, ...): Draws a solid green vertical line at the calculated median value location.
axes[0].set_title("5 bin histogram"): Adds a main header text label above the first plot.
axes[0].set_xlabel('Scores'): Sets the title for the horizontal axis of the first plot.
axes[0].set_ylabel('Number of Players'): Sets the title for the vertical axis of the first plot.
axes[0].set_xlim(0, 100): Restricts the horizontal view boundaries of the first graph from 0 to 100.
axes[0].legend(): Displays a floating key box identifying what the red and green lines stand for.
axes[0].grid(): Overlays background grid lines on the first graph to make data reading easier.
plt.tight_layout(): Automatically adjusts graph positions so titles and labels do not overlap each other.
plt.show(): Opens up the finalized window to display both generated plots on the screen.

## Interpretation
Shape of the Distribution:
The distribution is moderately right-skewed (positively skewed). This is confirmed both visually by the longer tail extending toward the higher scores (80–100) and mathematically because the mean (46.2) is greater than the median (42.5).
Which bin width tells the story better?
The 5-bin configuration (bin width = 20) tells the story better for this small dataset of 20 players. With 10 bins (bin width = 10), the data becomes too fragmented, resulting in an unstable, blocky appearance with several uniform gaps. The 5-bin plot cleanly aggregates the counts [2, 7, 6, 3, 2], showing a clear peak in the 20–40 range followed by a smooth decline.
