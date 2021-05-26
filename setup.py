from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")


setup(
    name="ftw",
    version="0.0.1",
    description="Featurizers for Twitter bot detection",
    author="Ahmed Furkan Özkalay",
    author_email="afozkalay@gmail.com",
    package_dir={"": "."},
    packages=find_packages(include=["ftw", "ftw.*"]),
    install_requires=reqs,
    include_package_data=True,
)
