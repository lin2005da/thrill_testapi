'''
  @Project ：JungleApiTest 
  @File ：route.py 
  @Author ：lin20 
  @Date ：2025/9/19 11:41 
  @Describe：生成文件路径
 '''


import os
import time
# 根目录
r_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# module路径
common_dir=os.path.join(r_dir,'common')
conf_dir=os.path.join(r_dir,'conf')
data_dir=os.path.join(r_dir,'data')
log_dir=os.path.join(r_dir,'log')
result_dir=os.path.join(r_dir,'result')
case_dir=os.path.join(r_dir,'case')
testcase_dir=os.path.join(r_dir,'test_case')
#配置文件
conffile=os.path.join(conf_dir,'thrilldata.conf')
datafile=os.path.join(data_dir,'testdata.xlsx')
existfile=os.path.join(conf_dir,'existdata.conf')

#报告文件路径
html_dir=os.path.join(result_dir)
html_file=os.path.join(html_dir,'report_{0}.html'.format(time.strftime('%Y%m%d')))


