import typing
import collections.abc
import bpy.types
import mathutils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class Buffer:
    """For Python access to GPU functions requiring a pointer.return the buffer as a list"""

    dimensions: typing.Any
    """ Undocumented, consider contributing."""

class GPUBatch:
    """Reusable container for drawable geometry."""

    def draw(self, program: GPUShader = None):
        """Run the drawing program with the parameters assigned to the batch.

                :param program: Program that performs the drawing operations.
        If None is passed, the last program set to this batch will run.
                :type program: GPUShader
        """
        ...

    def draw_instanced(
        self, program: GPUShader, *, instance_start: int = 0, instance_count: int = 0
    ):
        """Draw multiple instances of the drawing program with the parameters assigned
        to the batch. In the vertex shader, gl_InstanceID will contain the instance
        number being drawn.

                :param program: Program that performs the drawing operations.
                :type program: GPUShader
                :param instance_start: Number of the first instance to draw.
                :type instance_start: int
                :param instance_count: Number of instances to draw. When not provided or set to 0
        the number of instances will be determined by the number of rows in the first
        vertex buffer.
                :type instance_count: int
        """
        ...

    def draw_range(
        self, program: GPUShader, *, elem_start: int = 0, elem_count: int = 0
    ):
        """Run the drawing program with the parameters assigned to the batch. Only draw
        the elem_count elements of the index buffer starting at elem_start

                :param program: Program that performs the drawing operations.
                :type program: GPUShader
                :param elem_start: First index to draw. When not provided or set to 0 drawing
        will start from the first element of the index buffer.
                :type elem_start: int
                :param elem_count: Number of elements of the index buffer to draw. When not
        provided or set to 0 all elements from elem_start to the end of the
        index buffer will be drawn.
                :type elem_count: int
        """
        ...

    def program_set(self, program: GPUShader):
        """Assign a shader to this batch that will be used for drawing when not overwritten later.
        Note: This method has to be called in the draw context that the batch will be drawn in.
        This function does not need to be called when you always
        set the shader when calling `gpu.types.GPUBatch.draw`.

                :param program: The program/shader the batch will use in future draw calls.
                :type program: GPUShader
        """
        ...

    def vertbuf_add(self, buf: GPUVertBuf):
        """Add another vertex buffer to the Batch.
        It is not possible to add more vertices to the batch using this method.
        Instead it can be used to add more attributes to the existing vertices.
        A good use case would be when you have a separate
        vertex buffer for vertex positions and vertex normals.
        Current a batch can have at most 16 vertex buffers.

                :param buf: The vertex buffer that will be added to the batch.
                :type buf: GPUVertBuf
        """
        ...

class GPUFrameBuffer:
    """This object gives access to framebuffer functionalities.
    When a 'layer' is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer.
    For cube map textures, layer is translated into a cube map face.
    """

    is_bound: typing.Any
    """ Checks if this is the active framebuffer in the context."""

    def bind(self):
        """Context manager to ensure balanced bind calls, even in the case of an error."""
        ...

    def clear(self, color=None, depth: float = None, stencil: int = None):
        """Fill color, depth and stencil textures with specific value.
        Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.

                :param color: float sequence each representing (r, g, b, a).
                :param depth: depth value.
                :type depth: float
                :param stencil: stencil value.
                :type stencil: int
        """
        ...

    def read_color(
        self,
        x: int,
        y,
        xsize,
        ysize,
        channels: int,
        slot: int,
        format: str,
        data: Buffer | None = None,
    ) -> Buffer:
        """Read a block of pixels from the frame buffer.

                :param x: Lower left corner of a rectangular block of pixels.
                :type x: int
                :param y:
                :param xsize: Dimensions of the pixel rectangle.
                :param ysize:
                :param channels: Number of components to read.
                :type channels: int
                :param slot: The framebuffer slot to read data from.
                :type slot: int
                :param format: The format that describes the content of a single channel.
        Possible values are FLOAT, INT, UINT, UBYTE, UINT_24_8 and 10_11_11_REV.
                :type format: str
                :param data: Optional Buffer object to fill with the pixels values.
                :type data: Buffer | None
                :return: The Buffer with the read pixels.
                :rtype: Buffer
        """
        ...

    def read_depth(
        self, x: int, y, xsize: int, ysize, data: Buffer | None = None
    ) -> Buffer:
        """Read a pixel depth block from the frame buffer.

        :param x: Lower left corner of a rectangular block of pixels.
        :type x: int
        :param y:
        :param xsize: Dimensions of the pixel rectangle.
        :type xsize: int
        :param ysize:
        :param data: Optional Buffer object to fill with the pixels values.
        :type data: Buffer | None
        :return: The Buffer with the read pixels.
        :rtype: Buffer
        """
        ...

    def viewport_get(self):
        """Returns position and dimension to current viewport."""
        ...

    def viewport_set(self, x: int, y, xsize: int, ysize):
        """Set the viewport for this framebuffer object.
        Note: The viewport state is not saved upon framebuffer rebind.

                :param x: lower left corner of the viewport_set rectangle, in pixels.
                :type x: int
                :param y:
                :param xsize: width and height of the viewport_set.
                :type xsize: int
                :param ysize:
        """
        ...

