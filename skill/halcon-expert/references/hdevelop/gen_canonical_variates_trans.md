# gen_canonical_variates_trans (Operator)

## Name

`gen_canonical_variates_trans` — Compute the transformation matrix of a multichannel image using the
canonical variates analysis.

## Signature

`gen_canonical_variates_trans( : : TrainingSamples, NumComponents : TransMat)`

## Description

`gen_canonical_variates_trans` computes the affine transformation
matrix of a multichannel image into an image with a different number
of channels using class-specific canonical variates analysis.
This can be used to reduce the number of channels of an image while
at the same time keeping the classes separable as good as possible.

One or more multichannel images are passed in *`TrainingSamples`*.
If multiple images are passed, all must have the same number of channels.
An array of regions is passed in *`TrainingSamples`*, describing which
pixel of the input image *`TrainingSamples`* belongs to which
class.
The number of objects in *`TrainingSamples`* must be equal to the number of
images times the number of classes. If a class contains no pixels of a
particulate image, the corresponding entry in *`TrainingSamples`* must be
set to the empty region.

The number of channels in the transformed image are passed in
*`NumComponents`*.
Note that *`NumComponents`* can be at most one less than the
number of classes.

The affine transformation is returned in *`TransMat`*.
This transformation can be used with, for example, [`linear_trans_color`](linear_trans_color.md)
to transform an image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TrainingSamples`** (input_control)  dict-array `→`  (handle)

Training samples.

**`NumComponents`** (input_control)  integer `→`  (integer)

Number of target components.

Default:
3

**`TransMat`** (output_control)  real-array `→`  (real)

Transformation matrix for transforming the input image.

## Result

The operator `gen_canonical_variates_trans` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise an exception is raised.

## Possible Successors

`linear_trans_color`

## Alternatives

`principal_comp`,
`gen_principal_comp_trans`

## Module

Foundation
