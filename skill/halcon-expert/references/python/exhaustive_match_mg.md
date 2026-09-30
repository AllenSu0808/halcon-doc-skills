# exhaustive_match_mg (Operator)

## Name

`exhaustive_match_mg` — Matching a template and an image in a resolution pyramid.

## Signature

`def exhaustive_match_mg(image: HObject, image_template: HObject, mode: str, level: int, threshold: int) -> HObject`

## Description

The operator `exhaustive_match_mg` is an additional option for the
operator [`exhaustive_match`](exhaustive_match.md) performing a matching of the image
*`image`* and the template *`image_template`*.
Hereby *`image_template`* will be moved over all points
of the region of *`image`*, a matching criterion will be
calculated with regard to the parameter *`mode`*
and the result values will be stored in *`image_match`*.

Of images having been filtered this way, normally only those areas
with good matching results are of interest. The size of the area to
be searched, i.e. the region of the input image *`image`*,
determines decisively the runtime of the matching filter.
Therefore it is recommendable to use at first `exhaustive_match_mg`
with reduced image resolution in order to determine a
“region of interest” in which good matching results can be expected;
then in this restricted area only the real matching (see also
[`exhaustive_match`](exhaustive_match.md)) will be executed with normal resolution.

Hereby the Gauss-pyramids of *`image`* and *`image_template`*
will be composed (in particular the corresponding regions will be
transformed as well). Then on each level of the resolution pyramids -
starting with the startlevel *`level`* - the matching inside
the current “region of interest” will be executed. Whereby the
“region of interest” on the startlevel is equivalent to the
region of the input image *`image`*.
After the filtering, a new “region of interest” is determined with
the help of a threshold operation and will be transformed on the
next resolution level:

threshold(...:...:0,Threshold,...:), if Mode = 'dfd'
threshold(...:...:Threshold,255,...:), if Mode = 'norm_correlation'

The final matching in the determined “region of interest” will then be
calculated with the highest resolution (*`level`* 0).
The output image *`image_match`* includes the corresponding
filter result and the final “region of interest”, which
is determined on the result image with the help of a threshold operation.

The operator `exhaustive_match_mg` therefore is not simply
a filter, but can also be considered as a member of the class of region
transformations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image.

**`image_template`** (input_object)  singlechannelimage `→` HObject (byte)

The domain of this image will be
matched with *`image`*.

**`image_match`** (output_object)  image(-array) `→` HObject (byte)

Result image and result region: values of the matching
criterion within the determined “region of interest”.

Number of elements:
ImageMatch == Image

**`mode`** (input_control)  string `→` str

Desired matching criterion.

Default:
"dfd"

List of values:
"dfd", "norm_correlation"

**`level`** (input_control)  integer `→` int

Startlevel in the resolution pyramid (highest
resolution: Level 0).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

Restriction:
`Level <= ld(width(Image)) && Level <= ld(height(Image)) && Level <= ld(width(ImageTemplate)) && Level <= ld(height(ImageTemplate))`

**`threshold`** (input_control)  integer `→` int

Threshold to determine the “region of interest”.

Default:
30

Suggested values:
5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250

Value range:
`0
≤
threshold
≤
255`

Minimum increment:
1

Recommended increment:
5

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
draw_rectangle2(WindowHandle,&Row,&Column,&Phi,&Length1,&Length2);
gen_rectangle2(&Rectangle,Row,Column,Phi,Length1,Length2);
reduce_domain(Image,Rectangle,&Template);
exhaustive_match_mg(Image,Template,&ImageMatch,'dfd'1,30);
invert_image(ImageMatch,&ImageInvert);
local_max(ImageInvert,&BestFit);
disp_region(BestFit,WindowHandle);
```

## Result

If the parameter values are correct, the operator
`exhaustive_match_mg` returns the value 2 (
H_MSG_TRUE)
.
If the input is empty (no input images are available) the behavior can
be set via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`draw_region`,
`draw_rectangle1`

## Possible Successors

`threshold`,
`local_max`

## Alternatives

`exhaustive_match`

## See also

`gen_gauss_pyramid`

## Module

Foundation
