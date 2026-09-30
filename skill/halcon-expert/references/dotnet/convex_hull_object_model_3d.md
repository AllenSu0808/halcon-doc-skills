# ConvexHullObjectModel3d (Operator)

## Name

`ConvexHullObjectModel3d` — Calculate the convex hull of a 3D object model.

## Signature

`static void HOperatorSet.ConvexHullObjectModel3d(HTuple objectModel3D, out HTuple objectModel3DConvexHull)`

`static HObjectModel3D[] HObjectModel3D.ConvexHullObjectModel3d(HObjectModel3D[] objectModel3D)`

`HObjectModel3D HObjectModel3D.ConvexHullObjectModel3d()`

## Description

`ConvexHullObjectModel3d` calculates the convex hull of
the 3D object model given in *`objectModel3D`*. The operator returns
the convex hull as a 3D object model with the handle
*`objectModel3DConvexHull`*.

If one of the dimensions of the input points has no deviation at all,
the result will consist of lines and not triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`objectModel3DConvexHull`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

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

`ConvexHullObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`ConnectionObjectModel3d`,
`SelectPointsObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`

## Module

3D Metrology
