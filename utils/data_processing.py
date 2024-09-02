# utils/data_processing.py

import numpy as np


def load_data(file_path):
    """
    从文件加载实验数据。

    参数：
    file_path: 数据文件的路径

    返回：
    data: 加载的实验数据（NumPy数组）
    """
    data = np.loadtxt(file_path, delimiter=',')
    return data


def preprocess_data(data):
    """
    对数据进行预处理，例如归一化或特征提取。

    参数：
    data: 原始数据（NumPy数组）

    返回：
    preprocessed_data: 预处理后的数据
    """
    # 示例：数据归一化
    preprocessed_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return preprocessed_data
