import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="docx-assembler_a-g-d",
    version="0.1.1",
    author="AGD / A-G-D",
    author_email="agd.91939@protonmail.com",
    description="A utility tool for assembling sparse .docx documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/A-G-D/docx-assembler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'wheel',
        'lxml',
        'python-docx',
        'docx2pdf',
        'docxcompose'
    ],
    python_requires='>=3.0',
)
