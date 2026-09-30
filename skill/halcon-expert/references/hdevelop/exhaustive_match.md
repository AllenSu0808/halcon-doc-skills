# exhaustive_match (Operator)

## Name

`exhaustive_match` — Matching of a template and an image.

## Signature

`exhaustive_match(Image, RegionOfInterest, ImageTemplate : ImageMatch : Mode : )`

## Description

The operator `exhaustive_match` matches *`ImageTemplate`*
and *`Image`* within the region of interest
*`RegionOfInterest`*. Hereby the *`ImageTemplate`*
will be moved over all points of *`Image`* which lie within
the *`RegionOfInterest`*. With regard to the parameter
*`Mode`*, a matching criterion will be calculated. The result
values will be stored in *`ImageMatch`*.

The following matching criteria (*`Mode`*) are available:

- **'norm_correlation'** —

  $$ImageMatch[i][j] = 255. \frac{\sum_{u,v}(Image[i-u][j-v] \cdot ImageTemplate[l-u][c-v])}{\sqrt{\sum_{u,v}(Image[i-u][j-v]^{2}) \cdot \sum_{u,v}(ImageTemplate[l-u][c-v]^{2})}}$$ ![figure](../assets/bbd6efccf1883995.svg)
  whereby $X[i][j]$ indicates the gray value in the $i$-th
  column and $j$-th row of the image $X$. $(l,c)$ is
  the center of the region of *`ImageTemplate`*.
  $u$ and $v$ are chosen so that all points of the template will
  be reached, $i,j$ run across the *`RegionOfInterest`*.
  At the image frame only those parts of *`ImageTemplate`*
  will be considered which lie inside the image (i.e. $u$ and
  $v$ will be restricted correspondingly). Higher values returned in
  *`ImageMatch`*, represent better matches.

  *Range of values:* [*0* ... *255* (best fit)].
- **'dfd'** —

  Calculating the average “displaced frame difference”:
  $$ImageMatch[i][j] = \frac{\sum_{u,v} |Image[i - u][j - v] - ImageTemplate[l - u][c - v]|}{AREA(ImageTemplate)}$$ ![figure](../assets/e304a8f8c810a168.svg)
  The terms are the same as in *'norm_correlation'*.
  $AREA(X)$ means the area of the region $X$.
  Lower values returned in *`ImageMatch`*, represent better matches.

  *Range of values:* [*0* (best fit) .. *255*].

To calculate the normalized correlation as well as the “displaced frame
difference” is (with regard to the area of *`ImageTemplate`*)
very time consuming.
Therefore it is important to restrict the input region
(*`RegionOfInterest`* if possible, i.e. to apply the filter only
in a very confined “region of interest”.

As far as quality is concerned, both modes return comparable results,
whereby the mode *'dfd'* is faster by a factor of about 3.5.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image.

**`RegionOfInterest`** (input_object)  region `→` object

Area to be searched in the input image.

**`ImageTemplate`** (input_object)  singlechannelimage `→` object (byte)

This area will be “matched”
by *`Image`* within the
*`RegionOfInterest`*.

**`ImageMatch`** (output_object)  image(-array) `→` object (byte)

Result image: values of the matching criterion.

**`Mode`** (input_control)  string `→`  (string)

Desired matching criterion.

Default:
'dfd'

List of values:
'dfd', 'norm_correlation'

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display(Image)
draw_rectangle2(WindowHandle,Row,Column,Phi,Length1,Length2)
gen_rectangle2(Rectangle,Row,Column,Phi,Length1,Length2)
reduce_domain(Image,Rectangle,Template)
exhaustive_match(Image,Image,Template,ImageMatch,'dfd')
invert_image(ImageMatch,ImageInvert)
local_max(Image,Maxima)
union1(Maxima,AllMaxima)
add_channels(AllMaxima,ImageInvert,FitMaxima)
threshold(FitMaxima,BestFit,230.0,255.0)
dev_display(BestFit)
```

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
