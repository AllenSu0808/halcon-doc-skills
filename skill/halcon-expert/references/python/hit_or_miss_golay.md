# hit_or_miss_golay (Operator)

## Name

`hit_or_miss_golay` — Hit-or-miss operation for regions using the Golay alphabet.

## Warning

**`hit_or_miss_golay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def hit_or_miss_golay(region: HObject, golay_element: str, rotation: int) -> HObject`

## Description

`hit_or_miss_golay` performs the
hit-or-miss-transformation for the input regions *`region`*
(using structuring elements from the Golay alphabet). First, an
erosion with the foreground of the structuring element
*`golay_element`* is done on the input region
*`region`*. Then an erosion with the background of the
structuring element *`golay_element`* is performed on the
complement of the input region. The intersection of the two
resulting regions is the result *`region_hit_miss`* of
`hit_or_miss_golay`. The following structuring elements
are available:

'l', 'm', 'd', 'c', 'e','i', 'f', 'f2', 'h', 'k'.

The rotation number *`rotation`* determines which rotation of
the element should be used. The hit-or-miss-transformation selects
precisely the points for which the conditions given by the selected
Golay element are fulfilled.

## Attention

Not all values of *`rotation`* are valid for any Golay
element.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be processed.

**`region_hit_miss`** (output_object)  region(-array) `→` HObject

Result of the hit-or-miss operation.

**`golay_element`** (input_control)  string `→` str

Structuring element from the Golay alphabet.

Default:
"h"

List of values:
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

**`rotation`** (input_control)  integer `→` int

Rotation of the Golay element. Depending on the
element, not all rotations are valid.

Default:
0

List of values:
0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15

## Complexity

Let F be the area of an input region. Then the runtime complexity for one
region is:
$$O(6\cdot \sqrt{F}) .$$ ![figure](../assets/566293828579d365.svg)

## Result

`hit_or_miss_golay` returns 2 (
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

`hit_or_miss_seq`,
`hit_or_miss`

## See also

`erosion_golay`,
`dilation_golay`,
`opening_golay`,
`closing_golay`,
`thinning_golay`,
`thickening_golay`,
`golay_elements`

## Module

Foundation
