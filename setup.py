from setuptools import setup, Extension

dotspath_module = Extension('dotspath', sources=['./dotspath/module.cpp'])

setup(
    name='dotsgameenv',
    version='0.1.2',
    description='Python Environment for dots game',
    url='https://github.com/cobets/dots-env',
    author='Kobets Serhii',
    author_email='cobets@gmail.com',
    license='MIT',
    ext_modules=[dotspath_module],
    install_requires=[
        'numpy',
        'matplotlib'
    ]
)


