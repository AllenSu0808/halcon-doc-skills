# bandpass_image (Operator)

## Name

`bandpass_image` — Edge extraction using bandpass filters.

## Signature

`def bandpass_image(image: HObject, filter_type: str) -> HObject`

## Description

`bandpass_image` serves as an edge filter. It applies a
linear filter with the following convolution mask to
*`image`*:

*`filter_type`*: *"lines"*
In contrast to the edge operator [`sobel_amp`](sobel_amp.md) this filter
detects lines instead of edges, i.e., two closely adjacent edges.
0 -2 -2 -2 0
-2 0 3 0 -2
-2 3 12 3 -2
-2 0 3 0 -2
0 -2 -2 -2 0

At the border of the image the gray values are mirrored. Over- and
underflows of gray values are clipped.
The resulting images are returned in *`image_bandpass`*.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Input images.

**`image_bandpass`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Bandpass-filtered images.

**`filter_type`** (input_control)  string `→` str

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

`bandpass_image` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Successors

`threshold`,
`skeleton`

## Alternatives

`convol_image`,
`topographic_sketch`,
`texture_laws`

## See also

`highpass_image`,
`gray_skeleton`

## Module

Foundation
