"""
This module provides Python wrappers for the GPU implementation in Blender.
Some higher level functions can be found in the gpu_extras module.

gpu.types.rst
gpu.matrix.rst
gpu.select.rst
gpu.shader.rst
gpu.state.rst
gpu.texture.rst
gpu.platform.rst
gpu.capabilities.rst

:maxdepth: 1
:caption: Submodules


--------------------

Geometry is drawn in batches.
A batch contains the necessary data to perform the drawing.
That includes an obligatory *Vertex Buffer* and an optional *Index Buffer*,
each of which is described in more detail in the following sections.
A batch also defines a draw type.
Typical draw types are POINTS, LINES and TRIS.
The draw type determines how the data will be interpreted and drawn.


--------------------

A *Vertex Buffer Object* (VBO) (gpu.types.GPUVertBuf)
is an array that contains the vertex attributes needed for drawing using a specific shader.
Typical vertex attributes are *location*, *normal*, *color*, and *uv*.
Every vertex buffer has a *Vertex Format* (gpu.types.GPUVertFormat)
and a length corresponding to the number of vertices in the buffer.
A vertex format describes the attributes stored per vertex and their types.

The following code demonstrates the creation of a vertex buffer that contains 6 vertices.
For each vertex 2 attributes will be stored: The position and the normal.

```
import gpu
vertex_positions = [(0, 0, 0), ...]
vertex_normals = [(0, 0, 1), ...]

fmt = gpu.types.GPUVertFormat()
fmt.attr_add(id="pos", comp_type='F32', len=3, fetch_mode='FLOAT')
fmt.attr_add(id="normal", comp_type='F32', len=3, fetch_mode='FLOAT')

vbo = gpu.types.GPUVertBuf(len=6, format=fmt)
vbo.attr_fill(id="pos", data=vertex_positions)
vbo.attr_fill(id="normal", data=vertex_normals)
```

This vertex buffer could be used to draw 6 points, 3 separate lines, 5 consecutive lines, 2 separate triangles, ...
E.g. in the case of lines, each two consecutive vertices define a line.
The type that will actually be drawn is determined when the batch is created later.


--------------------

Often triangles and lines share one or more vertices.
With only a vertex buffer one would have to store all attributes for the these vertices multiple times.
This is very inefficient because in a connected triangle mesh every vertex is used 6 times on average.
A more efficient approach would be to use an *Index Buffer* (IBO) (gpu.types.GPUIndexBuf),
sometimes referred to as *Element Buffer*.
An *Index Buffer* is an array that references vertices based on their index in the vertex buffer.

For instance, to draw a rectangle composed of two triangles, one could use an index buffer.

```
positions = (
    (-1,  1), (1,  1),
    (-1, -1), (1, -1))

indices = ((0, 1, 2), (2, 1, 3))

ibo = gpu.types.GPUIndexBuf(type='TRIS', seq=indices)
```

Here the first tuple in indices describes which vertices should be used for the first triangle
(same for the second tuple).
Note how the diagonal vertices 1 and 2 are shared between both triangles.


--------------------

A shader is a program that runs on the GPU (written in GLSL in our case).
There are multiple types of shaders.
The most important ones are *Vertex Shaders* and *Fragment Shaders*.
Typically multiple shaders are linked together into a *Program*.
However, in the Blender Python API the term *Shader* refers to an OpenGL Program.
Every gpu.types.GPUShader consists of a vertex shader, a fragment shader and an optional geometry shader.
For common drawing tasks there are some built-in shaders accessible from gpu.shader.from_builtin
with an identifier such as UNIFORM_COLOR or FLAT_COLOR.

Every shader defines a set of attributes and uniforms that have to be set in order to use the shader.
Attributes are properties that are set using a vertex buffer and can be different for individual vertices.
Uniforms are properties that are constant per draw call.
They can be set using the shader.uniform_* functions after the shader has been bound.


--------------------

Batches can be creates by first manually creating VBOs and IBOs.
However, it is recommended to use the gpu_extras.batch.batch_for_shader function.
It makes sure that all the vertex attributes necessary for a specific shader are provided.
Consequently, the shader has to be passed to the function as well.
When using this function one rarely has to care about the vertex format, VBOs and IBOs created in the background.
This is still something one should know when drawing stuff though.

Since batches can be drawn multiple times, they should be cached and reused whenever possible.


--------------------

What one can see on the screen after rendering is called the *Front Buffer*.
When draw calls are issued, batches are drawn on a *Back Buffer* that will only be displayed
when all drawing is done and the current back buffer will become the new front buffer.
Sometimes, one might want to draw the batches into a distinct buffer that could be used as
texture to display on another object or to be saved as image on disk.
This is called Offscreen Rendering.
In Blender Offscreen Rendering is done using the gpu.types.GPUOffScreen type.

[WARNING]
GPUOffScreen objects are bound to the OpenGL context they have been created in.
This means that once Blender discards this context (i.e. the window is closed),
the offscreen instance will be freed.


--------------------

To try these examples, just copy them into Blenders text editor and execute them.
To keep the examples relatively small, they just register a draw function that can't easily be removed anymore.
Blender has to be restarted in order to delete the draw handlers.


--------------------

```../examples/gpu.1.py```


--------------------

```../examples/gpu.2.py```


--------------------

```../examples/gpu.3.py```


--------------------

```../examples/gpu.4.py```


--------------------

```../examples/gpu.5.py```


--------------------

To use this example you have to provide an image that should be displayed.

```../examples/gpu.6.py```


--------------------

1. Create an gpu.types.GPUOffScreen object.
2. Draw some circles into it.
3. Make a new shader for drawing a planar texture in 3D.
4. Draw the generated texture using the new shader.

```../examples/gpu.7.py```


--------------------

This will create a new image with the given name.
If it already exists, it will override the existing one.

Currently almost all of the execution time is spent in the last line.
In the future this will hopefully be solved by implementing the Python buffer protocol
for gpu.types.Buffer and bpy.types.Image.pixels (aka bpy_prop_array

).

```../examples/gpu.8.py```


--------------------

The scene has to have a camera for this example to work.
You could also make this independent of a specific camera,
but Blender does not expose good functions to create view and projection matrices yet.

```../examples/gpu.9.py```


--------------------

In this example the arc length (distance to the first point on the line) is calculated in every vertex.
Between the vertex and fragment shader that value is automatically interpolated
for all points that will be visible on the screen.
In the fragment shader the sin

 of the arc length is calculated.
Based on the result a decision is made on whether the fragment should be drawn or not.

```../examples/gpu.10.py```


--------------------

This is an example of how to use a custom compute shader to write to a texture and then use that texture in a vertex/fragment shader.
The expected result is a 2x2 plane (size of the default cube), which changes color from a green-black gradient to a green-red gradient,
based on current time.

```../examples/gpu.11.py```

"""

import typing
import collections.abc
from . import capabilities
from . import matrix
from . import platform
from . import select
from . import shader
from . import state
from . import texture
from . import types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")
