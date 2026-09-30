# ThinningSeq (Operator)

## Name

`ThinningSeq` — Remove the result of a hit-or-miss operation from a region (sequential).

## Warning

**`ThinningSeq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ThinningSeq(HObject region, out HObject regionThin, HTuple golayElement, HTuple iterations)`

`HRegion HRegion.ThinningSeq(string golayElement, HTuple iterations)`

`HRegion HRegion.ThinningSeq(string golayElement, int iterations)`

## Description

`ThinningSeq` calculates the sequential thinning of
the input regions with a structuring element from the Golay alphabet
(*`golayElement`*). To do so, `ThinningSeq`
calls the operator [`ThinningGolay`](thinning_golay.md) with all possible
rotations of the structuring element *`iterations`* times.
If *`iterations`* is chosen large enough, the operator
calculates the skeleton of a region if the structuring elements 'l'
or 'm' are used. For the element 'c' the background and foreground
are exchanged in order to have an effect on the interior boundary of
a region. If a very large value or 'maximal' is passed for
*`iterations`* the iteration stops if no more changes occur.
The following structuring elements are available:

- **'l'** —

  Skeleton, similar to [`Skeleton`](skeleton.md). This structuring
  element is also used in [`MorphSkiz`](morph_skiz.md).
- **'m'** —

  A skeleton with many “hairs” and multiple (parallel)
  branches.
- **'d'** —

  A skeleton without multiple branches, but with many gaps,
  similar to [`MorphSkeleton`](morph_skeleton.md).
- **'c'** —

  Uniform erosion of the region.
- **'e'** —

  One pixel wide lines are shortened. This structuring element
  is also used in [`MorphSkiz`](morph_skiz.md).
- **'i'** —

  Isolated points are removed. (Only *`iterations`* = 1
  is useful.)
- **'f'** —

  Y-junctions are eliminated. (Only *`iterations`* = 1
  is useful.)
- **'f2'** —

  One pixel long branches and corners are removed. (Only
  *`iterations`* = 1 is useful.)
- **'h'** —

  A kind of inner boundary, which, however, is thicker than the
  result of [`Boundary`](boundary.md), is generated. (Only
  *`iterations`* = 1 is useful.)
- **'k'** —

  Junction points are eliminated, but also new ones are
  generated.

The Golay elements, together with all possible rotations, are
described with the operator [`GolayElements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`regionThin`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the thinning operator.

**`golayElement`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Structuring element from the Golay alphabet.

Default:
"l"

List of values:
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Number of iterations. For 'f', 'f2', 'h' and 'i'
the only useful value is 1.

Default:
20

Suggested values:
"maximal", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200

Value range:
`1
≤
iterations` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of an input region. Then the runtime complexity for one
region is:
$$O(Iterations \cdot 6 \cdot \sqrt{F})$$ ![figure](../assets/2bd06aa8b3654f52.svg)

## Result

`ThinningSeq` returns 2 (
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

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`DrawRegion`,
`GenRegionPoints`,
`GenStructElements`,
`GenRegionPolygonFilled`

## Possible Successors

`Pruning`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`,
`Complement`

## Alternatives

`Skeleton`,
`MorphSkiz`,
`ExpandRegion`

## See also

`HitOrMissSeq`,
`ErosionGolay`,
`Difference`,
`ThinningGolay`,
`Thinning`,
`ThickeningSeq`

## Module

Foundation
