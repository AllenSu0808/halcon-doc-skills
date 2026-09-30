# BilateralFilter (Operator)

## Name

`BilateralFilter` — bilateral filtering of an image.

## Signature

`static void HOperatorSet.BilateralFilter(HObject image, HObject imageJoint, out HObject imageBilateral, HTuple sigmaSpatial, HTuple sigmaRange, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BilateralFilter(HImage imageJoint, double sigmaSpatial, double sigmaRange, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BilateralFilter(HImage imageJoint, double sigmaSpatial, double sigmaRange, string genParamName, double genParamValue)`

## Description

`BilateralFilter` performs a joint bilateral filtering
on the input *`image`* using the guidance image
*`imageJoint`* and returns the result in *`imageBilateral`*.
*`image`* and *`imageJoint`* must be of the same size and type.

*`sigmaSpatial`* defines the size of the filter mask and
corresponds to the standard deviation of a conventional Gauss filter.
Bigger values increase the area of influence of the filter and less detail
is preserved.

*`sigmaRange`* is used to modify the filter mask depending on the
pixels of *`imageJoint`* around the current pixel.
Only pixels in areas with weak edges that have a contrast lower than
*`sigmaRange`* contribute to the smoothing. Please note that the
contrast in uint2 or real images may differ significantly from the
default values of *`sigmaRange`* and adjust the parameter accordingly.

*`genParamName`* and *`genParamValue`* currently can be used to
control the trade-off between accuracy and speed (see below).

### Influence of the Joint Image

Each pixel of *`image`* is filtered with a filter mask that
depends on *`imageJoint`*. The filter mask combines a Gaussian
closeness function depending on *`sigmaSpatial`*
and a Gaussian similarity function that weights gray value differences
depending on *`sigmaRange`*.

![figure](../assets/1ccd197b3b7825a8.svg)

Examples for local filter masks depending on *`imageJoint`*:
Left: In homogeneous areas the filter mask is nearly Gaussian.
Center: The filter mask follows the line. That means, only the dark pixels
are smoothed and the edge is preserved.
Right: The filter mask resembles the corner. Note that the filter mask
extends across the shadow into areas with similar gray values.

If *`image`* and *`imageJoint`* are identical,
`BilateralFilter` behaves like an edge-preserving smoothing
where *`sigmaSpatial`* defines the size of the filter mask.
Pixels at edges that have a contrast significantly greater than
*`sigmaRange`* are preserved, while pixels in homogeneous areas are
smoothed.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/95234d212522b10e.svg) | ![figure](../assets/95234d212522b10e.svg) | ![figure](../assets/f630eff3392a3cef.svg) |
| ( 1) | ( 2) | ( 3) |

(1) *`image`* and (2) *`imageJoint`* are identical.
That leads to edge-preserving smoothing in (3) *`imageBilateral`*.

If *`image`* and *`imageJoint`* are different, each pixel of
*`image`* is smoothed with a filter mask that is influenced by
*`imageJoint`*. Pixels at positions where *`imageJoint`* has
strong edges with a contrast significantly greater than
*`sigmaRange`* are smoothed less than pixels in homogeneous areas.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/95234d212522b10e.svg) | ![figure](../assets/466509a72ca800ed.svg) | ![figure](../assets/e6433011d2392fb5.svg) |
| ( 1) | ( 2) | ( 3) |

(1) *`image`* and (2) *`imageJoint`* are different.
(3) *`imageBilateral`*: Only edges are preserved where
*`imageJoint`* has edges.

If *`imageJoint`* is constant, `BilateralFilter` is equivalent
to a Gaussian smoothing with *`sigmaSpatial`* (see
[`GaussFilter`](gauss_filter.md) or [`SmoothImage`](smooth_image.md)).

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/95234d212522b10e.svg) | ![figure](../assets/90dbbc2d37d9d458.svg) | ![figure](../assets/848c8f6857641e40.svg) |
| ( 1) | ( 2) | ( 3) |

