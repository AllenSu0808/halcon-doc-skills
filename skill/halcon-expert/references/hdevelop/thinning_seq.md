# thinning_seq (Operator)

## Name

`thinning_seq` — Remove the result of a hit-or-miss operation from a region (sequential).

## Warning

**`thinning_seq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`thinning_seq(Region : RegionThin : GolayElement, Iterations : )`

## Description

`thinning_seq` calculates the sequential thinning of
the input regions with a structuring element from the Golay alphabet
(*`GolayElement`*). To do so, `thinning_seq`
calls the operator [`thinning_golay`](thinning_golay.md) with all possible
rotations of the structuring element *`Iterations`* times.
If *`Iterations`* is chosen large enough, the operator
calculates the skeleton of a region if the structuring elements 'l'
or 'm' are used. For the element 'c' the background and foreground
are exchanged in order to have an effect on the interior boundary of
a region. If a very large value or 'maximal' is passed for
*`Iterations`* the iteration stops if no more changes occur.
The following structuring elements are available:

- **'l'** —

  Skeleton, similar to [`skeleton`](skeleton.md). This structuring
  element is also used in [`morph_skiz`](morph_skiz.md).
- **'m'** —

  A skeleton with many “hairs” and multiple (parallel)
  branches.
- **'d'** —

  A skeleton without multiple branches, but with many gaps,
  similar to [`morph_skeleton`](morph_skeleton.md).
- **'c'** —

  Uniform erosion of the region.
- **'e'** —

  One pixel wide lines are shortened. This structuring element
  is also used in [`morph_skiz`](morph_skiz.md).
- **'i'** —

  Isolated points are removed. (Only *`Iterations`* = 1
  is useful.)
- **'f'** —

  Y-junctions are eliminated. (Only *`Iterations`* = 1
  is useful.)
- **'f2'** —

  One pixel long branches and corners are removed. (Only
  *`Iterations`* = 1 is useful.)
- **'h'** —

  A kind of inner boundary, which, however, is thicker than the
  result of [`boundary`](boundary.md), is generated. (Only
  *`Iterations`* = 1 is useful.)
- **'k'** —

  Junction points are eliminated, but also new ones are
  generated.

The Golay elements, together with all possible rotations, are
described with the operator [`golay_elements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`RegionThin`** (output_object)  region(-array) `→` object

Result of the thinning operator.

**`GolayElement`** (input_control)  string `→`  (string)

Structuring element from the Golay alphabet.

Default:
'l'

List of values:
'c', 'd', 'e', 'f', 'f2', 'h', 'i', 'k', 'l', 'm'

**`Iterations`** (input_control)  integer `→`  (integer / string)

Number of iterations. For 'f', 'f2', 'h' and 'i'
the only useful value is 1.

Default:
20

Suggested values:
'maximal', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200

Value range:
`1
≤
Iterations` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of an input region. Then the runtime complexity for one
region is:
$$O(Iterations \cdot 6 \cdot \sqrt{F})$$ ![figure](../assets/2bd06aa8b3654f52.svg)

## Result

`thinning_seq` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`draw_region`,
`gen_region_points`,
`gen_struct_elements`,
`gen_region_polygon_filled`

## Possible Successors

`pruning`,
`reduce_domain`,
`select_shape`,
`area_center`,
`connection`,
`complement`

## Alternatives

`skeleton`,
`morph_skiz`,
`expand_region`

## See also

`hit_or_miss_seq`,
`erosion_golay`,
`difference`,
`thinning_golay`,
`thinning`,
`thickening_seq`

## Module

Foundation
