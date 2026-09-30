# ErosionSeq (Operator)

## Name

`ErosionSeq` — Erode a region sequentially.

## Warning

**`ErosionSeq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ErosionSeq(HObject region, out HObject regionErosion, HTuple golayElement, HTuple iterations)`

`HRegion HRegion.ErosionSeq(string golayElement, int iterations)`

## Description

`ErosionSeq` computes the sequential erosion of the
input region *`region`* with the selected structuring element
*`golayElement`* from the Golay alphabet. This is done by
executing the operator [`ErosionGolay`](erosion_golay.md) with all rotations
of the structuring element *`iterations`* times. The
following structuring elements can be selected:

'l', 'd', 'c', 'f', 'h', 'k'.

Only the “foreground elements” (even rotation numbers) are used.
The elements 'i' and 'e' result in unchanged output regions. The
elements 'l', 'm' and 'f2' are identical for the foreground. The
Golay elements, together with all possible rotations, are described
with the operator [`GolayElements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be eroded.

**`regionErosion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Eroded regions.

**`golayElement`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Structuring element from the Golay alphabet.

Default:
"h"

List of values:
"c", "d", "f", "h", "k", "l"

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

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
$$O(Ieiterations \cdot 20 \cdot \sqrt{F})$$ ![figure](../assets/21ec6d726f081269.svg)

## Result

`ErosionSeq` returns 2 (
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
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`Connection`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`

## Alternatives

`ErosionGolay`,
`Erosion1`,
`Erosion2`

## See also

`DilationSeq`,
`HitOrMissSeq`,
`ThinningSeq`

## Module

Foundation
