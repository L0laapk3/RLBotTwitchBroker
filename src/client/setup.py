# coding: utf-8

"""
    Bot Action Server

    Allows custom Rocket League bots to accept tactical suggestions in the middle of a game.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: rlbotofficial@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "rlbot-action-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Bot Action Server",
    author_email="rlbotofficial@gmail.com",
    url="",
    keywords=["Swagger", "Bot Action Server"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Allows custom Rocket League bots to accept tactical suggestions in the middle of a game.  # noqa: E501
    """
)
