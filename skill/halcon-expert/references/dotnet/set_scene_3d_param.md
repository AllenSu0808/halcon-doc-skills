# SetScene3dParam (Operator)

## Name

`SetScene3dParam` — Set parameters of a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dParam(HTuple scene3D, HTuple genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dParam(string genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dParam(string genParamName, string genParamValue)`

## Description

`SetScene3dParam` sets parameters of the 3D scene *`scene3D`*.
The name and value of a parameter must be given in *`genParamName`* and
*`genParamValue`*.

All parameters that can be set with [`SetScene3dInstanceParam`](set_scene_3d_instance_param.md)
can be set with `SetScene3dParam` for all instances of a scene.

Additionally, the following parameters can be set:

- ***"disp_background"*:** —

  Flag, if the current window content should be used as background.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"colored"*:** —

  Set the colors of all currently added instances to different
  colors. The value of this parameter defines the number of colors
  that are used.

  List of values:
   *3*, *6*, *12*.

  Default:
   All objects are displayed white.
- ***"object_index_persistence"*:** —

  Must be set to *"true"* to enable the object index query
  with [`GetDisplayScene3dInfo`](get_display_scene_3d_info.md).

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"depth_persistence"*:** —

  Must be set to *"true"* to enable the depth query with
  [`GetDisplayScene3dInfo`](get_display_scene_3d_info.md).

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"quality"*:** —

  Must be set to *"low"* to enable faster rendering without
  anti aliasing.

  List of values:
   *"low"*, *"high"*.

  Default:
   *"high"*.
- ***"compatibility_mode_enable"*:** —

  Enforce the usage of the fallback mode to OpenGL 1.1.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"quality"

List of values:
"alpha", "attribute", "blue_channel_attrib", "color", "color_attrib", "color_attrib_end", "color_attrib_start", "colored", "compatibility_mode_enable", "depth_persistence", "disp_background", "disp_lines", "disp_normals", "disp_pose", "green_channel_attrib", "line_color", "line_width", "lut", "normal_color", "object_index_persistence", "point_size", "quality", "red_channel_attrib", "rgb_channel_attrib_end", "rgb_channel_attrib_start", "visible"

**`genParamValue`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

Default:
"high"

Suggested values:
"true", "false", "high", "low", "coord_x", "coord_y", "coord_z", "normal_x", "normal_y", "normal_z", "red", "green", "blue", "auto", "faces", "primitive", "points", "lines"

## Result

`SetScene3dParam` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## See also

`SetScene3dInstanceParam`

## Module

3D Metrology