(1) *`image`*. (2) *`imageJoint`* is constant.
(3) *`imageBilateral`* is equal to *`image`* after Gaussian
smoothing.

### Influence of the smoothing parameters

The following examples show the influence of *`sigmaRange`* on an
artificial image. In this image, the noise level is 10 gray values,
the left edge has a contrast of 50 gray values, the right edge has a
contrast of 100 gray values.
The yellow line shows a gray-value profile of a horizontal cross section.

![figure](../assets/960a88927f58af8c.svg)

Original image with overlaid gray profile, used as *`image`* and
*`imageJoint`*.

![figure](../assets/e1cf25b6ce363568.svg)

Filter result with *`sigmaRange`* = 1:
No effect because *`sigmaRange`* is below noise level.
Therefore noise is treated as edge and preserved.

![figure](../assets/f6d536d31ff2a383.svg)

Filter result with *`sigmaRange`* = 25:
Noise is smoothed, edges are preserved.

![figure](../assets/55031eee7ac9d4ad.svg)

Filter result with *`sigmaRange`* = 50:
The weaker edge is smoothed, the stronger edge is preserved.

![figure](../assets/3b1008bd0c71e34a.svg)

Filter result with *`sigmaRange`* = 100: Both edges are smoothed.

### Generic Parameters

The following values for *`genParamName`* are supported:

- ***"sampling_method"*** —

  Per default, `BilateralFilter`
  uses an approximation of the bilateral filter that only uses a
  subset of sampled points for the calculation of the local filter masks.

  By setting *"sampling_method"*, the used approximation can be
  selected. Possible values are:

  - ***"grid"* (default)** —

    Uses a regular grid for subsampling
    the filter masks.
  - ***"poisson_disk"*** —

    Uses a Poisson disk sampling. This method
    is slower than *"grid"*, but may produce less artifacts.
  - ***"exact"*** —

    Uses all available points. This method is
    slowest, but the most accurate. If *"exact"* is used,
    *"sampling_ratio"* is ignored.
- ***"sampling_ratio"*** —

  Controls how many points are used for
  the subsampling of the local filter masks.

  By setting *"sampling_ratio"* to *1.0*, the exact
  method is used. Using a lower sampling ratio leads to faster filtering,
  but also to slightly less accurate results.

  Suggested values: 0.25, 0.5, 0.75, 1.0

  Default: 0.50

### Rolling Bilateral Filter

`BilateralFilter` can be applied iteratively. In this case, the
result of one iteration is used as guidance image for the next iteration.
This can be useful, e.g., to remove small structures from the original
image even if they have a high contrast.

The following example shows the effect of a rolling filter on an artificial
image. In this image, the noise level is 10 gray values, the contrast
between dark and bright areas is 100 gray values, the left bright
bar is 10 pixels wide, the right bar is 40 pixels wide.
The yellow line shows a gray-value profile of a horizontal cross section.
Used parameters: *`imageJoint`* constant,
*`sigmaSpatial`* = 25, *`sigmaRange`* = 15.

|  |
| --- |
| `* Apply the rolling bilateral filter` |
| `* (use a constant guide for the first iteration).` |
| [`GenImageProto(Image, ImageJoint, 128)`](gen_image_proto.md) |
| `for I := 1 to 6 by 1` |
| ![figure](../assets/0f8e322aa1b0286d.svg)`BilateralFilter(Image, ImageJoint, ImageJoint, 25, 15, [], [])` |
| `endfor` |

|  |  |
| --- | --- |
| ![figure](../assets/8a68dcd0d9af8e95.svg) | ![figure](../assets/6ada26387a1f587d.svg) |
| ( 1) | ( 2) |

(1) Input *`image`* and (2) *`imageJoint`* for first iteration
of the rolling filter.

![figure](../assets/4c449f7cc70b0238.svg)

