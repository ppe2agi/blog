import os
from pathlib import Path
from datetime import datetime

# 配置
NOW = datetime.now().strftime('%Y-%m-%d %H:%M')
SRC = Path('python')
ROOT_MD = Path('README.md')
SRC_MD = SRC / 'README.md'

def build():
    SRC.mkdir(exist_ok=True)
    py_files = sorted(SRC.glob('*.py'))
    
    # 生成 python/README.md
    with open(SRC_MD, 'w', encoding='utf-8') as f:
        f.write(f"# 🐍 Python 源码汇总\n\n[⬅️ 返回首页](../README.md)\n\n---\n\n")
        for py in py_files:
            f.write(f"## 📄 {py.name}\n\n```python\n{py.read_text('utf-8')}\n```\n\n---\n\n")

    # 生成根目录 README.md
    content = [
        f"<sub>更新: {NOW}</sub>\n",
        "# 🚀 代码库",
        f"- [Python 源码详情](./python/README.md) ({len(py_files)} 个案例)"
    ]
    ROOT_MD.write_text('\n'.join(content), 'utf-8')

if __name__ == "__main__":
    build()
    print("✅ 已更新")