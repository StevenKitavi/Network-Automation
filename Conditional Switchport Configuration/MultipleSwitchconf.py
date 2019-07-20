from jinja2 import Environment,FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("MultipleSwitchConf.j2")


intdict = {
    "GigabitEthernet0/1" : "Server Port Number one",
    "GigabitEthernet0/2" : "Server Port Number two",
    "GigabitEthernet0/3" : "Server Port Number three"
}
print(template.render(interface_dict=intdict))