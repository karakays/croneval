from setuptools import setup, find_packages


pkg_vars = {}


setup(
    name='croneval',
    description='cron schedule expression evaluator',
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    maintainer='Selçuk Karakayalı',
    url='http://github.com/karakays/croneval/',
    packages=find_packages(),
    python_requires='>=3.8',
    license='MIT',
    scripts=['bin/croneval'],
    long_description=open('README.md').read(),
    classifiers=[ "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
