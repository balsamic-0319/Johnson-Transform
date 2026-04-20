from setuptools import setup, find_packages

setup(
    name='Johnson_Transform',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="A Johnson transformation package I created for my own use",  # 説明
    author='ARATA',  # 作者名
    packages=find_packages(), # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
