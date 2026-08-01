import random
import pandas as pd


data = []

for _ in range(10000):

    cpu = random.randint(1, 100)
    memory = random.randint(10, 100)
    disk = random.randint(20, 100)
    processes = random.randint(50, 600)

    # Rule-based labeling
    if cpu > 90 and memory > 85 and processes > 450:
        threat = "Malware"

    elif cpu > 75 or memory > 75 or processes > 300:
        threat = "Suspicious"

    else:
        threat = "Normal"

    data.append({
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk,
        "process_count": processes,
        "threat": threat
    })


df = pd.DataFrame(data)

df.to_csv("cyber_dataset.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())