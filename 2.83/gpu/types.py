import sys
import typing
import bpy.types
import mathutils


class GPUBatch:
    ''' Reusable container for drawable geometry. :arg type: One of these primitive types: { POINTS , LINES , TRIS , LINE_STRIP , LINE_LOOP , TRI_STRIP , TRI_FAN , LINES_ADJ , TRIS_ADJ , LINE_STRIP_ADJ } :type type: str :arg buf: Vertex buffer containing all or some of the attributes required for drawing. :type buf: gpu.types.GPUVertBuf :arg elem: An optional index buffer. :type elem: gpu.types.GPUIndexBuf
    '''

    def draw(self, program: 'GPUShader' = None):
        ''' Run the drawing program with the parameters assigned to the batch.

        :param program: 
        :type program: 'GPUShader'
        '''
        pass

    def program_set(self, program: 'GPUShader'):
        ''' Assign a shader to this batch that will be used for drawing when not overwritten later. Note: This method has to be called in the draw context that the batch will be drawn in. This function does not need to be called when you always set the shader when calling batch.draw .

        :param program: 
        :type program: 'GPUShader'
        '''
        pass

    def vertbuf_add(self, buf: 'GPUVertBuf'):
        ''' Add another vertex buffer to the Batch. It is not possible to add more vertices to the batch using this method. Instead it can be used to add more attributes to the existing vertices. A good use case would be when you have a separate vertex buffer for vertex positions and vertex normals. Current a batch can have at most 6 vertex buffers.

        :param buf: 
        :type buf: 'GPUVertBuf'
        '''
        pass


class GPUIndexBuf:
    ''' Contains an index buffer. :param type: One of these primitive types: { POINTS , LINES , TRIS , LINE_STRIP_ADJ } :type type: str :param seq: Indices this index buffer will contain. Whether a 1D or 2D sequence is required depends on the type. Optionally the sequence can support the buffer protocol. :type seq: 1D or 2D sequence
    '''

    pass


class GPUOffScreen:
    ''' This object gives access to off screen buffers. :arg width: Horizontal dimension of the buffer. :type width: int :arg height: Vertical dimension of the buffer. :type height: int :arg samples: OpenGL samples to use for MSAA or zero to disable. :type samples: int
    '''

    color_texture: int = None
    ''' OpenGL bindcode for the color texture.

    :type: int
    '''

    height: int = None
    ''' Height of the texture.

    :type: int
    '''

    width: int = None
    ''' Width of the texture.

    :type: int
    '''

    def bind(self, save: bool = True):
        ''' Bind the offscreen object. To make sure that the offscreen gets unbind whether an exception occurs or not, pack it into a with statement.

        :param save: Save the current OpenGL state, so that it can be restored when unbinding.
        :type save: bool
        '''
        pass

    def draw_view3d(
            self, scene: 'bpy.types.Scene', view_layer: 'bpy.types.ViewLayer',
            view3d: 'bpy.types.SpaceView3D', region: 'bpy.types.Region',
            view_matrix: 'mathutils.Matrix',
            projection_matrix: 'mathutils.Matrix'):
        ''' Draw the 3d viewport in the offscreen object.

        :param scene: Scene to draw.
        :type scene: 'bpy.types.Scene'
        :param view_layer: View layer to draw.
        :type view_layer: 'bpy.types.ViewLayer'
        :param view3d: 3D View to get the drawing settings from.
        :type view3d: 'bpy.types.SpaceView3D'
        :param region: Region of the 3D View (required as temporary draw target).
        :type region: 'bpy.types.Region'
        :param view_matrix: View Matrix (e.g. camera.matrix_world.inverted() ).
        :type view_matrix: 'mathutils.Matrix'
        :param projection_matrix: Projection Matrix (e.g. camera.calc_matrix_camera(...) ).
        :type projection_matrix: 'mathutils.Matrix'
        '''
        pass

    def free(self):
        ''' Free the offscreen object. The framebuffer, texture and render objects will no longer be accessible.

        '''
        pass

    def unbind(self, restore: bool = True):
        ''' Unbind the offscreen object.

        :param restore: Restore the OpenGL state, can only be used when the state has been saved before.
        :type restore: bool
        '''
        pass


