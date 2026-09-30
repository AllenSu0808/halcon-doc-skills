# GenSphereObjectModel3dCenter (Operator)

## Name

`GenSphereObjectModel3dCenter` — Create a 3D object model that represents a sphere from x,y,z coordinates.

## Signature

`static void HOperatorSet.GenSphereObjectModel3dCenter(HTuple x, HTuple y, HTuple z, HTuple radius, out HTuple objectModel3D)`

`static HObjectModel3D[] HObjectModel3D.GenSphereObjectModel3dCenter(HTuple x, HTuple y, HTuple z, HTuple radius)`

`void HObjectModel3D.GenSphereObjectModel3dCenter(double x, double y, double z, double radius)`

## Description

`GenSphereObjectModel3dCenter` creates a sphere-shaped 3D
primitive, i.e., a 3D object model that represents a sphere. A sphere
is defined by its center given in *`x`*, *`y`*, and
*`z`*, and its radius given in *`radius`*.
The handle of the 3D object model is returned by the
parameter *`objectModel3D`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`x`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

The x-coordinate of the center point of
the sphere.

**`y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

The y-coordinate of the center point of
the sphere.

**`z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

The z-coordinate of the center point of
the sphere.

**`radius`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The radius of the sphere.

**`objectModel3D`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

`GenSphereObjectModel3dCenter` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`SmallestSphereObjectModel3d`

## Possible Successors

`GetObjectModel3dParams`,
`SampleObjectModel3d`,
`ClearObjectModel3d`

## Alternatives

`GenSphereObjectModel3d`

## See also

`GenCylinderObjectModel3d`,
`GenPlaneObjectModel3d`,
`GenBoxObjectModel3d`

## Module

3D Metrology
