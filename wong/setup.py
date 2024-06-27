from setuptools import setup, find_packages

setup(
    name='wong',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # 如果你的包需要依赖其他包，在这里添加
    author='wong',
    author_email='qingniao10001@outbook.com',
    description='A simple Python package for beginners',
    long_description=open('README.md').read(),  # 替换为你的实际文件名
    long_description_content_type='text/markdown',
    url='https://github.com/your_github_username/wong',  # 替换为你的实际 GitHub 仓库地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 如果你的包使用 MIT 许可证，确保添加这个分类
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Development Status :: 3 - Alpha',  # 根据你的开发状态选择相应的分类
    ],
)
