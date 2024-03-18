import os
from setuptools import setup, find_packages

# Leitura das dependências do arquivo requirements.txt
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    with open(requirements_path) as f:
        return [line.strip() for line in f if not line.strip().startswith('#')]

# Carregamento da descrição longa do README.md
def load_long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(
    name="bittensor_subnet_template",  
    version="0.1.0",  # Defina a versão do seu pacote
    author="Seu Nome",
    author_email="seu@email.com",
    description="Descrição do seu pacote",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/seu-repositorio",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
