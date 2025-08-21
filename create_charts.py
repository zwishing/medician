#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
药物数据柱状图生成器
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_drug_charts():
    """创建药物数据的各种柱状图"""
    
    # 读取数据
    print("正在读取药物数据...")
    df = pd.read_csv('data/Pillbox_-_Archived_Data.csv')
    print(f"数据读取完成，共 {len(df)} 条记录")
    
    # 设置中文字体支持
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 1. 药物形状分布柱状图
    print("正在创建药物形状分布图...")
    plt.figure(figsize=(14, 8))
    
    shape_counts = df['splshape_text'].value_counts().head(12)
    bars = plt.bar(range(len(shape_counts)), shape_counts.values, 
                   color=plt.cm.Set3(np.linspace(0, 1, len(shape_counts))))
    
    plt.title('药物形状分布 (前12种)', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('药物形状', fontsize=14)
    plt.ylabel('数量', fontsize=14)
    plt.xticks(range(len(shape_counts)), list(shape_counts.index), rotation=45, ha='right')
    
    # 添加数值标签
    for i, bar in enumerate(bars):
        height = float(bar.get_height())
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{int(height):,}', ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('drug_shape_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. 药物大小分布柱状图
    print("正在创建药物大小分布图...")
    plt.figure(figsize=(14, 8))
    
    size_counts = df['splsize'].value_counts().head(15)
    bars2 = plt.bar(range(len(size_counts)), size_counts.values, 
                    color=plt.cm.viridis(np.linspace(0, 1, len(size_counts))))
    
    plt.title('药物大小分布 (前15种)', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('药物大小 (mm)', fontsize=14)
    plt.ylabel('数量', fontsize=14)
    plt.xticks(range(len(size_counts)), list(size_counts.index), rotation=45, ha='right')
    
    # 添加数值标签
    for i, bar in enumerate(bars2):
        height = float(bar.get_height())
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{int(height):,}', ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('drug_size_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 3. 药物启用状态分布柱状图
    print("正在创建药物启用状态分布图...")
    plt.figure(figsize=(10, 6))
    
    enabled_counts = df['Enabled?'].value_counts()
    colors = ['#2E8B57', '#DC143C']  # 绿色表示启用，红色表示禁用
    bars3 = plt.bar(range(len(enabled_counts)), enabled_counts.values, color=colors)
    
    plt.title('药物启用状态分布', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('启用状态', fontsize=14)
    plt.ylabel('数量', fontsize=14)
    plt.xticks(range(len(enabled_counts)), list(enabled_counts.index))
    
    # 添加数值标签
    for i, bar in enumerate(bars3):
        height = float(bar.get_height())
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{int(height):,}', ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('drug_enabled_status.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. 药物版本号分布柱状图
    print("正在创建药物版本号分布图...")
    plt.figure(figsize=(12, 6))
    
    version_counts = df['version_number'].value_counts().head(10)
    bars4 = plt.bar(range(len(version_counts)), version_counts.values, 
                    color=plt.cm.plasma(np.linspace(0, 1, len(version_counts))))
    
    plt.title('药物版本号分布 (前10种)', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('版本号', fontsize=14)
    plt.ylabel('数量', fontsize=14)
    plt.xticks(range(len(version_counts)), list(version_counts.index))
    
    # 添加数值标签
    for i, bar in enumerate(bars4):
        height = float(bar.get_height())
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{int(height):,}', ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('drug_version_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n所有柱状图创建完成！")
    print("保存的图片文件：")
    print("- drug_shape_distribution.png")
    print("- drug_size_distribution.png") 
    print("- drug_enabled_status.png")
    print("- drug_version_distribution.png")

if __name__ == "__main__":
    try:
        create_drug_charts()
    except Exception as e:
        print(f"创建图表时出错: {e}")
        print("请确保数据文件存在且格式正确")
