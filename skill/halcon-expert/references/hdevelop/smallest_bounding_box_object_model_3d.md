# smallest_bounding_box_object_model_3d (Operator)

## Name

`smallest_bounding_box_object_model_3d` — Calculate the smallest bounding box around the points of a
3D object model.

## Signature

`smallest_bounding_box_object_model_3d( : : ObjectModel3D, Type : Pose, Length1, Length2, Length3)`

## Description

`smallest_bounding_box_object_model_3d` calculates the smallest
bounding box around the points of a 3D object model.
The resulting bounding box is described using its coordinate system
(*`Pose`*), which is oriented such that the longest side of the
box is aligned with the x-axis, the second longest side is aligned with
the y-axis and the smallest side is aligned with the z-axis.
The lengths of the sides are returned in *`Length1`*,
*`Length2`*, and *`Length3`*, in descending order.
The box can be either axis-aligned or oriented, which can be chosen by the
*`Type`*. The algorithm for *'oriented'* is
computationally significantly more costly than the algorithm for
*'axis_aligned'*, and returns only an approximation of the
oriented bounding box. Note that the algorithm for the oriented bounding
box is randomized and can return a different box for each call.

In order to retrieve the corners of the *'axis_aligned'* box,
the operator [`get_object_model_3d_params`](get_object_model_3d_params.md) can be used with the
parameter *'bounding_box1'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`Type`** (input_control)  string `→`  (string)

The method that is used to estimate the
smallest box.

Default:
'oriented'

List of values:
'axis_aligned', 'oriented'

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

The pose that describes the position and
orientation of the box that is generated.
The pose has its origin in the center of the
box and is oriented such
that the x-axis is aligned with the longest
side of the box.

**`Length1`** (output_control)  number(-array) `→`  (real)

The length of the longest side of the box.

Number of elements:
Length1 == ObjectModel3D

**`Length2`** (output_control)  number(-array) `→`  (real)

The length of the second longest side of the
box.

Number of elements:
Length2 == ObjectModel3D

**`Length3`** (output_control)  number(-array) `→`  (real)

The length of the third longest side of the
box.

Number of elements:
Length3 == ObjectModel3D

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(20), rand(20), rand(20), \
                                 ObjectModel3D)
smallest_bounding_box_object_model_3d (ObjectModel3D, 'oriented', \
                                       Pose, Length1, Length2, Length3)
gen_box_object_model_3d (Pose, Length1, Length2, Length3, ObjectModel3D1)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3D,ObjectModel3D1], \
                           [], [], ['alpha_1'], [0.5], [], [], [], PoseOut)
```

## Result

`smallest_bounding_box_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`connection_object_model_3d`,
`simplify_object_model_3d`

## Possible Successors

`gen_box_object_model_3d`

## See also

`smallest_sphere_object_model_3d`

## Module

3D Metrology
