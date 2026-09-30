# laplace_of_gauss (Operator)

## Name

`laplace_of_gauss` — LoG-Operator (Laplace of Gaussian).

## Signature

`def laplace_of_gauss(image: HObject, sigma: Union[float, int]) -> HObject`

## Description

`laplace_of_gauss` calculates the Laplace-of-Gaussian
operator, i.e., the Laplace operator on a Gaussian smoothed image,
for arbitrary smoothing parameters *`sigma`*. The Laplace
operator is given by:
$$\Delta g(x, y) = \frac{\partial^{2} g(x, y)}{\partial x^{2}} + \frac{\partial^{2} g(x, y)}{\partial y^{2}}$$ ![figure](../assets/0f66c19d9f880432.svg)
The derivatives in `laplace_of_gauss` are calculated by
appropriate derivatives of the Gaussian, resulting in the following
formula for the convolution mask:
$$\Delta G_{\sigma}(x,y) = \frac{1}{2\pi\sigma^{4}}\left( \frac{x^{2}+y^{2}}{2\sigma^{2}} - 1 \right)\left[ \exp\left(-\frac{x^{2}+y^{2}}{2\sigma^{2}}\right)\right]$$ ![figure](../assets/952c6c73fb8a4d67.svg)

## Attention

Note that filter operators may return may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`image_laplace`** (output_object)  (multichannel-)image(-array) `→` HObject (int2)

Laplace filtered image.

**`sigma`** (input_control)  number `→` Union[float, int]

Smoothing parameter of the Gaussian.

Default:
2.0

Suggested values:
0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0

Value range:
`0.01
≤
sigma
≤
25.0`

Minimum increment:
0.01

Recommended increment:
0.1

## Example (C)

```
read_image(&Image,"mreut");
laplace_of_gauss(Image,&Laplace,2.0);
zero_crossing(Laplace,&ZeroCrossings);
```

## Possible Successors

`zero_crossing`,
`dual_threshold`

## Alternatives

`laplace`,
`diff_of_gauss`,
`derivate_gauss`

## See also

`derivate_gauss`

## Module

Foundation
