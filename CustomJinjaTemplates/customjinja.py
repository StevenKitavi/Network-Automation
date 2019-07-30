from jinja2 import Environment, FileSystemLoader
import yaml
ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    #def_interface_speed returns the default Mbps value for a given 
    #network interface by looking for certain keywords in the name

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

#Filters are added to the ENV object after declatation.
#the get_interface_speed is actually being passed and not run 
#when the funtion template.render is called the temlate engine will execute this funtion

ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("temlatestuff/customjinja.j2")

#load our YAML file and pass it in to the temlate when rendering it 
with open("templatestuff/data.yml") as f:
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))
    