from setuptools import setup, find_packages

setup(
    name='Gibox',  # 包名
    version='1.8',  # 版本
    description="将所有Widget都加入到Gib.Gibox盒子上",  # 包简介
    long_description=open('README.md', "r", encoding='UTF-8').read(),  # 读取文件中介绍包的详细内容
    include_package_data=True,  # 是否允许上传资源文件
    author='XiangQinxi',  # 作者
    author_email='XiangQinxi@outlook.com',  # 作者邮件
    maintainer='XiangQinxi',  # 维护者
    maintainer_email='XiangQinxi@outlook.com',  # 维护者邮件
    license='MIT License',  # 协议
    url='https://github.com/XiangQinxi',  # github或者自己的网站地址
    project_urls={
        "Gibox": "https://github.com/XiangQinxi/Gibox",
    },
    packages=find_packages(where="src"),  # 包的目录
    package_dir={"": "src"},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  # 设置编写时的python版本
    ],
    python_requires='>=3.6',  # 设置python版本要求
    install_requires=['pygobject'],  # 安装所需要的库
    entry_points={
        'console_scripts': [
            ''],
    },  # 设置命令行工具(可不使用就可以注释掉)

)
