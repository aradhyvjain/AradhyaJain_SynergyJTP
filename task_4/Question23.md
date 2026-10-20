# Question-23 Goal Check Across Two Weeks
## Aim
Create a figure with two subplots side by side that share the y-axis, one per week. Draw bars for the daily steps, add a horizontal reference line at the 8000-step goal, color bars below the goal differently, and give each subplot a title. Use one overall figure title and a sensible figure size. Interpret: did the user improve in the second week?

## Code
```python
import matplotlib.pyplot as plt
week1 = [8200, 10400, 6100, 12000, 9800, 3000, 7500]
week2 = [9000, 11000, 8500, 7000, 12500, 5000, 9500]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
goal = 8000
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), sharey=True)
def get_bar_colors(data, step_goal):
    return ['skyblue' if steps >= step_goal else 'salmon' for steps in data]
ax1.bar(days, week1, color=get_bar_colors(week1, goal), edgecolor='grey')
ax1.axhline(goal, color='red', linestyle='--', linewidth=1.5, label='8000 Step Goal')
ax1.set_title('Week 1')
ax1.set_ylabel('Steps Taken')
ax1.legend()
ax2.bar(days, week2, color=get_bar_colors(week2, goal), edgecolor='grey')
ax2.axhline(goal, color='red', linestyle='--', linewidth=1.5)
ax2.set_title('Week 2')
plt.suptitle('Goal Check Across Two Weeks', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

## Output
```text
(image in the figure section)
```

## Explanation
line 12: Initializes a figure window containing a single row of two side-by-side subplots (ax1 and ax2) that share the same vertical Y-axis.
Line 13: Defines a custom function named get_bar_colors that accepts a data list and a target step goal as inputs.
Line 14: Returns a list of colors, using 'skyblue' for days that met or exceeded the goal and 'salmon' for days that fell short.
Line 15: Plots a bar chart for Week 1 on the first subplot (ax1), dynamic-coloring the bars and giving them grey borders.
Line 16: Draws a horizontal dashed red line across the first subplot at the 8000-step mark to visually highlight the goal.
Line 17: Sets the title of the first subplot to 'Week 1'.
Line 18: Labels the vertical Y-axis of the first subplot as 'Steps Taken'.
Line 19: Displays the legend on the first subplot to show what the red dashed line represents.
Line 20: Plots a bar chart for Week 2 on the second subplot (ax2) using the same dynamic color logic and grey borders.
Line 21: Draws an identical horizontal dashed red line across the second subplot at the 8000-step mark.
Line 22: Sets the title of the second subplot to 'Week 2'.
Line 23: Adds a main, bold overarching title ('Goal Check Across Two Weeks') centered above both subplots.
Line 24: Automatically adjusts the spacing between and around the subplots so that text and labels do not overlap.

## Interpretation
Yes, the user improved in the second week.
• Higher Goal Consistency: In Week 1, the user achieved the 8,000-step goal on 4 days (Mon, Tue, Thu, Fri). In Week 2, they improved consistency by achieving the goal on 5 days (Mon, Tue, Wed, Fri, Sun).
• Higher Step Volume: The user's weekly average increased significantly from ~8,142.86 steps in Week 1 to ~8,928.57 steps in Week 2.