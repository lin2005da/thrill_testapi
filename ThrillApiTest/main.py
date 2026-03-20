'''
  @Project ：JungleApiTest 
  @File ：main.py 
  @Author ：lin20 
  @Date ：2025/10/27 11:05 
  @Describe：
 '''
import shutil
from pathlib import Path
import pytest
from common import route



if __name__ == '__main__':
  # remove previous Allure report/results so each run starts fresh
  project_root = Path(__file__).parent
  report_dir = project_root / 'allure-report'
  results_dir = project_root / 'allure'
  for d in (report_dir, results_dir):
    if d.exists():
      try:
        shutil.rmtree(d)
        print(f"Removed existing directory: {d}")
      except Exception as e:
        print(f"Warning: failed to remove {d}: {e}")
  args = ['-m', 'smoke', '--capture=no']

#生成allure报告
  try:
    import allure_commons
  except Exception:
    print("allure-pytest not installed: skipping --alluredir option (install with 'pip install allure-pytest' to enable)")
  else:
    args.append('--alluredir=allure')

  pytest.main(args)


  ## 生成pytest-html报告
  # optional pytest-html (--html=) plugin
  # try:
  #   import pytest_html  # plugin package for pytest-html
  # except Exception:
  #   print("pytest-html not installed: skipping --html option (install with 'pip install pytest-html' to enable)")
  # else:
  #   args.append('--html={0}'.format(route.html_file))

  # # optional allure (--alluredir=) plugin



# 1、快速检查（确认虚拟环境是否存在）
# Set-Location d:\cyl\test\JungleApiTest
# Get-ChildItem -Name | Where-Object { $_ -match '^\.venv' }   # 列出以 .venv 开头的目录
# Test-Path .\.venv\Scripts\python.exe                         # True 表示可用
#
# 2、运行main（在项目根运行：.venv\Scripts\python.exe main.py
# 脚本删除了旧的 allure-report / allure（如存在）。
#
# 运行 pytest 并生成 Allure 结果到 allure。）
# .\.venv\Scripts\python.exe .\main.py
#
# 3、使用 Allure CLI 生成 HTML：
# allure generate .\allure -o .\allure-report --clean
# 输出：Report successfully generated to .\allure-report
#
#
# 4、打开报告：
# allure open .\allure
# python -m http.server 8000 -d .\allure-report
# 打开报告
# Start-Process "http://127.0.0.1:8000/index.html"

