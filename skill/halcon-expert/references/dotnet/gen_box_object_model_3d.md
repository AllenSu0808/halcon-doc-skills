# GenBoxObjectModel3d (Operator)

## Name

`GenBoxObjectModel3d` — Create a 3D object model that represents a box.

## Signature

`static void HOperatorSet.GenBoxObjectModel3d(HTuple pose, HTuple lengthX, HTuple lengthY, HTuple lengthZ, out HTuple objectModel3D)`

`static HObjectModel3D[] HObjectModel3D.GenBoxObjectModel3d(HPose[] pose, HTuple lengthX, HTuple lengthY, HTuple lengthZ)`

`void HObjectModel3D.GenBoxObjectModel3d(HPose pose, double lengthX, double lengthY, double lengthZ)`

## Description

`GenBoxObjectModel3d` creates a box-shaped 3D primitive, i.e.,
a 3D object model that represents a box. The box is specified by a
*`pose`* and the side lengths *`lengthX`*, *`lengthY`*, and
*`lengthZ`* along the respective axis of the pose. The handle of
the resulting 3D object model is returned by parameter
*`objectModel3D`*.

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

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The pose that describes the position and
orientation of the box. The pose has its
origin in the center of the box.

**`lengthX`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The length of the box along the x-axis.

**`lengthY`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The length of the box along the y-axis.

Number of elements:
LengthY == LengthX

**`lengthZ`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The length of the box along the z-axis.

Number of elements:
LengthZ == LengthX

**`objectModel3D`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

`GenBoxObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`SmallestBoundingBoxObjectModel3d`

## Possible Successors

`GetObjectModel3dParams`,
`SampleObjectModel3d`,
`ClearObjectModel3d`

## See also

`GenCylinderObjectModel3d`,
`GenSphereObjectModel3d`,
`GenSphereObjectModel3dCenter`,
`GenPlaneObjectModel3d`

## Module

3D Metrology
