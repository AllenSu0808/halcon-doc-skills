# render_scene_3d (Operator)

## Name

`render_scene_3d` — Render an image of a 3D scene.

## Signature

`render_scene_3d( : Image : Scene3D, CameraIndex : )`

## Description

`render_scene_3d` renders an image of the 3D scene *`Scene3D`*
and returns the result in *`Image`*. The view of the camera
*`CameraIndex`* is used to render the image.

The [`set_scene_3d_param`](set_scene_3d_param.md) parameters
*'object_index_persistence'* and *'disp_background'* are
ignored. The background of *`Image`* is black.

`render_scene_3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode is automatically enabled. The compatibility
mode requires OpenGL 1.1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  (multichannel-)image `→` object (byte)

Rendered 3D scene.

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`CameraIndex`** (input_control)  integer `→`  (integer)

Index of the camera used to display the scene.

## Result

`render_scene_3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Alternatives

`display_scene_3d`

## See also

`create_scene_3d`

## Module

3D Metrology
