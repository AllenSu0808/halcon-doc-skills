# RenderScene3d (Operator)

## Name

`RenderScene3d` — Render an image of a 3D scene.

## Signature

`static void HOperatorSet.RenderScene3d(out HObject image, HTuple scene3D, HTuple cameraIndex)`

`HImage HScene3D.RenderScene3d(int cameraIndex)`

## Description

`RenderScene3d` renders an image of the 3D scene *`scene3D`*
and returns the result in *`image`*. The view of the camera
*`cameraIndex`* is used to render the image.

The [`SetScene3dParam`](set_scene_3d_param.md) parameters
*"object_index_persistence"* and *"disp_background"* are
ignored. The background of *`image`* is black.

`RenderScene3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode is automatically enabled. The compatibility
mode requires OpenGL 1.1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte)

Rendered 3D scene.

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`cameraIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the camera used to display the scene.

## Result

`RenderScene3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Alternatives

`DisplayScene3d`

## See also

`CreateScene3d`

## Module

3D Metrology
