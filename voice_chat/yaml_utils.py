import yaml

'''

        #documents = yaml.full_load(file)

        def nested_parser(params: dict):
            for key, value in params.items():
                if isinstance(value, str):
                    try:
                        value = units.Quantity(value)
                    except UndefinedUnitError:
                        pass
                    yield key, value
                if isinstance(value, dict):
                    if value.keys() == {'values', 'units'}:
                        yield key, [i * UNITS(value['units']) for i in value['values']]
                    else:
                        yield key, dict(nested_parser(value))
                if isinstance(value, list):
                    values, unit = value

                    yield key, [i * UNITS(unit) for i in values]
                    '''
#with open(r'config.yaml') as file:

def nested_item_children(params, item):
    if isinstance(params, list):
        for entry in params:
            children = nested_item_children(entry, item)
    elif isinstance(params, dict):
        for key, value in params.items():
            if key == item:
                return value
            else:
                children = nested_item_children(value, item)
    else:  # type is string
        return None
    return children


#children = nested_item_children(yaml.safe_load(file), "form")
#print (children)