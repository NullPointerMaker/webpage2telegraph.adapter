import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webpage2telegraph",
    version="2021.6.22",
    author="NullPointerMaker",
    description="Transfer webpage to Telegraph archive.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NullPointerMaker/webpage2telegraph.adapter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'export_to_telegraph>=0.0.128',
        'html_telegraph_poster>=0.4.0',
    ],
    python_requires='>=3.0',
)
