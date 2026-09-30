# rigid_trans_object_model_3d (Operator)

## Name

`rigid_trans_object_model_3d` — Apply a rigid 3D transformation to 3D object models.

## Signature

`rigid_trans_object_model_3d( : : ObjectModel3D, Pose : ObjectModel3DRigidTrans)`

## Description

`rigid_trans_object_model_3d` applies rigid 3D transformations, i.e.,
rotations and translations, to 3D
object models and returns the handles of the transformed 3D object
models. The transformations are described by the poses given in
*`Pose`*, which are in the form
$\mathit{cst} P_{mcsi}$ ![figure](../assets/ae31094bdd7d394c.svg), where
*mcsi* denotes the coordinate system of the input object model and
*cst* the coordinate system of the transformed model, e.g., the
coordinate system of the scene (see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`).
A pose can be created using the operators
[`create_pose`](create_pose.md), [`pose_invert`](pose_invert.md), etc., or it can be
the result of [`get_object_model_3d_params`](get_object_model_3d_params.md).

`rigid_trans_object_model_3d` transforms one or more 3D object
models with the same pose if only one transformation matrix
is passed in *`Pose`* (N:1).
If a single 3D object model is passed in *`ObjectModel3D`*, it is
transformed with all passed poses (1:N).
If the number of poses corresponds to the number of 3D
object models, every 3D object model is transformed individually with
the respective pose (N:N). In those cases, N can be zero, i.e., no pose
or no 3D object model can be passed to the operator. In this case, an empty
tuple is returned in *`ObjectModel3DRigidTrans`*. This can be used to,
for example, transform the results of [`find_surface_model`](find_surface_model.md) without
checking first if at least one match was returned.

## Attention

`rigid_trans_object_model_3d` transforms the attributes of type
3D points, 3D point normals, and the prepared shape model for shape-based
3D matching, as well as 3D primitives. Precomputed data structures for 3D
distance computation are not copied. All other attributes are copied
without modification.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handles of the 3D object models.

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

Poses.

**`ObjectModel3DRigidTrans`** (output_control)  object_model_3d(-array) `→`  (handle)

Handles of the transformed 3D object models.

## Result

`rigid_trans_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`fit_primitives_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`,
`get_object_model_3d_params`

## See also

`affine_trans_point_3d`,
`affine_trans_object_model_3d`

## Module

3D Metrology
