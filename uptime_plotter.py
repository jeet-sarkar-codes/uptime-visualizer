import matplotlib.pyplot as plt
import random

time_stamps = list(range(1, 25))  # 24 hours
uptime_status = [random.choice([1, 1, 1, 0]) for _ in time_stamps]  # 1 = up, 0 = down

plt.plot(time_stamps, uptime_status, marker='o', linestyle='--')
plt.yticks([0, 1], ['Down', 'Up'])
plt.xlabel('Hour')
plt.ylabel('Status')
plt.title('Simulated System Uptime Over 24 Hours')
plt.grid(True)
plt.savefig('uptime_chart.png')
plt.show()