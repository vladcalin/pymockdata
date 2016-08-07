# pymockdata 
[![Build Status](https://travis-ci.org/vladcalin/pymockdata.svg?branch=master)](https://travis-ci.org/vladcalin/pymockdata) 
[![Coverage Status](https://coveralls.io/repos/github/vladcalin/pymockdata/badge.svg?branch=master)](https://coveralls.io/github/vladcalin/pymockdata?branch=master)

A Python library for generating mock data and exporting it in various formats.

***Table of contents***

1. [Motivation](#motivation)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)

	a) [The DataModel class](#data_model_class)
	b) [The MockDataGenerator class](#mock_data_generator_class)
	c) [The DataFactory class and exporters](#data_factory_class)
	
5. [Known issues](#issues)
6. [Contributing](#contributing)
7. [Credits and references](#credits)


<a name="motivation"/>
## Motivation

In various cases I needed real-looking generated data for tests and presentations and I thought that I might build a tool
that generates such data and exports it to various formats such as HTML, XML, CSV, JSON, etc. or even exporting it directly into a database.

<a name="description"/>
## Description

TODO

<a name="dependencies"/>
## Dependencies

TODO

<a name="installation"/>
## Installation

TODO

<a name="usage"/>
## Usage

There are various methods to generate mock data. 

<a name="data_model_class"/>
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
 
The `DataModel.generate_one()` method will generate a `dict` instance populated with mock data, and the `DataModel.generate_batch(count)` will generate a list if `dict` instances.

<a name="mock_data_generator_class"/>
### The MockDataGenerator class


This class can be used to generate one value of a kind. Example usage:

```python
	generator = MockDataGenerator()

	# calling specific methods that will generate just one mock value from each category
    	print(generator.full_name())
    	# Alberto Jack P. Montes
    
    	print(generator.mac_addr())
    	# da:76:20:3f:75:e3
    
    	print(generator.ipv4_addr())
    	# 171.15.230.181
    
    	print(generator.domain())
    	# farnecessarily.ru
    
    	print(generator.forum_username())
    	# magnificent.harmony9
```

<a name="data_factory_class"/>
### The DataFactory class and exporters

Exporters are classes specialized in exporting the generated data in various formats. Available exporters are: 
- `pymockdata.exporters.StreamExporter`(writes the data directly to a stream, default `sys.stdout`)
- `pymockdata.exporters.file.CsvExporter` (writes the data into a CSV file, the field names are not preserved)
- `pymockdata.exporters.file.JsonExporter` (writes the data into a JSON file, using the JSON specifications)
- `pymockdata.exporters.file.XmlExporter` (writes data into a XML file, respecting the XML specifications. The exported file will have the structure:

```xml
	<entries>
		<entry>
			<field_one>value</field_one>
			<field_two>value</field_two>
			...
		</entry>
		...
	</entries>
```	
- `pymockdata.exporters.file.HtmlTableExporter` (will export data to a HTML file, in a table structure)

The `DataFactory` constructor takes as parameters a `DataModel` instance and an exporter instance.

Example usage:

	# the data_model instance is declared as in the previous examples
	from pymockdata.exporters.file import JsonExporter

    exporter = JsonExporter("myfile.json")
    DataFactory(data_model, exporter).generate(100)

After that, in the `myfile.json` file we will have generated 100 mock instances:

	{
    "entries": [
        {
            "third_field": "112.125.80.60",
            "first_field": "Cristal Joyce",
            "second_field": "santiago_mohammedhouston@talk.io"
        },
        {
            "third_field": "254.167.37.229",
            "first_field": "Guadalupe Cindy Fitzpatrick",
            "second_field": "heidi_sageware@yawningly.biz"
        },
        ...

## Known issues

TODO

## Contributing

TODO

## Credits and references

TODO