class GPUIndexBuf:
    """Contains an index buffer."""

    ...

class GPUOffScreen:
    """This object gives access to off screen buffers."""

    color_texture: int
    """ OpenGL bindcode for the color texture.

    :type: int
    """

    height: int
    """ Height of the texture.

    :type: int
    """

    texture_color: GPUTexture
    """ The color texture attached.

    :type: GPUTexture
    """

    width: int
    """ Width of the texture.

    :type: int
    """

    def bind(self):
        """Context manager to ensure balanced bind calls, even in the case of an error."""
        ...

    def draw_view3d(
        self,
        scene: bpy.types.Scene,
        view_layer: bpy.types.ViewLayer,
        view3d: bpy.types.SpaceView3D,
        region: bpy.types.Region,
        view_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        projection_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        do_color_management: bool = False,
        draw_background: bool = True,
    ):
        """Draw the 3d viewport in the offscreen object.

        :param scene: Scene to draw.
        :type scene: bpy.types.Scene
        :param view_layer: View layer to draw.
        :type view_layer: bpy.types.ViewLayer
        :param view3d: 3D View to get the drawing settings from.
        :type view3d: bpy.types.SpaceView3D
        :param region: Region of the 3D View (required as temporary draw target).
        :type region: bpy.types.Region
        :param view_matrix: View Matrix (e.g. camera.matrix_world.inverted()).
        :type view_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
        :param projection_matrix: Projection Matrix (e.g. camera.calc_matrix_camera(...)).
        :type projection_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
        :param do_color_management: Color manage the output.
        :type do_color_management: bool
        :param draw_background: Draw background.
        :type draw_background: bool
        """
        ...

    def free(self):
        """Free the offscreen object.
        The framebuffer, texture and render objects will no longer be accessible.

        """
        ...

    def unbind(self, restore: bool = True):
        """Unbind the offscreen object.

        :param restore: Restore the OpenGL state, can only be used when the state has been saved before.
        :type restore: bool
        """
        ...

