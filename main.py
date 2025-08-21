import pandas as pd

def read_from_file(file_path: str) -> pd.DataFrame:
    """
    从 CSV 文件读取数据并返回 DataFrame。
    """
    # 读取 CSV
    df = pd.read_csv(file_path)
    return df

def main():
    file_path = "data/Pillbox_-_Archived_Data.csv"
    df = read_from_file(file_path=file_path)

    # 查看前 5 行
    # print("=== 前 5 行数据 ===")
    # print(df.head())

    # 查看第一行（行索引 0）
    # print("\n=== 第一行数据 ===")
    # print(df.iloc[0])  # iloc 按行号定位
    #
    # # 查看第一列（列索引 0）
    # print("\n=== 第一列数据 ===")
    # print(df.iloc[:, 0])  # iloc 按列号定位
    #
    # # 查看数据的基本信息（行数、列数、数据类型等）
    # print("\n=== 数据信息 ===")
    # print(df.info())
    #
    # # 查看列名
    # print("\n=== 列名列表 ===")
    # print(df.columns)
    #
    # # 查看每列的缺失值情况
    # print("\n=== 缺失值统计 ===")
    # print(df.isnull().sum())

    # idx = df.iloc[:, 0].idxmax()
    # print("\n=== 最大值所在的行（idxmax法） ===")
    # print(df.loc[idx])
    print(df.mean(axis=0))



if __name__ == "__main__":
    main()
