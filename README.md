# pymockdata 
[![Build Status](https://travis-ci.org/vladcalin/pymockdata.svg?branch=master)](https://travis-ci.org/vladcalin/pymockdata) 
[![Coverage Status](https://coveralls.io/repos/github/vladcalin/pymockdata/badge.svg?branch=master)](https://coveralls.io/github/vladcalin/pymockdata?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pymockdata/badge/?version=latest)](http://pymockdata.readthedocs.io/en/latest/?badge=latest)

A Python library for generating mock data and exporting it in various formats.

***Table of contents***

1. [Motivation](#motivation)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [Credits and references](#credits)


<a name="motivation"/>
## Motivation

This project aims to provide a method for generating mock data for other
applications that might need it for various reasons. Some of these reasons 
might be: presenting a demo of your application in an realistic manner
 with users that look real, test your applications capabilities and behaviour when 
the database has more than 10 entries or measure the performance of your application
when dealing with huge amount of data.

<a name="description"/>
## Description

The *`pymockdata`* Python library is capable of generating mock data for your applications.

<a name="installation"/>
## Installation

Download the project and run 
```
python setup.py install
```
and the project should be ready to run.

<a name="usage"/>
## Simple usage

### The DataModel class
The simpliest method is by using a DataModel instance:

```python
	from pymockdata import DataModel
	
	# define the DataModel fields with field_name=field_type
	data_model = DataModel(
		first_field=DataModel.full_name,
		second_field=DataModel.email,
		third_field=DataModel.ipv4_addr
	)
	# generate one instance
	data_model.generate_one()
	# {
	#	'first_field': 'Gracie-Lillian Meyers', 
	#	'second_field': 'bpetty@mistequal.jp', 
	#	'third_field': '238.247.120.38'
	# }

	# or generate multiple instances at once
	data_model.generate_batch(10)
	# [{
	#	'first_field': 'Gianni Yair A. Li', 
	#	'second_field': 'malia_chasitygibbs@judgementally.ru', 
	#	'third_field': '44.68.62.124'
	# }, 
	# {
	#	'first_field': 'Belen X. Pitts', 
	#	'second_field': 'sofia_adapaul@mortally.es', 
	#	'third_field': '117.69.254.192'
	# }
	# ...
	# ]
	# or generate a single instance
	data_model.value_for(DataModel.forum_username)
```

The `DataModel` class exposes constants that should be used as field type in the constructor. The supported constants so far are:
- male_name
- female_name
- last_name
- full_male_name
- full_female_name
- full_name
- noun
- adjective
- forum_username
- professional_username
- tld
- domain
- email
- ipv4_addr
- ipv6_addr
- mac_addr

<a name="contributing"/>
## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

<a name="credits"/>
## Credits and references

- This project was inspired by [`fake-factory`](https://github.com/joke2k/faker)
- The base name/nouns/adjectives/adverbs lists were produced by [`RandomLists.com`](<https://www.randomlists.com/>)

