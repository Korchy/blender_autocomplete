import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


class Buffer:
    ''' For Python access to GPU functions requiring a pointer. :arg format: Format type to interpret the buffer. Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`. :type format: str :arg dimensions: Array describing the dimensions. :type dimensions: int :arg data: Optional data array. :type data: sequence return the buffer as a list
    '''

    dimensions = None
    ''' Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.'''


class GPUBatch:
    ''' Reusable container for drawable geometry. :arg type: The primitive type of geometry to be drawn. Possible values are `POINTS`, `LINES`, `TRIS`, `LINE_STRIP`, `LINE_LOOP`, `TRI_STRIP`, `TRI_FAN`, `LINES_ADJ`, `TRIS_ADJ` and `LINE_STRIP_ADJ`. :type type: str :arg buf: Vertex buffer containing all or some of the attributes required for drawing. :type buf: `gpu.types.GPUVertBuf` :arg elem: An optional index buffer. :type elem: `gpu.types.GPUIndexBuf`
    '''

    def draw(self, program: 'GPUShader' = None):
        ''' Run the drawing program with the parameters assigned to the batch.

        :param program: Program that performs the drawing operations. If ``None`` is passed, the last program set to this batch will run.
        :type program: 'GPUShader'
        '''
        pass

    def program_set(self, program: 'GPUShader'):
        ''' Assign a shader to this batch that will be used for drawing when not overwritten later. Note: This method has to be called in the draw context that the batch will be drawn in. This function does not need to be called when you always set the shader when calling :meth:`gpu.types.GPUBatch.draw`.

        :param program: The program/shader the batch will use in future draw calls.
        :type program: 'GPUShader'
        '''
        pass

    def vertbuf_add(self, buf: 'GPUVertBuf'):
        ''' Add another vertex buffer to the Batch. It is not possible to add more vertices to the batch using this method. Instead it can be used to add more attributes to the existing vertices. A good use case would be when you have a separate vertex buffer for vertex positions and vertex normals. Current a batch can have at most 16 vertex buffers.

        :param buf: The vertex buffer that will be added to the batch.
        :type buf: 'GPUVertBuf'
        '''
        pass


class GPUFrameBuffer:
    ''' This object gives access to framebuffer functionalities. When a 'layer' is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer. For cube map textures, layer is translated into a cube map face. :arg depth_slot: GPUTexture to attach or a `dict` containing keywords: 'texture', 'layer' and 'mip'. :type depth_slot: `gpu.types.GPUTexture`, dict or Nonetype :arg color_slots: Tuple where each item can be a GPUTexture or a `dict` containing keywords: 'texture', 'layer' and 'mip'. :type color_slots: tuple or Nonetype
    '''

    is_bound = None
    ''' Checks if this is the active framebuffer in the context.'''

    @staticmethod
    def bind():
        ''' Context manager to ensure balanced bind calls, even in the case of an error.

        '''
        pass

    def clear(self,
              color: typing.List = None,
              depth: float = None,
              stencil: int = None):
        ''' Fill color, depth and stencil textures with specific value. Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.

        :param color: float sequence each representing ``(r, g, b, a)``.
        :type color: typing.List
        :param depth: depth value.
        :type depth: float
        :param stencil: stencil value.
        :type stencil: int
        '''
        pass

    @staticmethod
    def read_color(x: int,
                   y: int,
                   xsize: int,
                   ysize: int,
                   channels: int,
                   slot: int,
                   format: str,
                   data: 'Buffer' = 'data') -> 'Buffer':
        ''' Read a block of pixels from the frame buffer.

        :param x: Lower left corner of a rectangular block of pixels.
        :type x: int
        :param y: Lower left corner of a rectangular block of pixels.
        :type y: int
        :param xsize: Dimensions of the pixel rectangle.
        :type xsize: int
        :param ysize: Dimensions of the pixel rectangle.
        :type ysize: int
        :param channels: Number of components to read.
        :type channels: int
        :param slot: The framebuffer slot to read data from.
        :type slot: int
        :param format: The format that describes the content of a single channel. Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`.
        :type format: str
        :param data: Optional Buffer object to fill with the pixels values.
        :type data: 'Buffer'
        :rtype: 'Buffer'
        :return: The Buffer with the read pixels.
        '''
        pass

    @staticmethod
    def read_depth(x: int,
                   y: int,
                   xsize: int,
                   ysize: int,
                   data: 'Buffer' = 'data') -> 'Buffer':
        ''' Read a pixel depth block from the frame buffer.

        :param x: Lower left corner of a rectangular block of pixels.
        :type x: int
        :param y: Lower left corner of a rectangular block of pixels.
        :type y: int
        :param xsize: Dimensions of the pixel rectangle.
        :type xsize: int
        :param ysize: Dimensions of the pixel rectangle.
        :type ysize: int
        :param data: Optional Buffer object to fill with the pixels values.
        :type data: 'Buffer'
        :rtype: 'Buffer'
        :return: The Buffer with the read pixels.
        '''
        pass

    @staticmethod
    def viewport_get():
        ''' Returns position and dimension to current viewport.

        '''
        pass

    @staticmethod
    def viewport_set(x: int, y: int, xsize: int, ysize: int):
        ''' Set the viewport for this framebuffer object. Note: The viewport state is not saved upon framebuffer rebind.

        :param x: lower left corner of the viewport_set rectangle, in pixels.
        :type x: int
        :param y: lower left corner of the viewport_set rectangle, in pixels.
        :type y: int
        :param xsize: width and height of the viewport_set.
        :type xsize: int
        :param ysize: width and height of the viewport_set.
        :type ysize: int
        '''
        pass


