import sys
import typing
import bpy


class Buffer:
    '''The Buffer object is simply a block of memory that is delineated and initialized by the user. Many OpenGL functions return data to a C-style pointer, however, because this is not possible in python the Buffer object can be used to this end. Wherever pointer notation is used in the OpenGL functions the Buffer object can be used in it’s bgl wrapper. In some instances the Buffer object will need to be initialized with the template parameter, while in other instances the user will want to create just a blank buffer which will be zeroed by default. '''

    dimensions = None
    '''The number of dimensions of the Buffer. '''

    def to_list(self):
        '''The contents of the Buffer as a python list. 

        '''
        pass

    def __init__(
            self,
            type: int,
            dimensions: int,
            template: 'bpy.context.object' = None) -> 'bpy.context.object':
        '''This will create a new Buffer object for use with other bgl OpenGL commands. Only the type of argument to store in the buffer and the dimensions of the buffer are necessary. Buffers are zeroed by default unless a template is supplied, in which case the buffer is initialized to the template. 

        :param type: The format to store data in. The type should be one of GL_BYTE, GL_SHORT, GL_INT, or GL_FLOAT. 
        :type type: int
        :param dimensions: If the dimensions are specified as an int a linear array will be created for the buffer. If a sequence is passed for the dimensions, the buffer becomes n-Dimensional, where n is equal to the number of parameters passed in the sequence. Example: [256,2] is a two- dimensional buffer while [256,256,4] creates a three- dimensional buffer. You can think of each additional dimension as a sub-item of the dimension to the left. i.e. [10,2] is a 10 element array each with 2 sub-items. [(0,0), (0,1), (1,0), (1,1), (2,0), …] etc. 
        :type dimensions: int
        :param template: A sequence of matching dimensions which will be used to initialize the Buffer. If a template is not passed in all fields will be initialized to 0. 
        :type template: 'bpy.context.object'
        :rtype: 'bpy.context.object'
        :return:  The newly created buffer as a PyObject. 
        '''
        pass


def glAccum(op: int, value: float):
    '''Operate on the accumulation buffer. 

    :param op: The accumulation buffer operation. 
    :type op: int
    :param value: a value used in the accumulation buffer operation. 
    :type value: float
    '''

    pass


def glActiveTexture(texture: int):
    '''Select active texture unit. 

    :param texture: Constant in GL_TEXTURE0 0 - 8 
    :type texture: int
    '''

    pass


def glAlphaFunc(func: int, ref: float):
    '''Specify the alpha test function. 

    :param func: Specifies the alpha comparison function. 
    :type func: int
    :param ref: The reference value that incoming alpha values are compared to. Clamped between 0 and 1. 
    :type ref: float
    '''

    pass


def glAreTexturesResident(n: int, textures: 'bpy.context.object',
                          residences: bool):
    '''Determine if textures are loaded in texture memory 

    :param n: Specifies the number of textures to be queried. 
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be queried 
    :type textures: 'bpy.context.object'
    :param residences: An array in which the texture residence status in returned. The residence status of a texture named by an element of textures is returned in the corresponding element of residences. 
    :type residences: bool
    '''

    pass


def glAttachShader(program: int, shader: int):
    '''Attaches a shader object to a program object. 

    :param program: Specifies the program object to which a shader object will be attached. 
    :type program: int
    :param shader: Specifies the shader object that is to be attached. 
    :type shader: int
    '''

    pass


def glBegin(mode: int):
    '''Delimit the vertices of a primitive or a group of like primatives 

    :param mode: Specifies the primitive that will be create from vertices between glBegin and glEnd. 
    :type mode: int
    '''

    pass


def glBindTexture(target: int, texture: int):
    '''Bind a named texture to a texturing target 

    :param target: Specifies the target to which the texture is bound. 
    :type target: int
    :param texture: Specifies the name of a texture. 
    :type texture: int
    '''

    pass


def glBitmap(width, height, xorig, yorig, xmove, ymove,
             bitmap: 'bpy.context.object'):
    '''Draw a bitmap 

    :param height: Specify the pixel width and height of the bitmap image. 
    :param yorig: Specify the location of the origin in the bitmap image. The origin is measured from the lower left corner of the bitmap, with right and up being the positive axes. 
    :param ymove: Specify the x and y offsets to be added to the current raster position after the bitmap is drawn. 
    :param bitmap: Specifies the address of the bitmap image. 
    :type bitmap: 'bpy.context.object'
    '''

    pass


def glBlendFunc(sfactor: int, dfactor: int):
    '''Specify pixel arithmetic 

    :param sfactor: Specifies how the red, green, blue, and alpha source blending factors are computed. 
    :type sfactor: int
    :param dfactor: Specifies how the red, green, blue, and alpha destination blending factors are computed. 
    :type dfactor: int
    '''

    pass


def glCallList(list: int):
    '''Execute a display list 

    :param list: Specifies the integer name of the display list to be executed. 
    :type list: int
    '''

    pass


def glCallLists(n: int, type: int, lists: 'bpy.context.object'):
    '''Execute a list of display lists 

    :param n: Specifies the number of display lists to be executed. 
    :type n: int
    :param type: Specifies the type of values in lists. 
    :type type: int
    :param lists: Specifies the address of an array of name offsets in the display list. The pointer type is void because the offsets can be bytes, shorts, ints, or floats, depending on the value of type. 
    :type lists: 'bpy.context.object'
    '''

    pass


def glClear(mask):
    '''Clear buffers to preset values 

    :param mask: Bitwise OR of masks that indicate the buffers to be cleared. 
    '''

    pass


