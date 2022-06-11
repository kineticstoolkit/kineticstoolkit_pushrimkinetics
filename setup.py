"""Setup tool for building a pip-accessible package."""

import setuptools

#--------------------------------------------------------------------------------
# Please modify to fit your extension (particularly the text in CAPITALS)
#--------------------------------------------------------------------------------
name = "kineticstoolkit_EXTENSIONNAME"
description = "An extension to Kinetics Toolkit"
url = "https://github.com/USER/REPOSITORY"
author = "NAME"
author_email = "EMAIL"
#--------------------------------------------------------------------------------
# It may be advised to avoid modifying the rest of this file.
#--------------------------------------------------------------------------------


with open("README.md", "r") as fh:
    long_description = fh.readline()

setuptools.setup(
    name=name,
    description=(description),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=author_email,
    license='Apache',
        license_files=['LICENSE.txt', 'VERSION.txt'],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.8',
)