class GPUShader:
    """GPUShader combines multiple GLSL shaders into a program used for drawing.
    It must contain at least a vertex and fragment shaders.The GLSL #version directive is automatically included at the top of shaders,
    and set to 330. Some preprocessor directives are automatically added according to
    the Operating System or availability: GPU_ATI, GPU_NVIDIA and GPU_INTEL.The following extensions are enabled by default if supported by the GPU:
    GL_ARB_texture_gather, GL_ARB_texture_cube_map_array
    and GL_ARB_shader_draw_parameters.For drawing user interface elements and gizmos, use
    fragOutput = blender_srgb_to_framebuffer_space(fragOutput)
    to transform the output sRGB colors to the frame-buffer color-space.
    """

    name: str
    """ The name of the shader object for debugging purposes (read-only).

    :type: str
    """

    program: int
    """ The name of the program object for use by the OpenGL API (read-only).

    :type: int
    """

    def attr_from_name(self, name: str) -> int:
        """Get attribute location by name.

        :param name: The name of the attribute variable whose location is to be queried.
        :type name: str
        :return: The location of an attribute variable.
        :rtype: int
        """
        ...

    def attrs_info_get(self) -> tuple:
        """Information about the attributes used in the Shader.

        :return: tuples containing information about the attributes in order (name, type)
        :rtype: tuple
        """
        ...

    def bind(self):
        """Bind the shader object. Required to be able to change uniforms of this shader."""
        ...

    def format_calc(self) -> GPUVertFormat:
        """Build a new format based on the attributes of the shader.

        :return: vertex attribute format for the shader
        :rtype: GPUVertFormat
        """
        ...

    def image(self, name: str, texture: GPUTexture):
        """Specify the value of an image variable for the current GPUShader.

        :param name: Name of the image variable to which the texture is to be bound.
        :type name: str
        :param texture: Texture to attach.
        :type texture: GPUTexture
        """
        ...

    def uniform_block(self, name: str, ubo):
        """Specify the value of an uniform buffer object variable for the current GPUShader.

        :param name: name of the uniform variable whose UBO is to be specified.
        :type name: str
        :param ubo: Uniform Buffer to attach.
        """
        ...

    def uniform_block_from_name(self, name: str) -> int:
        """Get uniform block location by name.

        :param name: Name of the uniform block variable whose location is to be queried.
        :type name: str
        :return: The location of the uniform block variable.
        :rtype: int
        """
        ...

    def uniform_bool(self, name: str, value: bool):
        """Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param value: Value that will be used to update the specified uniform variable.
        :type value: bool
        """
        ...

    def uniform_float(self, name: str, value):
        """Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param value: Value that will be used to update the specified uniform variable.
        """
        ...

    def uniform_from_name(self, name: str) -> int:
        """Get uniform location by name.

        :param name: Name of the uniform variable whose location is to be queried.
        :type name: str
        :return: Location of the uniform variable.
        :rtype: int
        """
        ...

    def uniform_int(self, name: str, seq):
        """Specify the value of a uniform variable for the current program object.

        :param name: name of the uniform variable whose value is to be changed.
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable.
        """
        ...

    def uniform_sampler(self, name: str, texture: GPUTexture):
        """Specify the value of a texture uniform variable for the current GPUShader.

        :param name: name of the uniform variable whose texture is to be specified.
        :type name: str
        :param texture: Texture to attach.
        :type texture: GPUTexture
        """
        ...

    def uniform_vector_float(
        self, location: int, buffer: list[float], length: int, count: int
    ):
        """Set the buffer to fill the uniform.

                :param location: Location of the uniform variable to be modified.
                :type location: int
                :param buffer: The data that should be set. Can support the buffer protocol.
                :type buffer: list[float]
                :param length: Size of the uniform data type:

        1: float

        2: vec2 or float[2]

        3: vec3 or float[3]

        4: vec4 or float[4]

        9: mat3

        16: mat4
                :type length: int
                :param count: Specifies the number of elements, vector or matrices that are to be modified.
                :type count: int
        """
        ...

    def uniform_vector_int(self, location, buffer, length, count):
        """See GPUShader.uniform_vector_float(...) description.

        :param location:
        :param buffer:
        :param length:
        :param count:
        """
        ...

