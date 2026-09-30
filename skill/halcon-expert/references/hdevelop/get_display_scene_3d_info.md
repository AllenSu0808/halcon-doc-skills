# get_display_scene_3d_info (Operator)

## Name

`get_display_scene_3d_info` — Get the depth or the index of instances in a displayed 3D scene.

## Signature

`get_display_scene_3d_info( : : WindowHandle, Scene3D, Row, Column, Information : Value)`

## Description

`get_display_scene_3d_info` returns information on the
3D object models in the 3D scene *`Scene3D`* that have been displayed
with [`display_scene_3d`](display_scene_3d.md) in the window *`WindowHandle`*.
The requested information at the positions (*`Row`*, *`Column`*)
is returned in *`Value`*.

The following values can be queried via *`Information`*:

- ***'object_index'*** —

  The indices of the 3D object models that have been displayed at the
  positions (*`Row`*, *`Column`*).
  If no 3D object model was displayed at this position, -1 is returned.
  In order to retrieve this information, the parameter
  *'object_index_persistence'* must have been set to *'true'*
  with [`set_scene_3d_param`](set_scene_3d_param.md).
- ***'depth'*** —

  The depth (i.e. the Z coordinate in the camera coordinate system) at the
  positions (*`Row`*, *`Column`*). If no 3D object
  model was displayed at one of these positions, -1.0 is returned
  for this position.
  In order to retrieve this information, the parameter
  *'depth_persistence'* must have been set to *'true'*
  with [`set_scene_3d_param`](set_scene_3d_param.md).

The window coordinates *`Row`*, *`Column`* must be provided with
respect to the current image part. As a consequence, these coordinates are
subpixel coordinates. Given the current image part (row1,column1,row2,
column2), the upper left corner corresponds to the coordinates
(row1 - 0.5, col1 - 0.5). Accordingly, the bottom right corner
corresponds to the coordinates (row2 - 0.5, col2 - 0.5). Use
[`get_mposition_sub_pix`](get_mposition_sub_pix.md) or [`get_mbutton_sub_pix`](get_mbutton_sub_pix.md) to obtain these
coordinates directly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`Row`** (input_control)  integer(-array) `→`  (real / integer)

Row coordinates.

**`Column`** (input_control)  integer(-array) `→`  (real / integer)

Column coordinates.

**`Information`** (input_control)  string(-array) `→`  (string)

Information.

Default:
'depth'

List of values:
'depth', 'object_index'

**`Value`** (output_control)  integer(-array) `→`  (integer / real)

Indices or the depth of the objects at (Row,Column).

## Result

`get_display_scene_3d_info` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`display_scene_3d`,
`get_mbutton`,
`get_mbutton_sub_pix`,
`get_mposition`,
`get_mposition_sub_pix`

## See also

`display_scene_3d`

## Module

3D Metrology
