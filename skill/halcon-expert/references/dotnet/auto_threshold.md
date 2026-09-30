# AutoThreshold (Operator)

## Name

`AutoThreshold` — Segment an image using thresholds determined from its histogram.

## Signature

`static void HOperatorSet.AutoThreshold(HObject image, out HObject regions, HTuple sigma)`

`HRegion HImage.AutoThreshold(HTuple sigma)`

`HRegion HImage.AutoThreshold(double sigma)`

## Description

`AutoThreshold` segments a single-channel image using
multiple thresholding. First, the absolute histogram of the gray
values is determined. Then, relevant minima are extracted from the
histogram, which are used successively as parameters for a
thresholding operation. The thresholds used for byte images are 0,
255, and all minima extracted from the histogram (after the
histogram has been smoothed with a Gaussian filter with standard
deviation *`sigma`*). For each gray value interval *one*
region is generated. Thus, the number of regions is the number of
minima + 1. For uint2 images, the above procedure is used
analogously. However, here the highest threshold is 65535.
Furthermore, for uint2 images the value of *`sigma`* (virtually)
refers to a histogram with 256 values, although internally histograms
with a higher resolution are used. This is done to facilitate
switching between image types without having to change the parameter
*`sigma`*. For float images the thresholds are the minimum and
maximum gray value in the image and all minima extracted from the
histogram. Here, the scaling of the parameter *`sigma`* refers
to the original gray values of the image.
The larger the value of *`sigma`* is chosen,
the fewer regions will be extracted. This operator is useful if the
regions to be extracted exhibit similar gray values (homogeneous
regions).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`regions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Regions with gray values within the automatically
determined intervals.

**`sigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Sigma for the Gaussian smoothing of the histogram.

Default:
2.0

Suggested values:
0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0

Value range:
`sigma` (lin)

Minimum increment:
0.01

Recommended increment:
0.3

## Example (HDevelop)

```
read_image (Image, 'fabrik')
median_image (Image, Median, 'circle', 3, 'mirrored')
auto_threshold (Median, Seg, 2.0)
connection (Seg, Connected)
```

## Possible Predecessors

`AnisotropicDiffusion`,
`MedianImage`,
`Illuminate`

## Possible Successors

`Connection`,
`SelectShape`,
`SelectGray`

## Alternatives

`BinaryThreshold`,
`CharThreshold`

## See also

`GrayHisto`,
`GrayHistoAbs`,
`HistoToThresh`,
`SmoothFunct1dGauss`,
`Threshold`

## Module

Foundation
