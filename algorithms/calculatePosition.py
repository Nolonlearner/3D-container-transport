# algorithms/calculatePosition.py
def calculate_positions(best_solution, cargo_data, container_dimensions):
    """
    根据最优解决方案计算货物在集装箱中的位置。

    参数：
    best_solution: 最优解的货物索引列表
    cargo_data: 货物信息（DataFrame，包括重量、体积）
    container_dimensions: 集装箱尺寸（长、宽、高）

    返回：
    cargo_positions: 货物的位置列表，每个元素为 (CargoID, x, y, z, 长, 宽, 高)
    """
    cargo_positions = []
    container_length, container_width, container_height = container_dimensions
    current_height = 0  # 当前高度，用于叠放货物
    row_items = []  # 用于存储当前行的货物
    row_width = 0  # 当前行的宽度

    for idx in best_solution:
        cargo = cargo_data.iloc[idx]  # 获取当前货物的信息
        cargo_id = cargo['CargoID']
        weight = cargo['Weight']
        volume = cargo['Volume']

        # 假设每个货物的尺寸为 1x1x(体积)
        cargo_length = 1
        cargo_width = 1
        cargo_height = volume  # 体积直接作为高度

        # 检查是否能放入当前行
        if row_width + cargo_width <= container_width:
            # 添加货物到当前行
            cargo_positions.append((cargo_id, row_width, current_height, 0, cargo_length, cargo_width, cargo_height))
            row_width += cargo_width  # 更新当前行宽度
        else:
            # 如果当前行放不下，则换行
            current_height += max(cargo_height for _, _, height, _, _, _, _ in cargo_positions if height == 0)  # 找到当前行最高的货物
            row_width = cargo_width  # 新的一行宽度为当前货物的宽度
            cargo_positions.append((cargo_id, 0, current_height, 0, cargo_length, cargo_width, cargo_height))

        # 检查集装箱高度限制
        if current_height + cargo_height > container_height:
            print("警告：集装箱空间不足，无法装载所有货物。")
            break

    return cargo_positions