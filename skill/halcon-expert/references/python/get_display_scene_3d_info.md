# get_display_scene_3d_info (Operator)

## Name

`get_display_scene_3d_info` — Get the depth or the index of instances in a displayed 3D scene.

## Signature

`def get_display_scene_3d_info(window_handle: HHandle, scene_3d: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], information: MaybeSequence[str]) -> Sequence[Union[int, float]]`

`def get_display_scene_3d_info_s(window_handle: HHandle, scene_3d: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], information: MaybeSequence[str]) -> Union[int, float]`

## Description

`get_display_scene_3d_info` returns information on the
3D object models in the 3D scene *`scene_3d`* that have been displayed
with [`display_scene_3d`](display_scene_3d.md) in the window *`window_handle`*.
The requested information at the positions (*`row`*, *`column`*)
is returned in *`value`*.

The following values can be queried via *`information`*:

- ***"object_index"*** —

  The indices of the 3D object models that have been displayed at the
  positions (*`row`*, *`column`*).
  If no 3D object model was displayed at this position, -1 is returned.
  In order to retrieve this information, the parameter
  *"object_index_persistence"* must have been set to *"true"*
  with [`set_scene_3d_param`](set_scene_3d_param.md).
- ***"depth"*** —

  The depth (i.e. the Z coordinate in the camera coordinate system) at the
  positions (*`row`*, *`column`*). If no 3D object
  model was displayed at one of these positions, -1.0 is returned
  for this position.
  In order to retrieve this information, the parameter
  *"depth_persistence"* must have been set to *"true"*
  with [`set_scene_3d_param`](set_scene_3d_param.md).

The window coordinates *`row`*, *`column`* must be provided with
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

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`row`** (input_control)  integer(-array) `→` MaybeSequence[Union[float, int]]

Row coordinates.

**`column`** (input_control)  integer(-array) `→` MaybeSequence[Union[float, int]]

Column coordinates.

**`information`** (input_control)  string(-array) `→` MaybeSequence[str]

Information.

Default:
"depth"

List of values:
"depth", "object_index"

**`value`** (output_control)  integer(-array) `→` Sequence[Union[int, float]]

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
