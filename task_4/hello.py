import os
import matplotlib.pyplot as plt
subjects = ['Maths', 'Physics', 'Programming', 'Chemistry', 'English']
class_avg = [72.3, 65.1, 81.4, 58.9, 76.0]
target = 70
sorted_data = sorted(zip(class_avg, subjects))
sorted_avgs, sorted_subs = zip(*sorted_data)
plt.figure(figsize=(8, 5))
colors = ['#e74c3c' if avg < target else '#3498db' for avg in sorted_avgs]
bars = plt.barh(sorted_subs, sorted_avgs, color=colors, edgecolor='none')
plt.axvline(x=target, color='gray', linestyle='--', linewidth=1.5, label=f'Target ({target})')
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.1f}', 
             va='center', ha='left', fontsize=10, fontweight='bold')
plt.title('Class Average Performance by Subject', fontsize=14, pad=15)
plt.xlabel('Class Average (%)', fontsize=12)
plt.ylabel('Subjects', fontsize=12)
plt.xlim(0, 100) # Give extra breathing room for text labels
plt.legend(loc='lower right')
output_dir = 'task_4/figures'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'subject_performance.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
if os.path.exists(output_path):
    print(f"Success! Image saved and confirmed at: '{output_path}'")
plt.show()