Result after first iteration: The smaller bar is removed.

![figure](../assets/9cbf33d79485f9dc.svg)

Result after third iteration: The edges of the right bar are
partly restored.

![figure](../assets/4d680ceae106fe70.svg)

Result after sixth iteration: The edges of the right bar are
restored completely.

### Mathematical Background

The calculation of the filtered gray values $I_{i}^{\prime}$ is done on
the basis of the following formula:
$$I'_i = \frac{1}{K_i} \sum_{k \in \omega_i} c_{ik} \cdot s_{ik} \cdot I_k$$ ![figure](../assets/68a22aeac59d4ad7.svg)
where $c_{ik}$ is a closeness function
$$c_{ik} = \\exp\left(-\\frac{\\lVert i - k \\rVert^2}{2 \\\cdot \\Sigma_{Spatial}^2}\right)$$ ![figure](../assets/3d0b40edc782a51d.svg)
$s_{ik}$ is a similarity function
$$s_{ik} = \exp\left( -\frac{(J_i - J_k)^2}{2 \cdot S'\!\text{ig}maRang e^2} \right)$$ ![figure](../assets/03474e9bb2db2ad4.svg)
$K_{i}$ is a normalization factor
$$K_i = \sum_{k \in \omega_i} c_{ik} \cdot S_{ik}$$ ![figure](../assets/3655fe80c28df607.svg)
where $I_{i}^{\prime}$, $I_{i}$ and $J_{i}$ are the
gray values of *`image`* and *`imageJoint`* at the pixel position
$i$, and $\omega_{i}$ is the neighborhood around the
pixel $i$.

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

Image to be filtered.

**`imageJoint`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Joint image.

**`imageBilateral`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Filtered output image.

**`sigmaSpatial`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Size of the Gaussian of the closeness function.

Default:
3.0

Suggested values:
1.0, 2.0, 3.0, 10.0

Restriction:
`SigmaSpatial > 0.6`

**`sigmaRange`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Size of the Gaussian of the similarity function.

Default:
20.0

Suggested values:
3.0, 10.0, 20.0, 50.0, 100.0

Restriction:
`SigmaRange > 0.0001`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

List of values:
"sampling_method", "sampling_ratio"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Generic parameter value.

Default:
[]

Suggested values:
"grid", "poisson_disk", "exact", 0.5, 0.25, 0.75, 1.0

## Example (HDevelop)

```
read_image (Image, 'mreut')
* Edge-preserving smoothing
bilateral_filter (Image, Image, ImageBilateral, 5, 20, [], [])
* Rolling filter (5 iterations)
gen_image_proto (Image, ImageJoint, 0)
for I := 1 to 5 by 1
  bilateral_filter (Image, ImageJoint, ImageJoint, 5, 20, [], [])
endfor
```

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`VarThreshold`,
`Regiongrowing`

## Alternatives

`GuidedFilter`,
`AnisotropicDiffusion`,
`MedianImage`

## References

C. Tomasi, R. Manduchi: ”Bilateral filtering for gray and color images”;
Sixth International Conference in Computer Vision;
S. 839-846; January 1998.
  
F. Banterle, M. Corsini, P. Cignoni, R. Scopigno: ”A Low-Memory,
Straightforward and Fast Bilateral Filter Through Subsampling in
Spatial Domain”;
Computer Graphics Forum, no. 1, vol 31;
S. 19-23; February 2012.
  
G. Petschnigg, R. Szeliski, M. Agrawala, M. Cohen, H. Hoppe, K. Toyama:
”Digital Photography with Flash and No-flash Image Pairs”;
ACM Trans., no. 3, vol. 23;
S. 9; August 2004.
  
R. Bridson: ”Fast Poisson Disk Sampling in Arbitrary Dimensions”;
ACM SIGGRAPH 2007 Sketches, no. 22;
2007.

## Module

Foundation
