from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="fif",
    version="1.3.1",
    install_requires=['Pillow>=8.0.0','filetype>=1.0.7'],
    author="Hazar",
    description="A command line tool for embedding any file into PNG, GIF, WAV file formats and decoding back.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hazarek/fif",
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