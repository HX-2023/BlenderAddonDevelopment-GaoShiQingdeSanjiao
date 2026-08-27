import bpy
from bpy.types import Object, PropertyGroup, Panel
from bpy.props import StringProperty, IntProperty, BoolProperty, CollectionProperty


class Demo(PropertyGroup):
    name: StringProperty(name='name_id', default='') # type: ignore
    age: IntProperty(name='age_id', default=3) # type: ignore
    isfemale: BoolProperty(name='isfemale_id', default=True) # type: ignore

bpy.utils.register_class(Demo)
Object.custom_prop = CollectionProperty(type=Demo)

obj = bpy.data.objects[1]
collection_prop = obj.custom_prop.add()

collection_prop.name = 'Steven'
collection_prop.age = 17
collection_prop.isfemale = False

print(collection_prop.name, collection_prop.age, collection_prop.isfemale)


# bpy_prop_collection_idprop.add() # this is a function in Blender to add a new item to a collection


 
        
# for i, all_objects in enumerate(obj[0:len(obj)]):
#     obj.x = all_objects['name_id'][i]
#     obj.y = all_objects['age_id'][i]
#     obj.z = all_objects['isfemale_id'][i]
#     print(obj.x, obj.y, obj.z)