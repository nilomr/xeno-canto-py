from setuptools import setup

setup(
    name='xeno-canto',
    version='2.0.2',
    description='xeno-canto.org API Wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ntivirikin/xeno-canto-py',
    author='Nazariy Tivirikin',
    author_email='n.tivirikin@gmail.com',
    license="MIT",
    py_modules=['xenocanto'],
    install_requires=["tqdm"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["xeno-canto = xenocanto:main"]},
)
