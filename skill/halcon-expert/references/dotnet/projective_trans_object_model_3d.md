# ProjectiveTransObjectModel3d (Operator)

## Name

`ProjectiveTransObjectModel3d` — Apply an arbitrary projective 3D transformation to 3D object models.

## Signature

`static void HOperatorSet.ProjectiveTransObjectModel3d(HTuple objectModel3D, HTuple homMat3D, out HTuple objectModel3DProjectiveTrans)`

`static HObjectModel3D[] HObjectModel3D.ProjectiveTransObjectModel3d(HObjectModel3D[] objectModel3D, HHomMat3D homMat3D)`

`HObjectModel3D HObjectModel3D.ProjectiveTransObjectModel3d(HHomMat3D homMat3D)`

## Description

`ProjectiveTransObjectModel3d` applies an arbitrary
projective 3D transformation to the points of 3D object models
and returns the handles of the transformed 3D object models. The
projective transformation is described by the homogeneous
transformation matrix given in *`homMat3D`* (see
[`ProjectiveTransPoint3d`](projective_trans_point_3d.md)).

The transformation matrix can be created, e.g., using the operator
[`VectorToHomMat3d`](vector_to_hom_mat3d.md).

## Attention

`ProjectiveTransObjectModel3d` transforms
the attributes of type 3D points. Attributes of type shape model for
shape-based 3D matching, of type 3D primitive, and of type normals are
not transformed. Therefore, these attributes do not exist in the
transformed 3D object model. All other attributes are copied
without modification. To transform 3D primitives, the operator
[`RigidTransObjectModel3d`](rigid_trans_object_model_3d.md) must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the 3D object models.

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`objectModel3DProjectiveTrans`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the transformed 3D object models.

## Result

If the parameters are valid, the operator
`ProjectiveTransObjectModel3d` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`

## See also

`AffineTransPoint3d`,
`RigidTransObjectModel3d`,
`AffineTransObjectModel3d`

## Module

3D Metrology
