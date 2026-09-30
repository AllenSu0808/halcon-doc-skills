# GetDisplayScene3dInfo (Operator)

## Name

`GetDisplayScene3dInfo` — Get the depth or the index of instances in a displayed 3D scene.

## Signature

`static void HOperatorSet.GetDisplayScene3dInfo(HTuple windowHandle, HTuple scene3D, HTuple row, HTuple column, HTuple information, out HTuple value)`

`HTuple HScene3D.GetDisplayScene3dInfo(HWindow windowHandle, HTuple row, HTuple column, HTuple information)`

`int HScene3D.GetDisplayScene3dInfo(HWindow windowHandle, double row, double column, string information)`

## Description

`GetDisplayScene3dInfo` returns information on the
3D object models in the 3D scene *`scene3D`* that have been displayed
with [`DisplayScene3d`](display_scene_3d.md) in the window *`windowHandle`*.
The requested information at the positions (*`row`*, *`column`*)
is returned in *`value`*.

The following values can be queried via *`information`*:

- ***"object_index"*** —

  The indices of the 3D object models that have been displayed at the
  positions (*`row`*, *`column`*).
  If no 3D object model was displayed at this position, -1 is returned.
  In order to retrieve this information, the parameter
  *"object_index_persistence"* must have been set to *"true"*
  with [`SetScene3dParam`](set_scene_3d_param.md).
- ***"depth"*** —

  The depth (i.e. the Z coordinate in the camera coordinate system) at the
  positions (*`row`*, *`column`*). If no 3D object
  model was displayed at one of these positions, -1.0 is returned
  for this position.
  In order to retrieve this information, the parameter
  *"depth_persistence"* must have been set to *"true"*
  with [`SetScene3dParam`](set_scene_3d_param.md).

The window coordinates *`row`*, *`column`* must be provided with
respect to the current image part. As a consequence, these coordinates are
subpixel coordinates. Given the current image part (row1,column1,row2,
column2), the upper left corner corresponds to the coordinates
(row1 - 0.5, col1 - 0.5). Accordingly, the bottom right corner
corresponds to the coordinates (row2 - 0.5, col2 - 0.5). Use
[`GetMpositionSubPix`](get_mposition_sub_pix.md) or [`GetMbuttonSubPix`](get_mbutton_sub_pix.md) to obtain these
coordinates directly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`row`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates.

**`column`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates.

**`information`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Information.

Default:
"depth"

List of values:
"depth", "object_index"

**`value`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Indices or the depth of the objects at (Row,Column).

## Result

`GetDisplayScene3dInfo` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`DisplayScene3d`,
`GetMbutton`,
`GetMbuttonSubPix`,
`GetMposition`,
`GetMpositionSubPix`

## See also

`DisplayScene3d`

## Module

3D Metrology
