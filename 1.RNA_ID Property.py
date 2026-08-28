import bpy
from bpy.types import PropertyGroup, Panel, Object, Mesh, Scene


# RNA property
#bpy.types.Object.myInt = bpy.props.IntProperty(name='test', min=1, max=10, default=5)
#print(bpy.context.scene.objects['Cube'].myInt)
#print(bpy.data.objects['Cube'].myInt)
#del Object.myInt

#bpy.types.Mesh.myBool = bpy.props.BoolProperty(name='Boolean', default=False)
#print(bpy.data.meshes['Cube'].myBool)
#del Mesh.myBool

#bpy.types.Mesh.myFloat = bpy.props.FloatProperty(name='Float', min=-10, max=10, default=0.1)
#print(bpy.data.meshes['Cube'].myFloat)
#del Mesh.myFloat

#bpy.types.Scene.myString = bpy.props.StringProperty(name='string', default='Hello Xworld', maxlen=30)
#print(bpy.data.scenes['Scene'].myString)
#del Scene.myString


# ID property:object
bpy.data.objects['Cube']['idInt'] = 1
#print(bpy.data.objects['Cube']['idInt'], type(bpy.data.objects['Cube']['idInt']))
bpy.data.objects['Cube']['idFloat'] = 1.5
#print(bpy.data.objects['Cube']['idFloat'], type(bpy.data.objects['Cube']['idFloat']))
bpy.data.objects['Cube']['idString'] = 'Hello Xworld'
#print(bpy.data.objects['Cube']['idString'], type(bpy.data.objects['Cube']['idString']))

# ID property:data
bpy.context.object.data['myFloat'] = 0.1
bpy.context.object.data['myBool'] = True


# ID property:scene
bpy.context.scene.objects.data['myString'] = 'Hello Xworld'

# remove ID property
#del bpy.context.object['idInt'] # equal to: bpy.data.objects['Cube']['indInt']
#del bpy.context.object['idFloat'] # equal to: bpy.data.objects['Cube']['inFloat']
#del bpy.context.object['idString'] # equal to: bpy.data.objects['Cube']['indString']
#del bpy.context.object.data['myFloat']
#del bpy.context.object.data['myBool']
#del bpy.context.scene.objects.data['myString']


class ObjectProperties(PropertyGroup):
    # Object.myInt = bpy.props.IntProperty(name='Intest', min=1, max=10, default=5)
    myInt: bpy.props.IntProperty(name='Intest', min=1, max=10, default=5) # type: ignore
    # Object.myFloat = bpy.props.FloatProperty(name='Floatest', min=1, max=10, default=0.1)
    myFloat: bpy.props.FloatProperty(name='Floatest', min=1.0, max=10.0, default=0.1) # type: ignore
    # Object.myString = bpy.props.StringProperty(name='Strest', default='Hello Xworld!', maxlen=30)
    myString: bpy.props.StringProperty(name='Strest', default='Hello Xworld!', maxlen=30) # type: ignore
    # Object.myBoolean = bpy.props.BoolProperty(name='Boolest', default=True)
    myBool: bpy.props.BoolProperty(name='Boolest', default=True) # type: ignore
 

class MeshProperties(PropertyGroup):
    MeshInt: bpy.props.IntProperty(name='MeshIntest', min=1, max=10, default=5) # type: ignore
    MeshFloat: bpy.props.FloatProperty(name='MeshFloatest', min=1.0, max=10.0, default=0.1) # type: ignore
    MeshString: bpy.props.StringProperty(name='MeshStrest', default='Hello Blender', maxlen=30) # type: ignore
    MeshBool: bpy.props.BoolProperty(name='MeshBoolest', default=False) # type: ignore
    
    
class SceneProperties(PropertyGroup):
    SceneString: bpy.props.StringProperty(name='SceneStrest', default='Hello Xworld', maxlen=30) # type: ignore
    SceneBool: bpy.props.BoolProperty(name='SceneBoolest', default=True) # type: ignore
    

class MYCUSTOMPANEL_PT_Operations(Panel):
    bl_label = 'MyCustomPanel'
    bl_space_type = 'VIEW_3D' # display in 3D Viewport
    bl_region_type = 'UI' # display in sidebar(call it with press 'N')
    bl_category = 'MyCustomPanel' # display the label on sidebar
    #bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object # not bpy.context.object, that's global variable, but context is local variable. context.object=context.active_object
        mesh = context.object.data
        scene = context.scene.objects.data
        
        if obj and obj.select_get():
            for obj_props_name in ['myInt', 'myFloat', 'myString', 'myBool']:
                layout.prop(obj.my_props, obj_props_name)
        else:
            layout.label(text='pls make an object active')
        
        if mesh:
            for mesh_props_name in ['MeshInt', 'MeshFloat', 'MeshString', 'MeshBool']:
                layout.prop(mesh.my_props, mesh_props_name)
                
        if scene:
            for scene_props_name in ['SceneString', 'SceneBool']:
                layout.prop(scene.my_props, scene_props_name)
                

def register():
    bpy.utils.register_class(MYCUSTOMPANEL_PT_Operations)
    bpy.utils.register_class(ObjectProperties)
    bpy.utils.register_class(MeshProperties)
    bpy.utils.register_class(SceneProperties)
    print('Add-on launched')
    
    Object.my_props = bpy.props.PointerProperty(type=ObjectProperties)
    Mesh.my_props = bpy.props.PointerProperty(type=MeshProperties)
    Scene.my_props = bpy.props.PointerProperty(type=SceneProperties)
    

def unregister():
    del Object.my_props
    del Mesh.my_props
    del Scene.my_props
            
    bpy.utils.unregister_class(MYCUSTOMPANEL_PT_Operations)
    bpy.utils.unregister_class(ObjectProperties)
    bpy.utils.unregister_class(MeshProperties) 
    bpy.utils.unregister_class(SceneProperties)
    print('Add-on disable')
      
    
def main():
    register()
    #unregister()
    
    print(Panel.bl_rna.properties['bl_space_type'].enum_items.keys()) # ['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']
    
    print(type(MeshProperties)) # <class '_bpy_types._RNAMetaPropGroup'>
    
    for attr_name, attribute in MeshProperties.__annotations__.items(): # __annotations__, display type notions
        print(attr_name, attribute)
    # MeshInt <_PropertyDeferred, <built-in function IntProperty>, {'name': 'MeshIntest', 'min': 1, 'max': 10, 'default': 5, 'attr': 'MeshInt'}>
    # MeshFloat <_PropertyDeferred, <built-in function FloatProperty>, {'name': 'MeshFloatest', 'min': 1, 'max': 10, 'default': 0.1, 'attr': 'MeshFloat'}>
    # MeshString <_PropertyDeferred, <built-in function StringProperty>, {'name': 'MeshStrest', 'default': 'Hello Blender', 'maxlen': 30, 'attr': 'MeshString'}>
    # MeshBool <_PropertyDeferred, <built-in function BoolProperty>, {'name': 'MeshBoolest', 'default': False, 'attr': 'MeshBool'}>


main()