class GPUShaderCreateInfo:
    """Stores and describes types and variables that are used in shader sources."""

    def compute_source(self, source: str):
        """compute shader source code written in GLSL.Example:`GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__

        :param source: The compute shader source code.
        :type source: str
        """
        ...

    def define(self, name, value):
        """Add a preprocessing define directive. In GLSL it would be something like:

        :param name:
        :param value:
        """
        ...

    def fragment_out(self, slot: int, type: str, name: str, blend: str = "NONE"):
        """Specify a fragment output corresponding to a framebuffer target slot.

                :param slot: The attribute index.
                :type slot: int
                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: Name of the attribute.
                :type name: str
                :param blend: Dual Source Blending Index. It can be 'NONE', 'SRC_0' or 'SRC_1'.
                :type blend: str
        """
        ...

    def fragment_source(self, source: str):
        """Fragment shader source code written in GLSL.Example:`GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__

        :param source: The fragment shader source code.
        :type source: str
        """
        ...

    def image(
        self,
        slot: int,
        format: str,
        type: str,
        name: str,
        qualifiers: set = {"NO_RESTRICT"},
    ):
        """Specify an image resource used for arbitrary load and store operations.

                :param slot: The image resource index.
                :type slot: int
                :param format: The GPUTexture format that is passed to the shader. Possible values are:

        RGBA8UI

        RGBA8I

        RGBA8

        RGBA32UI

        RGBA32I

        RGBA32F

        RGBA16UI

        RGBA16I

        RGBA16F

        RGBA16

        RG8UI

        RG8I

        RG8

        RG32UI

        RG32I

        RG32F

        RG16UI

        RG16I

        RG16F

        RG16

        R8UI

        R8I

        R8

        R32UI

        R32I

        R32F

        R16UI

        R16I

        R16F

        R16

        R11F_G11F_B10F

        DEPTH32F_STENCIL8

        DEPTH24_STENCIL8

        SRGB8_A8

        RGB16F

        SRGB8_A8_DXT1

        SRGB8_A8_DXT3

        SRGB8_A8_DXT5

        RGBA8_DXT1

        RGBA8_DXT3

        RGBA8_DXT5

        DEPTH_COMPONENT32F

        DEPTH_COMPONENT24

        DEPTH_COMPONENT16
                :type format: str
                :param type: The data type describing how the image is to be read in the shader. Possible values are:

        FLOAT_BUFFER

        FLOAT_1D

        FLOAT_1D_ARRAY

        FLOAT_2D

        FLOAT_2D_ARRAY

        FLOAT_3D

        FLOAT_CUBE

        FLOAT_CUBE_ARRAY

        INT_BUFFER

        INT_1D

        INT_1D_ARRAY

        INT_2D

        INT_2D_ARRAY

        INT_3D

        INT_CUBE

        INT_CUBE_ARRAY

        UINT_BUFFER

        UINT_1D

        UINT_1D_ARRAY

        UINT_2D

        UINT_2D_ARRAY

        UINT_3D

        UINT_CUBE

        UINT_CUBE_ARRAY

        SHADOW_2D

        SHADOW_2D_ARRAY

        SHADOW_CUBE

        SHADOW_CUBE_ARRAY

        DEPTH_2D

        DEPTH_2D_ARRAY

        DEPTH_CUBE

        DEPTH_CUBE_ARRAY
                :type type: str
                :param name: The image resource name.
                :type name: str
                :param qualifiers: Set containing values that describe how the image resource is to be read or written. Possible values are:
        - NO_RESTRICT
        - READ
        - WRITE
                :type qualifiers: set
        """
        ...

    def local_group_size(self, x: int, y: int = -1, z: int = -1):
        """Specify the local group size for compute shaders.

        :param x: The local group size in the x dimension.
        :type x: int
        :param y: The local group size in the y dimension. Optional. Defaults to -1.
        :type y: int
        :param z: The local group size in the z dimension. Optional. Defaults to -1.
        :type z: int
        """
        ...

    def push_constant(self, type: str, name: str, size=0):
        """Specify a global access constant.

                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: Name of the constant.
                :type name: str
                :param size: If not zero, indicates that the constant is an array with the specified size.
        """
        ...

    def sampler(self, slot: int, type: str, name: str):
        """Specify an image texture sampler.

                :param slot: The image texture sampler index.
                :type slot: int
                :param type: The data type describing the format of each sampler unit. Possible values are:

        FLOAT_BUFFER

        FLOAT_1D

        FLOAT_1D_ARRAY

        FLOAT_2D

        FLOAT_2D_ARRAY

        FLOAT_3D

        FLOAT_CUBE

        FLOAT_CUBE_ARRAY

        INT_BUFFER

        INT_1D

        INT_1D_ARRAY

        INT_2D

        INT_2D_ARRAY

        INT_3D

        INT_CUBE

        INT_CUBE_ARRAY

        UINT_BUFFER

        UINT_1D

        UINT_1D_ARRAY

        UINT_2D

        UINT_2D_ARRAY

        UINT_3D

        UINT_CUBE

        UINT_CUBE_ARRAY

        SHADOW_2D

        SHADOW_2D_ARRAY

        SHADOW_CUBE

        SHADOW_CUBE_ARRAY

        DEPTH_2D

        DEPTH_2D_ARRAY

        DEPTH_CUBE

        DEPTH_CUBE_ARRAY
                :type type: str
                :param name: The image texture sampler name.
                :type name: str
        """
        ...

    def typedef_source(self, source):
        """Source code included before resource declaration. Useful for defining structs used by Uniform Buffers.Example:

        :param source:
        """
        ...

    def uniform_buf(self, slot: int, type_name: str, name: str):
        """Specify a uniform variable whose type can be one of those declared in typedef_source.

        :param slot: The uniform variable index.
        :type slot: int
        :param type_name: Name of the data type. It can be a struct type defined in the source passed through the `gpu.types.GPUShaderCreateInfo.typedef_source`.
        :type type_name: str
        :param name: The uniform variable name.
        :type name: str
        """
        ...

    def vertex_in(self, slot: int, type: str, name: str):
        """Add a vertex shader input attribute.

                :param slot: The attribute index.
                :type slot: int
                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: name of the attribute.
                :type name: str
        """
        ...

    def vertex_out(self, interface: GPUStageInterfaceInfo):
        """Add a vertex shader output interface block.

        :param interface: Object describing the block.
        :type interface: GPUStageInterfaceInfo
        """
        ...

    def vertex_source(self, source: str):
        """Vertex shader source code written in GLSL.Example:`GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__

        :param source: The vertex shader source code.
        :type source: str
        """
        ...

