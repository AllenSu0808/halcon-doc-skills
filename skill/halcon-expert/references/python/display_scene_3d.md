# display_scene_3d (Operator)

## Name

`display_scene_3d` — Display a 3D scene.

## Signature

`def display_scene_3d(window_handle: HHandle, scene_3d: HHandle, camera_index: Union[int, str]) -> None`

## Description

`display_scene_3d` displays the 3D scene *`scene_3d`* in the
window *`window_handle`*. The view of the camera *`camera_index`*
is used to render the scene.
Note that sometimes the aspect ratio
of *`window_handle`* should be similar to width and height
of the camera in order to obtain the wanted results.
See [`create_scene_3d`](create_scene_3d.md) for a short example.

`display_scene_3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode with less requirements but lower
quality is automatically enabled.
On graphics cards with low memory the following error messages could occur
if rendering in a window with high resolution:

Low level error: 'Incomplete attachment'

Unhanded Exception: 'Required framebuffer object is unsupported'

Solutions:

Set the parameter *"quality"* to *"low"* using
[`set_scene_3d_param`](set_scene_3d_param.md) or use the compatibility mode to reduce the
requirements of the graphics card.

The system variable (see [`set_system`](set_system.md))
*"opengl_compatibility_mode_enable"* can be set to *"true"*
to permanently enable the visualization in compatibility mode with lower
OpenGL requirements.
This mode requires OpenGL 1.1.
In compatibility mode the parameters *"object_index_persistence"*,
*"depth_persistence"* and *"quality"* are not used.

On Linux Remote Desktop *"disp_background"* is not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`camera_index`** (input_control)  integer `→` Union[int, str]

Index of the camera used to display the scene.

## Result

`display_scene_3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`create_scene_3d`,
`render_scene_3d`

## Module

3D Metrology