class GPUIndexBuf:
    ''' Contains an index buffer. :arg type: The primitive type this index buffer is composed of. Possible values are `POINTS`, `LINES`, `TRIS` and `LINE_STRIP_ADJ`. :type type: str :arg seq: Indices this index buffer will contain. Whether a 1D or 2D sequence is required depends on the type. Optionally the sequence can support the buffer protocol. :type seq: 1D or 2D sequence
    '''

    pass


class GPUOffScreen:
    ''' This object gives access to off screen buffers. :arg width: Horizontal dimension of the buffer. :type width: int :arg height: Vertical dimension of the buffer. :type height: int :arg format: Internal data format inside GPU memory for color attachment texture. Possible values are: `RGBA8`, `RGBA16`, `RGBA16F`, `RGBA32F`, :type format: str
    '''

    color_texture: int = None
    ''' OpenGL bindcode for the color texture.

    :type: int
    '''

    height: int = None
    ''' Height of the texture.

    :type: int
    '''

    texture_color: 'GPUTexture' = None
    ''' The color texture attached.

    :type: 'GPUTexture'
    '''

    width: int = None
    ''' Width of the texture.

    :type: int
    '''

    @staticmethod
    def bind():
        ''' Context manager to ensure balanced bind calls, even in the case of an error.

        '''
        pass

    def draw_view3d(self,
                    scene: 'bpy.types.Scene',
                    view_layer: 'bpy.types.ViewLayer',
                    view3d: 'bpy.types.SpaceView3D',
                    region: 'bpy.types.Region',
                    view_matrix: typing.
                    Union[typing.Sequence[float], 'mathutils.Matrix'],
                    projection_matrix: typing.
                    Union[typing.Sequence[float], 'mathutils.Matrix'],
                    do_color_management: bool = False):
        ''' Draw the 3d viewport in the offscreen object.

        :param scene: Scene to draw.
        :type scene: 'bpy.types.Scene'
        :param view_layer: View layer to draw.
        :type view_layer: 'bpy.types.ViewLayer'
        :param view3d: 3D View to get the drawing settings from.
        :type view3d: 'bpy.types.SpaceView3D'
        :param region: Region of the 3D View (required as temporary draw target).
        :type region: 'bpy.types.Region'
        :param view_matrix: View Matrix (e.g. ``camera.matrix_world.inverted()``).
        :type view_matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
        :param projection_matrix: Projection Matrix (e.g. ``camera.calc_matrix_camera(...)``).
        :type projection_matrix: typing.Union[typing.Sequence[float], 'mathutils.Matrix']
        :param do_color_management: Color manage the output.
        :type do_color_management: bool
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
    ''' GPUShader combines multiple GLSL shaders into a program used for drawing. It must contain at least a vertex and fragment shaders. The GLSL ``#version`` directive is automatically included at the top of shaders, and set to 330. Some preprocessor directives are automatically added according to the Operating System or availability: ``GPU_ATI``, ``GPU_NVIDIA`` and ``GPU_INTEL``. The following extensions are enabled by default if supported by the GPU: ``GL_ARB_texture_gather``, ``GL_ARB_texture_cube_map_array`` and ``GL_ARB_shader_draw_parameters``. For drawing user interface elements and gizmos, use ``fragOutput = blender_srgb_to_framebuffer_space(fragOutput)`` to transform the output sRGB colors to the frame-buffer color-space. :arg vertexcode: Vertex shader code. :type vertexcode: str :arg fragcode: Fragment shader code. :type value: str :arg geocode: Geometry shader code. :type value: str :arg libcode: Code with functions and presets to be shared between shaders. :type value: str :arg defines: Preprocessor directives. :type value: str :arg name: Name of shader code, for debugging purposes. :type value: str
    '''

    name: str = None
    ''' The name of the shader object for debugging purposes (read-only).

    :type: str
    '''

    program: int = None
    ''' The name of the program object for use by the OpenGL API (read-only).

    :type: int
    '''

    def attr_from_name(self, name: str) -> int:
        ''' Get attribute location by name.

        :param name: The name of the attribute variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: The location of an attribute variable.
        '''
        pass

    def attrs_info_get(self) -> typing.Tuple:
        ''' Information about the attributes used in the Shader.

        :rtype: typing.Tuple
        :return: tuples containing information about the attributes in order (name, type)
        '''
        pass

    def bind(self):
        ''' Bind the shader object. Required to be able to change uniforms of this shader.

        '''
        pass

    def format_calc(self) -> 'GPUVertFormat':
        ''' Build a new format based on the attributes of the shader.

        :rtype: 'GPUVertFormat'
        :return: vertex attribute format for the shader
        '''
        pass

    def uniform_block(self, name: str, ubo: typing.Any):
        ''' Specify the value of an uniform buffer object variable for the current GPUShader.

        :param name: name of the uniform variable whose UBO is to be specified.
        :type name: str
        :param texture: 
        :type texture: 'GPUUniformBuf'
        :param ubo:  Uniform Buffer to attach.
        :type ubo: typing.Any
        '''
        pass

    def uniform_block_from_name(self, name: str) -> int:
        ''' Get uniform block location by name.

        :param name: Name of the uniform block variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: The location of the uniform block variable.
        '''
        pass

    def uniform_bool(self, name: str, value: bool):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param value: Value that will be used to update the specified uniform variable.
        :type value: bool
        '''
        pass

    def uniform_float(self, name: str, value: typing.List):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param value: Value that will be used to update the specified uniform variable.
        :type value: typing.List
        '''
        pass

    def uniform_from_name(self, name: str) -> int:
        ''' Get uniform location by name.

        :param name: Name of the uniform variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: Location of the uniform variable.
        '''
        pass

    def uniform_int(self, name: str, seq: typing.List):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: name of the uniform variable whose value is to be changed.
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable.
        :type seq: typing.List
        '''
        pass

    def uniform_sampler(self, name: str, texture: 'GPUTexture'):
        ''' Specify the value of a texture uniform variable for the current GPUShader.

        :param name: name of the uniform variable whose texture is to be specified.
        :type name: str
        :param texture: Texture to attach.
        :type texture: 'GPUTexture'
        '''
        pass

    def uniform_vector_float(self, location: int, buffer: typing.List[float],
                             length: int, count: int):
        ''' Set the buffer to fill the uniform.

        :param location: Location of the uniform variable to be modified.
        :type location: int
        :param buffer: The data that should be set. Can support the buffer protocol.
        :type buffer: typing.List[float]
        :param length: - 1: float - 2: vec2 or float[2] - 3: vec3 or float[3] - 4: vec4 or float[4] - 9: mat3 - 16: mat4
        :type length: int
        :param count: Specifies the number of elements, vector or matrices that are to be modified.
        :type count: int
        '''
        pass

    def uniform_vector_int(self, location, buffer, length, count):
        ''' See GPUShader.uniform_vector_float(...) description.

        '''
        pass


