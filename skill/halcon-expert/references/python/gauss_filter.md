# gauss_filter (Operator)

## Name

`gauss_filter` — Smooth using discrete Gauss functions.

## Signature

`def gauss_filter(image: HObject, size: int) -> HObject`

## Description

The operator `gauss_filter` smoothes images using the discrete
Gaussian, a discrete approximation of the Gaussian function,
$$G_{\sigma}(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{x^{2}}{2\sigma^{2}}\right)$$ ![figure](../assets/fc951b4b1dfa5f4c.svg)

The smoothing effect increases with increasing filter
size. The following filter sizes (*`size`*) are supported
(the sigma value of the Gauss function is indicated in brackets):

- *3* (0.600)
- *5* (1.075)
- *7* (1.550)
- *9* (2.025)
- *11* (2.550)

For border treatment the gray values of the images are reflected at
the image borders. Notice that, contrary to the operator
[`gauss_image`](gauss_image.md), the relationship between the filter mask size
and its respective value for the sigma parameter is linear.

The operator [`binomial_filter`](binomial_filter.md) can be used as an alternative
to `gauss_filter`. [`binomial_filter`](binomial_filter.md) is significantly
faster than `gauss_filter`. It should be noted that the mask
size in [`binomial_filter`](binomial_filter.md) does not lead to the same amount of
smoothing as the mask size in `gauss_filter`. Corresponding
mask sizes can be determined based on the respective values of the
Gaussian smoothing parameter sigma.

`gauss_filter` can be executed on OpenCL devices for all supported
image types. However, the OpenCL implementation can produce slightly
different results from the scalar implementation.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

In order to be able to process `gauss_filter` on an OpenCL device,
*`image`* must be at least 64 pixels in both width and height.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Image to be smoothed.

**`image_gauss`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Filtered image.

**`size`** (input_control)  integer `→` int

Required filter size.

Default:
5

List of values:
3, 5, 7, 9, 11

## Complexity

For each pixel: O(Size * 2).

## Result

If the parameter values are correct the operator `gauss_filter`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`,
`grab_image`

## Possible Successors

`regiongrowing`,
`threshold`,
`sub_image`,
`dyn_threshold`,
`auto_threshold`

## Alternatives

`binomial_filter`,
`smooth_image`,
`derivate_gauss`,
`isotropic_diffusion`

## See also

`mean_image`,
`anisotropic_diffusion`,
`sigma_image`,
`gen_lowpass`

## Module

Foundation
