import os

# 替换为你要处理的目录的路径
directory = "./"

# 要保留的模式
patterns = ["2203", "2204", "2105", "2106", "2307", "2308", ".py", ".git"]

# 遍历目录中的每个文件
for filename in os.listdir(directory):
    # 检查文件名是否不包含指定的任何模式
    if not any(pattern in filename for pattern in patterns):
        # 构建完整的文件路径
        file_path = os.path.join(directory, filename)
        # 删除文件
        os.remove(file_path)
        print(f"Deleted: {filename}")