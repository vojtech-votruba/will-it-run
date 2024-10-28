from setuptools import setup, find_packages

setup(
    name='will-it-run',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'html2text',
        'rapidfuzz',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'will-it-run = will_it_run.scripts.will_it_run:cli',
        ],
    },
)