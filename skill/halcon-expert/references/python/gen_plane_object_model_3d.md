# gen_plane_object_model_3d (Operator)

## Name

`gen_plane_object_model_3d` — Create a 3D object model that represents a plane.

## Signature

`def gen_plane_object_model_3d(pose: Sequence[Union[int, float]], xextent: MaybeSequence[Union[float, int]], yextent: MaybeSequence[Union[float, int]]) -> HHandle`

## Description

`gen_plane_object_model_3d` creates a planar 3D primitive, i.e.,
a 3D object model that represents a plane. The plane is described by
its center and rotation. The normal vector of the plane is aligned to the
z-axis of the rotated coordinate system. The center and the rotation
is set with the parameter *`pose`*. Additionally, the plane can
be limited by a polygon, that is defined by points with the coordinates
*`xextent`* and *`yextent`*. The handle of the 3D object
model is returned by the parameter *`object_model_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pose`** (input_control)  pose `→` Sequence[Union[int, float]]

The center and the rotation of the plane.

Number of elements:
Pose == 7

**`xextent`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

x coordinates specifying the extent of the plane.

**`yextent`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

y coordinates specifying the extent of the plane.

Number of elements:
XExtent == YExtent

**`object_model_3d`** (output_control)  object_model_3d `→` HHandle

Handle of the resulting 3D object model.

## Result

`gen_plane_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`get_object_model_3d_params`,
`sample_object_model_3d`,
`clear_object_model_3d`

## See also

`gen_cylinder_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`gen_box_object_model_3d`

## Module

3D Metrology
