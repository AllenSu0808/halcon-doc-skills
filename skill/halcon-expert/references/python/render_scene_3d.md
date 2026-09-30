# render_scene_3d (Operator)

## Name

`render_scene_3d` — Render an image of a 3D scene.

## Signature

`def render_scene_3d(scene_3d: HHandle, camera_index: int) -> HObject`

## Description

`render_scene_3d` renders an image of the 3D scene *`scene_3d`*
and returns the result in *`image`*. The view of the camera
*`camera_index`* is used to render the image.

The [`set_scene_3d_param`](set_scene_3d_param.md) parameters
*"object_index_persistence"* and *"disp_background"* are
ignored. The background of *`image`* is black.

`render_scene_3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode is automatically enabled. The compatibility
mode requires OpenGL 1.1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  (multichannel-)image `→` HObject (byte)

Rendered 3D scene.

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`camera_index`** (input_control)  integer `→` int

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
