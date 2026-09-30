# DilationSeq (Operator)

## Name

`DilationSeq` — Dilate a region sequentially.

## Warning

**`DilationSeq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.DilationSeq(HObject region, out HObject regionDilation, HTuple golayElement, HTuple iterations)`

`HRegion HRegion.DilationSeq(string golayElement, int iterations)`

## Description

`DilationSeq` computes the sequential dilation of the
input region *`region`* with the selected structuring element
*`golayElement`* from the Golay alphabet. This is done by
executing the operator [`DilationGolay`](dilation_golay.md) with all rotations
of the structuring element *`iterations`* times. The
following structuring elements can be selected:

'l', 'd', 'c', 'f', 'h', 'k'.

In order to compute the skeleton of a region, usually the elements
'l' and 'm' are used. Only the “foreground elements” (even
rotation numbers) are used. The elements 'i' and 'e' result in
unchanged output regions. The elements 'l', 'm' and 'f2' are
identical for the foreground. The Golay elements, together with all
possible rotations, are described with the operator
[`GolayElements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be dilated.

**`regionDilation`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Dilated regions.

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

`DilationSeq` returns 2 (
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
`ClassNdimNorm`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Dilation1`,
`Dilation2`,
`DilationGolay`

## See also

`ErosionSeq`,
`HitOrMissSeq`,
`ThinningSeq`

## Module

Foundation
