# principal_comp (Operator)

## Name

`principal_comp` — Compute the principal components of multichannel images.

## Signature

`def principal_comp(multichannel_image: HObject) -> Tuple[HObject, Sequence[float]]`

## Description

`principal_comp` does a principal components analysis of
multichannel images. This is useful for images obtained, e.g.,
with the thematic mapper of the Landsat satellite. Because the
spectral bands are highly correlated, it is desirable to transform
them to uncorrelated images. This can be used to save storage,
since the bands containing little information can be discarded, and
with respect to a later classification step.

The operator `principal_comp` takes a (multichannel) image
*`multichannel_image`*
and transforms it to the output image *`pcaimage`*,
which contains the same number of channels, using the principal
components analysis. The parameter *`info_per_comp`* contains
the relative information content of each output channel.

## Attention

`principal_comp` can be executed on OpenCL devices if image consists
of eight channels or less. Since the calculations are done in single
precision floating point, the results may differ from those calculated by
the CPU.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multichannel_image`** (input_object)  (multichannel-)image `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Multichannel input image.

**`pcaimage`** (output_object)  multichannel-image `→` HObject (real)

Multichannel output image.

**`info_per_comp`** (output_control)  real-array `→` Sequence[float]

Information content of each output channel.

## Result

The operator `principal_comp` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct. Otherwise an exception is raised.

## Alternatives

`gen_principal_comp_trans`

## See also

`linear_trans_color`

## Module

Foundation
