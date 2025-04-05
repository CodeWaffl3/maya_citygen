import random
from maya import cmds

module_rules = {
    height:3,
}

module_variants = [
    "red",
    "blue",
    "green"
]


#TODO: Remove This, just for reference
result_tower = [
    {
        module: "red",
        floor_level: 0
    }
]
########

def GenerateFloorsJSON(minimun_floors, maximum_floors, modules, can_concat_modules=false):
    
    result_tower_blueprint = list()
    building_stories = random.randint(minimun_floors, maximum_floors)
    
    #Defaulting Init of first floor
    first_floor = {
        module: modules[random.randint(minimun_floors, maximum_floors)],
        floor_level: 0
    }
    
    result_tower_blueprint.append(first_floor)
    
    
    prev_floor_module = result_tower_blueprint[0]

    for i in range(1, building_stories+1):
        new_floor = {
            module: modules[random.randint(minimun_floors, maximum_floors)],
            floor_level: i
        }
        while (new_floor.module == prev_floor_module):
            new_floor.module = modules[random.randint(minimun_floors, maximum_floors)]
        result_tower_blueprint.append(new_module)

    return result_tower_blueprint

def stacKModules(building_floors_blueprint, module_rules):
    
    height_pos = module_rules.height/2
    
    for i, module in enumerate(building_floors_blueprint):
        module_instance = cmds.instance(module)[0]
        cmds.xform(module_instance, worldSpace=True, translation=(0, 0, 0))
        
    
