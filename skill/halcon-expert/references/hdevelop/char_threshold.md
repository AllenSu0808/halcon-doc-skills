# char_threshold (Operator)

## Name

`char_threshold` — Perform a threshold segmentation for extracting characters.

## Signature

`char_threshold(Image, HistoRegion : Characters : Sigma, Percent : Threshold)`

## Description

The main application of `char_threshold` is to segment single-channel
images of dark characters on bright paper. The operator works as follows:
First, a histogram of the gray values in the image *`Image`* is computed
for the points in the region *`HistoRegion`*{}. To eliminate noise, the
histogram is smoothed with the given *`Sigma`* (Gaussian smoothing). In
the histogram, the background (white paper) corresponds to a large peak at
high gray values, while the characters form a small peak at low gray
values. In contrast to the operator [`binary_threshold`](binary_threshold.md)
(with `Method`=*'smooth_histo'*), which locates the
minimum between the two peaks, here the threshold for the segmentation is
determined in relation to the maximum of the histogram, i.e., the background,
with the following condition:
histogram[threshold] * 100.0 < histogram[maximum] * (100.0 - *`Percent`*)

For example, if you choose *`Percent`* = 95 the operator locates the
gray value whose frequency is at most 5 percent of the maximum
frequency. Because `char_threshold` assumes that the characters are
darker than the background, the threshold is searched for “to the left” of
the maximum.

In comparison to [`binary_threshold`](binary_threshold.md), this operator should be used if
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

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image.

**`HistoRegion`** (input_object)  region `→` object

Region in which the histogram is computed.

**`Characters`** (output_object)  region(-array) `→` object

Dark regions (characters).

**`Sigma`** (input_control)  number `→`  (real)

Sigma for the Gaussian smoothing of the histogram.

Default:
2.0

Suggested values:
0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0

Value range:
`0.0
≤
Sigma
≤
50.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.2

**`Percent`** (input_control)  number `→`  (real / integer)

Percentage for the gray value difference.

Default:
95

Suggested values:
90, 92, 95, 96, 97, 98, 99, 99.5, 100

Value range:
`0.0
≤
Percent
≤
100.0` (lin)

Minimum increment:
0.1

Recommended increment:
0.5

**`Threshold`** (output_control)  integer(-array) `→`  (integer)

Calculated threshold.

## Example (HDevelop)

```
read_image (Image, 'letters')
char_threshold (Image, Image, Seg, 0.0, 5.0, Threshold)
connection (Seg, Connected)
```

## Possible Predecessors

`anisotropic_diffusion`,
`median_image`,
`illuminate`

## Possible Successors

`connection`,
`select_shape`,
`select_gray`

## Alternatives

`binary_threshold`,
`auto_threshold`,
`gray_histo`,
`smooth_funct_1d_gauss`,
`threshold`

## Module

Foundation
