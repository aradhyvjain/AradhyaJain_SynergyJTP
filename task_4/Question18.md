# Question-18 Who Is buying the Tickets?
## Aim
Draw a stacked bar chart of tickets sold per day, split by internal and external visitors. Then draw a grouped bar chart of the same data in a second figure. Design: which chart better shows the total footfall, and which better compares internal against external visitors? Justify in two sentences. Compute the external share for each day and state when the fest was most dependent on outside visitors.

## Code
```python
import matplotlib.pyplot as plt
day = ['Day 1', 'Day 2', 'Day 3']
internal = [120, 150, 90]
external = [30, 80, 160]
#definig bar 1
plt.bar(day,internal, width=0.5, label="Internal")
plt.bar(day,external,width=0.5, label='external')
plt.title("Stacked bar chart")
plt.xlabel("Days")
plt.ylabel("Tickets sold")
plt.legend(loc='best')
plt.show()
x = range(len(day))
width = 0.35
plt.bar([i - width/2 for i in x], internal,
        width, label='Internal Visitors')
plt.bar([i + width/2 for i in x], external,
        width, label='External Visitors')
plt.xlabel('Day')
plt.ylabel('Tickets Sold')
plt.title('Grouped Bar Chart')
plt.xticks(x, day)
plt.legend()
plt.show()
```

## Output
```
(image in figures section)
```

## Explanation
1. Data Setup (Lines 7–10)
day = ['Day 1', 'Day 2', 'Day 3']: Defines the labels for the X-axis.
internal = [120, 150, 90]: Represents the first set of values (e.g., internal tickets sold) for each of the three days.
external = [30, 80, 160]: Represents the second set of values (e.g., external tickets sold) for each day.

2. Part 1: Stacked Bar Chart (Lines 11–18)
This section attempts to create a stacked bar chart, though it contains a logical plotting mistake.

plt.bar(day, internal, ...): Plots the initial bars for "Internal" tickets.
plt.bar(day, external, ...): Overlays the "external" bars directly on top of the exact same position. Because a bottom argument wasn't specified (e.g., bottom=internal), the external bars are overlapping/hiding parts of the internal bars instead of stacking properly on top of them.
plt.title, plt.xlabel, plt.ylabel: Adds the title "Stacked bar chart" and labels the axes ("Days" and "Tickets sold").
plt.legend(loc='best'): Automatically places a legend box in the best available clear spot on the graph.
plt.show(): Renders and displays the first chart on your screen

3. Part 2: Grouped Bar Chart 
x = range(len(day)): Creates numerical positions [0, 1, 2]
width = 0.35: Sets the width of each individual bar.
Shifting the bars:
*[i - width/2 for i in x]: Shifts the "Internal Visitors" bars slightly to the left of the center tick mark.
[i + width/2 for i in x]: Shifts the "External Visitors" bars slightly to the right of the center tick mark.
plt.xticks(x, day): Replaces the temporary numeric positions ([0, 1, 2]) back with the actual text labels (['Day 1', 'Day 2', 'Day 3']).
plt.title, plt.xlabel, plt.ylabel, plt.legend, plt.show: Adds labels for the second chart ("Grouped Bar Chart") and displays it.

## Justification
The stacked bar chart better shows the total footfall because the overall height of each stacked bar directly represents the total sum of tickets sold each day.
The grouped bar chart better compares internal against external visitors because the bars are placed side-by-side along the same baseline, allowing the viewer to easily gauge the exact difference in their heights