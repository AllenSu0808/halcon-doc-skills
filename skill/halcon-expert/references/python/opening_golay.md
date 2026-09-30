# opening_golay (Operator)

## Name

`opening_golay` — Open a region with an element from the Golay alphabet.

## Warning

**`opening_golay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def opening_golay(region: HObject, golay_element: str, rotation: int) -> HObject`

## Description

`opening_golay` is defined as a Minkowski subtraction
followed by a Minkowski addition. First the Minkowski subtraction
of the input region (*`region`*) with the structuring element
from the Golay alphabet defined by *`golay_element`* and
*`rotation`* is computed. Then the Minkowski addition of the
result and the structuring element rotated by 180 degrees
is performed.

The following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The rotation number *`rotation`* determines which rotation of
the element should be used, and whether the foreground (even) or
background version (odd) of the selected element should be used.
The Golay elements, together with all possible rotations, are
described with the operator [`golay_elements`](golay_elements.md).

`opening_golay` serves to eliminate regions smaller than
the structuring element, and to smooth regions' boundaries.

## Attention

Not all values of *`rotation`* are valid for any Golay
element. For some of the values of *`rotation`*, the
resulting regions are identical to the input regions.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be opened.

**`region_opening`** (output_object)  region(-array) `→` HObject

Opened regions.

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

`opening_golay` returns 2 (
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

`opening_seg`,
`opening`

## See also

`erosion_golay`,
`dilation_golay`,
`closing_golay`,
`hit_or_miss_golay`,
`thinning_golay`,
`thickening_golay`,
`golay_elements`

## Module

Foundation