def glClearAccum(red, green, blue, alpha):
    '''Specify clear values for the accumulation buffer 

    :param alpha: Specify the red, green, blue, and alpha values used when the accumulation buffer is cleared. The initial values are all 0. 
    '''

    pass


def glClearColor(red, green, blue, alpha):
    '''Specify clear values for the color buffers 

    :param alpha: Specify the red, green, blue, and alpha values used when the color buffers are cleared. The initial values are all 0. 
    '''

    pass


def glClearDepth(depth: int):
    '''Specify the clear value for the depth buffer 

    :param depth: Specifies the depth value used when the depth buffer is cleared. The initial value is 1. 
    :type depth: int
    '''

    pass


def glClearIndex(c: float):
    '''Specify the clear value for the color index buffers 

    :param c: Specifies the index used when the color index buffers are cleared. The initial value is 0. 
    :type c: float
    '''

    pass


def glClearStencil(s: int):
    '''Specify the clear value for the stencil buffer 

    :param s: Specifies the index used when the stencil buffer is cleared. The initial value is 0. 
    :type s: int
    '''

    pass


def glClipPlane(plane: int, equation: 'bpy.context.object'):
    '''Specify a plane against which all geometry is clipped 

    :param plane: Specifies which clipping plane is being positioned. 
    :type plane: int
    :param equation: Specifies the address of an array of four double- precision floating-point values. These values are interpreted as a plane equation. 
    :type equation: 'bpy.context.object'
    '''

    pass


def glColor(red, green, blue, alpha):
    '''Set a new color. 

    :param blue: Specify new red, green, and blue values for the current color. 
    :param alpha: Specifies a new alpha value for the current color. Included only in the four-argument glColor4 commands. (With ‘4’ colors only) 
    '''

    pass


def glColorMask(red, green, blue, alpha):
    '''Enable and disable writing of frame buffer color components 

    :param alpha: Specify whether red, green, blue, and alpha can or cannot be written into the frame buffer. The initial values are all GL_TRUE, indicating that the color components can be written. 
    '''

    pass


def glColorMaterial(face: int, mode: int):
    '''Cause a material color to track the current color 

    :param face: Specifies whether front, back, or both front and back material parameters should track the current color. 
    :type face: int
    :param mode: Specifies which of several material parameters track the current color. 
    :type mode: int
    '''

    pass


def glCompileShader(shader: int):
    '''Compiles a shader object. 

    :param shader: Specifies the shader object to be compiled. 
    :type shader: int
    '''

    pass


def glCopyPixels(x, y, width: int, height: int, type):
    '''Copy pixels into a 2D texture image 

    :param target: Specifies the target texture. 
    :type target: int
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param y: Specify the window coordinates of the first pixel that is copied from the frame buffer. This location is the lower left corner of a rectangular block of pixels. 
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. 
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for some integer m. All implementations support texture images that are at least 64 texels high. 
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    '''

    pass


def glCreateProgram() -> int:
    '''Creates a program object 

    :return:  The new program or zero if an error occurs. 
    '''

    pass


def glCreateShader(shaderType) -> int:
    '''Creates a shader object. 

    :return:  0 if an error occurs. 
    '''

    pass


def glCullFace(mode: int):
    '''Specify whether front- or back-facing facets can be culled 

    :param mode: Specifies whether front- or back-facing facets are candidates for culling. 
    :type mode: int
    '''

    pass


def glDeleteLists(list: int, range: int):
    '''Delete a contiguous group of display lists 

    :param list: Specifies the integer name of the first display list to delete 
    :type list: int
    :param range: Specifies the number of display lists to delete 
    :type range: int
    '''

    pass


def glDeleteProgram(program: int):
    '''Deletes a program object. 

    :param program: Specifies the program object to be deleted. 
    :type program: int
    '''

    pass


def glDeleteShader(shader: int):
    '''Deletes a shader object. 

    :param shader: Specifies the shader object to be deleted. 
    :type shader: int
    '''

    pass


def glDeleteTextures(n: int, textures: 'Buffer'):
    '''Delete named textures 

    :param n: Specifies the number of textures to be deleted 
    :type n: int
    :param textures: Specifies an array of textures to be deleted 
    :type textures: 'Buffer'
    '''

    pass


def glDepthFunc(func: int):
    '''Specify the value used for depth buffer comparisons 

    :param func: Specifies the depth comparison function. 
    :type func: int
    '''

    pass


def glDepthMask(flag: int):
    '''Enable or disable writing into the depth buffer 

    :param flag: Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE, depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer writing is enabled. 
    :type flag: int
    '''

    pass


def glDepthRange(zNear: int, zFar: int):
    '''Specify mapping of depth values from normalized device coordinates to window coordinates 

    :param zNear: Specifies the mapping of the near clipping plane to window coordinates. The initial value is 0. 
    :type zNear: int
    :param zFar: Specifies the mapping of the far clipping plane to window coordinates. The initial value is 1. 
    :type zFar: int
    '''

    pass


def glDetachShader(program: int, shader: int):
    '''Detaches a shader object from a program object to which it is attached. 

    :param program: Specifies the program object from which to detach the shader object. 
    :type program: int
    :param shader: pecifies the program object from which to detach the shader object. 
    :type shader: int
    '''

    pass


def glDisable(cap: int):
    '''Disable server-side GL capabilities 

    :param cap: Specifies a symbolic constant indicating a GL capability. 
    :type cap: int
    '''

    pass


def glDrawBuffer(mode: int):
    '''Specify which color buffers are to be drawn into 

    :param mode: Specifies up to four color buffers to be drawn into. 
    :type mode: int
    '''

    pass


