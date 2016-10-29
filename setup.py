from distutils.core import setup

setup(
    name='xyscope',
    version='1.0',
    packages=['xyscope'],
    url='https://github.com/SopaXorzTaker/xyscope',
    license='GNU GPL v3',
    author='SopaXorzTaker',
    author_email='',
    description='A small X/Y oscilloscope for viewing wave files.', requires=['scipy', 'Pillow']
)
