from setuptools import setup, find_packages

setup(
    name='CLU_project',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='https://github.com/zakaria-source/dataleon_CLU_test.git',
    license='',
    author='Dbaba',
    author_email='zakaria-dbaba@hotmail.com',
    description='An conversational language understanding project',
    install_requires=[
        'azure-ai-language-conversations==1.1.0',
        'attrs==23.2.0',
        'cryptography==42.0.5',
        'packaging==24.0',
        'pytest==8.1.1',
        'python-dotenv>=1.0.1'
    ],
)
