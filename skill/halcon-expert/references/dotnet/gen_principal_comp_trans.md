# GenPrincipalCompTrans (Operator)

## Name

`GenPrincipalCompTrans` — Compute the transformation matrix of the principal component
analysis of multichannel images.

## Signature

`static void HOperatorSet.GenPrincipalCompTrans(HObject multichannelImage, out HTuple trans, out HTuple transInv, out HTuple mean, out HTuple cov, out HTuple infoPerComp)`

`HTuple HImage.GenPrincipalCompTrans(out HTuple transInv, out HTuple mean, out HTuple cov, out HTuple infoPerComp)`

## Description

`GenPrincipalCompTrans` computes the transformation matrix
of a principal components analysis of multichannel images. This is
useful for images obtained, e.g., with the thematic mapper of the
Landsat satellite. Because the spectral bands are highly correlated,
it is desirable to transform them to uncorrelated images. This can
be used to save storage, since the bands containing little
information can be discarded, and with respect to a later
classification step.

The operator `GenPrincipalCompTrans` takes one or more
multichannel images *`multichannelImage`* and computes the
transformation matrix *`trans`* for the principal components
analysis, as well as its inverse *`transInv`*. All input
images must have the same number of channels. The principal
components analysis is performed based on the collection of data of
all images. Hence, `GenPrincipalCompTrans` facilitates
using the statistics of multiple images.

If n is the number of channels, *`trans`* and
*`transInv`* are matrices of dimension n ×
(n+1), which describe an affine transformation of the multichannel
gray values. They can be used to transform a multichannel image
with [`LinearTransColor`](linear_trans_color.md). For information purposes, the mean
gray value of the channels and the n × n
covariance matrix of the channels are returned in *`mean`* and
*`cov`*, respectively. The parameter *`infoPerComp`*
contains the relative information content of each output channel.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multichannelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Multichannel input image.

**`trans`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Transformation matrix for the computation of the PCA.

**`transInv`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Transformation matrix for the computation of the
inverse PCA.

**`mean`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Mean gray value of the channels.

**`cov`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Covariance matrix of the channels.

**`infoPerComp`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Information content of the transformed channels.

## Result

The operator `GenPrincipalCompTrans` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise an exception is raised.

## Possible Successors

`LinearTransColor`

## Alternatives

`PrincipalComp`

## Module

Foundation