class GPUShaderCreateInfo:
    ''' Stores and describes types and variables that are used in shader sources.
    '''

    def define(self, name, value):
        ''' Add a preprocessing define directive. In GLSL it would be something like:

        '''
        pass

    def fragment_out(self,
                     slot: int,
                     type: str,
                     name: str,
                     blend: str = 'NONE'):
        ''' Specify a fragment output corresponding to a framebuffer target slot.

        :param slot: The attribute index.
        :type slot: int
        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: Name of the attribute.
        :type name: str
        :param blend: Dual Source Blending Index. It can be 'NONE', 'SRC_0' or 'SRC_1'.
        :type blend: str
        '''
        pass

    def fragment_source(self, source: str):
        ''' Fragment shader source code written in GLSL. Example:

        :param source: The fragment shader source code.
        :type source: str
        '''
        pass

    def push_constant(self, type: str, name: str, size: typing.Any = 0):
        ''' Specify a global access constant.

        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: Name of the constant.
        :type name: str
        :param size: If not zero, indicates that the constant is an array with the specified size.
        :type size: typing.Any
        '''
        pass

    def sampler(self, slot: int, type: str, name: str):
        ''' Specify an image texture sampler.

        :param slot: The image texture sampler index.
        :type slot: int
        :param type: - ``FLOAT_BUFFER`` - ``FLOAT_1D`` - ``FLOAT_1D_ARRAY`` - ``FLOAT_2D`` - ``FLOAT_2D_ARRAY`` - ``FLOAT_3D`` - ``FLOAT_CUBE`` - ``FLOAT_CUBE_ARRAY`` - ``INT_BUFFER`` - ``INT_1D`` - ``INT_1D_ARRAY`` - ``INT_2D`` - ``INT_2D_ARRAY`` - ``INT_3D`` - ``INT_CUBE`` - ``INT_CUBE_ARRAY`` - ``UINT_BUFFER`` - ``UINT_1D`` - ``UINT_1D_ARRAY`` - ``UINT_2D`` - ``UINT_2D_ARRAY`` - ``UINT_3D`` - ``UINT_CUBE`` - ``UINT_CUBE_ARRAY`` - ``SHADOW_2D`` - ``SHADOW_2D_ARRAY`` - ``SHADOW_CUBE`` - ``SHADOW_CUBE_ARRAY`` - ``DEPTH_2D`` - ``DEPTH_2D_ARRAY`` - ``DEPTH_CUBE`` - ``DEPTH_CUBE_ARRAY``
        :type type: str
        :param name: The image texture sampler name.
        :type name: str
        '''
        pass

    def typedef_source(self, source):
        ''' Source code included before resource declaration. Useful for defining structs used by Uniform Buffers. Example:

        '''
        pass

    def uniform_buf(self, slot: int, type_name: str, name: str):
        ''' Specify a uniform variable whose type can be one of those declared in `typedef_source`.

        :param slot: The uniform variable index.
        :type slot: int
        :param type_name: `gpu.types.GPUShaderCreateInfo.typedef_source`.
        :type type_name: str
        :param name: The uniform variable name.
        :type name: str
        '''
        pass

    def vertex_in(self, slot: int, type: str, name: str):
        ''' Add a vertex shader input attribute.

        :param slot: The attribute index.
        :type slot: int
        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: name of the attribute.
        :type name: str
        '''
        pass

    def vertex_out(self, interface: 'GPUStageInterfaceInfo'):
        ''' Add a vertex shader output interface block.

        :param interface: Object describing the block.
        :type interface: 'GPUStageInterfaceInfo'
        '''
        pass

    def vertex_source(self, source: str):
        ''' Vertex shader source code written in GLSL. Example:

        :param source: The vertex shader source code.
        :type source: str
        '''
        pass


