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
