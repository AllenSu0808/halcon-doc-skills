# projective_trans_object_model_3d (Operator)

## Name

`projective_trans_object_model_3d` — Apply an arbitrary projective 3D transformation to 3D object models.

## Signature

`def projective_trans_object_model_3d(object_model_3d: MaybeSequence[HHandle], hom_mat_3d: Sequence[float]) -> Sequence[HHandle]`

`def projective_trans_object_model_3d_s(object_model_3d: MaybeSequence[HHandle], hom_mat_3d: Sequence[float]) -> HHandle`

## Description

`projective_trans_object_model_3d` applies an arbitrary
projective 3D transformation to the points of 3D object models
and returns the handles of the transformed 3D object models. The
projective transformation is described by the homogeneous
transformation matrix given in *`hom_mat_3d`* (see
[`projective_trans_point_3d`](projective_trans_point_3d.md)).

The transformation matrix can be created, e.g., using the operator
[`vector_to_hom_mat3d`](vector_to_hom_mat3d.md).

## Attention

`projective_trans_object_model_3d` transforms
the attributes of type 3D points. Attributes of type shape model for
shape-based 3D matching, of type 3D primitive, and of type normals are
not transformed. Therefore, these attributes do not exist in the
transformed 3D object model. All other attributes are copied
without modification. To transform 3D primitives, the operator
[`rigid_trans_object_model_3d`](rigid_trans_object_model_3d.md) must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handles of the 3D object models.

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`object_model_3dprojective_trans`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handles of the transformed 3D object models.

## Result

If the parameters are valid, the operator
`projective_trans_object_model_3d` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`

## See also

`affine_trans_point_3d`,
`rigid_trans_object_model_3d`,
`affine_trans_object_model_3d`

## Module

3D Metrology
