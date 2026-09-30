# AddScene3dLabel (Operator)

## Name

`AddScene3dLabel` — Add a text label to a 3D scene.

## Signature

`static void HOperatorSet.AddScene3dLabel(HTuple scene3D, HTuple text, HTuple referencePoint, HTuple position, HTuple relatesTo, out HTuple labelIndex)`

`int HScene3D.AddScene3dLabel(HTuple text, HTuple referencePoint, HTuple position, HTuple relatesTo)`

`int HScene3D.AddScene3dLabel(string text, HTuple referencePoint, HTuple position, HTuple relatesTo)`

## Description

`AddScene3dLabel` adds a label with the text in *`text`* to the
3D scene *`scene3D`* and returns its index in *`labelIndex`*.

The reference point of the label must be given as *[X,Y,Z]* point in the
coordinate system of the 3D scene in *`referencePoint`*.
It is valid to create labels without a reference
point by passing an empty tuple to *`referencePoint`*, however
*`relatesTo`* must be set to *"window"* in this case
(see the description of *`relatesTo`* below).

If multiple label texts are supplied in *`text`*, multiple labels
are created. It is possible to set one reference
point for all labels or a specific reference point for each label.
The same applies to *`position`* and *`relatesTo`*.

Labels can be positioned fixed in window coordinates or relative to the
projection of the reference point. The two parameters *`position`*
and *`relatesTo`* are used for positioning.

**Fixed positioning**

If *`relatesTo`* is set to *"window"*, the Label is shown at
a fixed position in the window (or rendered image), even if the pose of the
3D scene is changed.
There are two ways to specify the position. You can either supply the
*[Row,Column]* coordinates of the top left corner of the label in
*`position`* or use one of the predefined positions:

|  |  |  |
| --- | --- | --- |
| *"top_left"* | *"top"* | *"top_right"* |
| *"left"* | *"center"* | *"right"* |
| *"bottom_left"* | *"bottom"* | *"bottom_right"* |

**Relative positioning**

If *`relatesTo`* is set to *"point"*, the Label is shown at
a position relative to the projection of the reference point. This way,
the label moves with the reference point if the pose of the 3D scene is
changed.
There are two ways to specify the position. You can either supply the
*[Row,Column]* offset of the top left corner of the label in
*`position`* or use one of the predefined positions:

|  |  |  |
| --- | --- | --- |
| *"top_left"* | *"top"* | *"top_right"* |
| *"left"* | *"center"* | *"right"* |
| *"bottom_left"* | *"bottom"* | *"bottom_right"* |

The operator [`SetScene3dLabelParam`](set_scene_3d_label_param.md) can be
used to change these values and to set other parameters such as the
label's color and font.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`text`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Text of the label.

Default:
"label"

**`referencePoint`** (input_control)  point-array `→` [HTuple](HTuple.md) (*double* / int / long)

Point of reference of the label.

Number of elements:
3

**`position`** (input_control)  point-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Position of the label.

Default:
"top"

List of values:
"bottom", "bottom_left", "bottom_right", "center", "left", "right", "top", "top_left", "top_right"

**`relatesTo`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Indicates fixed or relative positioning.

Number of elements:
1

Default:
"point"

List of values:
"point", "window"

**`labelIndex`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the new label in the 3D scene.

## Result

`AddScene3dLabel` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## Possible Successors

`SetScene3dLabelParam`

## See also

`RemoveScene3dInstance`

## Module

3D Metrology
