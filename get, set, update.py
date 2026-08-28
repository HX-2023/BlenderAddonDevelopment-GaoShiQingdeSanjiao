import bpy
from bpy.types import Scene, Object
from bpy.props import FloatProperty, IntProperty


def get_float(self):
    return self.get('testprop', 0.3)


def set_float(self, value):
    self['testprop'] = value
    print(value)


Scene.test_float = FloatProperty(get=get_float, set=set_float)

print(bpy.context.scene.test_float)
bpy.context.scene.test_float = 7
print(bpy.context.scene.test_float)


def get_int(self):
    return self['value'] * 10


def set_int(self, value):
    self['value'] = value
    print('set:', value)


Object.test_int = IntProperty(get=get_int, set=set_int)

bpy.data.objects[1].test_int = 3
print(bpy.data.objects[1].test_int)