def glDrawPixels(width, height, format: int, type: int,
                 pixels: 'bpy.context.object'):
    '''Write a block of pixels to the frame buffer 

    :param height: Specify the dimensions of the pixel rectangle to be written into the frame buffer. 
    :param format: Specifies the format of the pixel data. 
    :type format: int
    :param type: Specifies the data type for pixels. 
    :type type: int
    :param pixels: Specifies a pointer to the pixel data. 
    :type pixels: 'bpy.context.object'
    '''

    pass


def glEdgeFlag(flag):
    '''Flag edges as either boundary or non-boundary 

    :param flag: Specifies the current edge flag value.The initial value is GL_TRUE. 
    '''

    pass


def glEnable(cap: int):
    '''Enable server-side GL capabilities 

    :param cap: Specifies a symbolic constant indicating a GL capability. 
    :type cap: int
    '''

    pass


def glEnd():
    '''Delimit the vertices of a primitive or group of like primitives 

    '''

    pass


def glEndList():
    '''Create or replace a display list 

    '''

    pass


def glEvalCoord(u, v):
    '''Evaluate enabled one- and two-dimensional maps 

    :param u: Specifies a value that is the domain coordinate u to the basis function defined in a previous glMap1 or glMap2 command. If the function prototype ends in ‘v’ then u specifies a pointer to an array containing either one or two domain coordinates. The first coordinate is u. The second coordinate is v, which is present only in glEvalCoord2 versions. 
    :param v: Specifies a value that is the domain coordinate v to the basis function defined in a previous glMap2 command. This argument is not present in a glEvalCoord1 command. 
    '''

    pass


def glEvalMesh(mode: int, i1, i2):
    '''Compute a one- or two-dimensional grid of points or lines 

    :param mode: In glEvalMesh1, specifies whether to compute a one-dimensional mesh of points or lines. 
    :type mode: int
    :param i2: Specify the first and last integer values for the grid domain variable i. 
    '''

    pass


def glEvalPoint(i: int, j: int):
    '''Generate and evaluate a single point in a mesh 

    :param i: Specifies the integer value for grid domain variable i. 
    :type i: int
    :param j: Specifies the integer value for grid domain variable j (glEvalPoint2 only). 
    :type j: int
    '''

    pass


def glFeedbackBuffer(size: int, type: int, buffer: 'bpy.context.object'):
    '''Controls feedback mode 

    :param size: Specifies the maximum number of values that can be written into buffer. 
    :type size: int
    :param type: Specifies a symbolic constant that describes the information that will be returned for each vertex. 
    :type type: int
    :param buffer: Returns the feedback data. 
    :type buffer: 'bpy.context.object'
    '''

    pass


def glFinish():
    '''Block until all GL execution is complete 

    '''

    pass


def glFlush():
    '''Force Execution of GL commands in finite time 

    '''

    pass


def glFog(pname: int, param):
    '''Specify fog parameters 

    :param pname: Specifies a single-valued fog parameter. If the function prototype ends in ‘v’ specifies a fog parameter. 
    :type pname: int
    :param param: Specifies the value or values to be assigned to pname. GL_FOG_COLOR requires an array of four values. All other parameters accept an array containing only a single value. 
    '''

    pass


def glFrontFace(mode: int):
    '''Define front- and back-facing polygons 

    :param mode: Specifies the orientation of front-facing polygons. 
    :type mode: int
    '''

    pass


def glFrustum(left, right, bottom, top, zNear, zFar):
    '''Multiply the current matrix by a perspective matrix 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param bottom: Specify the coordinates for the bottom and top horizontal clipping planes. 
    :param zFar: Specify the distances to the near and far depth clipping planes. Both distances must be positive. 
    '''

    pass


def glGenLists(range: int):
    '''Generate a contiguous set of empty display lists 

    :param range: Specifies the number of contiguous empty display lists to be generated. 
    :type range: int
    '''

    pass


def glGenTextures(n: int, textures: 'bpy.context.object'):
    '''Generate texture names 

    :param n: Specifies the number of textures name to be generated. 
    :type n: int
    :param textures: Specifies an array in which the generated textures names are stored. 
    :type textures: 'bpy.context.object'
    '''

    pass


def glGet(pname: int, param):
    '''Return the value or values of a selected parameter 

    :param pname: Specifies the parameter value to be returned. 
    :type pname: int
    :param param: Returns the value or values of the specified parameter. 
    '''

    pass


def glGetAttachedShaders(program: int, maxCount: int, count: int,
                         shaders: int):
    '''Returns the handles of the shader objects attached to a program object. 

    :param program: Specifies the program object to be queried. 
    :type program: int
    :param maxCount: Specifies the size of the array for storing the returned object names. 
    :type maxCount: int
    :param count: Returns the number of names actually returned in objects. 
    :type count: int
    :param shaders: Specifies an array that is used to return the names of attached shader objects. 
    :type shaders: int
    '''

    pass


def glGetClipPlane(plane: int, equation: 'bpy.context.object'):
    '''Return the coefficients of the specified clipping plane 

    :param plane: Specifies a clipping plane. The number of clipping planes depends on the implementation, but at least six clipping planes are supported. They are identified by symbolic names of the form GL_CLIP_PLANEi where 0 < i < GL_MAX_CLIP_PLANES. 
    :type plane: int
    :param equation: Returns four float (double)-precision values that are the coefficients of the plane equation of plane in eye coordinates. The initial value is (0, 0, 0, 0). 
    :type equation: 'bpy.context.object'
    '''

    pass


def glGetError():
    '''Return error information 

    '''

    pass


