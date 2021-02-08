


import yaml
import json

with open("site.yaml") as f:
    data = yaml.safe_load(f)
    print(data)


def traverse_dict(data):
    print("\n")
    default = None
    tab_no = -1
    for key, val in data.items():
        print("\n")
        print(key)
        if val:
            if isinstance(val, list):
                for entry in val:
                    traverse_dict(entry)
            elif isinstance(val, dict):
                traverse_dict(val)
            else:
                print( val)

'''
<ul>
    {% for key, value in data.items %}
        <li>{{ key }}</li>

        { % if {{value}} %}
            {% if isinstance({{ value }}, list) %}
                <ul>
                    {% for entry in value %}
                        <li>
                          {% include "traverse_dict.html" %}
                        </li>
                    {% endfor %}
                </ul>
            {% endif %}
            {% if isinstance({{value}}, dict) %}
                <ul>
                {% for key, value in value %}
                    <li> {{key}}
                {% include "traverse_dict.html" %}
            < / li >
            { % endfor %}
            < / ul >
            { % endif %}
        {% endif %}
    {% endfor %}
</ul>



'''





traverse_dict(data)



