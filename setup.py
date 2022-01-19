import setuptools
long_desc = open("README.md").read()
required = [<Dependent Packages>] # Comma seperated dependent libraries name

setuptools.setup(
    name="<PACKAGE_NAME>",
    version="<VERSION_NUMBER>", # eg:1.0.0
    author="<YOUR NAME>",
    author_email="<YOUR EMAIL>",
    license="<YOUR_LICENSE>",
    description="<SHORT DESCRIPTION>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<PACKAGE GITHUB URL>",
    packages = ['<YOUR_PACKAGE_NAME>'],
    # project_urls is optional
    project_urls={
        "Bug Tracker": "<BUG_TRACKER_URL>",
    },
    key_words="<KEY WORDS>",
    install_requires=required,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)