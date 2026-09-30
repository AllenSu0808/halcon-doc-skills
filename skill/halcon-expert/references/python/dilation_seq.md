# dilation_seq (Operator)

## Name

`dilation_seq` — Dilate a region sequentially.

## Warning

**`dilation_seq` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def dilation_seq(region: HObject, golay_element: str, iterations: int) -> HObject`

## Description

`dilation_seq` computes the sequential dilation of the
input region *`region`* with the selected structuring element
*`golay_element`* from the Golay alphabet. This is done by
executing the operator [`dilation_golay`](dilation_golay.md) with all rotations
of the structuring element *`iterations`* times. The
following structuring elements can be selected:

'l', 'd', 'c', 'f', 'h', 'k'.

In order to compute the skeleton of a region, usually the elements
'l' and 'm' are used. Only the “foreground elements” (even
rotation numbers) are used. The elements 'i' and 'e' result in
unchanged output regions. The elements 'l', 'm' and 'f2' are
identical for the foreground. The Golay elements, together with all
possible rotations, are described with the operator
[`golay_elements`](golay_elements.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be dilated.

**`region_dilation`** (output_object)  region(-array) `→` HObject

Dilated regions.

**`golay_element`** (input_control)  string `→` str

Structuring element from the Golay alphabet.

Default:
"h"

List of values:
"c", "d", "f", "h", "k", "l"

**`iterations`** (input_control)  integer `→` int

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

`dilation_seq` returns 2 (
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
`dilation_golay`

## See also

`erosion_seq`,
`hit_or_miss_seq`,
`thinning_seq`

## Module

Foundation
