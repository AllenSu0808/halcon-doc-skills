# Roberts (Operator)

## Name

`Roberts` — Detect edges using the Roberts filter.

## Signature

`static void HOperatorSet.Roberts(HObject image, out HObject imageRoberts, HTuple filterType)`

`HImage HImage.Roberts(string filterType)`

## Description

`Roberts` calculates the first derivative of an image
and is used as an edge operator. If the following mask describes a
part of the image,
A B
C D
the different filter types are defined as follows:
'roberts_max' max(| A - D |,| B - C |)
'gradient_max' max(| A + B - (C + D)|,| A + C - (B + D)|)
'gradient_sum' |A + B - (C + D)| + |A + C - (B + D)|
If an overflow occurs the result is clipped. The result of the
operator is stored at the pixel with the coordinates of "D".

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Input image.

**`imageRoberts`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Roberts-filtered result images.

**`filterType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Filter type.

Default:
"gradient_sum"

List of values:
"gradient_max", "gradient_sum", "roberts_max"

## Example (HDevelop)

```
read_image(Image,'fabrik')
roberts(Image,Roberts,'roberts_max')
threshold(Roberts,Margin,128,255)
```

## Result

`Roberts` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`

## Possible Successors

`Threshold`,
`Skeleton`

## Alternatives

`EdgesImage`,
`SobelAmp`,
`FreiAmp`,
`KirschAmp`,
`PrewittAmp`

## See also

`Laplace`,
`HighpassImage`,
`BandpassImage`

## Module

Foundation
