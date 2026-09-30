# gen_object_model_3d_from_points (Operator)

## Name

`gen_object_model_3d_from_points` — Create a 3D object model that represents a point cloud from a set of 3D points.

## Signature

`gen_object_model_3d_from_points( : : X, Y, Z : ObjectModel3D)`

## Description

`gen_object_model_3d_from_points` creates a 3D object model
that represents a point cloud. The points are described by x-, y-, and
z-coordinates in the parameters *`X`*, *`Y`*, and
*`Z`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`X`** (input_control)  point3d.x(-array) `→`  (real)

The x-coordinates of the points in the 3D point
cloud.

**`Y`** (input_control)  point3d.y(-array) `→`  (real)

The y-coordinates of the points in the 3D point
cloud.

**`Z`** (input_control)  point3d.z(-array) `→`  (real)

The z-coordinates of the points in the 3D point
cloud.

**`ObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

Handle of the resulting 3D object model.

## Result

`gen_object_model_3d_from_points` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`get_object_model_3d_params`

## Possible Successors

`connection_object_model_3d`,
`convex_hull_object_model_3d`

## Alternatives

`xyz_to_object_model_3d`

## See also

`gen_box_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_cylinder_object_model_3d`

## Module

3D Metrology
