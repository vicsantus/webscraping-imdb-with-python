from setuptools import setup

setup(
    name="webscraping_with_python",
    version='1.0.0',
    description="Projeto de Webscraping com Python",
    install_requires=["pypubsub==4.0.3"],
    setup_requires=["pytest-runner", "scrapy"],
    tests_require=["pytest"],
    entry_points={
        'console_scripts': [
            'makeSpyder=comandos:executar_comando',
        ],
    }
)
