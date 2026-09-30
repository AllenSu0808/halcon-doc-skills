# thickening_seq (Operator)

## Name

`thickening_seq` — Add the result of a hit-or-miss operation to a region (sequential).

## Warning

**`thickening_seq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`thickening_seq(Region : RegionThick : GolayElement, Iterations : )`

## Description

`thickening_seq` calculates the sequential thickening of
the input regions with a structuring element from the Golay alphabet
(*`GolayElement`*). To do so, `thickening_seq`
calls the operator [`thickening_golay`](thickening_golay.md) with all possible
rotations of the structuring element *`Iterations`* times.
The following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The Golay elements, together with all possible rotations, are
described with the operator [`golay_elements`](golay_elements.md). For all
elements of the Golay alphabet, except for 'c', the foreground and
background masks are exchanged in order to have an effect for them
on the outer boundary of the region. The element 'c' can be used to
generate the convex hull of the input region if enough iterations
are performed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`RegionThick`** (output_object)  region(-array) `→` object

Result of the thickening operator.

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
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50, 70, 100, 200

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

`thickening_seq` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`thickening_golay`,
`thickening`

## See also

`erosion_golay`,
`thinning_seq`

## Module

Foundation
