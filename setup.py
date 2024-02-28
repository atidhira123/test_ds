from setuptools import setup, find_packages

install_requires = []
extra_requires_dev = [
    'pytest',
    'pytest-cov',
    'moto',
    'tox',
    'flake8'
]
desc = 'This package contains some functions that calculate number one.'
setup(
    name='theone',
    version='0.1.0',
    description=desc,
    author='Agung Atidhira',
    author_email='agungatd2@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=install_requires,
    extras_requires={'dev': extra_requires_dev},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Specify license
        'Operating System :: OS Independent',
    ]
)
