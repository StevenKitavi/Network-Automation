from jinja2 import Environment,FileSystemLoader
import yaml
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("GenInterfaceConfigs.j2")


with open("data.yml") as f:
    interfaces = yaml.load(f)
    output =template.render(interface_list=interfaces)
    print(output)

interfaces = [
    {
        "name" : "GigabitEthernet0/1",
        "desc" : "Uplink Port",
        "uplink" : True
    },
    {
        "name" : "GigabitEthernet0/2",
        "desc" : "Server port number one",
        "vlan" : 10
    },
    {
        "name" : "GigabitEthernet0/3",
        "desc" : "Server port number two",
        "vlan" : 10

    }
]

