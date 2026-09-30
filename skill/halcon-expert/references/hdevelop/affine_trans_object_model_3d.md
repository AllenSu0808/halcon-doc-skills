# affine_trans_object_model_3d (Operator)

## Name

`affine_trans_object_model_3d` — Apply an arbitrary affine 3D transformation to 3D object models.

## Signature

`affine_trans_object_model_3d( : : ObjectModel3D, HomMat3D : ObjectModel3DAffineTrans)`

## Description

`affine_trans_object_model_3d` applies arbitrary affine 3D
transformations, i.e., scaling, rotation, and translation, to 3D
object models and returns the handles of the transformed 3D object
models. The affine transformations are described by the homogeneous
transformation matrices given in *`HomMat3D`*.

The transformation matrices can be created using the operators
[`hom_mat3d_identity`](hom_mat3d_identity.md), [`hom_mat3d_scale`](hom_mat3d_scale.md),
[`hom_mat3d_rotate`](hom_mat3d_rotate.md), [`hom_mat3d_translate`](hom_mat3d_translate.md), etc., or it can be
the result of [`pose_to_hom_mat3d`](pose_to_hom_mat3d.md) (see
[`affine_trans_point_3d`](affine_trans_point_3d.md)).

In general, the operator `affine_trans_object_model_3d` is not
necessary in the context of shape based 3D matching. Instead, if a rotation
of the 3D object model into a reference orientation should be performed,
appropriate values for the parameters `RefRotX`,
`RefRotY`, `RefRotZ`, and `OrderOfRotation`
should be passed to the operator [`create_shape_model_3d`](create_shape_model_3d.md).

`affine_trans_object_model_3d` transforms one or more 3D object models
with the same transformation matrix if only one transformation matrix
is passed in *`HomMat3D`* (N:1).
If a single 3D object model is passed in *`ObjectModel3D`*, it is
transformed with all passed transformation matrices (1:N).
If the number of transformation matrices corresponds to the number of 3D
object models, every 3D object model is transformed individually with
the respective transformation matrix (N:N).
In those cases, N can be zero, i.e., no matrix
or no 3D object model can be passed to the operator. In this case, an empty
tuple is returned in *`ObjectModel3DAffineTrans`*. This can be used to,
for example, transform the results of other operators without checking first
if at least one matrix was returned.

## Attention

`affine_trans_object_model_3d` transforms the attributes of type
3D points, 3D point normals, and the prepared shape model for shape-based
3D matching. Primitives and precomputed data structures for 3D distance
computation are not copied. All other attributes are copied without
modification. To transform 3D primitives, the operator
[`rigid_trans_object_model_3d`](rigid_trans_object_model_3d.md) must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handles of the 3D object models.

**`HomMat3D`** (input_control)  hom_mat3d(-array) `→`  (real)

Transformation matrices.

**`ObjectModel3DAffineTrans`** (output_control)  object_model_3d(-array) `→`  (handle)

Handles of the transformed 3D object models.

## Result

`affine_trans_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`

## See also

`affine_trans_point_3d`,
`rigid_trans_object_model_3d`,
`projective_trans_object_model_3d`

## Module

3D Metrology
