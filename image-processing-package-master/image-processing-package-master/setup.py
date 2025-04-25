from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'matplotlib'
    ],
    author='Seu Nome',
    description='Pacote de exemplo para processamento de imagens com Python',
    license='MIT',
)
