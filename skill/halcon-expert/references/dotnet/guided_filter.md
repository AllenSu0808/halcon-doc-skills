# GuidedFilter (Operator)

## Name

`GuidedFilter` — Guided filtering of an image.

## Signature

`static void HOperatorSet.GuidedFilter(HObject image, HObject imageGuide, out HObject imageGuided, HTuple radius, HTuple amplitude)`

`HImage HImage.GuidedFilter(HImage imageGuide, int radius, double amplitude)`

## Description

`GuidedFilter` filters the input *`image`* using the
guidance image *`imageGuide`* and returns the result in
*`imageGuided`*. *`image`* and *`imageGuide`* must be of the
same size and type.

The *`radius`* is the size of the filter mask. Bigger values increase
the area of influence of the filter and less detail is preserved.
The value of *`radius`* does not influence the runtime of the operator.

*`amplitude`* is used to decide what is an edge and what is a
homogeneous area.
Bigger values of *`amplitude`* lead to stronger edges being smoothed.
As a rule of thumb, *`amplitude`* should be lower than the contrast of
the edges that should be preserved.
Please note that the contrast in uint2 or real images may differ
significantly from the default values of *`amplitude`* and adjust the
parameter accordingly.

### Influence of the Guidance Image

If *`image`* and *`imageGuide`* are identical,
`GuidedFilter` behaves like an edge-preserving smoothing with
a filter mask with *`radius`*.
Pixels at edges that have a contrast significantly greater than
*`amplitude`* are preserved, while pixels in homogeneous
areas are smoothed. Hence, `GuidedFilter` is a fast
alternative to [`AnisotropicDiffusion`](anisotropic_diffusion.md) or [`BilateralFilter`](bilateral_filter.md).

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/397b2eeec9f78c82.svg) | ![figure](../assets/397b2eeec9f78c82.svg) | ![figure](../assets/df12b2e473562ca4.svg) |
| ( 1) | ( 2) | ( 3) |

(1) *`image`* and (2) *`imageGuide`* are identical.
That leads to edge-preserving smoothing in (3) *`imageGuided`*.

If *`image`* and *`imageGuide`* are different, *`image`* is
smoothed with a filter mask with *`radius`*, except in areas
where *`imageGuide`* has edges with a contrast significantly greater
than *`amplitude`*.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/397b2eeec9f78c82.svg) | ![figure](../assets/b86327fae48357e9.svg) | ![figure](../assets/75eed518ab999d4f.svg) |
| ( 1) | ( 2) | ( 3) |

(1) *`image`* and (2) *`imageGuide`* are different.
(3) *`imageGuided`*: Only edges are preserved where
*`imageGuide`* has edges.

If *`imageGuide`* is constant, `GuidedFilter` is equivalent to
2 consecutive calls of [`MeanImage`](mean_image.md) with mask size
2**`radius`*+1.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/397b2eeec9f78c82.svg) | ![figure](../assets/70707cd2dc69cb3b.svg) | ![figure](../assets/98bcbaea8c9f91d5.svg) |
| ( 1) | ( 2) | ( 3) |

(2) *`imageGuide`* is constant. This is equivalent to a double
smoothing of (1) *`image`* with [`MeanImage`](mean_image.md).
(3) *`imageGuided`*

### Influence of the smoothing parameters

The following examples show the influence of *`amplitude`* on an
artificial image. In this image, the noise level is
10 gray values, the left edge has a contrast of 50 gray values,
the right edge has a contrast of 100 gray values.
The yellow line shows a gray-value profile of a horizontal cross section.

![figure](../assets/960a88927f58af8c.svg)

Original image with overlaid gray profile, used as *`image`* and
*`imageGuide`*.

![figure](../assets/2d1007fedf878182.svg)

Filter result with *`amplitude`* = 1:
No effect because *`amplitude`* is below noise level.
Therefore noise is treated as edge and preserved.

![figure](../assets/6e4f0928d0b0f3a3.svg)

Filter result with *`amplitude`* = 25:
Noise is smoothed, edges are preserved.

![figure](../assets/b0133d1795c64748.svg)

Filter result with *`amplitude`* = 50:
The weaker edge is smoothed, the stronger edge is preserved.

