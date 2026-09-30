# DisplayScene3d (Operator)

## Name

`DisplayScene3d` — Display a 3D scene.

## Signature

`static void HOperatorSet.DisplayScene3d(HTuple windowHandle, HTuple scene3D, HTuple cameraIndex)`

`void HScene3D.DisplayScene3d(HWindow windowHandle, HTuple cameraIndex)`

`void HScene3D.DisplayScene3d(HWindow windowHandle, string cameraIndex)`

## Description

`DisplayScene3d` displays the 3D scene *`scene3D`* in the
window *`windowHandle`*. The view of the camera *`cameraIndex`*
is used to render the scene.
Note that sometimes the aspect ratio
of *`windowHandle`* should be similar to width and height
of the camera in order to obtain the wanted results.
See [`CreateScene3d`](create_scene_3d.md) for a short example.

`DisplayScene3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode with less requirements but lower
quality is automatically enabled.
On graphics cards with low memory the following error messages could occur
if rendering in a window with high resolution:

Low level error: 'Incomplete attachment'

Unhanded Exception: 'Required framebuffer object is unsupported'

Solutions:

Set the parameter *"quality"* to *"low"* using
[`SetScene3dParam`](set_scene_3d_param.md) or use the compatibility mode to reduce the
requirements of the graphics card.

The system variable (see [`SetSystem`](set_system.md))
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`cameraIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the camera used to display the scene.

## Result

`DisplayScene3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`CreateScene3d`,
`RenderScene3d`

## Module

3D Metrology
