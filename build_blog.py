import os
from datetime import datetime  # 导入日期库

# 获取当前日期，格式为 YYYY-MM-DD
current_date = datetime.now().strftime('%Y-%m-%d')

# 1. 生成根目录的总 README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write("# 技术博客总入口\n")
    f.write("<sub>made by chanvel</sub>\n\n") # 添加了小字号副标题
    f.write("## 学习分类\n")
    f.write("- [🐍 Python 语言学习](./python/README.md)\n")
    # 使用动态获取的时间
    f.write(f"\n> 最近更新: {current_date}") 

# 2. 读取 py 内容并转为 md 格式
if os.path.exists('python'):
    with open('python/README.md', 'w', encoding='utf-8') as f:
        f.write("# Python 学习笔记\n\n")
        
        # 遍历 python 目录下的文件
        files = [file for file in os.listdir('python') if file.endswith('.py')]
        
        for file in files:
            file_path = os.path.join('python', file)
            f.write(f"## 文件名: {file}\n\n")
            
            with open(file_path, 'r', encoding='utf-8') as py_file:
                code_content = py_file.read()
                f.write("```python\n")
                f.write(code_content)
                f.write("\n```\n\n")
                f.write("---\n") 

print(f"✅ 博客已更新，当前同步时间: {current_date}")