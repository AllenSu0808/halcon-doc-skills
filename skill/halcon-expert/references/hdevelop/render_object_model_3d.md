# render_object_model_3d (Operator)

## Name

`render_object_model_3d` — Render 3D object models to get an image.

## Signature

`render_object_model_3d( : Image : ObjectModel3D, CamParam, Pose, GenParamName, GenParamValue : )`

## Description

`render_object_model_3d` renders the 3D object models of
*`ObjectModel3D`* and returns the result in the image *`Image`*.
To setup the scene to display, set *`CamParam`* and the individual
*`Pose`* of the objects. Be aware that *`Pose`* can contain either
one pose for each object or one pose for all objects.

The view of the output image is identical to that produced by
[`disp_object_model_3d`](disp_object_model_3d.md). The parameters and additional details are
documented with [`disp_object_model_3d`](disp_object_model_3d.md), except that the parameters
*'object_index_persistence'*, and *'disp_background'* can
not be set.

`render_object_model_3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode is automatically enabled. The compatibility
mode requires OpenGL 1.1.

## Attention

Cameras with hypercentric lenses are not supported.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  multichannel-image `→` object (byte)

Rendered scene.

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handles of the 3D object models.

**`CamParam`** (input_control)  campar `→`  (real / integer / string)

Camera parameters of the scene.

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

3D poses of the objects.

**`GenParamName`** (input_control)  string-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'alpha', 'attribute', 'blue_channel_attrib', 'color', 'color_attrib', 'color_attrib_end', 'color_attrib_start', 'colored', 'compatibility_mode_enable', 'disp_lines', 'disp_normals', 'disp_pose', 'green_channel_attrib', 'light_position', 'line_color', 'lut', 'normal_color', 'point_size', 'quality', 'red_channel_attrib', 'rgb_channel_attrib_end', 'rgb_channel_attrib_start'

**`GenParamValue`** (input_control)  string-array `→`  (string / integer / real)

Values of the generic parameters.

Default:
[]

List of values:
'auto', 'blue', 'coord_x', 'coord_y', 'coord_z', 'faces', 'false', 'green', 'lines', 'normal_x', 'normal_y', 'normal_z', 'points', 'primitive', 'red', 'true'

## Result

`render_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`find_surface_model`,
`fit_primitives_object_model_3d`,
`segment_object_model_3d`,
`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`disp_obj`

## See also

`disp_object_model_3d`,
`project_shape_model_3d`,
`object_model_3d_to_xyz`

## Module

3D Metrology
