# Planning

## General workflow and components

The project should provide and easy to understand architecture that can be extended with ease. I suggest the following workflow:

`Data` -> `Templates` -> `Generators` -> `Core` -> `Exporters`

1. `Data` = a collection of basic words, such as `male_names`,`female_names`, `adjectives`, `nouns`, etc.
2. `Templates` = a collection of rules that define how a specific value should be built. For example, a template for generating a `full_female_name` would be: 
> `"{female_name} {letter}. {last_name}"`

3. `Generators` = classes specialized in building specific values, depending the parameters. These classes will choose the right template, parse it and combine it with the proper data.
4. `Core` = Exposes an easy to understand API for programmatic use and command-line interface.
5. `Exporters` = classes that takes as input the generated data, parses it and outputs it in various formats, such as XML, CSV, JSON, etc.