import bpy
from bpy.types import Object, PropertyGroup, Panel


class Demo_enum_floatarray(PropertyGroup):
    my_enum: bpy.props.EnumProperty(
        name="Color",
        items=[
            ('RED', 'Red', 'it is red'),
            ('GREEN', 'Green', 'it is green'),
            ('YELLOW', 'Yellow', 'it is yellow'),
        ], # type: ignore
        default='RED'
    )

    my_float_array: bpy.props.FloatVectorProperty(name='float', size = 3, subtype='XYZ') # type: ignore


class MYCUSTOMPANEL_PT_Operations(Panel):
    bl_label = 'MyCustomPanel'
    bl_space_type = 'VIEW_3D' # display in 3D Viewport
    bl_region_type = 'UI' # display in sidebar(call it with press 'N')
    bl_category = 'MyCustomPanel' # display the label on sidebar

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        # show the enum, float array inside the object's PointerProperty
        if obj and obj.select_get():
            for prop_name in ['my_enum', 'my_float_array']:
                layout.prop(obj.my_property, prop_name)
        else:
            layout.label(text='pls make an object active')


def register():
    bpy.utils.register_class(MYCUSTOMPANEL_PT_Operations)
    bpy.utils.register_class(Demo_enum_floatarray)

    Object.my_property = bpy.props.PointerProperty(type=Demo_enum_floatarray)


def unregister():
    del Object.my_property

    bpy.utils.unregister_class(MYCUSTOMPANEL_PT_Operations)
    bpy.utils.unregister_class(Demo_enum_floatarray)


def main():
    register()
    # unregister()

  
main()



