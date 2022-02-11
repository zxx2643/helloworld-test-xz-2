from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='helloworld-test-xz-2',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="hello world",
    license="GNUv3",
    author="Xiaoxuan Zhang",
    author_email='zhangxiaoxuan258@gmail.com',
    url='https://github.com/zxx2643/helloworld-test-xz-2',
    packages=['helloworld_test_xz_2'],
    entry_points={
        'console_scripts': [
            'helloworld_test_xz_2=helloworld_test_xz_2.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='helloworld-test-xz-2',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
