# convex_hull_object_model_3d (Operator)

## Name

`convex_hull_object_model_3d` — Calculate the convex hull of a 3D object model.

## Signature

`def convex_hull_object_model_3d(object_model_3d: MaybeSequence[HHandle]) -> Sequence[HHandle]`

`def convex_hull_object_model_3d_s(object_model_3d: MaybeSequence[HHandle]) -> HHandle`

## Description

`convex_hull_object_model_3d` calculates the convex hull of
the 3D object model given in *`object_model_3d`*. The operator returns
the convex hull as a 3D object model with the handle
*`object_model_3dconvex_hull`*.

If one of the dimensions of the input points has no deviation at all,
the result will consist of lines and not triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`object_model_3dconvex_hull`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handle of the 3D object model that describes
the convex hull.

Number of elements:
ObjectModel3DConvexHull == ObjectModel3D

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(20)-0.5, rand(20)-0.5,\
                                 rand(20)-0.5, ObjectModel3D)
convex_hull_object_model_3d (ObjectModel3D, ObjectModel3DConvexHull)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3DConvexHull], \
                           [], [], [], [], [], [], [], PoseOut)
```

## Result

`convex_hull_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`connection_object_model_3d`,
`select_points_object_model_3d`

## Possible Successors

`project_object_model_3d`

## Module

3D Metrology