class GPUStageInterfaceInfo:
    ''' List of varyings between shader stages. :arg name: Name of the interface block. :type value: str
    '''

    name: str = None
    ''' Name of the interface block.

    :type: str
    '''

    def flat(self, type: str, name: str):
        ''' Add an attribute with qualifier of type `flat` to the interface block.

        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: name of the attribute.
        :type name: str
        '''
        pass

    def no_perspective(self, type: str, name: str):
        ''' Add an attribute with qualifier of type `no_perspective` to the interface block.

        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: name of the attribute.
        :type name: str
        '''
        pass

    def smooth(self, type: str, name: str):
        ''' Add an attribute with qualifier of type `smooth` to the interface block.

        :param type: - ``FLOAT`` - ``VEC2`` - ``VEC3`` - ``VEC4`` - ``MAT3`` - ``MAT4`` - ``UINT`` - ``UVEC2`` - ``UVEC3`` - ``UVEC4`` - ``INT`` - ``IVEC2`` - ``IVEC3`` - ``IVEC4`` - ``BOOL``
        :type type: str
        :param name: name of the attribute.
        :type name: str
        '''
        pass


class GPUTexture:
    ''' This object gives access to off GPU textures. :arg size: Dimensions of the texture 1D, 2D, 3D or cubemap. :type size: tuple or int :arg layers: Number of layers in texture array or number of cubemaps in cubemap array :type layers: int :arg is_cubemap: Indicates the creation of a cubemap texture. :type is_cubemap: int :arg format: Internal data format inside GPU memory. Possible values are: `RGBA8UI`, `RGBA8I`, `RGBA8`, `RGBA32UI`, `RGBA32I`, `RGBA32F`, `RGBA16UI`, `RGBA16I`, `RGBA16F`, `RGBA16`, `RG8UI`, `RG8I`, `RG8`, `RG32UI`, `RG32I`, `RG32F`, `RG16UI`, `RG16I`, `RG16F`, `RG16`, `R8UI`, `R8I`, `R8`, `R32UI`, `R32I`, `R32F`, `R16UI`, `R16I`, `R16F`, `R16`, `R11F_G11F_B10F`, `DEPTH32F_STENCIL8`, `DEPTH24_STENCIL8`, `SRGB8_A8`, `RGB16F`, `SRGB8_A8_DXT1`, `SRGB8_A8_DXT3`, `SRGB8_A8_DXT5`, `RGBA8_DXT1`, `RGBA8_DXT3`, `RGBA8_DXT5`, `DEPTH_COMPONENT32F`, `DEPTH_COMPONENT24`, `DEPTH_COMPONENT16`, :type format: str :arg data: Buffer object to fill the texture. :type data: `gpu.types.Buffer`
    '''

    format: str = None
    ''' Format of the texture.

    :type: str
    '''

    height: int = None
    ''' Height of the texture.

    :type: int
    '''

    width: int = None
    ''' Width of the texture.

    :type: int
    '''

    def clear(self,
              format: str = 'FLOAT',
              value: typing.List = (0.0, 0.0, 0.0, 1.0)):
        ''' Fill texture with specific value.

        :param format: The format that describes the content of a single item. Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`.
        :type format: str
        :param value: sequence each representing the value to fill.
        :type value: typing.List
        '''
        pass

    def read(self):
        ''' Creates a buffer with the value of all pixels.

        '''
        pass