def glGetLight(light: int, pname: int, params: 'Buffer'):
    '''Return light source parameter values 

    :param light: Specifies a light source. The number of possible lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS. 
    :type light: int
    :param pname: Specifies a light source parameter for light. 
    :type pname: int
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetMap(target: int, query: int, v: 'Buffer'):
    '''Return evaluator parameters 

    :param target: Specifies the symbolic name of a map. 
    :type target: int
    :param query: Specifies which parameter to return. 
    :type query: int
    :param v: Returns the requested data. 
    :type v: 'Buffer'
    '''

    pass


def glGetMaterial(face: int, pname: int, params: 'Buffer'):
    '''Return material parameters 

    :param face: Specifies which of the two materials is being queried. representing the front and back materials, respectively. 
    :type face: int
    :param pname: Specifies the material parameter to return. 
    :type pname: int
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetPixelMap(map: int, values: 'Buffer'):
    '''Return the specified pixel map 

    :param map: Specifies the name of the pixel map to return. 
    :type map: int
    :param values: Returns the pixel map contents. 
    :type values: 'Buffer'
    '''

    pass


def glGetPolygonStipple(mask: 'bpy.context.object'):
    '''Return the polygon stipple pattern 

    :param mask: Returns the stipple pattern. The initial value is all 1’s. 
    :type mask: 'bpy.context.object'
    '''

    pass


def glGetProgramInfoLog(program: int, maxLength: int, length: int,
                        infoLog: 'Buffer'):
    '''Returns the information log for a program object. 

    :param program: Specifies the program object whose information log is to be queried. 
    :type program: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log. 
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator). 
    :type length: int
    :param infoLog: Specifies an array of characters that is used to return the information log. 
    :type infoLog: 'Buffer'
    '''

    pass


def glGetProgramiv(program: int, pname: int, params: int):
    '''Returns a parameter from a program object. 

    :param program: Specifies the program object to be queried. 
    :type program: int
    :param pname: Specifies the object parameter. 
    :type pname: int
    :param params: Returns the requested object parameter. 
    :type params: int
    '''

    pass


def glGetShaderInfoLog(program, maxLength: int, length: int,
                       infoLog: 'Buffer'):
    '''Returns the information log for a shader object. 

    :param shader: Specifies the shader object whose information log is to be queried. 
    :type shader: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log. 
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator). 
    :type length: int
    :param infoLog: Specifies an array of characters that is used to return the information log. 
    :type infoLog: 'Buffer'
    '''

    pass


def glGetShaderSource(shader: int, bufSize: int, length: int,
                      source: 'Buffer'):
    '''Returns the source code string from a shader object 

    :param shader: Specifies the shader object to be queried. 
    :type shader: int
    :param bufSize: Specifies the size of the character buffer for storing the returned source code string. 
    :type bufSize: int
    :param length: Returns the length of the string returned in source (excluding the null terminator). 
    :type length: int
    :param source: Specifies an array of characters that is used to return the source code string. 
    :type source: 'Buffer'
    '''

    pass


def glGetString(name: int):
    '''Return a string describing the current GL connection 

    :param name: Specifies a symbolic constant. 
    :type name: int
    '''

    pass


def glGetTexEnv(target: int, pname: int, params: 'Buffer'):
    '''Return texture environment parameters 

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV. 
    :type target: int
    :param pname: Specifies the symbolic name of a texture environment parameter. 
    :type pname: int
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexGen(coord: int, pname: int, params: 'Buffer'):
    '''Return texture coordinate generation parameters 

    :param coord: Specifies a texture coordinate. 
    :type coord: int
    :param pname: Specifies the symbolic name of the value(s) to be returned. 
    :type pname: int
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexImage(target: int, level: int, format: int, type: int,
                  pixels: 'Buffer'):
    '''Return a texture image 

    :param target: Specifies which texture is to be obtained. 
    :type target: int
    :param level: Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param format: Specifies a pixel format for the returned data. 
    :type format: int
    :param type: Specifies a pixel type for the returned data. 
    :type type: int
    :param pixels: Returns the texture image. Should be a pointer to an array of the type specified by type 
    :type pixels: 'Buffer'
    '''

    pass


