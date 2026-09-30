# BandpassImage (Operator)

## Name

`BandpassImage` — Edge extraction using bandpass filters.

## Signature

`static void HOperatorSet.BandpassImage(HObject image, out HObject imageBandpass, HTuple filterType)`

`HImage HImage.BandpassImage(string filterType)`

## Description

`BandpassImage` serves as an edge filter. It applies a
linear filter with the following convolution mask to
*`image`*:

*`filterType`*: *"lines"*
In contrast to the edge operator [`SobelAmp`](sobel_amp.md) this filter
detects lines instead of edges, i.e., two closely adjacent edges.
0 -2 -2 -2 0
-2 0 3 0 -2
-2 3 12 3 -2
-2 0 3 0 -2
0 -2 -2 -2 0

At the border of the image the gray values are mirrored. Over- and
underflows of gray values are clipped.
The resulting images are returned in *`imageBandpass`*.

## Attention

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Input images.

**`imageBandpass`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Bandpass-filtered images.

**`filterType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Filter type: currently only 'lines' is supported.

Default:
"lines"

List of values:
"lines"

## Example (C)

```
bandpass_image(Image,&LineImage,"lines");
threshold(LineImage,&Lines,60.0,255.0);
skeleton(Lines,&ThinLines);
```

## Result

`BandpassImage` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Successors

`Threshold`,
`Skeleton`

## Alternatives

`ConvolImage`,
`TopographicSketch`,
`TextureLaws`

## See also

`HighpassImage`,
`GraySkeleton`

## Module

Foundation
