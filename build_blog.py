import os

# 1. 生成根目录的总 README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write("# 我的技术博客总入口\n\n")
    f.write("## 学习分类\n")
    f.write("- [🐍 Python 语言学习](./python/README.md)\n")
    f.write(f"\n> 最近更新: 2025-12-24")

# 2. 读取 py 内容并转为 md 格式
if os.path.exists('python'):
    with open('python/README.md', 'w', encoding='utf-8') as f:
        f.write("# Python 学习笔记\n\n")
        
        # 遍历 python 目录下的文件
        files = [file for file in os.listdir('python') if file.endswith('.py')]
        
        for file in files:
            file_path = os.path.join('python', file)
            f.write(f"## 文件名: {file}\n\n")
            
            # 读取 .py 文件实际内容
            with open(file_path, 'r', encoding='utf-8') as py_file:
                code_content = py_file.read()
                f.write("```python\n")
                f.write(code_content)
                f.write("\n```\n\n")
                f.write("---\n") # 添加分割线

print("✅ 已成功将 .py 内容提取并生成至 python/README.md")