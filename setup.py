from setuptools import setup, Extension

dotspath_module = Extension('dotspath', sources=['./dotspath/module.cpp'])

setup(
    name='dots-game-env',
    version='0.1.6',
    description='Python Environment for dots game',
    url='https://github.com/cobets/dots-env',
    author='Kobets Serhii',
    author_email='cobets@gmail.com',
    license='MIT',
    packages=['dotsenv'],
    ext_modules=[dotspath_module],
    install_requires=[
        'numpy',
        'matplotlib'
    ]
)


