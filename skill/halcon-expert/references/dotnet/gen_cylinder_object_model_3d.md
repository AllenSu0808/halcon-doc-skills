# GenCylinderObjectModel3d (Operator)

## Name

`GenCylinderObjectModel3d` — Create a 3D object model that represents a cylinder.

## Signature

`static void HOperatorSet.GenCylinderObjectModel3d(HTuple pose, HTuple radius, HTuple minExtent, HTuple maxExtent, out HTuple objectModel3D)`

`static HObjectModel3D[] HObjectModel3D.GenCylinderObjectModel3d(HPose[] pose, HTuple radius, HTuple minExtent, HTuple maxExtent)`

`void HObjectModel3D.GenCylinderObjectModel3d(HPose pose, double radius, double minExtent, double maxExtent)`

## Description

`GenCylinderObjectModel3d` creates a cylinder-shaped 3D
primitive, i.e., a 3D object model that represents a cylinder. A
cylinder is described by its center and the direction of its axis in
*`pose`* and by its radius in *`radius`*. The pose has the
origin on the rotation axis of the cylinder and is oriented such
that the z-axis is aligned with the main direction of the cylinder.
Additionally, the extensions of the cylinder are
given by *`minExtent`* and *`maxExtent`*. *`minExtent`*
and *`maxExtent`* represent the z-coordinates of the lowest and
highest points of the cylinder on the rotation axis. The handle of the
3D object model is returned by the parameter *`objectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The pose that describes the position and
orientation of the cylinder.

**`radius`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

The radius of the cylinder.

**`minExtent`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Lowest z-coordinate of the cylinder in the
direction of the rotation axis.

**`maxExtent`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Highest z-coordinate of the cylinder in the
direction of the rotation axis.

Restriction:
`MinExtent < MaxExtent`

**`objectModel3D`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

`GenCylinderObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`GetObjectModel3dParams`,
`SampleObjectModel3d`,
`ClearObjectModel3d`

## See also

`GenSphereObjectModel3d`,
`GenSphereObjectModel3dCenter`,
`GenPlaneObjectModel3d`,
`GenBoxObjectModel3d`

## Module

3D Metrology
