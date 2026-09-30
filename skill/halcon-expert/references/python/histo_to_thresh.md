# histo_to_thresh (Operator)

## Name

`histo_to_thresh` — Determine gray value thresholds from a histogram.

## Signature

`def histo_to_thresh(histogramm: Sequence[Union[int, float]], sigma: float) -> Tuple[Sequence[int], Sequence[int]]`

## Description

`histo_to_thresh` determines gray value thresholds from a
histogram for a segmentation of an image using [`threshold`](threshold.md).
The thresholds returned are 0, the maximum gray value in the
histogram, and all minima extracted from the histogram. Before the
thresholds are determined, the histogram is smoothed with a Gaussian
smoothing function.

`histo_to_thresh` can process the absolute and relative
histograms that are returned by [`gray_histo`](gray_histo.md). Note, however,
that here only byte images should be used, because otherwise the
returned thresholds cannot easily be transformed to the thresholds
for the actual image. For images of type uint2, the histograms
should be computed with [`gray_histo_abs`](gray_histo_abs.md) since this
facilitates a simple transformation of the thresholds by simply
multiplying the thresholds with the quantization selected in
[`gray_histo_abs`](gray_histo_abs.md). For uint2 images, it is important to ensure
that the quantization must be chosen in such a manner that the
histogram still contains salient information. For example, a 640 x 480 image with 16 bits per pixel gray value
resolution contains on average only 307200 / 65536 = 4.7 entries
per histogram bin, i.e., the histogram is too sparsely populated to
derive any useful statistics from it. To be able to extract useful
thresholds from such a histogram, *`sigma`* would have to be
set to an extremely large value, which would lead to very high run
times and numerical problems. The quantization in
[`gray_histo_abs`](gray_histo_abs.md) should therefore normally be chosen such that
the histogram contains a maximum of 1024 entries. Hence, for images
with more than 10 bits per pixel, the quantization must be chosen
greater than 1. The histogram returned by [`gray_histo_abs`](gray_histo_abs.md)
should furthermore be restricted to the parts that contain salient
information. For example, for an image with 12 bits per pixel, the
quantization should be set to 4. Only the first 1024 entries of the
computed histogram (which contains 16384 entries in this example)
should be passed to `histo_to_thresh`. Finally,
*`min_thresh`* must be multiplied by 4 (i.e., the quantization),
while *`max_thresh`* must be multiplied by 4 and increased by 3
(i.e., the quantization minus 1).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`histogramm`** (input_control)  histogram-array `→` Sequence[Union[int, float]]

Gray value histogram.

**`sigma`** (input_control)  number `→` float

Sigma for the Gaussian smoothing of the histogram.

Default:
2.0

Suggested values:
0.5, 1.0, 2.0, 3.0, 4.0, 5.0

Value range:
`0.5
≤
sigma
≤
30.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.2

**`min_thresh`** (output_control)  integer-array `→` Sequence[int]

Minimum thresholds.

**`max_thresh`** (output_control)  integer-array `→` Sequence[int]

Maximum thresholds.

## Example (HDevelop)

```
* Calculate thresholds from a byte image and threshold the image.
gray_histo (Image, Image, AbsoluteHisto, RelativeHisto)
histo_to_thresh (AbsoluteHisto, 4, MinThresh, MaxThresh)
threshold (Image, Region, MinThresh, MaxThresh)

* Calculate thresholds from a 12 bit uint2 image and threshold the image.
gray_histo_abs (Image, Image, 4, AbsoluteHisto)
AbsoluteHisto := AbsoluteHisto[0:1023]
histo_to_thresh (AbsoluteHisto, 16, MinThresh, MaxThresh)
MinThresh := MinThresh*4
MaxThresh := MaxThresh*4+3
threshold (Image, Region, MinThresh, MaxThresh)
```

## Possible Predecessors

`gray_histo`

## Possible Successors

`threshold`

## See also

`auto_threshold`,
`binary_threshold`,
`char_threshold`

## Module

Foundation
