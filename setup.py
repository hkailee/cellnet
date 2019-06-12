from setuptools import setup, find_packages

setup(
    name='CellNet',
    author='Lee Hong Kai',
    author_email='leehongkai@gmail.com',
    version='1.1.1.2',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    maintainer='CJM Lab',
    license='MIT',
    exclude_package_data={'': ['tools']},
    entry_points={
        'console_scripts':
            [
                'cellnet = cellphonedb.cellphonedb_cli:cli'
            ]
    },
    install_requires=[
        'click>=6.7,<6.7.99',
        'numpy',
        'pandas>=0.23,<0.23.99',
        'flask>=1.0,<1.0.99',
        'Flask-RESTful>=0.3,<0.3.99',
        'Flask-Testing>=0.7,<0.7.99',
        'SQLAlchemy>=1.2,<1.2.99',
        'PyYAML>=3.13,<3.13.99',
        'requests>=2.19,<2.19.99',
    ],
)
