# intersect_plane_object_model_3d (Operator)

## Name

`intersect_plane_object_model_3d` — Intersect a 3D object model with a plane.

## Signature

`def intersect_plane_object_model_3d(object_model_3d: MaybeSequence[HHandle], plane: Sequence[Union[int, float]]) -> Sequence[HHandle]`

`def intersect_plane_object_model_3d_s(object_model_3d: MaybeSequence[HHandle], plane: Sequence[Union[int, float]]) -> HHandle`

## Description

`intersect_plane_object_model_3d` intersects a 3D object model with
a plane that is defined by the x-y plane of the pose that is specified with
the parameter *`plane`*. The z-axis of the pose corresponds to the normal
of the plane.

The result is a set of 3D points connected by lines that is returned as 3D object model in
*`object_model_3dintersection`*.
Every triangle that intersects with the
plane creates two intersection points and a line between the two points.
The resulting set of lines is coplanar.

The lines can be displayed with [`disp_object_model_3d`](disp_object_model_3d.md) and queried
with [`get_object_model_3d_params`](get_object_model_3d_params.md)
using the parameter *"lines"*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* (*7* for *`plane`*) or
*N* (*N*7* for *`plane`*).
Parameters with tuple length *1* (*7* for *`plane`*) will be repeated internally
such that the number of computed output models is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`plane`** (input_control)  pose(-array) `→` Sequence[Union[int, float]]

Pose of the plane.

Default:
[0,0,0,0,0,0,0]

**`object_model_3dintersection`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handle of the 3D object model that describes
the intersection as a set of lines.

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(20)-0.5, rand(20)-0.5,\
                                 rand(20)-0.5, ObjectModel3D)
convex_hull_object_model_3d (ObjectModel3D, ObjectModel3DConvexHull)
intersect_plane_object_model_3d (ObjectModel3DConvexHull, [0,0,0,0,0,0,0], \
                                 ObjectModel3DIntersection)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3DIntersection, \
                           ObjectModel3DConvexHull], [], [], \
                           ['alpha_1'], [0.5], [], [], [], PoseOut)
```

## Result

`intersect_plane_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`select_points_object_model_3d`

## Possible Successors

`connection_object_model_3d`

## See also

`reduce_object_model_3d_by_view`

## Module

3D Metrology
