# expand_region (Operator)

## Name

`expand_region` — Fill gaps between regions or split overlapping regions.

## Signature

`def expand_region(regions: HObject, forbidden_area: HObject, iterations: Union[int, str], mode: str) -> HObject`

## Description

`expand_region` closes gaps between the input regions, which
resulted from the suppression of small regions in a segmentation
operator, for example, (mode *"image"*), or to separate
overlapping regions (mode *"region"*). Both uses result from the
expansion of regions. The operator works by adding or removing a
one pixel wide “strip” to a region.

The expansion takes place only in regions that are designated as
not “forbidden” (parameter *`forbidden_area`*). The number
of iterations is determined by the parameter *`iterations`*.
By passing *"maximal"*, `expand_region` iterates until
convergence, i.e., until no more changes occur. By passing 0 for
this parameter, all non-overlapping regions are returned. The two
modes of operation (*"image"* and *"region"*) are
different in the following ways:

- ***"image"*** —

  The input regions are expanded iteratively until they
  touch another region or the image border.
  In this case, the image border is defined to be the
  rectangle ranging from (0,0) to (row_max,col_max).
  Here, (row_max,col_max) corresponds to the lower right
  corner of the smallest surrounding rectangle of all input regions
  (i.e., of all regions that are passed in *`regions`* and
  *`forbidden_area`*).
  Because `expand_region` processes all regions simultaneously,
  gaps between regions are distributed evenly to all
  regions. Overlapping regions are split by distributing
  the area of overlap evenly to both regions.
- ***"region"*** —

  No expansion of the input regions is performed. Instead,
  only overlapping regions are split by distributing the
  area of overlap evenly to the respective regions. Because
  the intersection with the original region is computed
  after the shrinking operation gaps in the output regions
  may result, i.e., the segmentation is not complete. This
  can be prevented by calling `expand_region` a second
  time with the complement of the original regions as
  “forbidden area.”

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions for which the gaps are to be closed, or which
are to be separated.

**`forbidden_area`** (input_object)  region `→` HObject

Regions in which no expansion takes place.

**`region_expanded`** (output_object)  region(-array) `→` HObject

Expanded or separated regions.

**`iterations`** (input_control)  integer `→` Union[int, str]

Number of iterations.

Default:
"maximal"

Suggested values:
"maximal", 0, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 70, 100, 200

Value range:
`0
≤
iterations
≤
1000` (lin)

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

## Result

`expand_region` always returns the value 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`pouring`,
`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`dilation1`

## See also

`expand_gray`,
`interjacent`,
`skeleton`

## Module

Foundation
