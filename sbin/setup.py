from setuptools import setup

setup(
    name='hpcc-sbin',
    version='0.1',
    py_modules=[
        'vcl',
        'hpcc',
        'ecl',
        'thor',
        'roxie',
        'benchmark',
        'mycontroller',
        'mydriver',
    ],
    include_package_data=True,
    install_requires=[
        'click',
        'executor',
        'lxml',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'vcl=vcl:cli',
            'hpcc=hpcc:cli',
            'ecl=ecl:cli',
            'thor=thor:cli',
            'roxie=roxie:cli',
            'benchmark=benchmark:cli',
            'mycontroller=mycontroller:cli',
            'mydriver=mydriver:cli',
        ]
    }
)
