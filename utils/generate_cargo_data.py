# utils/generate_cargo_data.py
import pandas as pd
import random
import os

# 创建数据
cargo_data = pd.DataFrame({
    'CargoID': [f'C{i:03}' for i in range(1, 51)],
    'Weight': [random.randint(100, 1000) for _ in range(50)],
    'Length': [random.uniform(0.5, 2.0) for _ in range(50)],  # 长度在0.5到2.0米之间
    'Width': [random.uniform(0.5, 2.0) for _ in range(50)],   # 宽度在0.5到2.0米之间
    'Height': [random.uniform(0.5, 2.0) for _ in range(50)],  # 高度在0.5到2.0米之间
})

# 计算体积
cargo_data['Volume'] = cargo_data['Length'] * cargo_data['Width'] * cargo_data['Height']

# 随机生成优先级
cargo_data['Priority'] = [random.randint(1, 5) for _ in range(50)]

# 保存数据到data文件夹
output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cargo_details.csv')
cargo_data.to_csv(output_path, index=False)

print("Cargo data generated successfully!")
