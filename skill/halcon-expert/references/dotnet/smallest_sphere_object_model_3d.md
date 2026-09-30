# SmallestSphereObjectModel3d (Operator)

## Name

`SmallestSphereObjectModel3d` — Calculate the smallest sphere around the points of a 3D object model.

## Signature

`static void HOperatorSet.SmallestSphereObjectModel3d(HTuple objectModel3D, out HTuple centerPoint, out HTuple radius)`

`static HTuple HObjectModel3D.SmallestSphereObjectModel3d(HObjectModel3D[] objectModel3D, out HTuple radius)`

`HTuple HObjectModel3D.SmallestSphereObjectModel3d(out double radius)`

## Description

`SmallestSphereObjectModel3d` calculates the smallest sphere
around the points of the 3D object model given by
*`objectModel3D`*. The resulting center will be stored as x-, y-, and
z-coordinates in
*`centerPoint`* as 3 values representing X, Y, and Z.
The Radius is given in *`radius`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`centerPoint`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

x-, y-, and z-coordinates
describing the center point of the sphere.

Number of elements:
CenterPoint == 3 * ObjectModel3D

**`radius`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The estimated radius of the sphere.

Number of elements:
Radius == ObjectModel3D

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(20), rand(20), rand(20),\
                                 ObjectModel3D)
smallest_sphere_object_model_3d(ObjectModel3D, CenterPoint, Radius)
gen_sphere_object_model_3d_center (CenterPoint[0], CenterPoint[1], \
                                   CenterPoint[2], Radius, ObjectModel3D1)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3D,ObjectModel3D1], \
                           [], [], ['alpha_1'], [0.5], [], [], [], PoseOut)
```

## Result

`SmallestSphereObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ConnectionObjectModel3d`

## Possible Successors

`GenSphereObjectModel3d`

## See also

`SmallestBoundingBoxObjectModel3d`

## Module

3D Metrology
