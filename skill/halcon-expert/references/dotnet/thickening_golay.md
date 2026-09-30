# ThickeningGolay (Operator)

## Name

`ThickeningGolay` — Add the result of a hit-or-miss operation to a region (using a Golay
structuring element).

## Warning

**`ThickeningGolay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ThickeningGolay(HObject region, out HObject regionThick, HTuple golayElement, HTuple rotation)`

`HRegion HRegion.ThickeningGolay(string golayElement, int rotation)`

## Description

`ThickeningGolay` performs a thickening of the input
regions using morphological operations and structuring elements from
the Golay alphabet. The operator first applies a
hit-or-miss-transformation to *`region`* (cf.
[`HitOrMissGolay`](hit_or_miss_golay.md)), and then adds the detected points to
the input region. The following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The rotation number *`rotation`* determines which rotation of
the element should be used. The Golay elements, together with all
possible rotations, are described with the operator
[`GolayElements`](golay_elements.md).

## Attention

Not all values of *`rotation`* are valid for any Golay
element.

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

**`rotation`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

`ThickeningGolay` returns 2 (
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

`Thickening`,
`ThickeningSeq`

## See also

`ErosionGolay`,
`HitOrMissGolay`

## Module

Foundation
