import os
import re
from setuptools import setup


def find_packages(package, basepath):
    packages = [package]
    for name in os.listdir(basepath):
        path = os.path.join(basepath, name)
        if not os.path.isdir(path):
            continue
        packages.extend(find_packages('%s.%s'%(package, name), path))
    return packages


here = os.path.abspath(os.path.dirname(__file__))
desc = 'Multivariate function optimizer based on the tensor train approach.'
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    desc_long = f.read()


with open(os.path.join(here, 'ttopt/__init__.py'), encoding='utf-8') as f:
    text = f.read()
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", text, re.M)
    version = version.group(1)


with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split('\n')
    requirements = [r for r in requirements if len(r) >= 3]


setup_args = dict(
    name='ttopt',
    version=version,
    description=desc,
    long_description=desc_long,
    long_description_content_type='text/markdown',
    author='Andrei Chertkov',
    author_email='andre.chertkov@gmail.com',
    url='https://github.com/AndreiChertkov/ttopt',
    classifiers=[
        'Development Status :: 4 - Beta', # 3 - Alpha, 5 - Production/Stable
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='function optimization function minimization low-rank representation tensor train format TT-decomposition cross approximation',
    packages=find_packages('ttopt', './ttopt/'),
    package_data={'':['../ttopt-demo/*.py','../*.so']},
    python_requires='>=3.7',
    project_urls={
        'Source': 'https://github.com/AndreiChertkov/ttopt',
    },
)


if __name__ == '__main__':
    setup(
        **setup_args,
        install_requires=requirements,
        include_package_data=True)
