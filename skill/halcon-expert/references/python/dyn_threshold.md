# dyn_threshold (Operator)

## Name

`dyn_threshold` — Segment an image using a local threshold.

## Signature

`def dyn_threshold(orig_image: HObject, threshold_image: HObject, offset: Union[int, float], light_dark: str) -> HObject`

## Description

`dyn_threshold` selects from the input image those
regions in which the pixels fulfill a threshold condition. Let
g_{o} = g_{*`orig_image`*}, and g_{t} =
g_{*`threshold_image`*}. Then the condition for
*`light_dark`* = *"light"* is:
$$g_{o}\ge g_{t}+\texttt{Offset}$$
For *`light_dark`* = *"dark"* the condition is:
$$g_{o}\le g_{t}-\texttt{Offset}$$
For *`light_dark`* = *"equal"* it is:
$$g_{t}-\texttt{Offset}\le g_{o}\le g_{t}+\texttt{Offset}$$
Finally, for *`light_dark`* = *"not_equal"* it is:
$$g_{t}-\texttt{Offset}>g_{o}\vee g_{o}>g_{t}+\texttt{Offset}$$

Typically, the threshold images are smoothed versions of the
original image (e.g., by applying [`mean_image`](mean_image.md),
[`binomial_filter`](binomial_filter.md), [`gauss_filter`](gauss_filter.md), etc.). Then the
effect of `dyn_threshold` is similar to applying
[`threshold`](threshold.md) to a highpass-filtered version of the original
image (see [`highpass_image`](highpass_image.md)).

With `dyn_threshold`, contours of an object can be extracted,
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
components can be obtained by calling [`connection`](connection.md).

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

**`orig_image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Input image.

**`threshold_image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Image containing the local thresholds.

**`region_dyn_thresh`** (output_object)  region(-array) `→` HObject

Segmented regions.

**`offset`** (input_control)  number `→` Union[int, float]

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

**`light_dark`** (input_control)  string `→` str

Extract light, dark or similar areas?

Default:
"light"

List of values:
"dark", "equal", "light", "not_equal"

## Complexity

Let A be the area of the input region. Then the runtime
complexity is O(A).

## Result

`dyn_threshold` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`mean_image`,
`smooth_image`,
`binomial_filter`,
`gauss_filter`

## Possible Successors

`connection`,
`select_shape`,
`reduce_domain`,
`select_gray`,
`rank_region`,
`dilation1`,
`opening`,
`erosion1`

## Alternatives

`check_difference`,
`threshold`

## See also

`highpass_image`,
`sub_image`

## Module

Foundation
