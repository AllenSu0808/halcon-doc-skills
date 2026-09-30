# hamming_change_region (Operator)

## Name

`hamming_change_region` — Generate a region having a given Hamming distance.

## Warning

**`hamming_change_region` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`hamming_change_region(InputRegion : OutputRegion : Width, Height, Distance : )`

## Description

`hamming_change_region` changes the region in the left
upper part of the image given by *`Width`* and
*`Height`* such that the resulting regions have a Hamming
distance of *`Distance`* to the input regions. This is done
by adding or removing *`Distance`* points from the input
region.

## Attention

If *`Width`* and *`Height`* are chosen too large the
resulting region requires a lot of memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`InputRegion`** (input_object)  region(-array) `→` object

Region to be modified.

**`OutputRegion`** (output_object)  region(-array) `→` object

Regions having the required Hamming distance.

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the region to be changed.

Default:
100

Suggested values:
64, 128, 256, 512

Value range:
`1
≤
Width
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Width > 0`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the region to be changed.

Default:
100

Suggested values:
64, 128, 256, 512

Value range:
`1
≤
Height
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Height > 0`

**`Distance`** (input_control)  integer `→`  (integer)

Hamming distance between the old and new regions.

Default:
1000

Suggested values:
100, 500, 1000, 5000, 10000

Value range:
`0
≤
Distance
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
O(2 * *`Width`* * *`Height`*).

## Result

`hamming_change_region` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`connection`,
`regiongrowing`,
`pouring`,
`class_ndim_norm`

## Possible Successors

`select_shape`

## See also

`hamming_distance`

## Module

Foundation