class GPUShader:
    ''' GPUShader combines multiple GLSL shaders into a program used for drawing. It must contain a vertex and fragment shaders, with an optional geometry shader. The GLSL #version directive is automatically included at the top of shaders, and set to 330. Some preprocessor directives are automatically added according to the Operating System or availability: GPU_ATI , GPU_NVIDIA and GPU_INTEL . The following extensions are enabled by default if supported by the GPU: GL_ARB_texture_gather and GL_ARB_texture_query_lod . To debug shaders, use the --debug-gpu-shaders command line option to see full GLSL shader compilation and linking errors. For drawing user interface elements and gizmos, use fragOutput = blender_srgb_to_framebuffer_space(fragOutput) to transform the output sRGB colors to the framebuffer colorspace. :param vertexcode: Vertex shader code. :type vertexcode: str :param fragcode: Fragment shader code. :type value: str :param geocode: Geometry shader code. :type value: str :param libcode: Code with functions and presets to be shared between shaders. :type value: str :param defines: Preprocessor directives. :type value: str
    '''

    program: int = None
    ''' The name of the program object for use by the OpenGL API (read-only).

    :type: int
    '''

    def attr_from_name(self, name: str) -> int:
        ''' Get attribute location by name.

        :param name: 
        :type name: str
        :rtype: int
        :return: The location of an attribute variable.
        '''
        pass

    def bind(self):
        ''' Bind the shader object. Required to be able to change uniforms of this shader.

        '''
        pass

    def calc_format(self) -> 'GPUVertFormat':
        ''' Build a new format based on the attributes of the shader.

        :rtype: 'GPUVertFormat'
        :return: vertex attribute format for the shader
        '''
        pass

    def uniform_block_from_name(self, name: str) -> int:
        ''' Get uniform block location by name.

        :param name: 
        :type name: str
        :rtype: int
        :return: The location of the uniform block variable.
        '''
        pass

    def uniform_bool(self, name: str, seq: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: 
        :type name: str
        :param seq: 
        :type seq: list
        '''
        pass

    def uniform_float(self, name: str, value: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: 
        :type name: str
        :param value: 
        :type value: list
        '''
        pass

    def uniform_from_name(self, name: str) -> int:
        ''' Get uniform location by name.

        :param name: 
        :type name: str
        :rtype: int
        :return: Location of the uniform variable.
        '''
        pass

    def uniform_int(self, name: str, seq: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: 
        :type name: str
        :param seq: 
        :type seq: list
        '''
        pass

    def uniform_vector_float(self, location: int, buffer: list, length: int,
                             count: int):
        ''' Set the buffer to fill the uniform.

        :param location: 
        :type location: int
        :param buffer: 
        :type buffer: list
        :param length: 
        :type length: int
        :param count: 
        :type count: int
        '''
        pass

    def uniform_vector_int(self, location, buffer, length, count):
        ''' See GPUShader.uniform_vector_float(...) description.

        '''
        pass


class GPUVertBuf:
    ''' Contains a VBO. :param len: Amount of vertices that will fit into this buffer. :type type: int :param format: Vertex format. :type buf: gpu.types.GPUVertFormat
    '''

    def attr_fill(self, id: typing.Union[str, int], data: list):
        ''' Insert data into the buffer for a single attribute.

        :param id: 
        :type id: typing.Union[str, int]
        :param data: 
        :type data: list
        '''
        pass


class GPUVertFormat:
    ''' This object contains information about the structure of a vertex buffer.
    '''

    def attr_add(self, id: str, comp_type: str, len: int, fetch_mode: str):
        ''' Add a new attribute to the format.

        :param id: 
        :type id: str
        :param comp_type: 
        :type comp_type: str
        :param len: 
        :type len: int
        :param fetch_mode: 
        :type fetch_mode: str
        '''
        pass
