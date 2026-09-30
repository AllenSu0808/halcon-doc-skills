# TransPoseShapeModel3d (Operator)

## Name

`TransPoseShapeModel3d` — Transform a pose that refers to the coordinate system of a 3D object
model to a pose that refers to the reference coordinate system of a
3D shape model and vice versa.

## Signature

`static void HOperatorSet.TransPoseShapeModel3d(HTuple shapeModel3DID, HTuple poseIn, HTuple transformation, out HTuple poseOut)`

`HPose HShapeModel3D.TransPoseShapeModel3d(HPose poseIn, string transformation)`

`HPose HPose.TransPoseShapeModel3d(HShapeModel3D shapeModel3DID, string transformation)`

## Description

The operator `TransPoseShapeModel3d` transforms the pose
*`poseIn`* into the pose *`poseOut`* by using the
transformation direction specified in *`transformation`*. In
the majority of cases, the operator will be used to transform a
camera pose that is given relative to the source coordinate
system to a camera pose that refers to the target coordinate system.

The pose can be transformed between two coordinate systems. The
first coordinate system is the reference coordinate system of the 3D
shape model (*ref*) that is passed in *`shapeModel3DID`*.
The origin of the reference coordinate system lies at the reference point
of the underlying 3D object model. The orientation of the reference
coordinate system is determined by the reference orientation that
was specified when creating the 3D shape model with
[`CreateShapeModel3d`](create_shape_model_3d.md).

The second coordinate system is the world coordinate system, i.e.,
the coordinate system of the 3D object model (*mcs*) that underlies
the 3D shape model. This coordinate system is implicitly determined by the
coordinates that are stored in the CAD file that was read by using
[`ReadObjectModel3d`](read_object_model_3d.md).

If *`transformation`* is set to *"ref_to_model"*, it is
assumed that *`poseIn`* refers to the reference coordinate
system of the 3D shape model. Thus, *`poseIn`* is
$\mathcal{L}_{\mathrm{spec}} = \sum_i \mathrm{loss}_i$ ![figure](../assets/202217eb39bc7cd8.svg), where
*cs* denotes the coordinate system the input pose transforms into
(e.g., the camera coordinate system). For further information we refer to
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`.
The resulting output pose *`poseOut`* in this case refers to the
coordinate system of the 3D object model, thus
$\mathcal{CS} P_{mcs}$ ![figure](../assets/3890854067607498.svg).

If *`transformation`* is set to *"model_to_ref"*, it is
assumed that *`poseIn`* refers to the coordinate system of the
3D object model, $\mathcal{CS} P_{mcs}$ ![figure](../assets/3890854067607498.svg).
The resulting output pose *`poseOut`* in this
case refers to the reference coordinate system of the 3D shape
model, thus $\mathcal{L}_{\mathrm{spec}} = \sum_i \mathrm{loss}_i$ ![figure](../assets/202217eb39bc7cd8.svg).

The relative pose of the two coordinate systems can be queried by
passing *"reference_pose"* for `genParamName` in the
operator [`GetShapeModel3dParams`](get_shape_model_3d_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`poseIn`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose to be transformed in the source system.

**`transformation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Direction of the transformation.

Default:
"ref_to_model"

List of values:
"model_to_ref", "ref_to_model"

**`poseOut`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Transformed 3D pose in the target system.

## Result

If the parameters are valid, the operator
`TransPoseShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`FindShapeModel3d`

## Alternatives

`HomMat3dTranslate`,
`HomMat3dRotate`

## Module

3D Metrology
