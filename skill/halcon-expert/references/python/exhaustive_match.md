# exhaustive_match (Operator)

## Name

`exhaustive_match` — Matching of a template and an image.

## Signature

`def exhaustive_match(image: HObject, region_of_interest: HObject, image_template: HObject, mode: str) -> HObject`

## Description

The operator `exhaustive_match` matches *`image_template`*
and *`image`* within the region of interest
*`region_of_interest`*. Hereby the *`image_template`*
will be moved over all points of *`image`* which lie within
the *`region_of_interest`*. With regard to the parameter
*`mode`*, a matching criterion will be calculated. The result
values will be stored in *`image_match`*.

The following matching criteria (*`mode`*) are available:

- **'norm_correlation'** —

  $$ImageMatch[i][j] = 255. \frac{\sum_{u,v}(Image[i-u][j-v] \cdot ImageTemplate[l-u][c-v])}{\sqrt{\sum_{u,v}(Image[i-u][j-v]^{2}) \cdot \sum_{u,v}(ImageTemplate[l-u][c-v]^{2})}}$$ ![figure](../assets/bbd6efccf1883995.svg)
  whereby $X[i][j]$ indicates the gray value in the $i$-th
  column and $j$-th row of the image $X$. $(l,c)$ is
  the center of the region of *`image_template`*.
  $u$ and $v$ are chosen so that all points of the template will
  be reached, $i,j$ run across the *`region_of_interest`*.
  At the image frame only those parts of *`image_template`*
  will be considered which lie inside the image (i.e. $u$ and
  $v$ will be restricted correspondingly). Higher values returned in
  *`image_match`*, represent better matches.

  *Range of values:* [*0* ... *255* (best fit)].
- **'dfd'** —

  Calculating the average “displaced frame difference”:
  $$ImageMatch[i][j] = \frac{\sum_{u,v} |Image[i - u][j - v] - ImageTemplate[l - u][c - v]|}{AREA(ImageTemplate)}$$ ![figure](../assets/e304a8f8c810a168.svg)
  The terms are the same as in *"norm_correlation"*.
  $AREA(X)$ means the area of the region $X$.
  Lower values returned in *`image_match`*, represent better matches.

  *Range of values:* [*0* (best fit) .. *255*].

To calculate the normalized correlation as well as the “displaced frame
difference” is (with regard to the area of *`image_template`*)
very time consuming.
Therefore it is important to restrict the input region
(*`region_of_interest`* if possible, i.e. to apply the filter only
in a very confined “region of interest”.

As far as quality is concerned, both modes return comparable results,
whereby the mode *"dfd"* is faster by a factor of about 3.5.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image.

**`region_of_interest`** (input_object)  region `→` HObject

Area to be searched in the input image.

**`image_template`** (input_object)  singlechannelimage `→` HObject (byte)

This area will be “matched”
by *`image`* within the
*`region_of_interest`*.

**`image_match`** (output_object)  image(-array) `→` HObject (byte)

Result image: values of the matching criterion.

**`mode`** (input_control)  string `→` str

Desired matching criterion.

Default:
"dfd"

List of values:
"dfd", "norm_correlation"

## Result

If the parameter values are correct, the operator
`exhaustive_match` returns the value 2 (
H_MSG_TRUE)
.
If the input is empty (no input images are available) the behavior can
be set via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`draw_region`,
`draw_rectangle1`

## Possible Successors

`local_max`,
`threshold`

## Alternatives

`exhaustive_match_mg`

## Module

Foundation