![figure](../assets/0b63e8832314901f.svg)

Filter result with *`amplitude`* = 100: Both edges are smoothed.

### Rolling Guided Filter

`GuidedFilter` can be applied iteratively. In this case, the result
of one iteration is used as guidance image for the next iteration.
This can be useful, e.g., to remove
small structures from the original image even if they have a high contrast.

In the following example, the rolling guided filter is used to separate
the texture from the original image.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/12e1b48be722bdfa.svg) | ![figure](../assets/bc55b6c26b7d8c1a.svg) | ![figure](../assets/513a44d6e77005b1.svg) |
| ( 1) | ( 2) | ( 3) |

Texture removal with the rolling guided filter:
(1) Original, (2) separated structure, (3) separated texture.

|  |
| --- |
| `* Apply the rolling guided filter` |
| `* (use a constant guide for the first iteration).` |
| [`GenImageProto(Image, ImageStructure, 0)`](gen_image_proto.md) |
| `for I := 1 to 4 by 1` |
| ![figure](../assets/0f8e322aa1b0286d.svg)`GuidedFilter(Image, ImageStructure, ImageStructure, 1.5, 10)` |
| `endfor` |
| `* Separate texture by subtracting large structures from the original.` |
| [`SubImage(Image, ImageStructure, ImageTexture, 1, 128)`](sub_image.md) |
|  |

Since `GuidedFilter` with a constant *`imageGuide`* is similar to
[`MeanImage`](mean_image.md), the first iteration could be replaced by a call of
[`MeanImage`](mean_image.md) (or a similar smoothing filter), which is faster.

### Mathematical Background

The calculation of the filtered gray value $I_{i}^{\prime}$ at the
position $i$ is done according to the following formula:
$$I'_i = \\bar{a}_i G_i + \\bar{b}_i$$ ![figure](../assets/84060906fffc6dc2.svg)
where
$$a_i = \frac{\frac{1}{|\omega_i|}\sum_{k\in\omega_i} G_k I_k - \overline{G_i} I_i}{\sigma_G^2_i + Amplitude^2}$$ ![figure](../assets/7440ddc770a1601e.svg)
and
$$b_i = \overline{I}_i - a_i \overline{G}_i$$ ![figure](../assets/393e11cfe3573386.svg)
where $I_{i}$ and $G_{i}$ are the gray values of
*`image`* and *`imageGuide`* at the pixel position $i$,
$\omega_{i}$ is the neighborhood with radius *`radius`* around
the pixel $i$,
$\bar{a}_{i}$ ![figure](../assets/d5ae048b0a4fbcc6.svg), $\bar{b}_{i}$ ![figure](../assets/9cce44c72bef4fe6.svg),
$I_i$ ![figure](../assets/ab1aa4d167c563db.svg),
and $G_i$ ![figure](../assets/c3d417c97b129dd8.svg) are the mean of all $a$,
$b$, $I$, or $G$ in
$\omega_{i}$, $\sigma G_i$ ![figure](../assets/cbfab44ce79d97c4.svg) is the standard
deviation of all gray values of $G$ in $\omega_{i}$, and
$|\omega_{i}|$ is the number of pixels in $\omega_{i}$.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`imageGuide`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Guidance image.

**`imageGuided`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`radius`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Radius of the filtering operation.

Default:
3

Suggested values:
1, 2, 3, 5, 10

Restriction:
`Radius > 0`

**`amplitude`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Controls the influence of edges on the smoothing.

Default:
20.0

Suggested values:
3.0, 10.0, 20.0, 50.0, 100.0

Restriction:
`Amplitude > 0`

## Example (HDevelop)

```
read_image (Image, 'mreut')
* Edge-preserving smoothing
guided_filter (Image, Image, ImageGuided, 5, 20)
* Rolling filter (5 iterations)
gen_image_proto (Image, ImageGuide, 0)
for I := 1 to 5 by 1
  guided_filter (Image, ImageGuide, ImageGuide, 5, 20)
endfor
```

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`BilateralFilter`,
`AnisotropicDiffusion`,
`MedianImage`

## References

Kaiming He, Jian Sun, Xiaoou Tang: “Guided Image Filtering”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-35, no. 6;
S. 1397-1409; 2013.

## Module

Foundation
