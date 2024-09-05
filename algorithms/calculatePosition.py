# algorithms/calculatePositions.py

def calculate_positions(best_solution, cargo_data, container_dimensions):
    cargo_positions = []
    container_length, container_width, container_height = container_dimensions
    current_height = 0  # 当前高度
    row_width = 0  # 当前行宽度
    layer_height = 0  # 当前层高度
    used_volume = 0  # 已使用的集装箱体积

    print(f"集装箱尺寸: 长={container_length}, 宽={container_width}, 高={container_height}")

    sorted_solution = sorted(best_solution, key=lambda idx: cargo_data.iloc[idx]['Priority'], reverse=True)

    for idx in sorted_solution:
        cargo = cargo_data.iloc[idx]
        cargo_id = cargo['CargoID']
        length = cargo['Length']
        width = cargo['Width']
        height = cargo['Height']

        print(f"\n尝试放置货物: ID={cargo_id}, 长={length}, 宽={width}, 高={height}")
        print(f"当前集装箱剩余空间: 高={container_height - current_height}, 宽={container_width - row_width}")

        # 尝试在当前行放置货物
        if row_width + width <= container_width:
            if current_height + height <= container_height:
                cargo_positions.append((cargo_id, row_width, current_height, 0, length, width, height))
                print(f"放置货物: ID={cargo_id}, 位置=({row_width}, {current_height}, 0)")
                row_width += width  # 更新当前行宽度
                layer_height = max(layer_height, height)  # 更新当前层高度
                used_volume += length * width * height
            else:
                # 当前层放不下，尝试换层
                current_height += layer_height
                if current_height + height <= container_height:
                    cargo_positions.append((cargo_id, 0, current_height, 0, length, width, height))
                    print(f"放置货物: ID={cargo_id}, 位置=(0, {current_height}, 0)")
                    row_width = width  # 更新当前行宽度
                    layer_height = height  # 更新当前层高度
                    used_volume += length * width * height
                else:
                    print(f"警告：无法放置货物: ID={cargo_id}，当前高度={current_height}, 最大高度={container_height}")
                    continue  # 继续尝试放置下一个货物
        else:
            # 当前行放不下，换行
            current_height += layer_height  # 更新高度
            row_width = 0  # 重置行宽度
            layer_height = 0  # 重置层高度
            print(f"换行，当前高度更新为: {current_height}")

            if current_height + height <= container_height:
                cargo_positions.append((cargo_id, row_width, current_height, 0, length, width, height))
                print(f"放置货物: ID={cargo_id}, 位置=(0, {current_height}, 0)")
                row_width += width  # 更新当前行宽度
                layer_height = height  # 更新当前层高度
                used_volume += length * width * height
            else:
                print(f"警告：无法放置货物: ID={cargo_id}，当前高度={current_height}, 最大高度={container_height}")
                continue  # 继续尝试放置下一个货物

    print(f"\n已使用体积: {used_volume}")
    print(f"总集装箱体积: {container_length * container_width * container_height}")
    return cargo_positions