class GPUUniformBuf:
    ''' This object gives access to off uniform buffers. :arg data: Data to fill the buffer. :type data: object exposing buffer interface
    '''

    def update(self, data):
        ''' Update the data of the uniform buffer object.

        '''
        pass


class GPUVertBuf:
    ''' Contains a VBO. :arg format: Vertex format. :type format: `gpu.types.GPUVertFormat` :arg len: Amount of vertices that will fit into this buffer. :type len: int
    '''

    def attr_fill(self, id: typing.Union[int, str], data: typing.List[float]):
        ''' Insert data into the buffer for a single attribute.

        :param id: Either the name or the id of the attribute.
        :type id: typing.Union[int, str]
        :param data: Sequence of data that should be stored in the buffer
        :type data: typing.List[float]
        '''
        pass


class GPUVertFormat:
    ''' This object contains information about the structure of a vertex buffer.
    '''

    def attr_add(self, id: str, comp_type: str, len: int, fetch_mode: str):
        ''' Add a new attribute to the format.

        :param id: Name the attribute. Often `position`, `normal`, ...
        :type id: str
        :param comp_type: The data type that will be used store the value in memory. Possible values are `I8`, `U8`, `I16`, `U16`, `I32`, `U32`, `F32` and `I10`.
        :type comp_type: str
        :param len: How many individual values the attribute consists of (e.g. 2 for uv coordinates).
        :type len: int
        :param fetch_mode: How values from memory will be converted when used in the shader. This is mainly useful for memory optimizations when you want to store values with reduced precision. E.g. you can store a float in only 1 byte but it will be converted to a normal 4 byte float when used. Possible values are `FLOAT`, `INT`, `INT_TO_FLOAT_UNIT` and `INT_TO_FLOAT`.
        :type fetch_mode: str
        '''
        pass
