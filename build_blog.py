import os
import re
from datetime import datetime
from pathlib import Path

# === 配置 ===
current_date = datetime.now().strftime('%Y-%m-%d %H:%M')
author_info = "made by chanvel"
domain_name = "blog.ppe2agi.qzz.io"
source_dir = Path('python')

def get_file_description(content):
    """
    提取 Python 文件顶部的 docstring (多行注释)
    """
    # 匹配文件开头的 """...""" 或 '''...'''
    docstring_match = re.search(r'^(?:["\']{3})(.*?)(?:["\']{3})', content, re.DOTALL)
    if docstring_match:
        return docstring_match.group(1).strip()
    return "暂无详细说明"

def build():
    source_dir.mkdir(exist_ok=True)
    Path('CNAME').write_text(domain_name, encoding='utf-8')

    # 1. 生成根目录 README.md
    root_content = [
        f"<sub>{author_info} | 更新时间: {current_date}</sub>\n",
        "# 🚀 源码仓库索引",
        f"- [🤔 Python 语言源码库](./python/README.md) —— 共收录 {len(list(source_dir.glob('*.py')))} 个案例"
    ]
    Path('README.md').write_text('\n'.join(root_content), encoding='utf-8')

    # 2. 生成 python/README.md
    py_files = sorted([f for f in source_dir.glob('*.py')])
    
    with open(source_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(f"# 🤔 Python 源码详情\n\n[⬅️ 返回首页](../README.md)\n\n---\n\n")
        
        if not py_files:
            f.write("> 📂 目录目前是空的，快去添加代码吧！\n")
        else:
            for file_path in py_files:
                code_content = file_path.read_text(encoding='utf-8')
                description = get_file_description(code_content)
                
                # 写入标题和注释
                f.write(f"### 📄 {file_path.name}\n")
                f.write(f"> **功能描述：** {description}\n\n") 
                
                # 代码块展示
                f.write(f"<details>\n<summary>展开查看完整代码</summary>\n\n")
                f.write(f"```python\n{code_content}\n```\n")
                f.write(f"\n</details>\n\n---\n\n")

if __name__ == "__main__":
    build()
    print(f"✅ 构建完成！已提取注释并同步更新。")