def glGetTexLevelParameter(target: int, level: int, pname: int,
                           params: 'Buffer'):
    '''return texture parameter values for a specific level of detail 

    :param target: Specifies the symbolic name of the target texture. 
    :type target: int
    :param level: Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param pname: Specifies the symbolic name of a texture parameter. 
    :type pname: int
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexParameter(target: int, pname: int, params: 'Buffer'):
    '''Return texture parameter values 

    :param target: Specifies the symbolic name of the target texture. 
    :type target: int
    :param pname: Specifies the symbolic name the target texture. 
    :type pname: int
    :param params: Returns the texture parameters. 
    :type params: 'Buffer'
    '''

    pass


def glHint(target: int, mode: int):
    '''Specify implementation-specific hints 

    :param target: Specifies a symbolic constant indicating the behavior to be controlled. 
    :type target: int
    :param mode: Specifies a symbolic constant indicating the desired behavior. 
    :type mode: int
    '''

    pass


def glIndex(c: 'Buffer'):
    '''Set the current color index 

    :param c: Specifies a pointer to a one element array that contains the new value for the current color index. 
    :type c: 'Buffer'
    '''

    pass


def glIndexMask(mask: int):
    '''Control the writing of individual bits in the color index buffers 

    :param mask: Specifies a bit mask to enable and disable the writing of individual bits in the color index buffers. Initially, the mask is all 1’s. 
    :type mask: int
    '''

    pass


def glInitNames():
    '''Initialize the name stack 

    '''

    pass


def glIsEnabled(cap: int):
    '''Test whether a capability is enabled 

    :param cap: Specifies a constant representing a GL capability. 
    :type cap: int
    '''

    pass


def glIsList(list: int):
    '''Determine if a name corresponds to a display-list 

    :param list: Specifies a potential display-list name. 
    :type list: int
    '''

    pass


def glIsProgram(program: int):
    '''Determines if a name corresponds to a program object 

    :param program: Specifies a potential program object. 
    :type program: int
    '''

    pass


def glIsShader(shader: int):
    '''Determines if a name corresponds to a shader object. 

    :param shader: Specifies a potential shader object. 
    :type shader: int
    '''

    pass


def glIsTexture(texture: int):
    '''Determine if a name corresponds to a texture 

    :param texture: Specifies a value that may be the name of a texture. 
    :type texture: int
    '''

    pass


def glLight(light: int, pname: int, param):
    '''Set the light source parameters 

    :param light: Specifies a light. The number of lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS. 
    :type light: int
    :param pname: Specifies a single-valued light source parameter for light. 
    :type pname: int
    :param param: Specifies the value that parameter pname of light source light will be set to. If function prototype ends in ‘v’ specifies a pointer to the value or values that parameter pname of light source light will be set to. 
    '''

    pass


def glLightModel(pname: int, param):
    '''Set the lighting model parameters 

    :param pname: Specifies a single-value light model parameter. 
    :type pname: int
    :param param: Specifies the value that param will be set to. If function prototype ends in ‘v’ specifies a pointer to the value or values that param will be set to. 
    '''

    pass


def glLineStipple(factor: int, pattern: int):
    '''Specify the line stipple pattern 

    :param factor: Specifies a multiplier for each bit in the line stipple pattern. If factor is 3, for example, each bit in the pattern is used three times before the next bit in the pattern is used. factor is clamped to the range [1, 256] and defaults to 1. 
    :type factor: int
    :param pattern: Specifies a 16-bit integer whose bit pattern determines which fragments of a line will be drawn when the line is rasterized. Bit zero is used first; the default pattern is all 1’s. 
    :type pattern: int
    '''

    pass


def glLineWidth(width: float):
    '''Specify the width of rasterized lines. 

    :param width: Specifies the width of rasterized lines. The initial value is 1. 
    :type width: float
    '''

    pass


def glLinkProgram(program: int):
    '''Links a program object. 

    :param program: Specifies the handle of the program object to be linked. 
    :type program: int
    '''

    pass


def glListBase(base: int):
    '''Set the display-list base for glCallLists 

    :param base: Specifies an integer offset that will be added to glCallLists offsets to generate display-list names. The initial value is 0. 
    :type base: int
    '''

    pass


def glLoadIdentity():
    '''Replace the current matrix with the identity matrix 

    '''

    pass


def glLoadMatrix(m: 'Buffer'):
    '''Replace the current matrix with the specified matrix 

    :param m: Specifies a pointer to 16 consecutive values, which are used as the elements of a 4x4 column-major matrix. 
    :type m: 'Buffer'
    '''

    pass


def glLoadName(name: int):
    '''Load a name onto the name stack. 

    :param name: Specifies a name that will replace the top value on the name stack. 
    :type name: int
    '''

    pass


def glLogicOp(opcode: int):
    '''Specify a logical pixel operation for color index rendering 

    :param opcode: Specifies a symbolic constant that selects a logical operation. 
    :type opcode: int
    '''

    pass


def glMap1(target: int, u1, u2, stride: int, order: int, points: 'Buffer'):
    '''Define a one-dimensional evaluator 

    :param target: Specifies the kind of values that are generated by the evaluator. 
    :type target: int
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord1, to ^, t he variable that is evaluated by the equations specified by this command. 
    :param stride: Specifies the number of floats or float (double)s between the beginning of one control point and the beginning of the next one in the data structure referenced in points. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. 
    :type stride: int
    :param order: Specifies the number of control points. Must be positive. 
    :type order: int
    :param points: Specifies a pointer to the array of control points. 
    :type points: 'Buffer'
    '''

    pass


def glMap2(target: int, u1, u2, ustride: int, uorder: int, v1, v2,
           vstride: int, vorder: int, points: 'Buffer'):
    '''Define a two-dimensional evaluator 

    :param target: Specifies the kind of values that are generated by the evaluator. 
    :type target: int
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord2, to ^, t he variable that is evaluated by the equations specified by this command. Initially u1 is 0 and u2 is 1. 
    :param ustride: Specifies the number of floats or float (double)s between the beginning of control point R and the beginning of control point R ij, where i and j are the u and v control point indices, respectively. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. The initial value of ustride is 0. 
    :type ustride: int
    :param uorder: Specifies the dimension of the control point array in the u axis. Must be positive. The initial value is 1. 
    :type uorder: int
    :param v2: Specify a linear mapping of v, as presented to glEvalCoord2, to ^, one of the two variables that are evaluated by the equations specified by this command. Initially, v1 is 0 and v2 is 1. 
    :param vstride: Specifies the number of floats or float (double)s between the beginning of control point R and the beginning of control point R ij, where i and j are the u and v control point(indices, respectively. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. The initial value of vstride is 0. 
    :type vstride: int
    :param vorder: Specifies the dimension of the control point array in the v axis. Must be positive. The initial value is 1. 
    :type vorder: int
    :param points: Specifies a pointer to the array of control points. 
    :type points: 'Buffer'
    '''

    pass


def glMapGrid(un: int, u1, u2, vn: int, v1, v2):
    '''Define a one- or two-dimensional mesh 

    :param un: Specifies the number of partitions in the grid range interval [u1, u2]. Must be positive. 
    :type un: int
    :param u2: Specify the mappings for integer grid domain values i=0 and i=un. 
    :param vn: Specifies the number of partitions in the grid range interval [v1, v2] (glMapGrid2 only). 
    :type vn: int
    :param v2: Specify the mappings for integer grid domain values j=0 and j=vn (glMapGrid2 only). 
    '''

    pass


def glMaterial(face: int, pname: int, params: int):
    '''Specify material parameters for the lighting model. 

    :param face: Specifies which face or faces are being updated. Must be one of: 
    :type face: int
    :param pname: Specifies the single-valued material parameter of the face or faces that is being updated. Must be GL_SHININESS. 
    :type pname: int
    :param params: Specifies the value that parameter GL_SHININESS will be set to. If function prototype ends in ‘v’ specifies a pointer to the value or values that pname will be set to. 
    :type params: int
    '''

    pass


def glMatrixMode(mode: int):
    '''Specify which matrix is the current matrix. 

    :param mode: Specifies which matrix stack is the target for subsequent matrix operations. 
    :type mode: int
    '''

    pass


def glMultMatrix(m: 'Buffer'):
    '''Multiply the current matrix with the specified matrix 

    :param m: Points to 16 consecutive values that are used as the elements of a 4x4 column major matrix. 
    :type m: 'Buffer'
    '''

    pass


def glNewList(list: int, mode: int):
    '''Create or replace a display list 

    :param list: Specifies the display list name 
    :type list: int
    :param mode: Specifies the compilation mode. 
    :type mode: int
    '''

    pass


def glNormal3(nx, ny, nz, v: 'Buffer'):
    '''Set the current normal vector 

    :param nz: Specify the x, y, and z coordinates of the new current normal. The initial value of the current normal is the unit vector, (0, 0, 1). 
    :param v: Specifies a pointer to an array of three elements: the x, y, and z coordinates of the new current normal. 
    :type v: 'Buffer'
    '''

    pass


def glOrtho(left, right, bottom, top, zNear, zFar):
    '''Multiply the current matrix with an orthographic matrix 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param top: Specify the coordinates for the bottom and top horizontal clipping planes. 
    :param zFar: Specify the distances to the nearer and farther depth clipping planes. These values are negative if the plane is to be behind the viewer. 
    '''

    pass


def glPassThrough(token: float):
    '''Place a marker in the feedback buffer 

    :param token: Specifies a marker value to be placed in the feedback buffer following a GL_PASS_THROUGH_TOKEN. 
    :type token: float
    '''

    pass


def glPixelMap(map: int, mapsize: int, values: 'Buffer'):
    '''Set up pixel transfer maps 

    :param map: Specifies a symbolic map name. 
    :type map: int
    :param mapsize: Specifies the size of the map being defined. 
    :type mapsize: int
    :param values: Specifies an array of mapsize values. 
    :type values: 'Buffer'
    '''

    pass


def glPixelStore(pname: int, param):
    '''Set pixel storage modes 

    :param pname: Specifies the symbolic name of the parameter to be set. Six values affect the packing of pixel data into memory. Six more affect the unpacking of pixel data from memory. 
    :type pname: int
    :param param: Specifies the value that pname is set to. 
    '''

    pass


def glPixelTransfer(pname: int, param):
    '''Set pixel transfer modes 

    :param pname: Specifies the symbolic name of the pixel transfer parameter to be set. 
    :type pname: int
    :param param: Specifies the value that pname is set to. 
    '''

    pass


def glPixelZoom(xfactor, yfactor):
    '''Specify the pixel zoom factors 

    :param yfactor: Specify the x and y zoom factors for pixel write operations. 
    '''

    pass


def glPointSize(size: float):
    '''Specify the diameter of rasterized points 

    :param size: Specifies the diameter of rasterized points. The initial value is 1. 
    :type size: float
    '''

    pass


def glPolygonMode(face: int, mode: int):
    '''Select a polygon rasterization mode 

    :param face: Specifies the polygons that mode applies to. Must be GL_FRONT for front-facing polygons, GL_BACK for back- facing polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons. 
    :type face: int
    :param mode: Specifies how polygons will be rasterized. The initial value is GL_FILL for both front- and back- facing polygons. 
    :type mode: int
    '''

    pass


def glPolygonOffset(factor: float, units: float):
    '''Set the scale and units used to calculate depth values 

    :param factor: Specifies a scale factor that is used to create a variable depth offset for each polygon. The initial value is 0. 
    :type factor: float
    :param units: Is multiplied by an implementation-specific value to create a constant depth offset. The initial value is 0. 
    :type units: float
    '''

    pass


def glPolygonStipple(mask: 'bpy.context.object'):
    '''Set the polygon stippling pattern 

    :param mask: Specifies a pointer to a 32x32 stipple pattern that will be unpacked from memory in the same way that glDrawPixels unpacks pixels. 
    :type mask: 'bpy.context.object'
    '''

    pass


def glPopAttrib():
    '''Pop the server attribute stack 

    '''

    pass


def glPopClientAttrib():
    '''Pop the client attribute stack 

    '''

    pass


def glPopMatrix():
    '''Pop the current matrix stack 

    '''

    pass


def glPopName():
    '''Pop the name stack 

    '''

    pass


def glPrioritizeTextures(n: int, textures: 'Buffer', priorities: 'Buffer'):
    '''Set texture residence priority 

    :param n: Specifies the number of textures to be prioritized. 
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be prioritized. 
    :type textures: 'Buffer'
    :param priorities: Specifies an array containing the texture priorities. A priority given in an element of priorities applies to the texture named by the corresponding element of textures. 
    :type priorities: 'Buffer'
    '''

    pass


def glPushAttrib(mask):
    '''Push the server attribute stack 

    :param mask: Specifies a mask that indicates which attributes to save. 
    '''

    pass


def glPushClientAttrib(mask):
    '''Push the client attribute stack 

    :param mask: Specifies a mask that indicates which attributes to save. 
    '''

    pass


def glPushMatrix():
    '''Push the current matrix stack 

    '''

    pass


def glPushName(name: int):
    '''Push the name stack 

    :param name: Specifies a name that will be pushed onto the name stack. 
    :type name: int
    '''

    pass


def glRasterPos(x, y, z, w):
    '''Specify the raster position for pixel operations 

    :param w: Specify the x,y,z, and w object coordinates (if present) for the raster position. If function prototype ends in ‘v’ specifies a pointer to an array of two, three, or four elements, specifying x, y, z, and w coordinates, respectively. 
    '''

    pass


def glReadBuffer(mode: int):
    '''Select a color buffer source for pixels. 

    :param mode: Specifies a color buffer. 
    :type mode: int
    '''

    pass


def glReadPixels(x, y, width, height, format: int, type: int,
                 pixels: 'bpy.context.object'):
    '''Read a block of pixels from the frame buffer 

    :param y: Specify the window coordinates of the first pixel that is read from the frame buffer. This location is the lower left corner of a rectangular block of pixels. 
    :param height: Specify the dimensions of the pixel rectangle. width and height of one correspond to a single pixel. 
    :param format: Specifies the format of the pixel data. 
    :type format: int
    :param type: Specifies the data type of the pixel data. 
    :type type: int
    :param pixels: Returns the pixel data. 
    :type pixels: 'bpy.context.object'
    '''

    pass


def glRect(x1, y1, x2, y2, v1, v2):
    '''Draw a rectangle 

    :param y1: Specify one vertex of a rectangle 
    :param y2: Specify the opposite vertex of the rectangle 
    :param v2: Specifies a pointer to one vertex of a rectangle and the pointer to the opposite vertex of the rectangle 
    '''

    pass


def glRenderMode(mode: int):
    '''Set rasterization mode 

    :param mode: Specifies the rasterization mode. 
    :type mode: int
    '''

    pass


def glRotate(angle, x, y, z):
    '''Multiply the current matrix by a rotation matrix 

    :param angle: Specifies the angle of rotation in degrees. 
    :param z: Specify the x, y, and z coordinates of a vector respectively. 
    '''

    pass


def glScale(x, y, z):
    '''Multiply the current matrix by a general scaling matrix 

    :param z: Specify scale factors along the x, y, and z axes, respectively. 
    '''

    pass


def glScissor(x, y, width, height):
    '''Define the scissor box 

    :param y: Specify the lower left corner of the scissor box. Initially (0, 0). 
    :param height: Specify the width and height of the scissor box. When a GL context is first attached to a window, width and height are set to the dimensions of that window. 
    '''

    pass


def glSelectBuffer(size: int, buffer: 'Buffer'):
    '''Establish a buffer for selection mode values 

    :param size: Specifies the size of buffer 
    :type size: int
    :param buffer: Returns the selection data 
    :type buffer: 'Buffer'
    '''

    pass


def glShadeModel(mode: int):
    '''Select flat or smooth shading 

    :param mode: Specifies a symbolic value representing a shading technique. 
    :type mode: int
    '''

    pass


def glShaderSource(shader: int, shader_string: str):
    '''Replaces the source code in a shader object. 

    :param shader: Specifies the handle of the shader object whose source code is to be replaced. 
    :type shader: int
    :param shader_string: The shader string. 
    :type shader_string: str
    '''

    pass


def glStencilFunc(func: int, ref: int, mask: int):
    '''Set function and reference value for stencil testing 

    :param func: Specifies the test function. 
    :type func: int
    :param ref: Specifies the reference value for the stencil test. ref is clamped to the range [0,2n-1], where n is the number of bitplanes in the stencil buffer. The initial value is 0. 
    :type ref: int
    :param mask: Specifies a mask that is ANDed with both the reference value and the stored stencil value when the test is done. The initial value is all 1’s. 
    :type mask: int
    '''

    pass


def glStencilMask(mask: int):
    '''Control the writing of individual bits in the stencil planes 

    :param mask: Specifies a bit mask to enable and disable writing of individual bits in the stencil planes. Initially, the mask is all 1’s. 
    :type mask: int
    '''

    pass


def glStencilOp(fail: int, zfail: int, zpass: int):
    '''Set stencil test actions 

    :param fail: Specifies the action to take when the stencil test fails. The initial value is GL_KEEP. 
    :type fail: int
    :param zfail: Specifies the stencil action when the stencil test passes, but the depth test fails. zfail accepts the same symbolic constants as fail. The initial value is GL_KEEP. 
    :type zfail: int
    :param zpass: Specifies the stencil action when both the stencil test and the depth test pass, or when the stencil test passes and either there is no depth buffer or depth testing is not enabled. zpass accepts the same symbolic constants as fail. The initial value is GL_KEEP. 
    :type zpass: int
    '''

    pass


def glTexCoord(s, t, r, q, v: 'Buffer'):
    '''Set the current texture coordinates 

    :param q: Specify s, t, r, and q texture coordinates. Not all parameters are present in all forms of the command. 
    :param v: Specifies a pointer to an array of one, two, three, or four elements, which in turn specify the s, t, r, and q texture coordinates. 
    :type v: 'Buffer'
    '''

    pass


def glTexEnv(target: int, pname: int, param):
    '''Set texture environment parameters 

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV. 
    :type target: int
    :param pname: Specifies the symbolic name of a single-valued texture environment parameter. Must be GL_TEXTURE_ENV_MODE. 
    :type pname: int
    :param param: Specifies a single symbolic constant. If function prototype ends in ‘v’ specifies a pointer to a parameter array that contains either a single symbolic constant or an RGBA color 
    '''

    pass


def glTexGen(coord: int, pname: int, param):
    '''Control the generation of texture coordinates 

    :param coord: Specifies a texture coordinate. 
    :type coord: int
    :param pname: Specifies the symbolic name of the texture- coordinate generation function. 
    :type pname: int
    :param param: Specifies a single-valued texture generation parameter. If function prototype ends in ‘v’ specifies a pointer to an array of texture generation parameters. If pname is GL_TEXTURE_GEN_MODE, then the array must contain a single symbolic constant. Otherwise, params holds the coefficients for the texture-coordinate generation function specified by pname. 
    '''

    pass


def glTexImage1D(target: int, level: int, internalformat: int, width: int,
                 border: int, format: int, type: int, pixels: 'Buffer'):
    '''Specify a one-dimensional texture image 

    :param target: Specifies the target texture. 
    :type target: int
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. The height of the 1D texture image is 1. 
    :type width: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    :param format: Specifies the format of the pixel data. 
    :type format: int
    :param type: Specifies the data type of the pixel data. 
    :type type: int
    :param pixels: Specifies a pointer to the image data in memory. 
    :type pixels: 'Buffer'
    '''

    pass


def glTexImage2D(target: int, level: int, internalformat: int, width: int,
                 height: int, border: int, format: int, type: int,
                 pixels: 'Buffer'):
    '''Specify a two-dimensional texture image 

    :param target: Specifies the target texture. 
    :type target: int
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. 
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for some integer m. All implementations support texture images that are at least 64 texels high. 
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    :param format: Specifies the format of the pixel data. 
    :type format: int
    :param type: Specifies the data type of the pixel data. 
    :type type: int
    :param pixels: Specifies a pointer to the image data in memory. 
    :type pixels: 'Buffer'
    '''

    pass


def glTexParameter(target: int, pname: int, param):
    '''Set texture parameters 

    :param target: Specifies the target texture. 
    :type target: int
    :param pname: Specifies the symbolic name of a single-valued texture parameter. 
    :type pname: int
    :param param: Specifies the value of pname. If function prototype ends in ‘v’ specifies a pointer to an array where the value or values of pname are stored. 
    '''

    pass


def glTranslate(x, y, z):
    '''Multiply the current matrix by a translation matrix 

    :param z: Specify the x, y, and z coordinates of a translation vector. 
    '''

    pass


def glUseProgram(program: int):
    '''Installs a program object as part of current rendering state 

    :param program: Specifies the handle of the program object whose executables are to be used as part of current rendering state. 
    :type program: int
    '''

    pass


def glValidateProgram(program: int):
    '''Validates a program object 

    :param program: Specifies the handle of the program object to be validated. 
    :type program: int
    '''

    pass


def glVertex(x, y, z, w, v: 'Buffer'):
    '''Specify a vertex 

    :param w: Specify x, y, z, and w coordinates of a vertex. Not all parameters are present in all forms of the command. 
    :param v: Specifies a pointer to an array of two, three, or four elements. The elements of a two-element array are x and y; of a three-element array, x, y, and z; and of a four-element array, x, y, z, and w. 
    :type v: 'Buffer'
    '''

    pass


def glViewport(x, y, width, height):
    '''Set the viewport 

    :param y: Specify the lower left corner of the viewport rectangle, in pixels. The initial value is (0,0). 
    :param height: Specify the width and height of the viewport. When a GL context is first attached to a window, width and height are set to the dimensions of that window. 
    '''

    pass


def gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz):
    '''Define a viewing transformation. 

    :param eyez: Specifies the position of the eye point. 
    :param centerz: Specifies the position of the reference point. 
    :param upz: Specifies the direction of the up vector. 
    '''

    pass


def gluOrtho2D(left, right, bottom, top):
    '''Define a 2-D orthographic projection matrix. 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param top: Specify the coordinates for the bottom and top horizontal clipping planes. 
    '''

    pass


def gluPerspective(fovY, aspect, zNear, zFar):
    '''Set up a perspective projection matrix. 

    :param fovY: Specifies the field of view angle, in degrees, in the y direction. 
    :param aspect: Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height). 
    :param zNear: Specifies the distance from the viewer to the near clipping plane (always positive). 
    :param zFar: Specifies the distance from the viewer to the far clipping plane (always positive). 
    '''

    pass


def gluPickMatrix(x, y, width, height, viewport: 'Buffer'):
    '''Define a picking region. 

    :param y: Specify the center of a picking region in window coordinates. 
    :param height: Specify the width and height, respectively, of the picking region in window coordinates. 
    :param viewport: Specifies the current viewport. 
    :type viewport: 'Buffer'
    '''

    pass


def gluProject(objx, objy, objz, modelMatrix: 'Buffer', projMatrix: 'Buffer',
               viewport: 'Buffer', winx, winy, winz):
    '''Map object coordinates to window coordinates. 

    :param objz: Specify the object coordinates. 
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call). 
    :type modelMatrix: 'Buffer'
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call). 
    :type projMatrix: 'Buffer'
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call). 
    :type viewport: 'Buffer'
    :param winz: Return the computed window coordinates. 
    '''

    pass


def gluUnProject(winx, winy, winz, modelMatrix: 'Buffer', projMatrix: 'Buffer',
                 viewport: 'Buffer', objx, objy, objz):
    '''Map object coordinates to window coordinates. 

    :param winz: Specify the window coordinates to be mapped. 
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call). 
    :type modelMatrix: 'Buffer'
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call). 
    :type projMatrix: 'Buffer'
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call). 
    :type viewport: 'Buffer'
    :param objz: Return the computed object coordinates. 
    '''

    pass
