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
print(f"Confirm file exists: {file_exists}")


