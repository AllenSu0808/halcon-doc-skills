# GenObjectModel3dFromPoints (Operator)

## Name

`GenObjectModel3dFromPoints` — Create a 3D object model that represents a point cloud from a set of 3D points.

## Signature

`static void HOperatorSet.GenObjectModel3dFromPoints(HTuple x, HTuple y, HTuple z, out HTuple objectModel3D)`

`public HObjectModel3D(HTuple x, HTuple y, HTuple z)`

`public HObjectModel3D(double x, double y, double z)`

`void HObjectModel3D.GenObjectModel3dFromPoints(HTuple x, HTuple y, HTuple z)`

`void HObjectModel3D.GenObjectModel3dFromPoints(double x, double y, double z)`

## Description

`GenObjectModel3dFromPoints` creates a 3D object model
that represents a point cloud. The points are described by x-, y-, and
z-coordinates in the parameters *`x`*, *`y`*, and
*`z`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`x`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

The x-coordinates of the points in the 3D point
cloud.

**`y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

The y-coordinates of the points in the 3D point
cloud.

**`z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

The z-coordinates of the points in the 3D point
cloud.

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

`GenObjectModel3dFromPoints` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`GetObjectModel3dParams`

## Possible Successors

`ConnectionObjectModel3d`,
`ConvexHullObjectModel3d`

## Alternatives

`XyzToObjectModel3d`

## See also

`GenBoxObjectModel3d`,
`GenSphereObjectModel3d`,
`GenCylinderObjectModel3d`

## Module

3D Metrology
