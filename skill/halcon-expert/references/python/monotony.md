# monotony (Operator)

## Name

`monotony` — Calculating the monotony operation.

## Signature

`def monotony(image: HObject) -> HObject`

## Description

The operator `monotony` calculates the monotony operator.
Thereby the points which are strictly smaller than the current
gray value will be counted in the 8 neighborhood. This number
will be entered into the output imaged.

If there is a strict maximum, the value 8 is returned; in case of
a minimum or a plateau, the value 0 will be returned. A ridge or
a slope will return the corresponding intermediate values.

The monotony operator is often used to prepare matching operations
as it is invariant with regard to lightness modifications.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Input image.

**`image_monotony`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Result of the monotony operator.

Number of elements:
ImageMonotony == Image

## Example (C)

```
/* searching the strict maximums */
gauss_filter(Image,&Gauss,5);
monotony(Gauss,&Monotony);
threshold(Monotony,Maxima,8.0,8.0);
```

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`median_image`,
`mean_image`,
`smooth_image`,
`invert_image`

## Possible Successors

`threshold`,
`exhaustive_match`,
`disp_image`

## Alternatives

`local_max`,
`topographic_sketch`,
`corner_response`

## Module

Foundation
