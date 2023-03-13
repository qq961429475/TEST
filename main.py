import os
import time
import pytest

def init_env():
    """
    初始化图片目录
    """
    if not os.path.exists("./test_report" + "/image"):
        os.makedirs("./test_report" + "/image")

def run():
    init_env()
    # 指定目录/文件执行用例
    pytest.main(['-s', '-v',
                 '--html=./test_report/report.html',
                 # 捕获错误日志输出信息到测试报告
                 "--capture=sys",
                 # 把css样式合并到html里,避免分享时CSS样式丢失
                 "--self-contained-html"
                 #设置最大失败次数
                 "--maxfail", "5",
                 # 设置失败重跑次数
                 "--reruns", "1"
                ])


if __name__ == '__main__':
    run()