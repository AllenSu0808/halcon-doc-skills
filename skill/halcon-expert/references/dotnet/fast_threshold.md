# FastThreshold (Operator)

## Name

`FastThreshold` — Fast thresholding of images using global thresholds.

## Signature

`static void HOperatorSet.FastThreshold(HObject image, out HObject region, HTuple minGray, HTuple maxGray, HTuple minSize)`

`HRegion HImage.FastThreshold(HTuple minGray, HTuple maxGray, int minSize)`

`HRegion HImage.FastThreshold(double minGray, double maxGray, int minSize)`

## Description

`FastThreshold` selects the pixels from the input image
whose gray values g fulfill the following condition:

$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$

To reduce the processing time, the selection is done in two steps: At first,
all points lying on selected horizontal lines that are specified by their
distance *`minSize`* are processed. In the next step the neighborhood
(size (2*MinSize+1) x
(2*MinSize+1)) of all previously selected points are
processed.

## Attention

On multi-core computers supporting the SSE2 instruction set, [`Threshold`](threshold.md)
is most likely faster than `FastThreshold`.
`FastThreshold` may only be preferred to [`Threshold`](threshold.md) if those
features are not available, e.g., on embedded platforms.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / direction / cyclic / real)

Input image.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented regions.

**`minGray`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Lower threshold for the gray values.

Default:
128

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0

Value range:
`0.0
≤
minGray
≤
255.0` (lin)

Minimum increment:
1

Recommended increment:
5.0

**`maxGray`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Upper threshold for the gray values.

Default:
255.0

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0

Value range:
`0.0
≤
maxGray
≤
255.0` (lin)

Minimum increment:
1

Recommended increment:
5.0

**`minSize`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum size of objects to be extracted.

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 100

Value range:
`2
≤
minSize
≤
200` (lin)

Minimum increment:
1

Recommended increment:
2

## Complexity

Let A be the area of the output region and height the
height of *`image`*. Then the runtime
complexity is O(A + height / *`minSize`*).

## Result

`FastThreshold` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions
can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`HistoToThresh`,
`MinMaxGray`,
`SobelAmp`,
`BinomialFilter`,
`GaussFilter`,
`ReduceDomain`,
`FillInterlace`

## Possible Successors

`Connection`,
`Dilation1`,
`Erosion1`,
`Opening`,
`Closing`,
`RankRegion`,
`ShapeTrans`,
`Skeleton`

## Alternatives

`Threshold`,
`GenGridRegion`,
`DilationRectangle1`,
`DynThreshold`

## See also

`Class2dimSup`,
`HysteresisThreshold`

## Module

Foundation
