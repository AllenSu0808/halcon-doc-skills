# GenRegionRuns (Operator)

## Name

`GenRegionRuns` — Create a region from a runlength coding.

## Signature

`static void HOperatorSet.GenRegionRuns(out HObject region, HTuple row, HTuple columnBegin, HTuple columnEnd)`

`void HRegion.GenRegionRuns(HTuple row, HTuple columnBegin, HTuple columnEnd)`

`void HRegion.GenRegionRuns(int row, int columnBegin, int columnEnd)`

## Description

The operator `GenRegionRuns` creates a region described by the input
runlength structure. The runlength representation is created by examining
a region line by line with ascending line number (= from “top” to
“bottom”). Every line runs through from left to right
(ascending column number). All starting and ending points being stored
by region segments (=runs). Thus a region can be described
by a sequence of runs, a run being defined by line number
as well as starting and ending points (column number).

The storing is fastest when the runs are sorted.
The order is as follows:

$$(l_{1},b_{1},e_{1})\le(l_{2},b_{2},e_{2}):=(l_{1}<l_{2})\vee(l_{1}=l_{2})\wedge(b_{1}\le b_{2})$$.

## Attention

For runtime reasons, it is not checked whether the restriction
*`columnEnd`* >= *`columnBegin`* is fulfilled. Note that
if this restriction is violated, subsequent operations will likely
lead to errors or unexpected behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Created region.

**`row`** (input_control)  chord.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Lines of the runs.

Default:
100

Suggested values:
0, 50, 100, 200, 300, 500

Value range:
`row` (lin)

Minimum increment:
1

Recommended increment:
10

**`columnBegin`** (input_control)  chord.x1(-array) `→` [HTuple](HTuple.md) (*int* / long)

Columns of the starting points of the runs.

Number of elements:
ColumnBegin == Row

Default:
50

Suggested values:
0, 50, 100, 200, 300, 500

Value range:
`columnBegin` (lin)

Minimum increment:
1

Recommended increment:
10

**`columnEnd`** (input_control)  chord.x2(-array) `→` [HTuple](HTuple.md) (*int* / long)

Columns of the ending points of the runs.

Number of elements:
ColumnEnd == Row

Default:
200

Suggested values:
50, 100, 200, 300, 500

Value range:
`columnEnd` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`ColumnEnd >= ColumnBegin`

## Complexity

F shall be the number of pixels. If the pixels are sorted in ascending
order the runtime complexity is: O(F), otherwise it is O(log(F)*F).

## Result

If the data is correct the operator `GenRegionRuns` returns the value
2 (
H_MSG_TRUE)
, otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
If an empty region is created (by the clipping or by an empty input)
the operator
`set_system('store_empty_region',<'true'/'false'>)` determines
whether the region is returned or an empty object tuple.

## Possible Predecessors

`GetRegionRuns`

## Alternatives

`GenRegionPoints`,
`GenRegionPolygon`,
`GenRegionLine`,
`GenRegionPolygonFilled`

## See also

`ReduceDomain`

## Module

Foundation
