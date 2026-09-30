# gray_inside (Operator)

## Name

`gray_inside` — Calculate the lowest possible gray value on an arbitrary path to the
image border for each point in the image.

## Signature

`gray_inside(Image : ImageDist : : )`

## Description

`gray_inside` determines the “cheapest” path to the
image border for each point in the image, i.e., the path on which
the lowest gray values have to be overcome. The resulting image
contains the difference of the gray value of the particular point
and the maximum gray value on the path. Bright areas in the result
image therefore signify that these areas (which are typically dark
in the original image) are surrounded by bright areas. Dark areas
in the result image signify that there are only small gray value
differences between them and the image border (which doesn't mean
that they are surrounded by dark areas; a small “gap” of dark
values suffices). The value 0 (black) in the result image
signifies that only darker or equally bright pixels exist on the
path to the image border.

The operator is implemented by first segmenting into basins and
watersheds the image using the [`watersheds`](watersheds.md) operator. If
the image is regarded as a gray value mountain range, basins are the
places where water accumulates and the mountain ridges are the
watersheds. Then, the watersheds are distributed to adjacent
basins, thus leaving only basins. The border of the domain (region)
of the original image is now searched for the lowest gray value, and
the region in which it resides is given its result values. If the
lowest gray value resides on the image border, all result values can
be calculated immediately using the gray value differences to the
darkest point. If the smallest found gray value lies in the interior
of a basin, the lowest possible gray value has to be determined from
the already processed adjacent basins in order to compute the new
values. An 8-neighborhood is used to determine adjacency. The
found region is subtracted from the regions yet to process, and the
whole process is repeated. Thus, the image is “stripped” form the
outside.

Analogously to [`watersheds`](watersheds.md), it is advisable to apply a
smoothing operation before calling [`watersheds`](watersheds.md), e.g.,
[`binomial_filter`](binomial_filter.md) or [`gauss_filter`](gauss_filter.md), in order to reduce
the amount of regions that result from the watershed algorithm, and
thus to speed up the processing time.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Image being processed.

**`ImageDist`** (output_object)  (multichannel-)image(-array) `→` object (int2)

Result image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
gauss_filter (Image,GaussImage,11)
gray_inside(GaussImage,ImageOut)
dev_display(ImageOut)
```

## Result

`gray_inside` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`mean_image`,
`median_image`

## Possible Successors

`select_shape`,
`area_center`,
`count_obj`

## See also

`watersheds`

## Module

Foundation
