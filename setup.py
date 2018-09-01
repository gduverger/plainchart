import setuptools

with open('README.md', 'r') as fh:
	readme = fh.read()

setuptools.setup(
	name='plainchart',
	version='0.2.1',
	author='Georges Duverger',
	author_email='georges.duverger@gmail.com',
	description='A simple plain-text, no-dependencies, pip-installable, open-source charting utility in Python.',
	long_description=readme,
	long_description_content_type='text/markdown',
	url='https://github.com/gduverger/plainchart',
	license='MIT',
	packages=['plainchart'],
	# install_requires=[],
	python_requires='>=3',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Natural Language :: English'
	],
)
