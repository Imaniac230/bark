from setuptools import setup
from pathlib import Path

with open(Path(__file__).resolve().parent / 'README.md', encoding='utf-8') as f: long_description = f.read()

setup(
    name='suno-bark',
    version='0.0.1a',
    description='Bark text to audio model',
    url='https://github.com/suno-ai/bark',
    author='Suno Inc',
    author_email='hello@suno.ai',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["bark"],
    install_requires=[
        "boto3",
        "encodec",
        "funcy",
        "huggingface-hub>=0.14.1",
        "numpy",
        "scipy",
        "tokenizers",
        "torch",
        "tqdm",
        "transformers",
    ],
    extras_require={"dev": [
        "bandit",
        "black",
        "codecov",
        "flake8",
        "hypothesis>=6.14,<7",
        "isort>=5.0.0,<6",
        "jupyter",
        "mypy",
        "nbconvert",
        "nbformat",
        "pydocstyle",
        "pylint",
        "pytest",
        "pytest-cov",
    ]},
    python_requires='>=3.8',
    package_data={"bark": ["assets/prompts/*.npz", "assets/prompts/v2/*.npz"]},
    include_package_data=False)
