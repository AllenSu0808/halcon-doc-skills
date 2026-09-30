# VolumeObjectModel3dRelativeToPlane (Operator)

## Name

`VolumeObjectModel3dRelativeToPlane` — Calculate the volume of a 3D object model.

## Signature

`static void HOperatorSet.VolumeObjectModel3dRelativeToPlane(HTuple objectModel3D, HTuple plane, HTuple mode, HTuple useFaceOrientation, out HTuple volume)`

`static HTuple HObjectModel3D.VolumeObjectModel3dRelativeToPlane(HObjectModel3D[] objectModel3D, HPose[] plane, HTuple mode, HTuple useFaceOrientation)`

`double HObjectModel3D.VolumeObjectModel3dRelativeToPlane(HPose plane, string mode, string useFaceOrientation)`

## Description

`VolumeObjectModel3dRelativeToPlane` calculates the volume
under the faces of a 3D object model relative to a plane. The plane is
defined by the x-y plane of the pose given in *`plane`*.

For *`objectModel3D`*, a triangulation or a list of polygons must be
available. With default settings, if the mesh is watertight and ordered, the
operator calculates the actual volume of the 3D object model.
To also cover cases where the mesh is not closed or the faces are not
ordered consistently, the calculation of the volume can be influenced
with the parameters *`mode`* and *`useFaceOrientation`*.

**How the volume is calculated:**

First, the operator calculates the volume of the prisms that are constructed
by projecting each face onto the plane.

The individual volumes of the prisms can be positive or negative depending
on the orientation of the face (away or towards the plane) or the
location of the face (above or below the plane). This can be controlled
with the parameter *`useFaceOrientation`*.

After that, the volumes of the prisms are added up depending on the
parameter *`mode`*.

The volume returned in *`volume`* is the absolute value of the
calculated sum.

**How to set the parameters:**

*`mode`* can be set to the following options:

- **'signed' (default)** —

  The volumes above and below the plane are added.
- **'unsigned'** —

  The volume below the plane is subtracted from the volume
  above the plane.
- **'positive'** —

  Only faces above the plane are taken into account.
- **'negative'** —

  Only faces below the plane are taken into account.

*`useFaceOrientation`* can be set to the following options:

- **'true' (default)** —

  Use the orientation of the faces relative to the plane.
  A face points away from the plane if the corner points are ordered
  clockwise when viewed from the plane.
  The volume under a face is considered **positive** if the
  orientation of the face is **away from the plane**.
  In contrast, it is considered **negative** if the
  orientation of the face is **towards the plane**.
- **'false'** —

  The volume under a face is considered **positive** if the
  face is located **above** the plane. In contrast,
  it is considered **negative** if the face is
  located **below** the plane.

For example, with the default combination (*`mode`*: *"signed"*,
*`useFaceOrientation`*: *"true"*), you can approximate the
real volume of a closed object. In this case, the *`plane`* is still
required, but does not change the resulting volume.

![figure](../assets/2bb359af94c284c3.svg)

Example: (A) *`mode`*: *"signed"*,
*`useFaceOrientation`*: *"true"*: $V=(2\ast3\ast4)+(-2\ast3\ast2)=24-12=12$
(B) *`mode`*: *"signed"*,
*`useFaceOrientation`*: *"false"*: $V=(2\ast3\ast4)+(2\ast3\ast2)=24+12=36$ (C) *`mode`*: *"negative"*: $V=0$

## Attention

The calculation of the volume might be numerically unstable in
case of a large distance between the plane and the object (approx.
distance > 10000 times the object diameter).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`plane`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the plane.

Default:
[0,0,0,0,0,0,0]

**`mode`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Method to combine volumes laying
above and below the reference plane.

Default:
"signed"

List of values:
"negative", "positive", "signed", "unsigned"

**`useFaceOrientation`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Decides whether the orientation of a face should
affect the resulting sign of the underlying
volume.

Default:
"true"

List of values:
"false", "true"

**`volume`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Absolute value of the calculated volume.

Number of elements:
Volume == ObjectModel3D

## Example (HDevelop)

```
gen_box_object_model_3d ([0,0,0,0,0,0,0],3,2,1, ObjectModel3D)
convex_hull_object_model_3d (ObjectModel3D, ObjectModel3DConvexHull)
volume_object_model_3d_relative_to_plane (ObjectModel3DConvexHull,\
                                          [0,0,0,0,0,0,0], 'signed',\
                                          'true', Volume)
```

## Result

`VolumeObjectModel3dRelativeToPlane` returns 2 (
H_MSG_TRUE)
if all
parameters are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`SelectPointsObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`,
`SelectObjectModel3d`

## See also

`AreaObjectModel3d`

## Module

3D Metrology
