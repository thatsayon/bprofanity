from setuptools import setup
import bprofanity

setup(
    name="bprofanity",
    version=bprofanity.__version__,
    author="Ashiqul Islam Ayon",
    author_email="ashiqulislamayon28@gmail.com",
    packages=['bprofanity'],
    url='https://github.com/thatsayon/bprofanity',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',),
    data_files=[('data', ['bprofanity/data/wordlist.txt']), ],
    package_data={
        '': ['bprofanity/data/wordlist.txt'],
    },
    include_package_data=True,
)
