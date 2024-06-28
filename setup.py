from setuptools import setup, find_packages

setup(
    name='quote_chart',
    version='0.1.1',
    description='Customized dash/plotly chart for price candles.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Stan',
    author_email='barsvquotechart@gmail.com',
    url='https://github.com/barsv/quote_chart',
    py_modules=['quote_chart'],
    packages=find_packages(),
    install_requires=[
        'dash',
        'numpy<2.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
