# linear_trans_color (Operator)

## Name

`linear_trans_color` — Compute an affine transformation of the color values of a
multichannel image.

## Signature

`def linear_trans_color(image: HObject, trans_mat: Sequence[float]) -> HObject`

## Description

`linear_trans_color` performs an affine transformation of the
color values of the multichannel image *`image`* and returns
the result in *`image_trans`*. The affine transformation of the
color values is described by the transformation matrix
*`trans_mat`*. If n is the number of channels in
*`image`* and m is the number of channels in
*`image_trans`*, *`trans_mat`* is a homogeneous m × (n+1) matrix that is stored row by row. Homogeneous
means that the left m × n submatrix of
*`trans_mat`* describes a linear transformation of the color
values, while the last column of *`trans_mat`* describes a
constant offset of the color values. The transformation matrix is
typically computed with [`gen_principal_comp_trans`](gen_principal_comp_trans.md). In
particular, it is possible to project an image onto the first m
principal components by selecting the first m ×
(n+1) values of the transformation returned by
[`gen_principal_comp_trans`](gen_principal_comp_trans.md). The transformation can, however,
also be specified directly. For example, a transformation from RGB
to YIQ, which is described by the following transformation
$$\begin{pmatrix}Y\\I\\Q{}}$$ ![figure](../assets/076c6f680a12a13d.svg)
can be achieved by setting *`trans_mat`* to
[0.299,0.587,0.114,0.0,0.599,-0.276,-0.324,127.5,0.214,-0.522,0.309,127.5]
Here, it should be noted that the above transformation is
unnormalized, i.e., the resulting color values can lie outside the
range [0,255]. The transformation *"yiq"* in
[`trans_from_rgb`](trans_from_rgb.md) additionally scales the rows of the matrix
(except for the constant offset) appropriately.

To avoid a loss of information, `linear_trans_color` returns
an image of type real. If a different image type is desired, the
image can be transformed with [`convert_image_type`](convert_image_type.md).

## Attention

`linear_trans_color` can be executed on OpenCL devices if the image
*`image`* consists of nine channels or less and is transformed to
an image of three channels or less. Since the calculations are done in
single precision floating point, the results may differ from those
calculated by the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  multichannel-image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Multichannel input image.

**`image_trans`** (output_object)  multichannel-image(-array) `→` HObject (real)

Multichannel output image.

**`trans_mat`** (input_control)  real-array `→` Sequence[float]

Transformation matrix for the color values.

## Result

The operator `linear_trans_color` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct. Otherwise an exception is raised.

## Possible Predecessors

`gen_principal_comp_trans`

## Possible Successors

`convert_image_type`

## Alternatives

`principal_comp`,
`trans_from_rgb`,
`trans_to_rgb`

## Module

Foundation
