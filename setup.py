import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()

setuptools.setup(
	name = 'Text_cleaning_GRT',
	version = '0.0.1',
	author = 'Guadalupe Rivera-Torruco',
	author_email = 'GRT-coder@gmail.com',
	description = "This a text preprocessing package",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: GNU General Public',
	'Operating System :: OS Independent'],
	python_requires = '>3.5'
	)