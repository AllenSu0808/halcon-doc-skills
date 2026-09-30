# dilation_golay (Operator)

## Name

`dilation_golay` — Dilate a region with an element from the Golay alphabet.

## Warning

**`dilation_golay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`dilation_golay(Region : RegionDilation : GolayElement, Iterations, Rotation : )`

## Description

`dilation_golay` dilates a region with the selected
element *`GolayElement`* from the Golay alphabet. The
following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The rotation number *`Rotation`* determines which rotation of
the element should be used, and whether the foreground (even) or
background version (odd) of the selected element should be used.
The Golay elements, together with all possible rotations, are
described with the operator [`golay_elements`](golay_elements.md). The
operator works by shifting the structuring element over the region
to be processed (*`Region`*). For all positions of the
structuring element that intersect the region, the corresponding
reference point (relative to the structuring element) is added to
the output region. This means that the union of all translations of
the structuring element within the region is computed.

The parameter *`Iterations`* determines the number of
iterations which are to be performed with the structuring element.
The result of iteration n-1 is used as input for iteration n.

## Attention

Not all values of *`Rotation`* are valid for any Golay
element. For some of the values of *`Rotation`*, the
resulting regions are identical to the input regions.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be dilated.

**`RegionDilation`** (output_object)  region(-array) `→` object

Dilated regions.

**`GolayElement`** (input_control)  string `→`  (string)

Structuring element from the Golay alphabet.

Default:
'h'

List of values:
'c', 'd', 'e', 'f', 'f2', 'h', 'i', 'k', 'l', 'm'

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`1
≤
Iterations` (lin)

Minimum increment:
1

Recommended increment:
1

**`Rotation`** (input_control)  integer `→`  (integer)

Rotation of the Golay element. Depending on the
element, not all rotations are valid.

Default:
0

List of values:
0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15

## Complexity

Let F be the area of an input region. Then the runtime complexity for one
region is:
$$O(3\cdot \sqrt{F}) .$$ ![figure](../assets/002835c365864fd9.svg)

## Result

`dilation_golay` returns 2 (
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
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`dilation1`,
`dilation2`,
`dilation_seq`

## See also

`erosion_golay`,
`opening_golay`,
`closing_golay`,
`hit_or_miss_golay`,
`thinning_golay`,
`thickening_golay`,
`golay_elements`

## Module

Foundation
