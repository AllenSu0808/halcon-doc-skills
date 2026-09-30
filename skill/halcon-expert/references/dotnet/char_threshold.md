# CharThreshold (Operator)

## Name

`CharThreshold` — Perform a threshold segmentation for extracting characters.

## Signature

`static void HOperatorSet.CharThreshold(HObject image, HObject histoRegion, out HObject characters, HTuple sigma, HTuple percent, out HTuple threshold)`

`HRegion HImage.CharThreshold(HRegion histoRegion, double sigma, HTuple percent, out HTuple threshold)`

`HRegion HImage.CharThreshold(HRegion histoRegion, double sigma, double percent, out int threshold)`

## Description

The main application of `CharThreshold` is to segment single-channel
images of dark characters on bright paper. The operator works as follows:
First, a histogram of the gray values in the image *`image`* is computed
for the points in the region *`histoRegion`*{}. To eliminate noise, the
histogram is smoothed with the given *`sigma`* (Gaussian smoothing). In
the histogram, the background (white paper) corresponds to a large peak at
high gray values, while the characters form a small peak at low gray
values. In contrast to the operator [`BinaryThreshold`](binary_threshold.md)
(with `method`=*"smooth_histo"*), which locates the
minimum between the two peaks, here the threshold for the segmentation is
determined in relation to the maximum of the histogram, i.e., the background,
with the following condition:
histogram[threshold] * 100.0 < histogram[maximum] * (100.0 - *`percent`*)

For example, if you choose *`percent`* = 95 the operator locates the
gray value whose frequency is at most 5 percent of the maximum
frequency. Because `CharThreshold` assumes that the characters are
darker than the background, the threshold is searched for “to the left” of
the maximum.

In comparison to [`BinaryThreshold`](binary_threshold.md), this operator should be used if
there is no clear minimum between the histogram peaks corresponding to the
characters and the background, respectively, or if there is no peak
corresponding to the characters at all. This may happen, e.g., if the image
contains only few characters or in the case of a non-uniform illumination.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image.

**`histoRegion`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the histogram is computed.

**`characters`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Dark regions (characters).

**`sigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Sigma for the Gaussian smoothing of the histogram.

Default:
2.0

Suggested values:
0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0

Value range:
`0.0
≤
sigma
≤
50.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.2

**`percent`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Percentage for the gray value difference.

Default:
95

Suggested values:
90, 92, 95, 96, 97, 98, 99, 99.5, 100

Value range:
`0.0
≤
percent
≤
100.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`threshold`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Calculated threshold.

## Example (HDevelop)

```
read_image (Image, 'letters')
char_threshold (Image, Image, Seg, 0.0, 5.0, Threshold)
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
`AutoThreshold`,
`GrayHisto`,
`SmoothFunct1dGauss`,
`Threshold`

## Module

Foundation
