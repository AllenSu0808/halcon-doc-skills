# EquHistoImageRect (Operator)

## Name

`EquHistoImageRect` — Histogram linearization within a rectangluar mask.

## Signature

`static void HOperatorSet.EquHistoImageRect(HObject image, out HObject imageEquHisto, HTuple mode, HTuple maskWidth, HTuple maskHeight, HTuple maxContrast)`

`HImage HImage.EquHistoImageRect(string mode, int maskWidth, int maskHeight, HTuple maxContrast)`

`HImage HImage.EquHistoImageRect(string mode, int maskWidth, int maskHeight, double maxContrast)`

## Description

The operator `EquHistoImageRect` enhances the contrast.
Similar to [`EquHistoImage`](equ_histo_image.md), it applies a transformation to linearize
the cumulative histogram. However, instead of using the histogram of the
whole image, only the local neighborhood of each pixel is considered to
compute the transformation. The size of this rectangular neighborhood region
can be set by *`maskWidth`* and *`maskHeight`*.

The local contrast maximization improves the visibility of low-contrast
structures, but also amplifies noise. The parameter *`maxContrast`* can
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

The operator `EquHistoImageRect` primarily serves for
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Image to be enhanced.

**`imageEquHisto`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Image with linearized gray values.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Processing mode.

Default:
"accurate"

Suggested values:
"accurate", "fast"

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
51

Suggested values:
31, 51, 101, 151

Value range:
`1
≤
maskWidth`

Minimum increment:
2

Restriction:
`MaskWidth <= width(Image)`

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the filter mask.

Default:
51

Suggested values:
31, 51, 101, 151

Value range:
`1
≤
maskHeight`

Minimum increment:
2

Restriction:
`MaskHeight <= height(Image)`

**`maxContrast`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum contrast.

Default:
0.01

Suggested values:
0, 0.01, 0.02, 0.05, 0.1, 0.5, 1

Value range:
`0
≤
maxContrast
≤
1`

## Complexity

In *`mode`*=*"accurate"*, `EquHistoImageRect` uses an
algorithm with constant complexity per pixel, i.e., the runtime only depends
on the size of the input image and not on the mask size.

In *`mode`*=*"fast"*, the number of histograms to be computed
depends on the mask size. Hence, the runtime increases with smaller mask
sizes and decreases with larger mask sizes.

## Possible Successors

`DispImage`

## Alternatives

`EquHistoImage`,
`ScaleImage`,
`ScaleImageMax`,
`Illuminate`

## See also

`EquHistoImage`,
`ScaleImage`

## References

S. Pizer et al.: “Adaptive Histogram Equalization and Its Variations”;
Computer Vision, Graphics, and Image Processing, vol. 39, no. 3, pp. 355-368,
1987, doi: 10.1016/S0734-189X(87)80186-X.
  
Philipp Härtinger, Carsten Steger: “Adaptive histogram equalization in
constant time”; Journal of Real-Time Image Processing, vol. 21, article 93,
2024, doi: 10.1007/s11554-024-01465-1.

## Module

Foundation
