# GenPlaneObjectModel3d (Operator)

## Name

`GenPlaneObjectModel3d` — Create a 3D object model that represents a plane.

## Signature

`static void HOperatorSet.GenPlaneObjectModel3d(HTuple pose, HTuple XExtent, HTuple YExtent, out HTuple objectModel3D)`

`void HObjectModel3D.GenPlaneObjectModel3d(HPose pose, HTuple XExtent, HTuple YExtent)`

`void HObjectModel3D.GenPlaneObjectModel3d(HPose pose, double XExtent, double YExtent)`

## Description

`GenPlaneObjectModel3d` creates a planar 3D primitive, i.e.,
a 3D object model that represents a plane. The plane is described by
its center and rotation. The normal vector of the plane is aligned to the
z-axis of the rotated coordinate system. The center and the rotation
is set with the parameter *`pose`*. Additionally, the plane can
be limited by a polygon, that is defined by points with the coordinates
*`XExtent`* and *`YExtent`*. The handle of the 3D object
model is returned by the parameter *`objectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The center and the rotation of the plane.

Number of elements:
Pose == 7

**`XExtent`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

x coordinates specifying the extent of the plane.

**`YExtent`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

y coordinates specifying the extent of the plane.

Number of elements:
XExtent == YExtent

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

`GenPlaneObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`GetObjectModel3dParams`,
`SampleObjectModel3d`,
`ClearObjectModel3d`

## See also

`GenCylinderObjectModel3d`,
`GenSphereObjectModel3d`,
`GenSphereObjectModel3dCenter`,
`GenBoxObjectModel3d`

## Module

3D Metrology
