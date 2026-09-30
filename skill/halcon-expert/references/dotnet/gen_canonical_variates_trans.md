# GenCanonicalVariatesTrans (Operator)

## Name

`GenCanonicalVariatesTrans` — Compute the transformation matrix of a multichannel image using the
canonical variates analysis.

## Signature

`static void HOperatorSet.GenCanonicalVariatesTrans(HTuple trainingSamples, HTuple numComponents, out HTuple transMat)`

`static HTuple HImage.GenCanonicalVariatesTrans(HDict[] trainingSamples, int numComponents)`

## Description

`GenCanonicalVariatesTrans` computes the affine transformation
matrix of a multichannel image into an image with a different number
of channels using class-specific canonical variates analysis.
This can be used to reduce the number of channels of an image while
at the same time keeping the classes separable as good as possible.

One or more multichannel images are passed in *`trainingSamples`*.
If multiple images are passed, all must have the same number of channels.
An array of regions is passed in *`trainingSamples`*, describing which
pixel of the input image *`trainingSamples`* belongs to which
class.
The number of objects in *`trainingSamples`* must be equal to the number of
images times the number of classes. If a class contains no pixels of a
particulate image, the corresponding entry in *`trainingSamples`* must be
set to the empty region.

The number of channels in the transformed image are passed in
*`numComponents`*.
Note that *`numComponents`* can be at most one less than the
number of classes.

The affine transformation is returned in *`transMat`*.
This transformation can be used with, for example, [`LinearTransColor`](linear_trans_color.md)
to transform an image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`trainingSamples`** (input_control)  dict-array `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Training samples.

**`numComponents`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of target components.

Default:
3

**`transMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Transformation matrix for transforming the input image.

## Result

The operator `GenCanonicalVariatesTrans` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise an exception is raised.

## Possible Successors

`LinearTransColor`

## Alternatives

`PrincipalComp`,
`GenPrincipalCompTrans`

## Module

Foundation
