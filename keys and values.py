from multiprocessing import context

import bpy
from bpy.types import Object, PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty, CollectionProperty


class Demo(PropertyGroup):
    nickname: StringProperty(default='') # type: ignore
    age: IntProperty(default=3) # type: ignore
    isfemale: BoolProperty(default=True) # type: ignore


class Demo_1():
    def add_func(self, data):
        all_objects = {
        'nickname': ['Susan', 'Tom'],
        'age': [6, 9],
        'isfemale': [True, False]
        }
        obj = data.objects

        for obj in obj.prop:
            for i, obj in enumerate(obj[0:len(obj)]):
                obj.prop.nickname = all_objects['nickname'][i]
                obj.prop.age = all_objects['age'][i]
                obj.prop.isfemale = all_objects['isfemale'][i]
                print(obj.prop.add(obj.prop.nickname, obj.prop.age, obj.prop.isfemale))


def register():
    bpy.utils.register_class(Demo)
    bpy.utils.register_class(Demo_1)
    Object.prop = CollectionProperty(type=Demo)

def unregister():
    del Object.prop
    bpy.utils.unregister_class(Demo)
    bpy.utils.unregister_class(Demo_1)


def main():
    register
    # unregister()


main()