# VectorFieldToHomMat2d (Operator)

## Name

`VectorFieldToHomMat2d` — Approximate an affine map from a displacement vector field.

## Signature

`static void HOperatorSet.VectorFieldToHomMat2d(HObject vectorField, out HTuple homMat2D)`

`HHomMat2D HImage.VectorFieldToHomMat2d()`

`void HHomMat2D.VectorFieldToHomMat2d(HImage vectorField)`

## Description

`VectorFieldToHomMat2d` approximates an affine map from
the displacement vector field *`vectorField`*. The affine map
is returned in *`homMat2D`*.

If the displacement vector field has been computed from the original
image $I_{orig}$ ![figure](../assets/dc2fbca28aa474a2.svg) and the second image
$I_{res}$ ![figure](../assets/b6cb1352fcfe313e.svg), the internally stored transformation
matrix (see [`AffineTransImage`](affine_trans_image.md)) contains a map that
describes how to transform the first image
$I_{orig}$ ![figure](../assets/dc2fbca28aa474a2.svg) to the second image
$I_{res}$ ![figure](../assets/b6cb1352fcfe313e.svg). Note that the *`vectorField`* must be in
relative coordinates as returned by [`OpticalFlowMg`](optical_flow_mg.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`vectorField`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (vector_field)

Input image.

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Possible Predecessors

`OpticalFlowMg`

## Possible Successors

`AffineTransImage`

## Alternatives

`VectorToHomMat2d`

## Module

Foundation
