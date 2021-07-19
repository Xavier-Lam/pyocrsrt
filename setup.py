from setuptools import find_packages, setup

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")

with open("requirements.txt") as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name="pyocrsrt",
    version="0.1.0",
    author="Xavier-Lam",
    packages=find_packages(),
    keywords=["ocr", "subtitle", "srt", "rip", "video"],
    description="Rip hard subtitles from video into .srt files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities"
    ],
    entry_points = dict(
        console_scripts=[
            "pyocrsrt = pyocrsrt:main"
        ],
    ),
)