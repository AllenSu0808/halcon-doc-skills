# equ_histo_image_rect (Operator)

## Name

`equ_histo_image_rect` — Histogram linearization within a rectangluar mask.

## Signature

`def equ_histo_image_rect(image: HObject, mode: str, mask_width: int, mask_height: int, max_contrast: Union[float, int]) -> HObject`

## Description

The operator `equ_histo_image_rect` enhances the contrast.
Similar to [`equ_histo_image`](equ_histo_image.md), it applies a transformation to linearize
the cumulative histogram. However, instead of using the histogram of the
whole image, only the local neighborhood of each pixel is considered to
compute the transformation. The size of this rectangular neighborhood region
can be set by *`mask_width`* and *`mask_height`*.

The local contrast maximization improves the visibility of low-contrast
structures, but also amplifies noise. The parameter *`max_contrast`* can
be used to limit the maximum contrast in a local neighborhood, which
effectively reduces the amplification of noise. Therefore, the method is also
known as Contrast-Limited Adaptive Histogram Equalization (CLAHE).

The parameter *`mode`* determines the processing mode.
In the *"accurate"* mode, the transformation is computed for each
pixel as described above.
In the *"fast"* mode, the transformation is computed only for a subset
of all pixels and interpolated between those points.
Due to the interpolation, the results of both modes can differ significantly.

## Attention

The operator `equ_histo_image_rect` primarily serves for
optical processing of images for a human viewer. For example, the
contrast spreading can lead to a detection of fictitious edges.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte)

Image to be enhanced.

**`image_equ_histo`** (output_object)  (multichannel-)image(-array) `→` HObject (byte)

Image with linearized gray values.

**`mode`** (input_control)  string `→` str

Processing mode.

Default:
"accurate"

Suggested values:
"accurate", "fast"

**`mask_width`** (input_control)  extent.x `→` int

Width of the filter mask.

Default:
51

Suggested values:
31, 51, 101, 151

Value range:
`1
≤
mask_width`

Minimum increment:
2

Restriction:
`MaskWidth <= width(Image)`

**`mask_height`** (input_control)  extent.y `→` int

Height of the filter mask.

Default:
51

Suggested values:
31, 51, 101, 151

Value range:
`1
≤
mask_height`

Minimum increment:
2

Restriction:
`MaskHeight <= height(Image)`

**`max_contrast`** (input_control)  real `→` Union[float, int]

Maximum contrast.

Default:
0.01

Suggested values:
0, 0.01, 0.02, 0.05, 0.1, 0.5, 1

Value range:
`0
≤
max_contrast
≤
1`

## Complexity

In *`mode`*=*"accurate"*, `equ_histo_image_rect` uses an
algorithm with constant complexity per pixel, i.e., the runtime only depends
on the size of the input image and not on the mask size.

In *`mode`*=*"fast"*, the number of histograms to be computed
depends on the mask size. Hence, the runtime increases with smaller mask
sizes and decreases with larger mask sizes.

## Possible Successors

`disp_image`

## Alternatives

`equ_histo_image`,
`scale_image`,
`scale_image_max`,
`illuminate`

## See also

`equ_histo_image`,
`scale_image`

## References

S. Pizer et al.: “Adaptive Histogram Equalization and Its Variations”;
Computer Vision, Graphics, and Image Processing, vol. 39, no. 3, pp. 355-368,
1987, doi: 10.1016/S0734-189X(87)80186-X.
  
Philipp Härtinger, Carsten Steger: “Adaptive histogram equalization in
constant time”; Journal of Real-Time Image Processing, vol. 21, article 93,
2024, doi: 10.1007/s11554-024-01465-1.

## Module

Foundation