class GPUStageInterfaceInfo:
    """List of varyings between shader stages."""

    name: str
    """ Name of the interface block.

    :type: str
    """

    def flat(self, type: str, name: str):
        """Add an attribute with qualifier of type flat to the interface block.

                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: name of the attribute.
                :type name: str
        """
        ...

    def no_perspective(self, type: str, name: str):
        """Add an attribute with qualifier of type no_perspective to the interface block.

                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: name of the attribute.
                :type name: str
        """
        ...

    def smooth(self, type: str, name: str):
        """Add an attribute with qualifier of type smooth to the interface block.

                :param type: One of these types:

        FLOAT

        VEC2

        VEC3

        VEC4

        MAT3

        MAT4

        UINT

        UVEC2

        UVEC3

        UVEC4

        INT

        IVEC2

        IVEC3

        IVEC4

        BOOL
                :type type: str
                :param name: name of the attribute.
                :type name: str
        """
        ...

class GPUTexture:
    """This object gives access to off GPU textures."""

    format: str
    """ Format of the texture.

    :type: str
    """

    height: int
    """ Height of the texture.

    :type: int
    """

    width: int
    """ Width of the texture.

    :type: int
    """

    def clear(self, format: str = "FLOAT", value=(0.0, 0.0, 0.0, 1.0)):
        """Fill texture with specific value.

                :param format: The format that describes the content of a single item.
        Possible values are FLOAT, INT, UINT, UBYTE, UINT_24_8 and 10_11_11_REV.
                :type format: str
                :param value: sequence each representing the value to fill.
        """
        ...

    def read(self):
        """Creates a buffer with the value of all pixels."""
        ...

class GPUUniformBuf:
    """This object gives access to off uniform buffers."""

    def update(self, data):
        """Update the data of the uniform buffer object.

        :param data:
        """
        ...

class GPUVertBuf:
    """Contains a VBO."""

    def attr_fill(self, id: int | str, data: list[float]):
        """Insert data into the buffer for a single attribute.

        :param id: Either the name or the id of the attribute.
        :type id: int | str
        :param data: Sequence of data that should be stored in the buffer
        :type data: list[float]
        """
        ...

class GPUVertFormat:
    """This object contains information about the structure of a vertex buffer."""

    def attr_add(self, id: str, comp_type: str, len: int, fetch_mode: str):
        """Add a new attribute to the format.

                :param id: Name the attribute. Often position, normal, ...
                :type id: str
                :param comp_type: The data type that will be used store the value in memory.
        Possible values are I8, U8, I16, U16, I32, U32, F32 and I10.
                :type comp_type: str
                :param len: How many individual values the attribute consists of
        (e.g. 2 for uv coordinates).
                :type len: int
                :param fetch_mode: How values from memory will be converted when used in the shader.
        This is mainly useful for memory optimizations when you want to store values with
        reduced precision. E.g. you can store a float in only 1 byte but it will be
        converted to a normal 4 byte float when used.
        Possible values are FLOAT, INT, INT_TO_FLOAT_UNIT and INT_TO_FLOAT.
                :type fetch_mode: str
        """
        ...
