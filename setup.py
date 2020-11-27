from setuptools import setup, find_namespace_packages

setup(
    name="fif",
    version="1.1.0.dev1",
    install_requires=['Pillow>=8.0.0','filetype>=1.0.7'],
    python_requires='>=3',
    packages=find_namespace_packages(),
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',],
        
    entry_points={
        'console_scripts': [
            'fif = fif.main:run_fif'
        ]
    }
)
