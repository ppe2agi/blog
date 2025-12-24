import os
import shutil
from datetime import datetime

# === 配置 ===
current_date = datetime.now().strftime('%Y-%m-%d')
author_info = "made by chanvel"
domain_name = "blog.ppe2agi.qzz.io"

# 1. 彻底清理并重建 docs 文件夹，确保没有残留乱象
if os.path.exists('docs'):
    shutil.rmtree('docs')
os.makedirs('docs/python')

# 2. 生成 CNAME (只在 docs 里生成)
with open('docs/CNAME', 'w', encoding='utf-8') as f:
    f.write(domain_name)

# 3. 生成首页 index.md (只在 docs 里生成)
with open('docs/index.md', 'w', encoding='utf-8') as f:
    f.write(f"# 🏠 我的 Python 代码库\n\n")
    f.write(f"<sub>{author_info} | 更新日期: {current_date}</sub>\n\n")
    f.write("## 导航\n")
    f.write("- [🤔 Python 语言案例](./python/index.md)\n")

# 4. 提取根目录 python/ 文件夹下的源码并生成到 docs/python/index.md
source_dir = 'python' 
dest_file = 'docs/python/index.md'

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(f"# 🤔 Python 语言案例\n\n")
    if os.path.exists(source_dir):
        py_files = [file for file in os.listdir(source_dir) if file.endswith('.py')]
        for file in py_files:
            f.write(f"### 📄 {file}\n\n")
            with open(os.path.join(source_dir, file), 'r', encoding='utf-8') as py_content:
                f.write(f"```python\n{py_content.read()}\n```\n\n---\n\n")

print("✅ 文档已精简生成至 docs/ 目录")