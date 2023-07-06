from setuptools import setup

setup(
    name="webscraping_with_python",
    description="Projeto de Webscraping do IMDB com Python",
    install_requires=["pypubsub==4.0.3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
