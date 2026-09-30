# hit_or_miss_seq (Operator)

## Name

`hit_or_miss_seq` — Hit-or-miss operation for regions using the Golay alphabet (sequential).

## Warning

**`hit_or_miss_seq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`hit_or_miss_seq(Region : RegionHitMiss : GolayElement : )`

## Description

[`hit_or_miss_golay`](hit_or_miss_golay.md) performs the
hit-or-miss-transformation for the input regions *`Region`*
using all rotations of a structuring element from the Golay
alphabet. The result of the operator is the union of all
intermediate results of the respective rotations. The following
structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The Golay elements, together with all possible rotations, are
described with the operator [`golay_elements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`RegionHitMiss`** (output_object)  region(-array) `→` object

Result of the hit-or-miss operation.

**`GolayElement`** (input_control)  string `→`  (string)

Structuring element from the Golay alphabet.

Default:
'h'

List of values:
'c', 'd', 'e', 'f', 'f2', 'h', 'i', 'k', 'l', 'm'

## Complexity

Let F be the area of an input region, and R be the number of
rotations. Then the runtime complexity for one region is:
$$O(R \cdot 6 \cdot \sqrt{F})$$ ![figure](../assets/9239b9920d898617.svg)

## Result

`hit_or_miss_seq` returns 2 (
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

`hit_or_miss_golay`,
`hit_or_miss`

## See also

`thinning_seq`,
`thickening_seq`

## Module

Foundation
