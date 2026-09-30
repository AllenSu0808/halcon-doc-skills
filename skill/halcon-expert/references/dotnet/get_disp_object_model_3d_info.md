# GetDispObjectModel3dInfo (Operator)

## Name

`GetDispObjectModel3dInfo` — Get the depth or the index of a displayed 3D object model.

## Signature

`static void HOperatorSet.GetDispObjectModel3dInfo(HTuple windowHandle, HTuple row, HTuple column, HTuple information, out HTuple value)`

`static HTuple HObjectModel3D.GetDispObjectModel3dInfo(HWindow windowHandle, HTuple row, HTuple column, HTuple information)`

`static int HObjectModel3D.GetDispObjectModel3dInfo(HWindow windowHandle, double row, double column, string information)`

## Description

`GetDispObjectModel3dInfo` returns information on the
3D object models that have been displayed with [`DispObjectModel3d`](disp_object_model_3d.md)
in the window *`windowHandle`*. The requested information at the
positions (*`row`*, *`column`*) is returned in *`value`*.

The following values can be queried via *`information`*:

- ***"object_index"*** —

  The indices of the 3D object models that have been displayed at the
  positions (*`row`*, *`column`*).
  If no 3D object model was displayed at this position, -1 is returned.
  In order to retrieve this information, [`DispObjectModel3d`](disp_object_model_3d.md) must
  have been called with the generic parameter
  *"object_index_persistence"* set to *"true"*.
- ***"depth"*** —

  The depth (i.e. the Z coordinate in the camera coordinate system) at the
  positions (*`row`*, *`column`*). If no 3D object
  model was displayed at one of these positions, -1.0 is returned
  for this position.
  In order to retrieve this information, [`DispObjectModel3d`](disp_object_model_3d.md) must
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
Use [`GetMpositionSubPix`](get_mposition_sub_pix.md) or [`GetMbuttonSubPix`](get_mbutton_sub_pix.md) to obtain
these coordinates directly.
In case the window coordinates correspond to values outside the current
image part, the operator behavior is undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

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

`GetDispObjectModel3dInfo` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`DispObjectModel3d`,
`GetMbutton`,
`GetMbuttonSubPix`,
`GetMposition`,
`GetMpositionSubPix`

## See also

`DispObjectModel3d`

## Module

3D Metrology
