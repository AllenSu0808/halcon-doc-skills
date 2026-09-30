# trans_pose_shape_model_3d (Operator)

## Name

`trans_pose_shape_model_3d` — Transform a pose that refers to the coordinate system of a 3D object
model to a pose that refers to the reference coordinate system of a
3D shape model and vice versa.

## Signature

`trans_pose_shape_model_3d( : : ShapeModel3DID, PoseIn, Transformation : PoseOut)`

## Description

The operator `trans_pose_shape_model_3d` transforms the pose
*`PoseIn`* into the pose *`PoseOut`* by using the
transformation direction specified in *`Transformation`*. In
the majority of cases, the operator will be used to transform a
camera pose that is given relative to the source coordinate
system to a camera pose that refers to the target coordinate system.

The pose can be transformed between two coordinate systems. The
first coordinate system is the reference coordinate system of the 3D
shape model (*ref*) that is passed in *`ShapeModel3DID`*.
The origin of the reference coordinate system lies at the reference point
of the underlying 3D object model. The orientation of the reference
coordinate system is determined by the reference orientation that
was specified when creating the 3D shape model with
[`create_shape_model_3d`](create_shape_model_3d.md).

The second coordinate system is the world coordinate system, i.e.,
the coordinate system of the 3D object model (*mcs*) that underlies
the 3D shape model. This coordinate system is implicitly determined by the
coordinates that are stored in the CAD file that was read by using
[`read_object_model_3d`](read_object_model_3d.md).

If *`Transformation`* is set to *'ref_to_model'*, it is
assumed that *`PoseIn`* refers to the reference coordinate
system of the 3D shape model. Thus, *`PoseIn`* is
$\mathcal{L}_{\mathrm{spec}} = \sum_i \mathrm{loss}_i$ ![figure](../assets/202217eb39bc7cd8.svg), where
*cs* denotes the coordinate system the input pose transforms into
(e.g., the camera coordinate system). For further information we refer to
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`.
The resulting output pose *`PoseOut`* in this case refers to the
coordinate system of the 3D object model, thus
$\mathcal{CS} P_{mcs}$ ![figure](../assets/3890854067607498.svg).

If *`Transformation`* is set to *'model_to_ref'*, it is
assumed that *`PoseIn`* refers to the coordinate system of the
3D object model, $\mathcal{CS} P_{mcs}$ ![figure](../assets/3890854067607498.svg).
The resulting output pose *`PoseOut`* in this
case refers to the reference coordinate system of the 3D shape
model, thus $\mathcal{L}_{\mathrm{spec}} = \sum_i \mathrm{loss}_i$ ![figure](../assets/202217eb39bc7cd8.svg).

The relative pose of the two coordinate systems can be queried by
passing *'reference_pose'* for `GenParamName` in the
operator [`get_shape_model_3d_params`](get_shape_model_3d_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ShapeModel3DID`** (input_control)  shape_model_3d `→`  (handle)

Handle of the 3D shape model.

**`PoseIn`** (input_control)  pose `→`  (real / integer)

Pose to be transformed in the source system.

**`Transformation`** (input_control)  string `→`  (string)

Direction of the transformation.

Default:
'ref_to_model'

List of values:
'model_to_ref', 'ref_to_model'

**`PoseOut`** (output_control)  pose `→`  (real / integer)

Transformed 3D pose in the target system.

## Result

If the parameters are valid, the operator
`trans_pose_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`find_shape_model_3d`

## Alternatives

`hom_mat3d_translate`,
`hom_mat3d_rotate`

## Module

3D Metrology
