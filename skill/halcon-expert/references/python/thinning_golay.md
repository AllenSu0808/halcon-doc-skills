# thinning_golay (Operator)

## Name

`thinning_golay` — Remove the result of a hit-or-miss operation from a region (using a
Golay structuring element).

## Warning

**`thinning_golay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def thinning_golay(region: HObject, golay_element: str, rotation: int) -> HObject`

## Description

`thinning_golay` performs a thinning of the input regions
using morphological operations and structuring elements from the
Golay alphabet. The operator first applies a
hit-or-miss-transformation to *`region`* (cf.
[`hit_or_miss_golay`](hit_or_miss_golay.md)), and then removes the detected points
from the input region. The following structuring elements are
available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The rotation number *`rotation`* determines which rotation of
the element should be used. The Golay elements, together with all
possible rotations, are described with the operator
[`golay_elements`](golay_elements.md).

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

**`region_thin`** (output_object)  region(-array) `→` HObject

Result of the thinning operator.

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

`thinning_golay` returns 2 (
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

`thinning_seq`,
`thinning`

## See also

`erosion_golay`,
`hit_or_miss_golay`

## Module

Foundation
