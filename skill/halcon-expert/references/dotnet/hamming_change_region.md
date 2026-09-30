# HammingChangeRegion (Operator)

## Name

`HammingChangeRegion` — Generate a region having a given Hamming distance.

## Warning

**`HammingChangeRegion` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.HammingChangeRegion(HObject inputRegion, out HObject outputRegion, HTuple width, HTuple height, HTuple distance)`

`HRegion HRegion.HammingChangeRegion(int width, int height, int distance)`

## Description

`HammingChangeRegion` changes the region in the left
upper part of the image given by *`width`* and
*`height`* such that the resulting regions have a Hamming
distance of *`distance`* to the input regions. This is done
by adding or removing *`distance`* points from the input
region.

## Attention

If *`width`* and *`height`* are chosen too large the
resulting region requires a lot of memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`inputRegion`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be modified.

**`outputRegion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Regions having the required Hamming distance.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the region to be changed.

Default:
100

Suggested values:
64, 128, 256, 512

Value range:
`1
≤
width
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Width > 0`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the region to be changed.

Default:
100

Suggested values:
64, 128, 256, 512

Value range:
`1
≤
height
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Height > 0`

**`distance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Hamming distance between the old and new regions.

Default:
1000

Suggested values:
100, 500, 1000, 5000, 10000

Value range:
`0
≤
distance
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Distance >= 0 && Distance < Width * Height`

## Complexity

Memory requirement of the generated region (worst case):
O(2 * *`width`* * *`height`*).

## Result

`HammingChangeRegion` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`

## See also

`HammingDistance`

## Module

Foundation
