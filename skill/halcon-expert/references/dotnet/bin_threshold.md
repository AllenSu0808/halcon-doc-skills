# BinThreshold (Operator)

## Name

`BinThreshold` — Segment an image using an automatically determined
threshold.

## Warning

**`BinThreshold` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 25.11.
New applications should use
the operator [`BinaryThreshold`](binary_threshold.md) instead.**

## Signature

`static void HOperatorSet.BinThreshold(HObject image, out HObject region)`

`HRegion HImage.BinThreshold()`

## Description

`BinThreshold` segments a single-channel gray value image
using an automatically determined threshold. First, the relative
histogram of the gray values is determined. Then, relevant minima
are extracted from the histogram, which are used as parameters for a
thresholding operation. In order to reduce the number of minima,
the histogram is smoothed with a Gaussian, as in
[`AutoThreshold`](auto_threshold.md). The mask size is enlarged until there
is only one minimum in the smoothed histogram. The selected region
contains the pixels with gray values from 0 to the minimum or for real images
from the smallest value to the respective minimum. This
operator is, for example useful for the segmentation of dark
characters on a light paper.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Dark regions of the image.

## Example (HDevelop)

```
read_image (Image, 'letters')
bin_threshold (Image, Seg)
connection (Seg, Connected)
```

## Module

Foundation
