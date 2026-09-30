# DynThreshold (Operator)

## Name

`DynThreshold` — Segment an image using a local threshold.

## Signature

`static void HOperatorSet.DynThreshold(HObject origImage, HObject thresholdImage, out HObject regionDynThresh, HTuple offset, HTuple lightDark)`

`HRegion HImage.DynThreshold(HImage thresholdImage, HTuple offset, string lightDark)`

`HRegion HImage.DynThreshold(HImage thresholdImage, double offset, string lightDark)`

## Description

`DynThreshold` selects from the input image those
regions in which the pixels fulfill a threshold condition. Let
g_{o} = g_{*`origImage`*}, and g_{t} =
g_{*`thresholdImage`*}. Then the condition for
*`lightDark`* = *"light"* is:
$$g_{o}\ge g_{t}+\texttt{Offset}$$
For *`lightDark`* = *"dark"* the condition is:
$$g_{o}\le g_{t}-\texttt{Offset}$$
For *`lightDark`* = *"equal"* it is:
$$g_{t}-\texttt{Offset}\le g_{o}\le g_{t}+\texttt{Offset}$$
Finally, for *`lightDark`* = *"not_equal"* it is:
$$g_{t}-\texttt{Offset}>g_{o}\vee g_{o}>g_{t}+\texttt{Offset}$$

Typically, the threshold images are smoothed versions of the
original image (e.g., by applying [`MeanImage`](mean_image.md),
[`BinomialFilter`](binomial_filter.md), [`GaussFilter`](gauss_filter.md), etc.). Then the
effect of `DynThreshold` is similar to applying
[`Threshold`](threshold.md) to a highpass-filtered version of the original
image (see [`HighpassImage`](highpass_image.md)).

With `DynThreshold`, contours of an object can be extracted,
where the objects' size (diameter) is determined by the mask size of
the lowpass filter and the amplitude of the objects' edges:

The larger the mask size is chosen, the larger the found regions
become. As a rule of thumb, the mask size should be about twice the
diameter of the objects to be extracted. It is important not to set
the parameter *`offset`* to zero because in this case too
many small regions will be found (noise). Values between 5 and 40
are a useful choice. The larger *`offset`* is chosen, the
smaller the extracted regions become.

All points of the input image fulfilling the above condition are
stored jointly in one region. If necessary, the connected
components can be obtained by calling [`Connection`](connection.md).

## Attention

If *`offset`* is chosen from -1 to 1
usually a very noisy region is generated, requiring large storage.
If *`offset`* is chosen too large (> 60, say) it may happen
that no points fulfill the threshold condition (i.e., an empty
region is returned). If *`offset`* is chosen too small (<
-60, say) it may happen that all points fulfill the threshold
condition (i.e., a full region is returned).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`origImage`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Input image.

**`thresholdImage`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Image containing the local thresholds.

**`regionDynThresh`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented regions.

**`offset`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Offset applied to ThresholdImage.

Default:
5.0

Suggested values:
1.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0

Value range:
`-255.0
≤
offset
≤
255.0` (lin)

Minimum increment:
0.01

Recommended increment:
5

**`lightDark`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Extract light, dark or similar areas?

Default:
"light"

List of values:
"dark", "equal", "light", "not_equal"

## Example (HDevelop)

```
* Looking for regions with the diameter D
mean_image(Image,Mean,D*2+1,D*2+1)
dyn_threshold(Image,Mean,Seg,5,'light')
connection(Seg,Regions)
```

## Complexity

Let A be the area of the input region. Then the runtime
complexity is O(A).

## Result

`DynThreshold` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`MeanImage`,
`SmoothImage`,
`BinomialFilter`,
`GaussFilter`

## Possible Successors

`Connection`,
`SelectShape`,
`ReduceDomain`,
`SelectGray`,
`RankRegion`,
`Dilation1`,
`Opening`,
`Erosion1`

## Alternatives

`CheckDifference`,
`Threshold`

## See also

`HighpassImage`,
`SubImage`

## Module

Foundation
