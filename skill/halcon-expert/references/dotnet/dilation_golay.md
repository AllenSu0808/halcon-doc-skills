# DilationGolay (Operator)

## Name

`DilationGolay` — Dilate a region with an element from the Golay alphabet.

## Warning

**`DilationGolay` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.DilationGolay(HObject region, out HObject regionDilation, HTuple golayElement, HTuple iterations, HTuple rotation)`

`HRegion HRegion.DilationGolay(string golayElement, int iterations, int rotation)`

## Description

`DilationGolay` dilates a region with the selected
element *`golayElement`* from the Golay alphabet. The
following structuring elements are available:

'l', 'm', 'd', 'c', 'e', 'i', 'f', 'f2', 'h', 'k'.

The rotation number *`rotation`* determines which rotation of
the element should be used, and whether the foreground (even) or
background version (odd) of the selected element should be used.
The Golay elements, together with all possible rotations, are
described with the operator [`GolayElements`](golay_elements.md). The
operator works by shifting the structuring element over the region
to be processed (*`region`*). For all positions of the
structuring element that intersect the region, the corresponding
reference point (relative to the structuring element) is added to
the output region. This means that the union of all translations of
the structuring element within the region is computed.

The parameter *`iterations`* determines the number of
iterations which are to be performed with the structuring element.
The result of iteration n-1 is used as input for iteration n.

## Attention

Not all values of *`rotation`* are valid for any Golay
element. For some of the values of *`rotation`*, the
resulting regions are identical to the input regions.

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
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

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
$$O(3\cdot \sqrt{F}) .$$ ![figure](../assets/002835c365864fd9.svg)

## Result

`DilationGolay` returns 2 (
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
`DilationSeq`

## See also

`ErosionGolay`,
`OpeningGolay`,
`ClosingGolay`,
`HitOrMissGolay`,
`ThinningGolay`,
`ThickeningGolay`,
`GolayElements`

## Module

Foundation
