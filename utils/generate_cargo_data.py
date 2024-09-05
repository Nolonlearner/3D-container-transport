import pandas as pd
import random
import os

# 创建数据
cargo_data = pd.DataFrame({
    'CargoID': [f'C{i:03}' for i in range(1, 31)],
    'Weight': [random.randint(100, 1000) for _ in range(30)],
    'Volume': [random.randint(1, 50) for _ in range(30)],
    'Priority':[random.randint(1, 5) for _ in range(30)],
})

# 保存数据到data文件夹
output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cargo_details.csv')
cargo_data.to_csv(output_path, index=False)

print("Cargo data generated successfully!")
