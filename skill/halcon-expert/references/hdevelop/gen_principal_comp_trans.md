# gen_principal_comp_trans (Operator)

## Name

`gen_principal_comp_trans` — Compute the transformation matrix of the principal component
analysis of multichannel images.

## Signature

`gen_principal_comp_trans(MultichannelImage : : : Trans, TransInv, Mean, Cov, InfoPerComp)`

## Description

`gen_principal_comp_trans` computes the transformation matrix
of a principal components analysis of multichannel images. This is
useful for images obtained, e.g., with the thematic mapper of the
Landsat satellite. Because the spectral bands are highly correlated,
it is desirable to transform them to uncorrelated images. This can
be used to save storage, since the bands containing little
information can be discarded, and with respect to a later
classification step.

The operator `gen_principal_comp_trans` takes one or more
multichannel images *`MultichannelImage`* and computes the
transformation matrix *`Trans`* for the principal components
analysis, as well as its inverse *`TransInv`*. All input
images must have the same number of channels. The principal
components analysis is performed based on the collection of data of
all images. Hence, `gen_principal_comp_trans` facilitates
using the statistics of multiple images.

If n is the number of channels, *`Trans`* and
*`TransInv`* are matrices of dimension n ×
(n+1), which describe an affine transformation of the multichannel
gray values. They can be used to transform a multichannel image
with [`linear_trans_color`](linear_trans_color.md). For information purposes, the mean
gray value of the channels and the n × n
covariance matrix of the channels are returned in *`Mean`* and
*`Cov`*, respectively. The parameter *`InfoPerComp`*
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

**`MultichannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Multichannel input image.

**`Trans`** (output_control)  real-array `→`  (real)

Transformation matrix for the computation of the PCA.

**`TransInv`** (output_control)  real-array `→`  (real)

Transformation matrix for the computation of the
inverse PCA.

**`Mean`** (output_control)  real-array `→`  (real)

Mean gray value of the channels.

**`Cov`** (output_control)  real-array `→`  (real)

Covariance matrix of the channels.

**`InfoPerComp`** (output_control)  real-array `→`  (real)

Information content of the transformed channels.

## Result

The operator `gen_principal_comp_trans` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise an exception is raised.

## Possible Successors

`linear_trans_color`

## Alternatives

`principal_comp`

## Module

Foundation
