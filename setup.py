from setuptools import setup
import bprofanity

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="bprofanity",
    version=bprofanity.__version__,
    author="Ashiqul Islam Ayon",
    author_email="ashiqulislamayon28@gmail.com",
    description="A Python package for detecting and filtering profanity from bangla text",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['bprofanity'],
    url='https://github.com/thatsayon/bprofanity',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',),
    data_files=[('data', ['bprofanity/data/wordlist.enc']), ],
    package_data={
        '': ['bprofanity/data/wordlist.enc'],
    },
    include_package_data=True,
)
