# vector_field_to_hom_mat2d (Operator)

## Name

`vector_field_to_hom_mat2d` — Approximate an affine map from a displacement vector field.

## Signature

`def vector_field_to_hom_mat2d(vector_field: HObject) -> Sequence[float]`

## Description

`vector_field_to_hom_mat2d` approximates an affine map from
the displacement vector field *`vector_field`*. The affine map
is returned in *`hom_mat_2d`*.

If the displacement vector field has been computed from the original
image $I_{orig}$ ![figure](../assets/dc2fbca28aa474a2.svg) and the second image
$I_{res}$ ![figure](../assets/b6cb1352fcfe313e.svg), the internally stored transformation
matrix (see [`affine_trans_image`](affine_trans_image.md)) contains a map that
describes how to transform the first image
$I_{orig}$ ![figure](../assets/dc2fbca28aa474a2.svg) to the second image
$I_{res}$ ![figure](../assets/b6cb1352fcfe313e.svg). Note that the *`vector_field`* must be in
relative coordinates as returned by [`optical_flow_mg`](optical_flow_mg.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`vector_field`** (input_object)  singlechannelimage `→` HObject (vector_field)

Input image.

**`hom_mat_2d`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Possible Predecessors

`optical_flow_mg`

## Possible Successors

`affine_trans_image`

## Alternatives

`vector_to_hom_mat2d`

## Module

Foundation
