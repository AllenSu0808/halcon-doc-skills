# MedianSeparate (Operator)

## Name

`MedianSeparate` — Separated median filtering with rectangle masks.

## Signature

`static void HOperatorSet.MedianSeparate(HObject image, out HObject imageSMedian, HTuple maskWidth, HTuple maskHeight, HTuple margin)`

`HImage HImage.MedianSeparate(int maskWidth, int maskHeight, HTuple margin)`

`HImage HImage.MedianSeparate(int maskWidth, int maskHeight, string margin)`

## Description

The operator `MedianSeparate` carries out a variation of
the median filtering: First two auxiliary images are created. The
first one originates from a median filtering with a horizontal mask
having a height of one pixel and the width *`maskWidth`*
followed by filtering with a vertical mask having the height
*`maskHeight`* and width of one pixel.
The second auxiliary image is created by
filtering with the same masks, but with a reversed sequence of the
operation: first the vertical, then the horizontal mask. The output
image results from averaging the two auxiliary images pixel by
pixel.

The operator `MedianSeparate` is clearly faster than the
normal operator [`MedianImage`](median_image.md) because both masks are one pixel
wide, facilitating a very efficient processing. The runtime is
practically *independent* of the size of the mask. For example, the
operator `MedianSeparate` can be well used after texture
filters, where large masks are needed.

The filter can also be used several times in a row in order to
enhance the smoothing.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

Due to performance reasons, the input *`image`* is not checked whether
it contains NaNs. Using an input image with NaNs crashes HALCON.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`imageSMedian`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Median filtered image.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of rank mask.

Default:
25

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 43, 51, 67, 91, 121, 151

Value range:
`1
≤
maskWidth
≤
401`

Minimum increment:
2

Recommended increment:
2

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of rank mask.

Default:
25

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 43, 51, 67, 91, 121, 151

Value range:
`1
≤
maskHeight
≤
401`

Minimum increment:
2

Recommended increment:
2

**`margin`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long / double)

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image(Image,'fabrik')
median_separate(Image,MedianSeparate,5,5,3)
dev_display(MedianSeparate)
```

## Complexity

For each pixel: O(40).

## Possible Predecessors

`TextureLaws`,
`SobelAmp`,
`DeviationImage`

## Possible Successors

`LearnNdimNorm`,
`Regiongrowing`,
`AutoThreshold`

## Alternatives

`MedianImage`

## See also

`RankImage`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 319

## Module

Foundation
