# AffineTransObjectModel3d (Operator)

## Name

`AffineTransObjectModel3d` — Apply an arbitrary affine 3D transformation to 3D object models.

## Signature

`static void HOperatorSet.AffineTransObjectModel3d(HTuple objectModel3D, HTuple homMat3D, out HTuple objectModel3DAffineTrans)`

`static HObjectModel3D[] HObjectModel3D.AffineTransObjectModel3d(HObjectModel3D[] objectModel3D, HHomMat3D[] homMat3D)`

`HObjectModel3D HObjectModel3D.AffineTransObjectModel3d(HHomMat3D homMat3D)`

## Description

`AffineTransObjectModel3d` applies arbitrary affine 3D
transformations, i.e., scaling, rotation, and translation, to 3D
object models and returns the handles of the transformed 3D object
models. The affine transformations are described by the homogeneous
transformation matrices given in *`homMat3D`*.

The transformation matrices can be created using the operators
[`HomMat3dIdentity`](hom_mat3d_identity.md), [`HomMat3dScale`](hom_mat3d_scale.md),
[`HomMat3dRotate`](hom_mat3d_rotate.md), [`HomMat3dTranslate`](hom_mat3d_translate.md), etc., or it can be
the result of [`PoseToHomMat3d`](pose_to_hom_mat3d.md) (see
[`AffineTransPoint3d`](affine_trans_point_3d.md)).

In general, the operator `AffineTransObjectModel3d` is not
necessary in the context of shape based 3D matching. Instead, if a rotation
of the 3D object model into a reference orientation should be performed,
appropriate values for the parameters `refRotX`,
`refRotY`, `refRotZ`, and `orderOfRotation`
should be passed to the operator [`CreateShapeModel3d`](create_shape_model_3d.md).

`AffineTransObjectModel3d` transforms one or more 3D object models
with the same transformation matrix if only one transformation matrix
is passed in *`homMat3D`* (N:1).
If a single 3D object model is passed in *`objectModel3D`*, it is
transformed with all passed transformation matrices (1:N).
If the number of transformation matrices corresponds to the number of 3D
object models, every 3D object model is transformed individually with
the respective transformation matrix (N:N).
In those cases, N can be zero, i.e., no matrix
or no 3D object model can be passed to the operator. In this case, an empty
tuple is returned in *`objectModel3DAffineTrans`*. This can be used to,
for example, transform the results of other operators without checking first
if at least one matrix was returned.

## Attention

`AffineTransObjectModel3d` transforms the attributes of type
3D points, 3D point normals, and the prepared shape model for shape-based
3D matching. Primitives and precomputed data structures for 3D distance
computation are not copied. All other attributes are copied without
modification. To transform 3D primitives, the operator
[`RigidTransObjectModel3d`](rigid_trans_object_model_3d.md) must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the 3D object models.

**`homMat3D`** (input_control)  hom_mat3d(-array) `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Transformation matrices.

**`objectModel3DAffineTrans`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the transformed 3D object models.

## Result

`AffineTransObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`

## See also

`AffineTransPoint3d`,
`RigidTransObjectModel3d`,
`ProjectiveTransObjectModel3d`

## Module

3D Metrology
