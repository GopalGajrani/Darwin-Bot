import json
import matplotlib.pyplot as plt

# 1. Load the data from your score file
with open('score.json', 'r') as f:
    data = json.load(f)

history = data.get('history', [])
generations = list(range(1, len(history) + 1))

# 2. Create the plot
plt.figure(figsize=(10, 5))
plt.plot(generations, history, color='#2ca02c', linewidth=2, label='Best Fitness')

# 3. Add labels and styling
plt.title('Darwin Bot: Evolution Progress over 100 Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 4. Save or show
plt.savefig('fitness_curve.png')
print("Graph saved as fitness_curve.png")