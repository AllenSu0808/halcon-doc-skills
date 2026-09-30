# expand_gray (Operator)

## Name

`expand_gray` — Fill gaps between regions (depending on gray value or color) or split
overlapping regions.

## Signature

`def expand_gray(regions: HObject, image: HObject, forbidden_area: HObject, iterations: Union[int, str], mode: str, threshold: MaybeSequence[int]) -> HObject`

## Description

`expand_gray` closes gaps between the input regions,
which resulted from the suppression of small regions in a
segmentation operator, (mode *"image"*), for example, or
separates overlapping regions *"region"*).
Both uses result
from the expansion of regions. The operator works by adding a one
pixel wide “strip” to a region, in which the gray values or color
are different from the gray values or color of neighboring pixels on
the region's border by at most *`threshold`* (in each
channel). For images of type *"cyclic"* (e.g., direction
images), also points with a gray value difference of at least 255 -
*`threshold`* are added to the output region.

The expansion takes place only in regions, which are designated as
not “forbidden” (parameter *`forbidden_area`*). The number
of iterations is determined by the parameter *`iterations`*.
By passing *"maximal"*, `expand_gray` iterates
until convergence, i.e., until no more changes occur. By passing 0
for this parameter, all non-overlapping regions are returned. The
two modes of operation (*"image"* and *"region"*)
are different in the following ways:

- ***"image"*** —

  The input regions are expanded iteratively until they
  touch another region or the image border, or the expansion
  stops because of too high gray value differences. Because
  `expand_gray` processes all regions
  simultaneously, gaps between regions are distributed
  evenly to all regions with a similar gray value.
  Overlapping regions are split by distributing the area of
  overlap evenly to both regions.
- ***"region"*** —

  No expansion of the input regions is performed. Instead,
  only overlapping regions are split by distributing the
  area of overlap evenly to regions having a matching gray
  value or color.

## Attention

Because regions are only expanded into areas having a matching gray
value or color, usually gaps will remain between the output regions,
i.e., the segmentation is not complete.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions for which the gaps are to be closed, or which
are to be separated.

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic)

Image (possibly multi-channel) for gray value or color
comparison.

**`forbidden_area`** (input_object)  region `→` HObject

Regions in which no expansion takes place.

**`region_expand`** (output_object)  region(-array) `→` HObject

Expanded or separated regions.

**`iterations`** (input_control)  string `→` Union[int, str]

Number of iterations.

Default:
"maximal"

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "maximal"

Value range:
`1
≤
iterations
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`mode`** (input_control)  string `→` str

Expansion mode.

Default:
"image"

List of values:
"image", "region"

**`threshold`** (input_control)  integer(-array) `→` MaybeSequence[int]

Maximum difference between the gray value or color at
the region's border and a candidate for expansion.

Default:
32

Suggested values:
5, 10, 15, 20, 25, 30, 40, 50

Value range:
`1
≤
threshold
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

## Result

`expand_gray` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`connection`,
`regiongrowing`,
`pouring`,
`class_ndim_norm`

## Possible Successors

`select_shape`

## See also

`expand_gray_ref`,
`expand_region`

## Module

Foundation
