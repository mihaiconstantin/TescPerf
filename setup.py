from setuptools import setup


setup(
	name='TescPerf',
	version='1.0',
	py_modules=['tescperf'],
	install_requires=[
		'Click',
		'beautifulsoup4',
		'requests'
	],
	entry_points='''
		[console_scripts]
		tescperf=tescperf:cli
	''',
)
