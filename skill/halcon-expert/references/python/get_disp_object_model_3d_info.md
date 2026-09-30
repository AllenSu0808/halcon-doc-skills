# get_disp_object_model_3d_info (Operator)

## Name

`get_disp_object_model_3d_info` — Get the depth or the index of a displayed 3D object model.

## Signature

`def get_disp_object_model_3d_info(window_handle: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], information: MaybeSequence[str]) -> Sequence[Union[int, float]]`

`def get_disp_object_model_3d_info_s(window_handle: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], information: MaybeSequence[str]) -> Union[int, float]`

## Description

`get_disp_object_model_3d_info` returns information on the
3D object models that have been displayed with [`disp_object_model_3d`](disp_object_model_3d.md)
in the window *`window_handle`*. The requested information at the
positions (*`row`*, *`column`*) is returned in *`value`*.

The following values can be queried via *`information`*:

- ***"object_index"*** —

  The indices of the 3D object models that have been displayed at the
  positions (*`row`*, *`column`*).
  If no 3D object model was displayed at this position, -1 is returned.
  In order to retrieve this information, [`disp_object_model_3d`](disp_object_model_3d.md) must
  have been called with the generic parameter
  *"object_index_persistence"* set to *"true"*.
- ***"depth"*** —

  The depth (i.e. the Z coordinate in the camera coordinate system) at the
  positions (*`row`*, *`column`*). If no 3D object
  model was displayed at one of these positions, -1.0 is returned
  for this position.
  In order to retrieve this information, [`disp_object_model_3d`](disp_object_model_3d.md) must
  have been called with the generic parameter
  *"depth_persistence"* set to *"true"*.

The window coordinates *`row`*, *`column`* must be provided in
respect to the current image part. Thereby they are understood in
edge centered subpixel accurate coordinates,
see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md).
Given the current image part
(`row1`,`column1`,`row2`,`column2`,
in the HALCON standard coordinate system), the upper left corner corresponds
to the coordinates (`row1` - 0.5, `column1` - 0.5).
Accordingly, the bottom right corner corresponds to the coordinates
(`row2` - 0.5, `column2` - 0.5).
Use [`get_mposition_sub_pix`](get_mposition_sub_pix.md) or [`get_mbutton_sub_pix`](get_mbutton_sub_pix.md) to obtain
these coordinates directly.
In case the window coordinates correspond to values outside the current
image part, the operator behavior is undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

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

`get_disp_object_model_3d_info` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`disp_object_model_3d`,
`get_mbutton`,
`get_mbutton_sub_pix`,
`get_mposition`,
`get_mposition_sub_pix`

## See also

`disp_object_model_3d`

## Module

3D Metrology
