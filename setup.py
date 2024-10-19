from setuptools import setup, find_packages

setup(
    name='digit_counter',
    version='0.1.0',
    author='Nestor Urquiza',
    author_email='your.email@example.com',
    description='A package to count the number of base-10 digits in the integer part of a number.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nestoru/digit_counter',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'digit-counter = digit_counter.counter:main',
        ],
    },
    include_package_data=True,
)

