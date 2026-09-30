# RenderObjectModel3d (Operator)

## Name

`RenderObjectModel3d` — Render 3D object models to get an image.

## Signature

`static void HOperatorSet.RenderObjectModel3d(out HObject image, HTuple objectModel3D, HTuple camParam, HTuple pose, HTuple genParamName, HTuple genParamValue)`

`static HImage HObjectModel3D.RenderObjectModel3d(HObjectModel3D[] objectModel3D, HCamPar camParam, HPose[] pose, HTuple genParamName, HTuple genParamValue)`

`HImage HObjectModel3D.RenderObjectModel3d(HCamPar camParam, HPose pose, HTuple genParamName, HTuple genParamValue)`

`HImage HCamPar.RenderObjectModel3d(HObjectModel3D[] objectModel3D, HPose[] pose, HTuple genParamName, HTuple genParamValue)`

`HImage HCamPar.RenderObjectModel3d(HObjectModel3D objectModel3D, HPose pose, HTuple genParamName, HTuple genParamValue)`

`static HImage HPose.RenderObjectModel3d(HObjectModel3D[] objectModel3D, HCamPar camParam, HPose[] pose, HTuple genParamName, HTuple genParamValue)`

`HImage HPose.RenderObjectModel3d(HObjectModel3D objectModel3D, HCamPar camParam, HTuple genParamName, HTuple genParamValue)`

## Description

`RenderObjectModel3d` renders the 3D object models of
*`objectModel3D`* and returns the result in the image *`image`*.
To setup the scene to display, set *`camParam`* and the individual
*`pose`* of the objects. Be aware that *`pose`* can contain either
one pose for each object or one pose for all objects.

The view of the output image is identical to that produced by
[`DispObjectModel3d`](disp_object_model_3d.md). The parameters and additional details are
documented with [`DispObjectModel3d`](disp_object_model_3d.md), except that the parameters
*"object_index_persistence"*, and *"disp_background"* can
not be set.

`RenderObjectModel3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
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

**`image`** (output_object)  multichannel-image `→` [HImage](HImage.md) (byte)

Rendered scene.

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the 3D object models.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Camera parameters of the scene.

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D poses of the objects.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"alpha", "attribute", "blue_channel_attrib", "color", "color_attrib", "color_attrib_end", "color_attrib_start", "colored", "compatibility_mode_enable", "disp_lines", "disp_normals", "disp_pose", "green_channel_attrib", "light_position", "line_color", "lut", "normal_color", "point_size", "quality", "red_channel_attrib", "rgb_channel_attrib_end", "rgb_channel_attrib_start"

**`genParamValue`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

Default:
[]

List of values:
"auto", "blue", "coord_x", "coord_y", "coord_z", "faces", "false", "green", "lines", "normal_x", "normal_y", "normal_z", "points", "primitive", "red", "true"

## Result

`RenderObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`FindSurfaceModel`,
`FitPrimitivesObjectModel3d`,
`SegmentObjectModel3d`,
`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`DispObj`

## See also

`DispObjectModel3d`,
`ProjectShapeModel3d`,
`ObjectModel3dToXyz`

## Module

3D Metrology
