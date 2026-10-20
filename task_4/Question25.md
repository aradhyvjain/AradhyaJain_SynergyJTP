# Question-25 Publication-ready dashboard figure
## Aim
Create a horizontal bar chart of class averages sorted from lowest to highest. Color bars below the target differently, draw a vertical reference line at 70, write the value at the end of each bar, and set a title, axis labels and figsize=(8, 5). Save the figure as task_4/figures/subject_performance.png at 300 dpi with a tight bounding box (create the folder if it does not exist) and confirm the file exists. A colleague’s saved image came out blank because their code calls plt.show() before plt.savefig(...). Explain why that happens and what the correct order is. Interpret: which subjects need attention?

## Code
```python
import matplotlib.pyplot as plt
subjects = ['Maths', 'Physics', 'Programming', 'Chemistry', 'English']
class_avg = [72.3, 65.1, 81.4, 58.9, 76.0]
target = 70
sorted_data = sorted(zip(class_avg, subjects))
sorted_avgs, sorted_subs = zip(*sorted_data)
plt.figure(figsize=(8, 5))
colors = ['#e74c3c' if avg < target else '#2ecc71' for avg in sorted_avgs]
bars = plt.barh(sorted_subs, sorted_avgs, color=colors, height=0.6)
plt.axvline(x=target, color='#7f8c8d', linestyle='--', linewidth=1.5, label=f'Target ({target})')
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1.5, bar.get_y() + bar.get_height()/2, f'{width:.1f}', 
             va='center', ha='left', fontsize=10, fontweight='bold')
plt.title('Class Average Performance by Subject', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Average Score (%)', fontsize=12)
plt.ylabel('Subjects', fontsize=12)
plt.xlim(0, 100)
plt.legend(loc='lower right')
plt.grid(axis='x', linestyle=':', alpha=0.5)
file_path = 'task_4/figures/subject_performance.png'
plt.savefig(file_path, dpi=300, bbox_inches='tight')
file_exists = False
try:
    with open(file_path, 'rb'):
        file_exists = True
except FileNotFoundError:
    file_exists = False
```

## Output
```text
(image in yask_4\figures folder)
```
## Explanation
sorted_avgs, sorted_subs = zip(*sorted_data): Unzips the sorted pairs back into two separate tuples: one for sorted scores and one for sorted subjects.
bars = plt.barh(sorted_subs, sorted_avgs, color=colors, height=0.6): Creates a horizontal bar chart mapping the sorted subjects and scores using the generated conditional colors and a bar thickness of 0.6.
for bar in bars:: Begins a loop to iterate through each individual horizontal bar drawn on the chart. width = bar.get_width(): Retrieves the numerical width value of the current bar, which represents the subject's average score.plt.text(width + 1.5, bar.get_y() + bar.get_height()/2, f'{width:.1f}', va='center', ha='left', fontsize=10, fontweight='bold'): Places a bold, formatted text label showing the exact score just to the right of each horizontal bar.
file_path = 'task_4/figures/subject_performance.png': Defines a string variable indicating the directory pathway and filename where the chart image will be saved.
plt.savefig(file_path, dpi=300, bbox_inches='tight'): Saves the generated chart to disk as a high-resolution 300 DPI PNG file, trimming off excess white margins.
file_exists = False: Initializes a boolean tracking flag variable to False.
try:: Opens a structured testing block to attempt executing code that might potentially crash or fail.
with open(file_path, 'rb'):: Safely attempts to open the newly saved chart image file in read-binary mode.
file_exists = True: Flips the tracking flag variable to True if the file opens successfully without errors.
except FileNotFoundError:: Catches the specific structural error that triggers if the computer cannot find the specified file pathway.
file_exists = False: Sets the tracking flag variable explicitly back to False if the file could not be found or opened.

## Interpretation
Explanation: Why the Blank Image Happens
Calling plt.show() opens a window displaying the current active figure. Once that window is closed, Matplotlib considers the drawing cycle complete and automatically clears or resets the current figure canvas to free up memory. Calling plt.savefig() after plt.show() saves a fresh, completely blank canvas.
The Correct Order: Always call plt.savefig() first, and then call plt.show().

Based on the target threshold of 70, the following two subjects fall below expectations and require intervention:
Chemistry (Lowest average at 58.9)
Physics (Second lowest average at 65.1)

    
    

