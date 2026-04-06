"""
[WARNING]
This module is deprecated and will be removed in a future release,
when OpenGL is replaced by Metal and Vulkan.
Use the graphics API independent gpu module instead.

This module wraps OpenGL constants and functions, making them available from
within Blender Python.

The complete list can be retrieved from the module itself, by listing its
contents: dir(bgl).  A simple search on the web can point to more
than enough material to teach OpenGL programming, from books to many
collections of tutorials.

Here is a comprehensive list of books (non free).
Learn OpenGL is one of the best resources to learn modern OpenGL and
opengl-tutorial.org offers a set of extensive examples,
including advanced features.

[NOTE]
You can use the bpy.types.Image type to load and set textures.
See bpy.types.Image.gl_load and bpy.types.Image.gl_free,
for example.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class Buffer:
    """The Buffer object is simply a block of memory that is delineated and initialized by the
    user. Many OpenGL functions return data to a C-style pointer, however, because this
    is not possible in python the Buffer object can be used to this end. Wherever pointer
    notation is used in the OpenGL functions the Buffer object can be used in its bgl
    wrapper. In some instances the Buffer object will need to be initialized with the template
    parameter, while in other instances the user will want to create just a blank buffer
    which will be zeroed by default.
    """

    dimensions: typing.Any
    """ The number of dimensions of the Buffer."""

    def to_list(self) -> None:
        """The contents of the Buffer as a python list."""

    def __init__(self, type: int, dimensions, template=None) -> None:
        """This will create a new Buffer object for use with other bgl OpenGL commands.
        Only the type of argument to store in the buffer and the dimensions of the buffer
        are necessary. Buffers are zeroed by default unless a template is supplied, in
        which case the buffer is initialized to the template.

                :param type: The format to store data in. The type should be one of
        GL_BYTE, GL_SHORT, GL_INT, or GL_FLOAT.
                :param dimensions: If the dimensions are specified as an int a linear array will
        be created for the buffer. If a sequence is passed for the dimensions, the buffer
        becomes n-Dimensional, where n is equal to the number of parameters passed in the
        sequence. Example: [256,2] is a two- dimensional buffer while [256,256,4] creates
        a three- dimensional buffer. You can think of each additional dimension as a sub-item
        of the dimension to the left. i.e. [10,2] is a 10 element array each with 2 sub-items.
        [(0,0), (0,1), (1,0), (1,1), (2,0), ...] etc.
                :param template: A sequence of matching dimensions which will be used to initialize
        the Buffer. If a template is not passed in all fields will be initialized to 0.
                :return: The newly created buffer as a PyObject.
        """

def glActiveTexture(texture: int) -> None:
    """Select active texture unit.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glActiveTexture.xhtml>`__

    :param texture: Constant in GL_TEXTURE0 0 - 8
    """

def glAttachShader(program: int, shader: int) -> None:
    """Attaches a shader object to a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glAttachShader.xhtml>`__

    :param program: Specifies the program object to which a shader object will be attached.
    :param shader: Specifies the shader object that is to be attached.
    """

def glBeginQuery(p0: int, p1: int) -> None:
    """ """

def glBindAttribLocation(p0: int, p1: int, p2: str) -> None:
    """ """

def glBindBuffer(p0: int, p1: int) -> None:
    """ """

def glBindBufferBase(p0: int, p1: int, p2: int) -> None:
    """ """

def glBindBufferRange(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glBindFramebuffer(p0: int, p1: int) -> None:
    """ """

def glBindRenderbuffer(p0: int, p1: int) -> None:
    """ """

def glBindTexture(target: set[str], texture: int) -> None:
    """Bind a named texture to a texturing target`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTexture.xhtml>`__

    :param target: Specifies the target to which the texture is bound.
    :param texture: Specifies the name of a texture.
    """

def glBindVertexArray(p0: int) -> None:
    """ """

def glBlendColor(p0: float, p1: float, p2: float, p3: float) -> None:
    """ """

def glBlendEquation(p0: int) -> None:
    """ """

def glBlendEquationSeparate(p0: int, p1: int) -> None:
    """ """

def glBlendFunc(sfactor: set[str], dfactor: set[str]) -> None:
    """Specify pixel arithmetic`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml>`__

        :param sfactor: Specifies how the red, green, blue, and alpha source blending factors are
    computed.
        :param dfactor: Specifies how the red, green, blue, and alpha destination
    blending factors are computed.
    """

def glBlitFramebuffer(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: int,
    p9: int,
) -> None:
    """ """

def glBufferData(p0: int, p1: int, p2: typing.Any, p3: int) -> None:
    """ """

def glBufferSubData(p0: int, p1: int, p2: int, p3: typing.Any) -> None:
    """ """

def glCheckFramebufferStatus(p0: int) -> int:
    """ """

def glClear(mask) -> None:
    """Clear buffers to preset values`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClear.xhtml>`__

    :param mask: Bitwise OR of masks that indicate the buffers to be cleared.
    """

def glClearColor(red: float, green, blue, alpha) -> None:
    """Specify clear values for the color buffers`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearColor.xhtml>`__

        :param red: Specify the red, green, blue, and alpha values used when the
    color buffers are cleared. The initial values are all 0.
    """

def glClearDepth(depth: int) -> None:
    """Specify the clear value for the depth buffer`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearDepth.xhtml>`__

        :param depth: Specifies the depth value used when the depth buffer is cleared.
    The initial value is 1.
    """

def glClearStencil(s: int) -> None:
    """Specify the clear value for the stencil buffer`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearStencil.xhtml>`__

    :param s: Specifies the index used when the stencil buffer is cleared. The initial value is 0.
    """

def glClipPlane(plane: set[str], equation: Buffer) -> None:
    """Specify a plane against which all geometry is clipped`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClipPlane.xhtml>`__

        :param plane: Specifies which clipping plane is being positioned.
        :param equation: Specifies the address of an array of four double- precision
    floating-point values. These values are interpreted as a plane equation.
    """

def glColorMask(red: int, green, blue, alpha) -> None:
    """Enable and disable writing of frame buffer color components`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glColorMask.xhtml>`__

        :param red: Specify whether red, green, blue, and alpha can or cannot be
    written into the frame buffer. The initial values are all GL_TRUE, indicating that the
    color components can be written.
    """

def glCompileShader(shader: int) -> None:
    """Compiles a shader object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCompileShader.xhtml>`__

    :param shader: Specifies the shader object to be compiled.
    """

def glCompressedTexImage1D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: typing.Any
) -> None:
    """ """

def glCompressedTexImage2D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: typing.Any
) -> None:
    """ """

def glCompressedTexImage3D(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: typing.Any,
) -> None:
    """ """

def glCompressedTexSubImage1D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: typing.Any
) -> None:
    """ """

def glCompressedTexSubImage2D(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: typing.Any,
) -> None:
    """ """

def glCopyTexImage1D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int
) -> None:
    """ """

def glCopyTexImage2D(
    target: set[str],
    level: int,
    internalformat: int,
    x: int,
    y,
    width: int,
    height: int,
    border: int,
) -> None:
    """Copy pixels into a 2D texture image`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCopyTexImage2D.xhtml>`__

        :param target: Specifies the target texture.
        :param level: Specifies the level-of-detail number. Level 0 is the base image level.
    Level n is the nth mipmap reduction image.
        :param internalformat: Specifies the number of color components in the texture.
        :param x: Specify the window coordinates of the first pixel that is copied
    from the frame buffer. This location is the lower left corner of a rectangular
    block of pixels.
        :param width: Specifies the width of the texture image. Must be 2n+2(border) for
    some integer n. All implementations support texture images that are at least 64
    texels wide.
        :param height: Specifies the height of the texture image. Must be 2m+2(border) for
    some integer m. All implementations support texture images that are at least 64
    texels high.
        :param border: Specifies the width of the border. Must be either 0 or 1.
    """

def glCopyTexSubImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None:
    """ """

def glCopyTexSubImage2D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int
) -> None:
    """ """

def glCopyTexSubImage3D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int
) -> None:
    """ """

def glCreateProgram() -> int:
    """Creates a program object`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateProgram.xhtml>`__

    :return: The new program or zero if an error occurs.
    """

def glCreateShader(shaderType: GL_GEOMETRY_SHADER | typing.Any) -> int:
    """Creates a shader object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateShader.xhtml>`__

    :return: 0 if an error occurs.
    """

def glCullFace(mode: set[str]) -> None:
    """Specify whether front- or back-facing facets can be culled`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCullFace.xhtml>`__

    :param mode: Specifies whether front- or back-facing facets are candidates for culling.
    """

def glDeleteBuffers(p0: int, p1: int) -> None:
    """ """

def glDeleteFramebuffers(p0: int, p1: int) -> None:
    """ """

def glDeleteProgram(program: int) -> None:
    """Deletes a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteProgram.xhtml>`__

    :param program: Specifies the program object to be deleted.
    """

def glDeleteQueries(p0: int, p1: int) -> None:
    """ """

def glDeleteRenderbuffers(p0: int, p1: int) -> None:
    """ """

def glDeleteShader(shader: int) -> None:
    """Deletes a shader object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteShader.xhtml>`__

    :param shader: Specifies the shader object to be deleted.
    """

def glDeleteTextures(n: int, textures: Buffer) -> None:
    """Delete named textures`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteTextures.xhtml>`__

    :param n: Specifies the number of textures to be deleted
    :param textures: Specifies an array of textures to be deleted
    """

def glDeleteVertexArrays(p0: int, p1: int) -> None:
    """ """

def glDepthFunc(func: set[str]) -> None:
    """Specify the value used for depth buffer comparisons`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthFunc.xhtml>`__

    :param func: Specifies the depth comparison function.
    """

def glDepthMask(flag: int) -> None:
    """Enable or disable writing into the depth buffer`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthMask.xhtml>`__

        :param flag: Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE,
    depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer
    writing is enabled.
    """

def glDepthRange(zNear: int, zFar: int) -> None:
    """Specify mapping of depth values from normalized device coordinates to window coordinates`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRange.xhtml>`__

        :param zNear: Specifies the mapping of the near clipping plane to window coordinates.
    The initial value is 0.
        :param zFar: Specifies the mapping of the far clipping plane to window coordinates.
    The initial value is 1.
    """

def glDetachShader(program: int, shader: int) -> None:
    """Detaches a shader object from a program object to which it is attached.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDetachShader.xhtml>`__

    :param program: Specifies the program object from which to detach the shader object.
    :param shader: pecifies the program object from which to detach the shader object.
    """

def glDisable(cap: set[str]) -> None:
    """Disable server-side GL capabilities`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml>`__

    :param cap: Specifies a symbolic constant indicating a GL capability.
    """

def glDisableVertexAttribArray(p0: int) -> None:
    """ """

def glDrawArrays(p0: int, p1: int, p2: int) -> None:
    """ """

def glDrawBuffer(mode: set[str]) -> None:
    """Specify which color buffers are to be drawn into`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffer.xhtml>`__

    :param mode: Specifies up to four color buffers to be drawn into.
    """

def glDrawBuffers(p0: int, p1: int) -> None:
    """ """

def glDrawElements(p0: int, p1: int, p2: int, p3: typing.Any) -> None:
    """ """

def glDrawRangeElements(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: typing.Any
) -> None:
    """ """

def glEdgeFlag(flag) -> None:
    """B{glEdgeFlag, glEdgeFlagv}Flag edges as either boundary or non-boundary`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEdgeFlag.xhtml>`__

    :param flag: Specifies the current edge flag value.The initial value is GL_TRUE.
    """

def glEnable(cap: set[str]) -> None:
    """Enable server-side GL capabilities`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml>`__

    :param cap: Specifies a symbolic constant indicating a GL capability.
    """

def glEnableVertexAttribArray(p0: int) -> None:
    """ """

def glEndQuery(p0: int) -> None:
    """ """

def glEvalCoord(u: typing.Any, v: typing.Any) -> None:
    """B{glEvalCoord1d, glEvalCoord1f, glEvalCoord2d, glEvalCoord2f, glEvalCoord1dv, glEvalCoord1fv,
    glEvalCoord2dv, glEvalCoord2fv}Evaluate enabled one- and two-dimensional maps`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalCoord.xhtml>`__

        :param u: Specifies a value that is the domain coordinate u to the basis function defined
    in a previous glMap1 or glMap2 command. If the function prototype ends in v then
    u specifies a pointer to an array containing either one or two domain coordinates. The first
    coordinate is u. The second coordinate is v, which is present only in glEvalCoord2 versions.
        :param v: Specifies a value that is the domain coordinate v to the basis function defined
    in a previous glMap2 command. This argument is not present in a glEvalCoord1 command.
    """

def glEvalMesh(mode: set[str], i1: int, i2) -> None:
    """B{glEvalMesh1 or glEvalMesh2}Compute a one- or two-dimensional grid of points or lines`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalMesh.xhtml>`__

        :param mode: In glEvalMesh1, specifies whether to compute a one-dimensional
    mesh of points or lines.
        :param i1: Specify the first and last integer values for the grid domain variable i.
    """

def glEvalPoint(i: int, j) -> None:
    """B{glEvalPoint1 and glEvalPoint2}Generate and evaluate a single point in a mesh`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalPoint.xhtml>`__

    :param i: Specifies the integer value for grid domain variable i.
    :param j: Specifies the integer value for grid domain variable j (glEvalPoint2 only).
    """

def glFeedbackBuffer(size: int, type: set[str], buffer: Buffer) -> None:
    """Controls feedback mode`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFeedbackBuffer.xhtml>`__

        :param size: Specifies the maximum number of values that can be written into buffer.
        :param type: Specifies a symbolic constant that describes the information that
    will be returned for each vertex.
        :param buffer: Returns the feedback data.
    """

def glFinish() -> None:
    """Block until all GL execution is complete`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFinish.xhtml>`__"""

def glFlush() -> None:
    """Force Execution of GL commands in finite time`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFlush.xhtml>`__"""

def glFog(pname: set[str], param: typing.Any) -> None:
    """B{glFogf, glFogi, glFogfv, glFogiv}Specify fog parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFog.xhtml>`__

        :param pname: Specifies a single-valued fog parameter. If the function prototype
    ends in v specifies a fog parameter.
        :param param: Specifies the value or values to be assigned to pname. GL_FOG_COLOR
    requires an array of four values. All other parameters accept an array containing
    only a single value.
    """

def glFramebufferRenderbuffer(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glFramebufferTexture(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glFrontFace(mode: set[str]) -> None:
    """Define front- and back-facing polygons`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFrontFace.xhtml>`__

    :param mode: Specifies the orientation of front-facing polygons.
    """

def glGenBuffers(p0: int, p1: int) -> None:
    """ """

def glGenFramebuffers(p0: int, p1: int) -> None:
    """ """

def glGenQueries(p0: int, p1: int) -> None:
    """ """

def glGenRenderbuffers(p0: int, p1: int) -> None:
    """ """

def glGenTextures(n: int, textures: Buffer) -> None:
    """Generate texture names`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGenTextures.xhtml>`__

    :param n: Specifies the number of textures name to be generated.
    :param textures: Specifies an array in which the generated textures names are stored.
    """

def glGenVertexArrays(p0: int, p1: int) -> None:
    """ """

def glGet(pname: set[str], param: typing.Any) -> None:
    """B{glGetBooleanv, glGetfloatv, glGetFloatv, glGetIntegerv}Return the value or values of a selected parameter`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml>`__

    :param pname: Specifies the parameter value to be returned.
    :param param: Returns the value or values of the specified parameter.
    """

def glGetActiveAttrib(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int
) -> None:
    """ """

def glGetActiveUniform(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int
) -> None:
    """ """

def glGetActiveUniformBlockName(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glGetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glGetActiveUniformName(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glGetActiveUniformsiv(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glGetAttachedShaders(
    program: int, maxCount: int, count: Buffer, shaders: Buffer
) -> None:
    """Returns the handles of the shader objects attached to a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetAttachedShaders.xhtml>`__

    :param program: Specifies the program object to be queried.
    :param maxCount: Specifies the size of the array for storing the returned object names.
    :param count: Returns the number of names actually returned in objects.
    :param shaders: Specifies an array that is used to return the names of attached shader objects.
    """

def glGetAttribLocation(p0: int, p1: str) -> int:
    """ """

def glGetBooleanv(p0: int, p1: bool) -> None:
    """ """

def glGetBufferParameteri64v(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetBufferParameteriv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetBufferPointerv(p0: int, p1: int, p2: typing.Any) -> None:
    """ """

def glGetBufferSubData(p0: int, p1: int, p2: int, p3: typing.Any) -> None:
    """ """

def glGetCompressedTexImage(p0: int, p1: int, p2: typing.Any) -> None:
    """ """

def glGetDoublev(p0: int, p1: float) -> None:
    """ """

def glGetError() -> None:
    """Return error information`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetError.xhtml>`__"""

def glGetFloatv(p0: int, p1: float) -> None:
    """ """

def glGetIntegerv(p0: int, p1: int) -> None:
    """ """

def glGetLight(light: set[str], pname: set[str], params: Buffer) -> None:
    """B{glGetLightfv and glGetLightiv}Return light source parameter values`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetLight.xhtml>`__

        :param light: Specifies a light source. The number of possible lights depends on the
    implementation, but at least eight lights are supported. They are identified by symbolic
    names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS.
        :param pname: Specifies a light source parameter for light.
        :param params: Returns the requested data.
    """

def glGetMap(target: set[str], query: set[str], v: Buffer) -> None:
    """B{glGetMapdv, glGetMapfv, glGetMapiv}Return evaluator parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetMap.xhtml>`__

    :param target: Specifies the symbolic name of a map.
    :param query: Specifies which parameter to return.
    :param v: Returns the requested data.
    """

def glGetMaterial(face: set[str], pname: set[str], params: Buffer) -> None:
    """B{glGetMaterialfv, glGetMaterialiv}Return material parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetMaterial.xhtml>`__

        :param face: Specifies which of the two materials is being queried.
    representing the front and back materials, respectively.
        :param pname: Specifies the material parameter to return.
        :param params: Returns the requested data.
    """

def glGetMultisamplefv(p0: int, p1: int, p2: float) -> None:
    """ """

def glGetPixelMap(map: set[str], values: Buffer) -> None:
    """B{glGetPixelMapfv, glGetPixelMapuiv, glGetPixelMapusv}Return the specified pixel map`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetPixelMap.xhtml>`__

    :param map: Specifies the name of the pixel map to return.
    :param values: Returns the pixel map contents.
    """

def glGetProgramInfoLog(
    program: int, maxLength: int, length: Buffer, infoLog: Buffer
) -> None:
    """Returns the information log for a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramInfoLog.xhtml>`__

    :param program: Specifies the program object whose information log is to be queried.
    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :param infoLog: Specifies an array of characters that is used to return the information log.
    """

def glGetProgramiv(program: int, pname: int, params: Buffer) -> None:
    """Returns a parameter from a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgram.xhtml>`__

    :param program: Specifies the program object to be queried.
    :param pname: Specifies the object parameter.
    :param params: Returns the requested object parameter.
    """

def glGetQueryObjectiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetQueryObjectuiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetQueryiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetShaderInfoLog(
    program, maxLength: int, length: Buffer, infoLog: Buffer
) -> None:
    """Returns the information log for a shader object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderInfoLog.xhtml>`__

    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :param infoLog: Specifies an array of characters that is used to return the information log.
    """

def glGetShaderSource(
    shader: int, bufSize: int, length: Buffer, source: Buffer
) -> None:
    """Returns the source code string from a shader object`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderSource.xhtml>`__

    :param shader: Specifies the shader object to be queried.
    :param bufSize: Specifies the size of the character buffer for storing the returned source code string.
    :param length: Returns the length of the string returned in source (excluding the null terminator).
    :param source: Specifies an array of characters that is used to return the source code string.
    """

def glGetShaderiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetString(name: set[str]) -> None:
    """Return a string describing the current GL connection`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetString.xhtml>`__

    :param name: Specifies a symbolic constant.
    """

def glGetStringi(p0: int, p1: int) -> str:
    """ """

def glGetTexEnv(target: set[str], pname: set[str], params: Buffer) -> None:
    """B{glGetTexEnvfv, glGetTexEnviv}Return texture environment parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexEnv.xhtml>`__

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV.
    :param pname: Specifies the symbolic name of a texture environment parameter.
    :param params: Returns the requested data.
    """

def glGetTexGen(coord: set[str], pname: set[str], params: Buffer) -> None:
    """B{glGetTexGendv, glGetTexGenfv, glGetTexGeniv}Return texture coordinate generation parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexGen.xhtml>`__

    :param coord: Specifies a texture coordinate.
    :param pname: Specifies the symbolic name of the value(s) to be returned.
    :param params: Returns the requested data.
    """

def glGetTexImage(
    target: set[str], level: int, format: set[str], type: set[str], pixels: Buffer
) -> None:
    """Return a texture image`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml>`__

        :param target: Specifies which texture is to be obtained.
        :param level: Specifies the level-of-detail number of the desired image.
    Level 0 is the base image level. Level n is the nth mipmap reduction image.
        :param format: Specifies a pixel format for the returned data.
        :param type: Specifies a pixel type for the returned data.
        :param pixels: Returns the texture image. Should be a pointer to an array of the
    type specified by type
    """

def glGetTexLevelParameter(
    target: set[str], level: int, pname: set[str], params: Buffer
) -> None:
    """B{glGetTexLevelParameterfv, glGetTexLevelParameteriv}return texture parameter values for a specific level of detail`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml>`__

        :param target: Specifies the symbolic name of the target texture.
        :param level: Specifies the level-of-detail number of the desired image.
    Level 0 is the base image level. Level n is the nth mipmap reduction image.
        :param pname: Specifies the symbolic name of a texture parameter.
        :param params: Returns the requested data.
    """

def glGetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: float) -> None:
    """ """

def glGetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glGetTexParameter(target: set[str], pname: set[str], params: Buffer) -> None:
    """B{glGetTexParameterfv, glGetTexParameteriv}Return texture parameter values`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml>`__

    :param target: Specifies the symbolic name of the target texture.
    :param pname: Specifies the symbolic name the target texture.
    :param params: Returns the texture parameters.
    """

def glGetTexParameterfv(p0: int, p1: int, p2: float) -> None:
    """ """

def glGetTexParameteriv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetUniformBlockIndex(p0: int, p1: str) -> int:
    """ """

def glGetUniformIndices(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glGetUniformLocation(p0: int, p1: str) -> int:
    """ """

def glGetUniformfv(p0: int, p1: int, p2: float) -> None:
    """ """

def glGetUniformiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glGetVertexAttribPointerv(p0: int, p1: int, p2: typing.Any) -> None:
    """ """

def glGetVertexAttribdv(p0: int, p1: int, p2: float) -> None:
    """ """

def glGetVertexAttribfv(p0: int, p1: int, p2: float) -> None:
    """ """

def glGetVertexAttribiv(p0: int, p1: int, p2: int) -> None:
    """ """

def glHint(target: set[str], mode: set[str]) -> None:
    """Specify implementation-specific hints`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glHint.xhtml>`__

        :param target: Specifies a symbolic constant indicating the behavior to be
    controlled.
        :param mode: Specifies a symbolic constant indicating the desired behavior.
    """

def glIsBuffer(p0: int) -> bool:
    """ """

def glIsEnabled(cap: set[str]) -> None:
    """Test whether a capability is enabled`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsEnabled.xhtml>`__

    :param cap: Specifies a constant representing a GL capability.
    """

def glIsProgram(program: int) -> None:
    """Determines if a name corresponds to a program object`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsProgram.xhtml>`__

    :param program: Specifies a potential program object.
    """

def glIsQuery(p0: int) -> bool:
    """ """

def glIsShader(shader: int) -> None:
    """Determines if a name corresponds to a shader object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsShader.xhtml>`__

    :param shader: Specifies a potential shader object.
    """

def glIsTexture(texture: int) -> None:
    """Determine if a name corresponds to a texture`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsTexture.xhtml>`__

    :param texture: Specifies a value that may be the name of a texture.
    """

def glIsVertexArray(p0: int) -> bool:
    """ """

def glLight(light: set[str], pname: set[str], param: typing.Any) -> None:
    """B{glLightf,glLighti, glLightfv, glLightiv}Set the light source parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLight.xhtml>`__

        :param light: Specifies a light. The number of lights depends on the implementation,
    but at least eight lights are supported. They are identified by symbolic names of the
    form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS.
        :param pname: Specifies a single-valued light source parameter for light.
        :param param: Specifies the value that parameter pname of light source light will be set to.
    If function prototype ends in v specifies a pointer to the value or values that
    parameter pname of light source light will be set to.
    """

def glLightModel(pname: set[str], param: typing.Any) -> None:
    """B{glLightModelf, glLightModeli, glLightModelfv, glLightModeliv}Set the lighting model parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLightModel.xhtml>`__

        :param pname: Specifies a single-value light model parameter.
        :param param: Specifies the value that param will be set to. If function prototype ends in v
    specifies a pointer to the value or values that param will be set to.
    """

def glLineWidth(width: float) -> None:
    """Specify the width of rasterized lines.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLineWidth.xhtml>`__

    :param width: Specifies the width of rasterized lines. The initial value is 1.
    """

def glLinkProgram(program: int) -> None:
    """Links a program object.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLinkProgram.xhtml>`__

    :param program: Specifies the handle of the program object to be linked.
    """

def glLoadMatrix(m: Buffer) -> None:
    """B{glLoadMatrixd, glLoadMatixf}Replace the current matrix with the specified matrix`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLoadMatrix.xhtml>`__

        :param m: Specifies a pointer to 16 consecutive values, which are used as the elements
    of a 4x4 column-major matrix.
    """

def glLogicOp(opcode: set[str]) -> None:
    """Specify a logical pixel operation for color index rendering`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLogicOp.xhtml>`__

    :param opcode: Specifies a symbolic constant that selects a logical operation.
    """

def glMap1(
    target: set[str], u1: typing.Any, u2, stride: int, order: int, points: Buffer
) -> None:
    """B{glMap1d, glMap1f}Define a one-dimensional evaluator`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMap1.xhtml>`__

        :param target: Specifies the kind of values that are generated by the evaluator.
        :param u1: Specify a linear mapping of u, as presented to glEvalCoord1, to ^, t
    he variable that is evaluated by the equations specified by this command.
        :param stride: Specifies the number of floats or float (double)s between the beginning
    of one control point and the beginning of the next one in the data structure
    referenced in points. This allows control points to be embedded in arbitrary data
    structures. The only constraint is that the values for a particular control point must
    occupy contiguous memory locations.
        :param order: Specifies the number of control points. Must be positive.
        :param points: Specifies a pointer to the array of control points.
    """

def glMap2(
    target: set[str],
    u1: typing.Any,
    u2,
    ustride: int,
    uorder: int,
    v1: typing.Any,
    v2,
    vstride: int,
    vorder: int,
    points: Buffer,
) -> None:
    """B{glMap2d, glMap2f}Define a two-dimensional evaluator`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMap2.xhtml>`__

        :param target: Specifies the kind of values that are generated by the evaluator.
        :param u1: Specify a linear mapping of u, as presented to glEvalCoord2, to ^, t
    he variable that is evaluated by the equations specified by this command. Initially
    u1 is 0 and u2 is 1.
        :param ustride: Specifies the number of floats or float (double)s between the beginning
    of control point R and the beginning of control point R ij, where i and j are the u
    and v control point indices, respectively. This allows control points to be embedded
    in arbitrary data structures. The only constraint is that the values for a particular
    control point must occupy contiguous memory locations. The initial value of ustride is 0.
        :param uorder: Specifies the dimension of the control point array in the u axis.
    Must be positive. The initial value is 1.
        :param v1: Specify a linear mapping of v, as presented to glEvalCoord2,
    to ^, one of the two variables that are evaluated by the equations
    specified by this command. Initially, v1 is 0 and v2 is 1.
        :param vstride: Specifies the number of floats or float (double)s between the
    beginning of control point R and the beginning of control point R ij,
    where i and j are the u and v control point(indices, respectively.
    This allows control points to be embedded in arbitrary data structures.
    The only constraint is that the values for a particular control point must
    occupy contiguous memory locations. The initial value of vstride is 0.
        :param vorder: Specifies the dimension of the control point array in the v axis.
    Must be positive. The initial value is 1.
        :param points: Specifies a pointer to the array of control points.
    """

def glMapBuffer(p0: int, p1: int) -> None:
    """ """

def glMapGrid(un: int, u1: typing.Any, u2, vn: int, v1: typing.Any, v2) -> None:
    """B{glMapGrid1d, glMapGrid1f, glMapGrid2d, glMapGrid2f}Define a one- or two-dimensional mesh`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMapGrid.xhtml>`__

        :param un: Specifies the number of partitions in the grid range interval
    [u1, u2]. Must be positive.
        :param u1: Specify the mappings for integer grid domain values i=0 and i=un.
        :param vn: Specifies the number of partitions in the grid range interval
    [v1, v2] (glMapGrid2 only).
        :param v1: Specify the mappings for integer grid domain values j=0 and j=vn
    (glMapGrid2 only).
    """

def glMaterial(face: set[str], pname: set[str], params: int) -> None:
    """Specify material parameters for the lighting model.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMaterial.xhtml>`__

        :param face: Specifies which face or faces are being updated. Must be one of:
        :param pname: Specifies the single-valued material parameter of the face
    or faces that is being updated. Must be GL_SHININESS.
        :param params: Specifies the value that parameter GL_SHININESS will be set to.
    If function prototype ends in v specifies a pointer to the value or values that
    pname will be set to.
    """

def glMultMatrix(m: Buffer) -> None:
    """B{glMultMatrixd, glMultMatrixf}Multiply the current matrix with the specified matrix`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMultMatrix.xhtml>`__

        :param m: Points to 16 consecutive values that are used as the elements of a 4x4 column
    major matrix.
    """

def glNormal3(nx: typing.Any, ny, nz, v: Buffer) -> None:
    """B{Normal3b, Normal3bv, Normal3d, Normal3dv, Normal3f, Normal3fv, Normal3i, Normal3iv,
    Normal3s, Normal3sv}Set the current normal vector`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glNormal.xhtml>`__

        :param nx: Specify the x, y, and z coordinates of the new current normal.
    The initial value of the current normal is the unit vector, (0, 0, 1).
        :param v: Specifies a pointer to an array of three elements: the x, y, and z coordinates
    of the new current normal.
    """

def glPixelMap(map: set[str], mapsize: int, values: Buffer) -> None:
    """B{glPixelMapfv, glPixelMapuiv, glPixelMapusv}Set up pixel transfer maps`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelMap.xhtml>`__

    :param map: Specifies a symbolic map name.
    :param mapsize: Specifies the size of the map being defined.
    :param values: Specifies an array of mapsize values.
    """

def glPixelStore(pname: set[str], param: typing.Any) -> None:
    """B{glPixelStoref, glPixelStorei}Set pixel storage modes`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelStore.xhtml>`__

        :param pname: Specifies the symbolic name of the parameter to be set.
    Six values affect the packing of pixel data into memory.
    Six more affect the unpacking of pixel data from memory.
        :param param: Specifies the value that pname is set to.
    """

def glPixelStoref(p0: int, p1: float) -> None:
    """ """

def glPixelStorei(p0: int, p1: int) -> None:
    """ """

def glPixelTransfer(pname: set[str], param: typing.Any) -> None:
    """B{glPixelTransferf, glPixelTransferi}Set pixel transfer modes`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelTransfer.xhtml>`__

    :param pname: Specifies the symbolic name of the pixel transfer parameter to be set.
    :param param: Specifies the value that pname is set to.
    """

def glPointSize(size: float) -> None:
    """Specify the diameter of rasterized points`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPointSize.xhtml>`__

    :param size: Specifies the diameter of rasterized points. The initial value is 1.
    """

def glPolygonMode(face: set[str], mode: set[str]) -> None:
    """Select a polygon rasterization mode`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonMode.xhtml>`__

        :param face: Specifies the polygons that mode applies to.
    Must be GL_FRONT for front-facing polygons, GL_BACK for back- facing
    polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons.
        :param mode: Specifies how polygons will be rasterized.
    The initial value is GL_FILL for both front- and back- facing polygons.
    """

def glPolygonOffset(factor: float, units: float) -> None:
    """Set the scale and units used to calculate depth values`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonOffset.xhtml>`__

        :param factor: Specifies a scale factor that is used to create a variable depth
    offset for each polygon. The initial value is 0.
        :param units: Is multiplied by an implementation-specific value to create a
    constant depth offset. The initial value is 0.
    """

def glRasterPos(x: typing.Any, y, z, w) -> None:
    """B{glRasterPos2d, glRasterPos2f, glRasterPos2i, glRasterPos2s, glRasterPos3d,
    glRasterPos3f, glRasterPos3i, glRasterPos3s, glRasterPos4d, glRasterPos4f,
    glRasterPos4i, glRasterPos4s, glRasterPos2dv, glRasterPos2fv, glRasterPos2iv,
    glRasterPos2sv, glRasterPos3dv, glRasterPos3fv, glRasterPos3iv, glRasterPos3sv,
    glRasterPos4dv, glRasterPos4fv, glRasterPos4iv, glRasterPos4sv}Specify the raster position for pixel operations`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRasterPos.xhtml>`__

        :param x: Specify the x,y,z, and w object coordinates (if present) for the
    raster position.  If function prototype ends in v specifies a pointer to an array of two,
    three, or four elements, specifying x, y, z, and w coordinates, respectively.
    """

def glReadBuffer(mode: set[str]) -> None:
    """Select a color buffer source for pixels.`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glReadBuffer.xhtml>`__

    :param mode: Specifies a color buffer.
    """

def glReadPixels(
    x: int, y, width: int, height, format: set[str], type: set[str], pixels: Buffer
) -> None:
    """Read a block of pixels from the frame buffer`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glReadPixels.xhtml>`__

        :param x: Specify the window coordinates of the first pixel that is read
    from the frame buffer. This location is the lower left corner of a rectangular
    block of pixels.
        :param width: Specify the dimensions of the pixel rectangle. width and
    height of one correspond to a single pixel.
        :param format: Specifies the format of the pixel data.
        :param type: Specifies the data type of the pixel data.
        :param pixels: Returns the pixel data.
    """

def glRect(x1: typing.Any, y1, x2: typing.Any, y2, v1: typing.Any, v2) -> None:
    """B{glRectd, glRectf, glRecti, glRects, glRectdv, glRectfv, glRectiv, glRectsv}Draw a rectangle`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRect.xhtml>`__

        :param x1: Specify one vertex of a rectangle
        :param x2: Specify the opposite vertex of the rectangle
        :param v1: Specifies a pointer to one vertex of a rectangle and the pointer
    to the opposite vertex of the rectangle
    """

def glRenderbufferStorage(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glRotate(angle: typing.Any, x: typing.Any, y, z) -> None:
    """B{glRotated, glRotatef}Multiply the current matrix by a rotation matrix`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRotate.xhtml>`__

    :param angle: Specifies the angle of rotation in degrees.
    :param x: Specify the x, y, and z coordinates of a vector respectively.
    """

def glSampleCoverage(p0: float, p1: bool) -> None:
    """ """

def glSampleMaski(p0: int, p1: int) -> None:
    """ """

def glScale(x: typing.Any, y, z) -> None:
    """B{glScaled, glScalef}Multiply the current matrix by a general scaling matrix`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glScale.xhtml>`__

    :param x: Specify scale factors along the x, y, and z axes, respectively.
    """

def glScissor(x: int, y, width: int, height) -> None:
    """Define the scissor box`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glScissor.xhtml>`__

        :param x: Specify the lower left corner of the scissor box. Initially (0, 0).
        :param width: Specify the width and height of the scissor box. When a
    GL context is first attached to a window, width and height are set to the
    dimensions of that window.
    """

def glShaderSource(shader: int, shader_string: str) -> None:
    """Replaces the source code in a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man/html/glShaderSource.xhtml>`__

    :param shader: Specifies the handle of the shader object whose source code is to be replaced.
    :param shader_string: The shader string.
    """

def glStencilFunc(func: set[str], ref: int, mask: int) -> None:
    """Set function and reference value for stencil testing`OpenGL Docs <https://www.opengl.org/sdk/docs/man/docbook4/xhtml/glStencilFunc.xhtml>`__

        :param func: Specifies the test function.
        :param ref: Specifies the reference value for the stencil test. ref is clamped
    to the range [0,2n-1], where n is the number of bitplanes in the stencil
    buffer. The initial value is 0.
        :param mask: Specifies a mask that is ANDed with both the reference value and
    the stored stencil value when the test is done. The initial value is all 1s.
    """

def glStencilFuncSeparate(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glStencilMask(mask: int) -> None:
    """Control the writing of individual bits in the stencil planes`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilMask.xhtml>`__

        :param mask: Specifies a bit mask to enable and disable writing of individual bits
    in the stencil planes. Initially, the mask is all 1s.
    """

def glStencilMaskSeparate(p0: int, p1: int) -> None:
    """ """

def glStencilOp(fail: set[str], zfail: set[str], zpass: set[str]) -> None:
    """Set stencil test actions`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilOp.xhtml>`__

        :param fail: Specifies the action to take when the stencil test fails.
    The initial value is GL_KEEP.
        :param zfail: Specifies the stencil action when the stencil test passes, but the
    depth test fails. zfail accepts the same symbolic constants as fail.
    The initial value is GL_KEEP.
        :param zpass: Specifies the stencil action when both the stencil test and the
    depth test pass, or when the stencil test passes and either there is no
    depth buffer or depth testing is not enabled. zpass accepts the same
    symbolic constants
    as fail. The initial value is GL_KEEP.
    """

def glStencilOpSeparate(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glTexCoord(s: typing.Any, t, r, q, v: Buffer) -> None:
    """B{glTexCoord1d, glTexCoord1f, glTexCoord1i, glTexCoord1s, glTexCoord2d, glTexCoord2f,
    glTexCoord2i, glTexCoord2s, glTexCoord3d, glTexCoord3f, glTexCoord3i, glTexCoord3s,
    glTexCoord4d, glTexCoord4f, glTexCoord4i, glTexCoord4s, glTexCoord1dv, glTexCoord1fv,
    glTexCoord1iv, glTexCoord1sv, glTexCoord2dv, glTexCoord2fv, glTexCoord2iv,
    glTexCoord2sv, glTexCoord3dv, glTexCoord3fv, glTexCoord3iv, glTexCoord3sv,
    glTexCoord4dv, glTexCoord4fv, glTexCoord4iv, glTexCoord4sv}Set the current texture coordinates`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexCoord.xhtml>`__

        :param s: Specify s, t, r, and q texture coordinates. Not all parameters are
    present in all forms of the command.
        :param v: Specifies a pointer to an array of one, two, three, or four elements,
    which in turn specify the s, t, r, and q texture coordinates.
    """

def glTexEnv(target: set[str], pname: set[str], param: typing.Any) -> None:
    """B{glTextEnvf, glTextEnvi, glTextEnvfv, glTextEnviv}Set texture environment parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexEnv.xhtml>`__

        :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV.
        :param pname: Specifies the symbolic name of a single-valued texture environment
    parameter. Must be GL_TEXTURE_ENV_MODE.
        :param param: Specifies a single symbolic constant. If function prototype ends in v
    specifies a pointer to a parameter array that contains either a single
    symbolic constant or an RGBA color
    """

def glTexGen(coord: set[str], pname: set[str], param: typing.Any) -> None:
    """B{glTexGend, glTexGenf, glTexGeni, glTexGendv, glTexGenfv, glTexGeniv}Control the generation of texture coordinates`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexGen.xhtml>`__

        :param coord: Specifies a texture coordinate.
        :param pname: Specifies the symbolic name of the texture- coordinate generation function.
        :param param: Specifies a single-valued texture generation parameter.
    If function prototype ends in v specifies a pointer to an array of texture
    generation parameters. If pname is GL_TEXTURE_GEN_MODE, then the array must
    contain a single symbolic constant. Otherwise, params holds the coefficients
    for the texture-coordinate generation function specified by pname.
    """

def glTexImage1D(
    target: set[str],
    level: int,
    internalformat: int,
    width: int,
    border: int,
    format: set[str],
    type: set[str],
    pixels: Buffer,
) -> None:
    """Specify a one-dimensional texture image`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexImage1D.xhtml>`__

        :param target: Specifies the target texture.
        :param level: Specifies the level-of-detail number. Level 0 is the base image level.
    Level n is the nth mipmap reduction image.
        :param internalformat: Specifies the number of color components in the texture.
        :param width: Specifies the width of the texture image. Must be 2n+2(border)
    for some integer n. All implementations support texture images that are
    at least 64 texels wide. The height of the 1D texture image is 1.
        :param border: Specifies the width of the border. Must be either 0 or 1.
        :param format: Specifies the format of the pixel data.
        :param type: Specifies the data type of the pixel data.
        :param pixels: Specifies a pointer to the image data in memory.
    """

def glTexImage2D(
    target: set[str],
    level: int,
    internalformat: int,
    width: int,
    height: int,
    border: int,
    format: set[str],
    type: set[str],
    pixels: Buffer,
) -> None:
    """Specify a two-dimensional texture image`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexImage2D.xhtml>`__

        :param target: Specifies the target texture.
        :param level: Specifies the level-of-detail number. Level 0 is the base image level.
    Level n is the nth mipmap reduction image.
        :param internalformat: Specifies the number of color components in the texture.
        :param width: Specifies the width of the texture image. Must be 2n+2(border)
    for some integer n. All implementations support texture images that are at
    least 64 texels wide.
        :param height: Specifies the height of the texture image. Must be 2m+2(border) for
    some integer m. All implementations support texture images that are at
    least 64 texels high.
        :param border: Specifies the width of the border. Must be either 0 or 1.
        :param format: Specifies the format of the pixel data.
        :param type: Specifies the data type of the pixel data.
        :param pixels: Specifies a pointer to the image data in memory.
    """

def glTexImage2DMultisample(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: bool
) -> None:
    """ """

def glTexImage3D(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: int,
    p9: typing.Any,
) -> None:
    """ """

def glTexImage3DMultisample(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: bool
) -> None:
    """ """

def glTexParameter(target: set[str], pname: set[str], param: typing.Any) -> None:
    """B{glTexParameterf, glTexParameteri, glTexParameterfv, glTexParameteriv}Set texture parameters`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml>`__

        :param target: Specifies the target texture.
        :param pname: Specifies the symbolic name of a single-valued texture parameter.
        :param param: Specifies the value of pname. If function prototype ends in v specifies
    a pointer to an array where the value or values of pname are stored.
    """

def glTexParameterf(p0: int, p1: int, p2: float) -> None:
    """ """

def glTexParameterfv(p0: int, p1: int, p2: float) -> None:
    """ """

def glTexParameteri(p0: int, p1: int, p2: int) -> None:
    """ """

def glTexParameteriv(p0: int, p1: int, p2: int) -> None:
    """ """

def glTexSubImage1D(
    p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: typing.Any
) -> None:
    """ """

def glTexSubImage2D(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: typing.Any,
) -> None:
    """ """

def glTexSubImage3D(
    p0: int,
    p1: int,
    p2: int,
    p3: int,
    p4: int,
    p5: int,
    p6: int,
    p7: int,
    p8: int,
    p9: int,
    p10: typing.Any,
) -> None:
    """ """

def glTranslate(x: typing.Any, y, z) -> None:
    """B{glTranslatef, glTranslated}Multiply the current matrix by a translation matrix`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTranslate.xhtml>`__

    :param x: Specify the x, y, and z coordinates of a translation vector.
    """

def glUniform1f(p0: int, p1: float) -> None:
    """ """

def glUniform1fv(p0: int, p1: int, p2: float) -> None:
    """ """

def glUniform1i(p0: int, p1: int) -> None:
    """ """

def glUniform1iv(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniform2f(p0: int, p1: float, p2: float) -> None:
    """ """

def glUniform2fv(p0: int, p1: int, p2: float) -> None:
    """ """

def glUniform2i(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniform2iv(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniform3f(p0: int, p1: float, p2: float, p3: float) -> None:
    """ """

def glUniform3fv(p0: int, p1: int, p2: float) -> None:
    """ """

def glUniform3i(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glUniform3iv(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniform4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None:
    """ """

def glUniform4fv(p0: int, p1: int, p2: float) -> None:
    """ """

def glUniform4i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glUniform4iv(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniformBlockBinding(p0: int, p1: int, p2: int) -> None:
    """ """

def glUniformMatrix2fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix3fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix4fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: float) -> None:
    """ """

def glUnmapBuffer(p0: int) -> bool:
    """ """

def glUseProgram(program: int) -> None:
    """Installs a program object as part of current rendering state`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glUseProgram.xhtml>`__

    :param program: Specifies the handle of the program object whose executables are to be used as part of current rendering state.
    """

def glValidateProgram(program: int) -> None:
    """Validates a program object`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glValidateProgram.xhtml>`__

    :param program: Specifies the handle of the program object to be validated.
    """

def glVertexAttrib1d(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib1dv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib1f(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib1fv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib1s(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib1sv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib2d(p0: int, p1: float, p2: float) -> None:
    """ """

def glVertexAttrib2dv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib2f(p0: int, p1: float, p2: float) -> None:
    """ """

def glVertexAttrib2fv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib2s(p0: int, p1: int, p2: int) -> None:
    """ """

def glVertexAttrib2sv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib3d(p0: int, p1: float, p2: float, p3: float) -> None:
    """ """

def glVertexAttrib3dv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib3f(p0: int, p1: float, p2: float, p3: float) -> None:
    """ """

def glVertexAttrib3fv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib3s(p0: int, p1: int, p2: int, p3: int) -> None:
    """ """

def glVertexAttrib3sv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Nbv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Niv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Nsv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Nub(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glVertexAttrib4Nubv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Nuiv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4Nusv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4bv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4d(p0: int, p1: float, p2: float, p3: float, p4: float) -> None:
    """ """

def glVertexAttrib4dv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None:
    """ """

def glVertexAttrib4fv(p0: int, p1: float) -> None:
    """ """

def glVertexAttrib4iv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4s(p0: int, p1: int, p2: int, p3: int, p4: int) -> None:
    """ """

def glVertexAttrib4sv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4ubv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4uiv(p0: int, p1: int) -> None:
    """ """

def glVertexAttrib4usv(p0: int, p1: int) -> None:
    """ """

def glVertexAttribIPointer(p0: int, p1: int, p2: int, p3: int, p4: typing.Any) -> None:
    """ """

def glVertexAttribPointer(
    p0: int, p1: int, p2: int, p3: bool, p4: int, p5: typing.Any
) -> None:
    """ """

def glViewport(x: int, y, width: int, height) -> None:
    """Set the viewport`OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml>`__

        :param x: Specify the lower left corner of the viewport rectangle,
    in pixels. The initial value is (0,0).
        :param width: Specify the width and height of the viewport. When a GL
    context is first attached to a window, width and height are set to the
    dimensions of that window.
    """

GL_ACTIVE_ATTRIBUTES: float

GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: float

GL_ACTIVE_TEXTURE: float

GL_ACTIVE_UNIFORMS: float

GL_ACTIVE_UNIFORM_BLOCKS: float

GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: float

GL_ACTIVE_UNIFORM_MAX_LENGTH: float

GL_ALIASED_LINE_WIDTH_RANGE: float

GL_ALPHA: float

GL_ALREADY_SIGNALED: float

GL_ALWAYS: float

GL_AND: float

GL_AND_INVERTED: float

GL_AND_REVERSE: float

GL_ANY_SAMPLES_PASSED: float

GL_ARRAY_BUFFER: float

GL_ARRAY_BUFFER_BINDING: float

GL_ATTACHED_SHADERS: float

GL_BACK: float

GL_BACK_LEFT: float

GL_BACK_RIGHT: float

GL_BGR: float

GL_BGRA: float

GL_BGRA_INTEGER: float

GL_BGR_INTEGER: float

GL_BLEND: float

GL_BLEND_DST: float

GL_BLEND_DST_ALPHA: float

GL_BLEND_DST_RGB: float

GL_BLEND_EQUATION_ALPHA: float

GL_BLEND_EQUATION_RGB: float

GL_BLEND_SRC: float

GL_BLEND_SRC_ALPHA: float

GL_BLEND_SRC_RGB: float

GL_BLUE: float

GL_BLUE_INTEGER: float

GL_BOOL: float

GL_BOOL_VEC2: float

GL_BOOL_VEC3: float

GL_BOOL_VEC4: float

GL_BUFFER_ACCESS: float

GL_BUFFER_ACCESS_FLAGS: float

GL_BUFFER_MAPPED: float

GL_BUFFER_MAP_LENGTH: float

GL_BUFFER_MAP_OFFSET: float

GL_BUFFER_MAP_POINTER: float

GL_BUFFER_SIZE: float

GL_BUFFER_USAGE: float

GL_BYTE: float

GL_CCW: float

GL_CLAMP_READ_COLOR: float

GL_CLAMP_TO_BORDER: float

GL_CLAMP_TO_EDGE: float

GL_CLEAR: float

GL_CLIP_DISTANCE0: float

GL_CLIP_DISTANCE1: float

GL_CLIP_DISTANCE2: float

GL_CLIP_DISTANCE3: float

GL_CLIP_DISTANCE4: float

GL_CLIP_DISTANCE5: float

GL_CLIP_DISTANCE6: float

GL_CLIP_DISTANCE7: float

GL_COLOR: float

GL_COLOR_ATTACHMENT0: float

GL_COLOR_ATTACHMENT1: float

GL_COLOR_ATTACHMENT10: float

GL_COLOR_ATTACHMENT11: float

GL_COLOR_ATTACHMENT12: float

GL_COLOR_ATTACHMENT13: float

GL_COLOR_ATTACHMENT14: float

GL_COLOR_ATTACHMENT15: float

GL_COLOR_ATTACHMENT16: float

GL_COLOR_ATTACHMENT17: float

GL_COLOR_ATTACHMENT18: float

GL_COLOR_ATTACHMENT19: float

GL_COLOR_ATTACHMENT2: float

GL_COLOR_ATTACHMENT20: float

GL_COLOR_ATTACHMENT21: float

GL_COLOR_ATTACHMENT22: float

GL_COLOR_ATTACHMENT23: float

GL_COLOR_ATTACHMENT24: float

GL_COLOR_ATTACHMENT25: float

GL_COLOR_ATTACHMENT26: float

GL_COLOR_ATTACHMENT27: float

GL_COLOR_ATTACHMENT28: float

GL_COLOR_ATTACHMENT29: float

GL_COLOR_ATTACHMENT3: float

GL_COLOR_ATTACHMENT30: float

GL_COLOR_ATTACHMENT31: float

GL_COLOR_ATTACHMENT4: float

GL_COLOR_ATTACHMENT5: float

GL_COLOR_ATTACHMENT6: float

GL_COLOR_ATTACHMENT7: float

GL_COLOR_ATTACHMENT8: float

GL_COLOR_ATTACHMENT9: float

GL_COLOR_BUFFER_BIT: float

GL_COLOR_CLEAR_VALUE: float

GL_COLOR_LOGIC_OP: float

GL_COLOR_WRITEMASK: float

GL_COMPARE_REF_TO_TEXTURE: float

GL_COMPILE_STATUS: float

GL_COMPRESSED_RED: float

GL_COMPRESSED_RED_RGTC1: float

GL_COMPRESSED_RG: float

GL_COMPRESSED_RGB: float

GL_COMPRESSED_RGBA: float

GL_COMPRESSED_RG_RGTC2: float

GL_COMPRESSED_SIGNED_RED_RGTC1: float

GL_COMPRESSED_SIGNED_RG_RGTC2: float

GL_COMPRESSED_SRGB: float

GL_COMPRESSED_SRGB_ALPHA: float

GL_COMPRESSED_TEXTURE_FORMATS: float

GL_CONDITION_SATISFIED: float

GL_CONSTANT_ALPHA: float

GL_CONSTANT_COLOR: float

GL_CONTEXT_COMPATIBILITY_PROFILE_BIT: float

GL_CONTEXT_CORE_PROFILE_BIT: float

GL_CONTEXT_FLAGS: float

GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT: float

GL_CONTEXT_PROFILE_MASK: float

GL_COPY: float

GL_COPY_INVERTED: float

GL_COPY_READ_BUFFER: float

GL_COPY_WRITE_BUFFER: float

GL_CULL_FACE: float

GL_CULL_FACE_MODE: float

GL_CURRENT_PROGRAM: float

GL_CURRENT_QUERY: float

GL_CURRENT_VERTEX_ATTRIB: float

GL_CW: float

GL_DECR: float

GL_DECR_WRAP: float

GL_DELETE_STATUS: float

GL_DEPTH: float

GL_DEPTH24_STENCIL8: float

GL_DEPTH32F_STENCIL8: float

GL_DEPTH_ATTACHMENT: float

GL_DEPTH_BUFFER_BIT: float

GL_DEPTH_CLAMP: float

GL_DEPTH_CLEAR_VALUE: float

GL_DEPTH_COMPONENT: float

GL_DEPTH_COMPONENT16: float

GL_DEPTH_COMPONENT24: float

GL_DEPTH_COMPONENT32: float

GL_DEPTH_COMPONENT32F: float

GL_DEPTH_FUNC: float

GL_DEPTH_RANGE: float

GL_DEPTH_STENCIL: float

GL_DEPTH_STENCIL_ATTACHMENT: float

GL_DEPTH_TEST: float

GL_DEPTH_WRITEMASK: float

GL_DITHER: float

GL_DONT_CARE: float

GL_DOUBLE: float

GL_DOUBLEBUFFER: float

GL_DRAW_BUFFER: float

GL_DRAW_BUFFER0: float

GL_DRAW_BUFFER1: float

GL_DRAW_BUFFER10: float

GL_DRAW_BUFFER11: float

GL_DRAW_BUFFER12: float

GL_DRAW_BUFFER13: float

GL_DRAW_BUFFER14: float

GL_DRAW_BUFFER15: float

GL_DRAW_BUFFER2: float

GL_DRAW_BUFFER3: float

GL_DRAW_BUFFER4: float

GL_DRAW_BUFFER5: float

GL_DRAW_BUFFER6: float

GL_DRAW_BUFFER7: float

GL_DRAW_BUFFER8: float

GL_DRAW_BUFFER9: float

GL_DRAW_FRAMEBUFFER: float

GL_DRAW_FRAMEBUFFER_BINDING: float

GL_DST_ALPHA: float

GL_DST_COLOR: float

GL_DYNAMIC_COPY: float

GL_DYNAMIC_DRAW: float

GL_DYNAMIC_READ: float

GL_ELEMENT_ARRAY_BUFFER: float

GL_ELEMENT_ARRAY_BUFFER_BINDING: float

GL_EQUAL: float

GL_EQUIV: float

GL_EXTENSIONS: float

GL_FALSE: float

GL_FASTEST: float

GL_FILL: float

GL_FIRST_VERTEX_CONVENTION: float

GL_FIXED_ONLY: float

GL_FLOAT: float

GL_FLOAT_32_UNSIGNED_INT_24_8_REV: float

GL_FLOAT_MAT2: float

GL_FLOAT_MAT2x3: float

GL_FLOAT_MAT2x4: float

GL_FLOAT_MAT3: float

GL_FLOAT_MAT3x2: float

GL_FLOAT_MAT3x4: float

GL_FLOAT_MAT4: float

GL_FLOAT_MAT4x2: float

GL_FLOAT_MAT4x3: float

GL_FLOAT_VEC2: float

GL_FLOAT_VEC3: float

GL_FLOAT_VEC4: float

GL_FRAGMENT_SHADER: float

GL_FRAGMENT_SHADER_DERIVATIVE_HINT: float

GL_FRAMEBUFFER: float

GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: float

GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: float

GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_LAYERED: float

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: float

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: float

GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: float

GL_FRAMEBUFFER_BINDING: float

GL_FRAMEBUFFER_COMPLETE: float

GL_FRAMEBUFFER_DEFAULT: float

GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: float

GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER: float

GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: float

GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: float

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: float

GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER: float

GL_FRAMEBUFFER_SRGB: float

GL_FRAMEBUFFER_UNDEFINED: float

GL_FRAMEBUFFER_UNSUPPORTED: float

GL_FRONT: float

GL_FRONT_AND_BACK: float

GL_FRONT_FACE: float

GL_FRONT_LEFT: float

GL_FRONT_RIGHT: float

GL_FUNC_ADD: float

GL_FUNC_REVERSE_SUBTRACT: float

GL_FUNC_SUBTRACT: float

GL_GEOMETRY_INPUT_TYPE: float

GL_GEOMETRY_OUTPUT_TYPE: float

GL_GEOMETRY_SHADER: float

GL_GEOMETRY_VERTICES_OUT: float

GL_GEQUAL: float

GL_GREATER: float

GL_GREEN: float

GL_GREEN_INTEGER: float

GL_HALF_FLOAT: float

GL_INCR: float

GL_INCR_WRAP: float

GL_INDEX: float

GL_INFO_LOG_LENGTH: float

GL_INT: float

GL_INTERLEAVED_ATTRIBS: float

GL_INT_2_10_10_10_REV: float

GL_INT_SAMPLER_1D: float

GL_INT_SAMPLER_1D_ARRAY: float

GL_INT_SAMPLER_2D: float

GL_INT_SAMPLER_2D_ARRAY: float

GL_INT_SAMPLER_2D_MULTISAMPLE: float

GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_INT_SAMPLER_2D_RECT: float

GL_INT_SAMPLER_3D: float

GL_INT_SAMPLER_BUFFER: float

GL_INT_SAMPLER_CUBE: float

GL_INT_VEC2: float

GL_INT_VEC3: float

GL_INT_VEC4: float

GL_INVALID_ENUM: float

GL_INVALID_FRAMEBUFFER_OPERATION: float

GL_INVALID_INDEX: float

GL_INVALID_OPERATION: float

GL_INVALID_VALUE: float

GL_INVERT: float

GL_KEEP: float

GL_LAST_VERTEX_CONVENTION: float

GL_LEFT: float

GL_LEQUAL: float

GL_LESS: float

GL_LINE: float

GL_LINEAR: float

GL_LINEAR_MIPMAP_LINEAR: float

GL_LINEAR_MIPMAP_NEAREST: float

GL_LINES: float

GL_LINES_ADJACENCY: float

GL_LINE_LOOP: float

GL_LINE_SMOOTH: float

GL_LINE_SMOOTH_HINT: float

GL_LINE_STRIP: float

GL_LINE_STRIP_ADJACENCY: float

GL_LINE_WIDTH: float

GL_LINE_WIDTH_GRANULARITY: float

GL_LINE_WIDTH_RANGE: float

GL_LINK_STATUS: float

GL_LOGIC_OP_MODE: float

GL_LOWER_LEFT: float

GL_MAJOR_VERSION: float

GL_MAP_FLUSH_EXPLICIT_BIT: float

GL_MAP_INVALIDATE_BUFFER_BIT: float

GL_MAP_INVALIDATE_RANGE_BIT: float

GL_MAP_READ_BIT: float

GL_MAP_UNSYNCHRONIZED_BIT: float

GL_MAP_WRITE_BIT: float

GL_MAX: float

GL_MAX_3D_TEXTURE_SIZE: float

GL_MAX_ARRAY_TEXTURE_LAYERS: float

GL_MAX_CLIP_DISTANCES: float

GL_MAX_COLOR_ATTACHMENTS: float

GL_MAX_COLOR_TEXTURE_SAMPLES: float

GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: float

GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: float

GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: float

GL_MAX_COMBINED_UNIFORM_BLOCKS: float

GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: float

GL_MAX_CUBE_MAP_TEXTURE_SIZE: float

GL_MAX_DEPTH_TEXTURE_SAMPLES: float

GL_MAX_DRAW_BUFFERS: float

GL_MAX_DUAL_SOURCE_DRAW_BUFFERS: float

GL_MAX_ELEMENTS_INDICES: float

GL_MAX_ELEMENTS_VERTICES: float

GL_MAX_FRAGMENT_INPUT_COMPONENTS: float

GL_MAX_FRAGMENT_UNIFORM_BLOCKS: float

GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: float

GL_MAX_GEOMETRY_INPUT_COMPONENTS: float

GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: float

GL_MAX_GEOMETRY_OUTPUT_VERTICES: float

GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: float

GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: float

GL_MAX_GEOMETRY_UNIFORM_BLOCKS: float

GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: float

GL_MAX_INTEGER_SAMPLES: float

GL_MAX_PROGRAM_TEXEL_OFFSET: float

GL_MAX_RECTANGLE_TEXTURE_SIZE: float

GL_MAX_RENDERBUFFER_SIZE: float

GL_MAX_SAMPLES: float

GL_MAX_SAMPLE_MASK_WORDS: float

GL_MAX_SERVER_WAIT_TIMEOUT: float

GL_MAX_TEXTURE_BUFFER_SIZE: float

GL_MAX_TEXTURE_IMAGE_UNITS: float

GL_MAX_TEXTURE_LOD_BIAS: float

GL_MAX_TEXTURE_SIZE: float

GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: float

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: float

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: float

GL_MAX_UNIFORM_BLOCK_SIZE: float

GL_MAX_UNIFORM_BUFFER_BINDINGS: float

GL_MAX_VARYING_COMPONENTS: float

GL_MAX_VARYING_FLOATS: float

GL_MAX_VERTEX_ATTRIBS: float

GL_MAX_VERTEX_OUTPUT_COMPONENTS: float

GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: float

GL_MAX_VERTEX_UNIFORM_BLOCKS: float

GL_MAX_VERTEX_UNIFORM_COMPONENTS: float

GL_MAX_VIEWPORT_DIMS: float

GL_MIN: float

GL_MINOR_VERSION: float

GL_MIN_PROGRAM_TEXEL_OFFSET: float

GL_MIRRORED_REPEAT: float

GL_MULTISAMPLE: float

GL_NAND: float

GL_NEAREST: float

GL_NEAREST_MIPMAP_LINEAR: float

GL_NEAREST_MIPMAP_NEAREST: float

GL_NEVER: float

GL_NICEST: float

GL_NONE: float

GL_NOOP: float

GL_NOR: float

GL_NOTEQUAL: float

GL_NO_ERROR: float

GL_NUM_COMPRESSED_TEXTURE_FORMATS: float

GL_NUM_EXTENSIONS: float

GL_OBJECT_TYPE: float

GL_ONE: float

GL_ONE_MINUS_CONSTANT_ALPHA: float

GL_ONE_MINUS_CONSTANT_COLOR: float

GL_ONE_MINUS_DST_ALPHA: float

GL_ONE_MINUS_DST_COLOR: float

GL_ONE_MINUS_SRC1_ALPHA: float

GL_ONE_MINUS_SRC1_COLOR: float

GL_ONE_MINUS_SRC_ALPHA: float

GL_ONE_MINUS_SRC_COLOR: float

GL_OR: float

GL_OR_INVERTED: float

GL_OR_REVERSE: float

GL_OUT_OF_MEMORY: float

GL_PACK_ALIGNMENT: float

GL_PACK_IMAGE_HEIGHT: float

GL_PACK_LSB_FIRST: float

GL_PACK_ROW_LENGTH: float

GL_PACK_SKIP_IMAGES: float

GL_PACK_SKIP_PIXELS: float

GL_PACK_SKIP_ROWS: float

GL_PACK_SWAP_BYTES: float

GL_PIXEL_PACK_BUFFER: float

GL_PIXEL_PACK_BUFFER_BINDING: float

GL_PIXEL_UNPACK_BUFFER: float

GL_PIXEL_UNPACK_BUFFER_BINDING: float

GL_POINT: float

GL_POINTS: float

GL_POINT_FADE_THRESHOLD_SIZE: float

GL_POINT_SIZE: float

GL_POINT_SPRITE_COORD_ORIGIN: float

GL_POLYGON_MODE: float

GL_POLYGON_OFFSET_FACTOR: float

GL_POLYGON_OFFSET_FILL: float

GL_POLYGON_OFFSET_LINE: float

GL_POLYGON_OFFSET_POINT: float

GL_POLYGON_OFFSET_UNITS: float

GL_POLYGON_SMOOTH: float

GL_POLYGON_SMOOTH_HINT: float

GL_PRIMITIVES_GENERATED: float

GL_PRIMITIVE_RESTART: float

GL_PRIMITIVE_RESTART_INDEX: float

GL_PROGRAM_POINT_SIZE: float

GL_PROVOKING_VERTEX: float

GL_PROXY_TEXTURE_1D: float

GL_PROXY_TEXTURE_1D_ARRAY: float

GL_PROXY_TEXTURE_2D: float

GL_PROXY_TEXTURE_2D_ARRAY: float

GL_PROXY_TEXTURE_2D_MULTISAMPLE: float

GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY: float

GL_PROXY_TEXTURE_3D: float

GL_PROXY_TEXTURE_CUBE_MAP: float

GL_PROXY_TEXTURE_RECTANGLE: float

GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION: float

GL_QUERY_BY_REGION_NO_WAIT: float

GL_QUERY_BY_REGION_WAIT: float

GL_QUERY_COUNTER_BITS: float

GL_QUERY_NO_WAIT: float

GL_QUERY_RESULT: float

GL_QUERY_RESULT_AVAILABLE: float

GL_QUERY_WAIT: float

GL_R11F_G11F_B10F: float

GL_R16: float

GL_R16F: float

GL_R16I: float

GL_R16UI: float

GL_R16_SNORM: float

GL_R32F: float

GL_R32I: float

GL_R32UI: float

GL_R3_G3_B2: float

GL_R8: float

GL_R8I: float

GL_R8UI: float

GL_R8_SNORM: float

GL_RASTERIZER_DISCARD: float

GL_READ_BUFFER: float

GL_READ_FRAMEBUFFER: float

GL_READ_FRAMEBUFFER_BINDING: float

GL_READ_ONLY: float

GL_READ_WRITE: float

GL_RED: float

GL_RED_INTEGER: float

GL_RENDERBUFFER: float

GL_RENDERBUFFER_ALPHA_SIZE: float

GL_RENDERBUFFER_BINDING: float

GL_RENDERBUFFER_BLUE_SIZE: float

GL_RENDERBUFFER_DEPTH_SIZE: float

GL_RENDERBUFFER_GREEN_SIZE: float

GL_RENDERBUFFER_HEIGHT: float

GL_RENDERBUFFER_INTERNAL_FORMAT: float

GL_RENDERBUFFER_RED_SIZE: float

GL_RENDERBUFFER_SAMPLES: float

GL_RENDERBUFFER_STENCIL_SIZE: float

GL_RENDERBUFFER_WIDTH: float

GL_RENDERER: float

GL_REPEAT: float

GL_REPLACE: float

GL_RG: float

GL_RG16: float

GL_RG16F: float

GL_RG16I: float

GL_RG16UI: float

GL_RG16_SNORM: float

GL_RG32F: float

GL_RG32I: float

GL_RG32UI: float

GL_RG8: float

GL_RG8I: float

GL_RG8UI: float

GL_RG8_SNORM: float

GL_RGB: float

GL_RGB10: float

GL_RGB10_A2: float

GL_RGB10_A2UI: float

GL_RGB12: float

GL_RGB16: float

GL_RGB16F: float

GL_RGB16I: float

GL_RGB16UI: float

GL_RGB16_SNORM: float

GL_RGB32F: float

GL_RGB32I: float

GL_RGB32UI: float

GL_RGB4: float

GL_RGB5: float

GL_RGB5_A1: float

GL_RGB8: float

GL_RGB8I: float

GL_RGB8UI: float

GL_RGB8_SNORM: float

GL_RGB9_E5: float

GL_RGBA: float

GL_RGBA12: float

GL_RGBA16: float

GL_RGBA16F: float

GL_RGBA16I: float

GL_RGBA16UI: float

GL_RGBA16_SNORM: float

GL_RGBA2: float

GL_RGBA32F: float

GL_RGBA32I: float

GL_RGBA32UI: float

GL_RGBA4: float

GL_RGBA8: float

GL_RGBA8I: float

GL_RGBA8UI: float

GL_RGBA8_SNORM: float

GL_RGBA_INTEGER: float

GL_RGB_INTEGER: float

GL_RG_INTEGER: float

GL_RIGHT: float

GL_SAMPLER_1D: float

GL_SAMPLER_1D_ARRAY: float

GL_SAMPLER_1D_ARRAY_SHADOW: float

GL_SAMPLER_1D_SHADOW: float

GL_SAMPLER_2D: float

GL_SAMPLER_2D_ARRAY: float

GL_SAMPLER_2D_ARRAY_SHADOW: float

GL_SAMPLER_2D_MULTISAMPLE: float

GL_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_SAMPLER_2D_RECT: float

GL_SAMPLER_2D_RECT_SHADOW: float

GL_SAMPLER_2D_SHADOW: float

GL_SAMPLER_3D: float

GL_SAMPLER_BINDING: float

GL_SAMPLER_BUFFER: float

GL_SAMPLER_CUBE: float

GL_SAMPLER_CUBE_SHADOW: float

GL_SAMPLES: float

GL_SAMPLES_PASSED: float

GL_SAMPLE_ALPHA_TO_COVERAGE: float

GL_SAMPLE_ALPHA_TO_ONE: float

GL_SAMPLE_BUFFERS: float

GL_SAMPLE_COVERAGE: float

GL_SAMPLE_COVERAGE_INVERT: float

GL_SAMPLE_COVERAGE_VALUE: float

GL_SAMPLE_MASK: float

GL_SAMPLE_MASK_VALUE: float

GL_SAMPLE_POSITION: float

GL_SCISSOR_BOX: float

GL_SCISSOR_TEST: float

GL_SEPARATE_ATTRIBS: float

GL_SET: float

GL_SHADER_SOURCE_LENGTH: float

GL_SHADER_TYPE: float

GL_SHADING_LANGUAGE_VERSION: float

GL_SHORT: float

GL_SIGNALED: float

GL_SIGNED_NORMALIZED: float

GL_SMOOTH_LINE_WIDTH_GRANULARITY: float

GL_SMOOTH_LINE_WIDTH_RANGE: float

GL_SMOOTH_POINT_SIZE_GRANULARITY: float

GL_SMOOTH_POINT_SIZE_RANGE: float

GL_SRC1_COLOR: float

GL_SRC_ALPHA: float

GL_SRC_ALPHA_SATURATE: float

GL_SRC_COLOR: float

GL_SRGB: float

GL_SRGB8: float

GL_SRGB8_ALPHA8: float

GL_SRGB_ALPHA: float

GL_STATIC_COPY: float

GL_STATIC_DRAW: float

GL_STATIC_READ: float

GL_STENCIL: float

GL_STENCIL_ATTACHMENT: float

GL_STENCIL_BACK_FAIL: float

GL_STENCIL_BACK_FUNC: float

GL_STENCIL_BACK_PASS_DEPTH_FAIL: float

GL_STENCIL_BACK_PASS_DEPTH_PASS: float

GL_STENCIL_BACK_REF: float

GL_STENCIL_BACK_VALUE_MASK: float

GL_STENCIL_BACK_WRITEMASK: float

GL_STENCIL_BUFFER_BIT: float

GL_STENCIL_CLEAR_VALUE: float

GL_STENCIL_FAIL: float

GL_STENCIL_FUNC: float

GL_STENCIL_INDEX: float

GL_STENCIL_INDEX1: float

GL_STENCIL_INDEX16: float

GL_STENCIL_INDEX4: float

GL_STENCIL_INDEX8: float

GL_STENCIL_PASS_DEPTH_FAIL: float

GL_STENCIL_PASS_DEPTH_PASS: float

GL_STENCIL_REF: float

GL_STENCIL_TEST: float

GL_STENCIL_VALUE_MASK: float

GL_STENCIL_WRITEMASK: float

GL_STEREO: float

GL_STREAM_COPY: float

GL_STREAM_DRAW: float

GL_STREAM_READ: float

GL_SUBPIXEL_BITS: float

GL_SYNC_CONDITION: float

GL_SYNC_FENCE: float

GL_SYNC_FLAGS: float

GL_SYNC_FLUSH_COMMANDS_BIT: float

GL_SYNC_GPU_COMMANDS_COMPLETE: float

GL_SYNC_STATUS: float

GL_TEXTURE: float

GL_TEXTURE0: float

GL_TEXTURE1: float

GL_TEXTURE10: float

GL_TEXTURE11: float

GL_TEXTURE12: float

GL_TEXTURE13: float

GL_TEXTURE14: float

GL_TEXTURE15: float

GL_TEXTURE16: float

GL_TEXTURE17: float

GL_TEXTURE18: float

GL_TEXTURE19: float

GL_TEXTURE2: float

GL_TEXTURE20: float

GL_TEXTURE21: float

GL_TEXTURE22: float

GL_TEXTURE23: float

GL_TEXTURE24: float

GL_TEXTURE25: float

GL_TEXTURE26: float

GL_TEXTURE27: float

GL_TEXTURE28: float

GL_TEXTURE29: float

GL_TEXTURE3: float

GL_TEXTURE30: float

GL_TEXTURE31: float

GL_TEXTURE4: float

GL_TEXTURE5: float

GL_TEXTURE6: float

GL_TEXTURE7: float

GL_TEXTURE8: float

GL_TEXTURE9: float

GL_TEXTURE_1D: float

GL_TEXTURE_1D_ARRAY: float

GL_TEXTURE_2D: float

GL_TEXTURE_2D_ARRAY: float

GL_TEXTURE_2D_MULTISAMPLE: float

GL_TEXTURE_2D_MULTISAMPLE_ARRAY: float

GL_TEXTURE_3D: float

GL_TEXTURE_ALPHA_SIZE: float

GL_TEXTURE_ALPHA_TYPE: float

GL_TEXTURE_BASE_LEVEL: float

GL_TEXTURE_BINDING_1D: float

GL_TEXTURE_BINDING_1D_ARRAY: float

GL_TEXTURE_BINDING_2D: float

GL_TEXTURE_BINDING_2D_ARRAY: float

GL_TEXTURE_BINDING_2D_MULTISAMPLE: float

GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: float

GL_TEXTURE_BINDING_3D: float

GL_TEXTURE_BINDING_BUFFER: float

GL_TEXTURE_BINDING_CUBE_MAP: float

GL_TEXTURE_BINDING_RECTANGLE: float

GL_TEXTURE_BLUE_SIZE: float

GL_TEXTURE_BLUE_TYPE: float

GL_TEXTURE_BORDER_COLOR: float

GL_TEXTURE_BUFFER: float

GL_TEXTURE_BUFFER_DATA_STORE_BINDING: float

GL_TEXTURE_COMPARE_FUNC: float

GL_TEXTURE_COMPARE_MODE: float

GL_TEXTURE_COMPRESSED: float

GL_TEXTURE_COMPRESSED_IMAGE_SIZE: float

GL_TEXTURE_COMPRESSION_HINT: float

GL_TEXTURE_CUBE_MAP: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_X: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: float

GL_TEXTURE_CUBE_MAP_POSITIVE_X: float

GL_TEXTURE_CUBE_MAP_POSITIVE_Y: float

GL_TEXTURE_CUBE_MAP_POSITIVE_Z: float

GL_TEXTURE_CUBE_MAP_SEAMLESS: float

GL_TEXTURE_DEPTH: float

GL_TEXTURE_DEPTH_SIZE: float

GL_TEXTURE_DEPTH_TYPE: float

GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: float

GL_TEXTURE_GREEN_SIZE: float

GL_TEXTURE_GREEN_TYPE: float

GL_TEXTURE_HEIGHT: float

GL_TEXTURE_INTERNAL_FORMAT: float

GL_TEXTURE_LOD_BIAS: float

GL_TEXTURE_MAG_FILTER: float

GL_TEXTURE_MAX_LEVEL: float

GL_TEXTURE_MAX_LOD: float

GL_TEXTURE_MIN_FILTER: float

GL_TEXTURE_MIN_LOD: float

GL_TEXTURE_RECTANGLE: float

GL_TEXTURE_RED_SIZE: float

GL_TEXTURE_RED_TYPE: float

GL_TEXTURE_SAMPLES: float

GL_TEXTURE_SHARED_SIZE: float

GL_TEXTURE_STENCIL_SIZE: float

GL_TEXTURE_SWIZZLE_A: float

GL_TEXTURE_SWIZZLE_B: float

GL_TEXTURE_SWIZZLE_G: float

GL_TEXTURE_SWIZZLE_R: float

GL_TEXTURE_SWIZZLE_RGBA: float

GL_TEXTURE_WIDTH: float

GL_TEXTURE_WRAP_R: float

GL_TEXTURE_WRAP_S: float

GL_TEXTURE_WRAP_T: float

GL_TIMEOUT_EXPIRED: float

GL_TIMEOUT_IGNORED: float

GL_TIMESTAMP: float

GL_TIME_ELAPSED: float

GL_TRANSFORM_FEEDBACK_BUFFER: float

GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: float

GL_TRANSFORM_FEEDBACK_BUFFER_MODE: float

GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: float

GL_TRANSFORM_FEEDBACK_BUFFER_START: float

GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: float

GL_TRANSFORM_FEEDBACK_VARYINGS: float

GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: float

GL_TRIANGLES: float

GL_TRIANGLES_ADJACENCY: float

GL_TRIANGLE_FAN: float

GL_TRIANGLE_STRIP: float

GL_TRIANGLE_STRIP_ADJACENCY: float

GL_TRUE: float

GL_UNIFORM_ARRAY_STRIDE: float

GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: float

GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: float

GL_UNIFORM_BLOCK_BINDING: float

GL_UNIFORM_BLOCK_DATA_SIZE: float

GL_UNIFORM_BLOCK_INDEX: float

GL_UNIFORM_BLOCK_NAME_LENGTH: float

GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: float

GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER: float

GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: float

GL_UNIFORM_BUFFER: float

GL_UNIFORM_BUFFER_BINDING: float

GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: float

GL_UNIFORM_BUFFER_SIZE: float

GL_UNIFORM_BUFFER_START: float

GL_UNIFORM_IS_ROW_MAJOR: float

GL_UNIFORM_MATRIX_STRIDE: float

GL_UNIFORM_NAME_LENGTH: float

GL_UNIFORM_OFFSET: float

GL_UNIFORM_SIZE: float

GL_UNIFORM_TYPE: float

GL_UNPACK_ALIGNMENT: float

GL_UNPACK_IMAGE_HEIGHT: float

GL_UNPACK_LSB_FIRST: float

GL_UNPACK_ROW_LENGTH: float

GL_UNPACK_SKIP_IMAGES: float

GL_UNPACK_SKIP_PIXELS: float

GL_UNPACK_SKIP_ROWS: float

GL_UNPACK_SWAP_BYTES: float

GL_UNSIGNALED: float

GL_UNSIGNED_BYTE: float

GL_UNSIGNED_BYTE_2_3_3_REV: float

GL_UNSIGNED_BYTE_3_3_2: float

GL_UNSIGNED_INT: float

GL_UNSIGNED_INT_10F_11F_11F_REV: float

GL_UNSIGNED_INT_10_10_10_2: float

GL_UNSIGNED_INT_24_8: float

GL_UNSIGNED_INT_2_10_10_10_REV: float

GL_UNSIGNED_INT_5_9_9_9_REV: float

GL_UNSIGNED_INT_8_8_8_8: float

GL_UNSIGNED_INT_8_8_8_8_REV: float

GL_UNSIGNED_INT_SAMPLER_1D: float

GL_UNSIGNED_INT_SAMPLER_1D_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D: float

GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: float

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D_RECT: float

GL_UNSIGNED_INT_SAMPLER_3D: float

GL_UNSIGNED_INT_SAMPLER_BUFFER: float

GL_UNSIGNED_INT_SAMPLER_CUBE: float

GL_UNSIGNED_INT_VEC2: float

GL_UNSIGNED_INT_VEC3: float

GL_UNSIGNED_INT_VEC4: float

GL_UNSIGNED_NORMALIZED: float

GL_UNSIGNED_SHORT: float

GL_UNSIGNED_SHORT_1_5_5_5_REV: float

GL_UNSIGNED_SHORT_4_4_4_4: float

GL_UNSIGNED_SHORT_4_4_4_4_REV: float

GL_UNSIGNED_SHORT_5_5_5_1: float

GL_UNSIGNED_SHORT_5_6_5: float

GL_UNSIGNED_SHORT_5_6_5_REV: float

GL_UPPER_LEFT: float

GL_VALIDATE_STATUS: float

GL_VENDOR: float

GL_VERSION: float

GL_VERTEX_ARRAY_BINDING: float

GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: float

GL_VERTEX_ATTRIB_ARRAY_DIVISOR: float

GL_VERTEX_ATTRIB_ARRAY_ENABLED: float

GL_VERTEX_ATTRIB_ARRAY_INTEGER: float

GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: float

GL_VERTEX_ATTRIB_ARRAY_POINTER: float

GL_VERTEX_ATTRIB_ARRAY_SIZE: float

GL_VERTEX_ATTRIB_ARRAY_STRIDE: float

GL_VERTEX_ATTRIB_ARRAY_TYPE: float

GL_VERTEX_PROGRAM_POINT_SIZE: float

GL_VERTEX_SHADER: float

GL_VIEWPORT: float

GL_WAIT_FAILED: float

GL_WRITE_ONLY: float

GL_XOR: float

GL_ZERO: float
