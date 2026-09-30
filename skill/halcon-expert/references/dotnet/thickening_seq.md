# ThickeningSeq (Operator)

## Name

`ThickeningSeq` — Add the result of a hit-or-miss operation to a region (sequential).

## Warning

**`ThickeningSeq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ThickeningSeq(HObject region, out HObject regionThick, HTuple golayElement, HTuple iterations)`

`HRegion HRegion.ThickeningSeq(string golayElement, int iterations)`

## Description

`ThickeningSeq` calculates the sequential thickening of
the input regions with a structuring element from the Golay alphabet
(*`golayElement`*). To do so, `ThickeningSeq`
calls the operator [`ThickeningGolay`](thickening_golay.md) with all possible
rotations of the structuring element *`iterations`* times.
The following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The Golay elements, together with all possible rotations, are
described with the operator [`GolayElements`](golay_elements.md). For all
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

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`regionThick`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the thickening operator.

**`golayElement`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Structuring element from the Golay alphabet.

Default:
"h"

List of values:
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50, 70, 100, 200

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

`ThickeningSeq` returns 2 (
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

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`ThickeningGolay`,
`Thickening`

## See also

`ErosionGolay`,
`ThinningSeq`

## Module

Foundation
