# HitOrMissSeq (Operator)

## Name

`HitOrMissSeq` — Hit-or-miss operation for regions using the Golay alphabet (sequential).

## Warning

**`HitOrMissSeq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.HitOrMissSeq(HObject region, out HObject regionHitMiss, HTuple golayElement)`

`HRegion HRegion.HitOrMissSeq(string golayElement)`

## Description

[`HitOrMissGolay`](hit_or_miss_golay.md) performs the
hit-or-miss-transformation for the input regions *`region`*
using all rotations of a structuring element from the Golay
alphabet. The result of the operator is the union of all
intermediate results of the respective rotations. The following
structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The Golay elements, together with all possible rotations, are
described with the operator [`GolayElements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`regionHitMiss`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the hit-or-miss operation.

**`golayElement`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Structuring element from the Golay alphabet.

Default:
"h"

List of values:
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

## Complexity

Let F be the area of an input region, and R be the number of
rotations. Then the runtime complexity for one region is:
$$O(R \cdot 6 \cdot \sqrt{F})$$ ![figure](../assets/9239b9920d898617.svg)

## Result

`HitOrMissSeq` returns 2 (
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

`HitOrMissGolay`,
`HitOrMiss`

## See also

`ThinningSeq`,
`ThickeningSeq`

## Module

Foundation
