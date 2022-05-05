from setuptools import setup


setup(
    name="depth2water",
    version="0.0.1",
    license="MIT",
    author="David M. Brown",
    author_email="davebshow@gmail.com",
    description="Client for depth2water",
    url='',
    packages=['depth2water'],
    extras_require={
        'test': ['pytest']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ]
)