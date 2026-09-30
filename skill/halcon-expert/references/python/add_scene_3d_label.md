# add_scene_3d_label (Operator)

## Name

`add_scene_3d_label` — Add a text label to a 3D scene.

## Signature

`def add_scene_3d_label(scene_3d: HHandle, text: MaybeSequence[str], reference_point: Sequence[Union[float, int]], position: Sequence[Union[float, int, str]], relates_to: Sequence[str]) -> int`

## Description

`add_scene_3d_label` adds a label with the text in *`text`* to the
3D scene *`scene_3d`* and returns its index in *`label_index`*.

The reference point of the label must be given as *[X,Y,Z]* point in the
coordinate system of the 3D scene in *`reference_point`*.
It is valid to create labels without a reference
point by passing an empty tuple to *`reference_point`*, however
*`relates_to`* must be set to *"window"* in this case
(see the description of *`relates_to`* below).

If multiple label texts are supplied in *`text`*, multiple labels
are created. It is possible to set one reference
point for all labels or a specific reference point for each label.
The same applies to *`position`* and *`relates_to`*.

Labels can be positioned fixed in window coordinates or relative to the
projection of the reference point. The two parameters *`position`*
and *`relates_to`* are used for positioning.

**Fixed positioning**

If *`relates_to`* is set to *"window"*, the Label is shown at
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

If *`relates_to`* is set to *"point"*, the Label is shown at
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

The operator [`set_scene_3d_label_param`](set_scene_3d_label_param.md) can be
used to change these values and to set other parameters such as the
label's color and font.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`text`** (input_control)  string(-array) `→` MaybeSequence[str]

Text of the label.

Default:
"label"

**`reference_point`** (input_control)  point-array `→` Sequence[Union[float, int]]

Point of reference of the label.

Number of elements:
3

**`position`** (input_control)  point-array `→` Sequence[Union[float, int, str]]

Position of the label.

Default:
"top"

List of values:
"bottom", "bottom_left", "bottom_right", "center", "left", "right", "top", "top_left", "top_right"

**`relates_to`** (input_control)  string-array `→` Sequence[str]

Indicates fixed or relative positioning.

Number of elements:
1

Default:
"point"

List of values:
"point", "window"

**`label_index`** (output_control)  integer `→` int

Index of the new label in the 3D scene.

## Result

`add_scene_3d_label` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`create_scene_3d`

## Possible Successors

`set_scene_3d_label_param`

## See also

`remove_scene_3d_instance`

## Module

3D Metrology
