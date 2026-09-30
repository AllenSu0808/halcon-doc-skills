# smallest_sphere_object_model_3d (Operator)

## Name

`smallest_sphere_object_model_3d` — Calculate the smallest sphere around the points of a 3D object model.

## Signature

`smallest_sphere_object_model_3d( : : ObjectModel3D : CenterPoint, Radius)`

## Description

`smallest_sphere_object_model_3d` calculates the smallest sphere
around the points of the 3D object model given by
*`ObjectModel3D`*. The resulting center will be stored as x-, y-, and
z-coordinates in
*`CenterPoint`* as 3 values representing X, Y, and Z.
The Radius is given in *`Radius`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`CenterPoint`** (output_control)  number-array `→`  (real)

x-, y-, and z-coordinates
describing the center point of the sphere.

Number of elements:
CenterPoint == 3 * ObjectModel3D

**`Radius`** (output_control)  number(-array) `→`  (real)

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

`smallest_sphere_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`connection_object_model_3d`

## Possible Successors

`gen_sphere_object_model_3d`

## See also

`smallest_bounding_box_object_model_3d`

## Module

3D Metrology
