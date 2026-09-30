# gen_region_runs (Operator)

## Name

`gen_region_runs` — Create a region from a runlength coding.

## Signature

`gen_region_runs( : Region : Row, ColumnBegin, ColumnEnd : )`

## Description

The operator `gen_region_runs` creates a region described by the input
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
*`ColumnEnd`* >= *`ColumnBegin`* is fulfilled. Note that
if this restriction is violated, subsequent operations will likely
lead to errors or unexpected behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Region`** (output_object)  region `→` object

Created region.

**`Row`** (input_control)  chord.y(-array) `→`  (integer)

Lines of the runs.

Default:
100

Suggested values:
0, 50, 100, 200, 300, 500

Value range:
`Row` (lin)

Minimum increment:
1

Recommended increment:
10

**`ColumnBegin`** (input_control)  chord.x1(-array) `→`  (integer)

Columns of the starting points of the runs.

Number of elements:
ColumnBegin == Row

Default:
50

Suggested values:
0, 50, 100, 200, 300, 500

Value range:
`ColumnBegin` (lin)

Minimum increment:
1

Recommended increment:
10

**`ColumnEnd`** (input_control)  chord.x2(-array) `→`  (integer)

Columns of the ending points of the runs.

Number of elements:
ColumnEnd == Row

Default:
200

Suggested values:
50, 100, 200, 300, 500

Value range:
`ColumnEnd` (lin)

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

If the data is correct the operator `gen_region_runs` returns the value
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

`get_region_runs`

## Alternatives

`gen_region_points`,
`gen_region_polygon`,
`gen_region_line`,
`gen_region_polygon_filled`

## See also

`reduce_domain`

## Module

Foundation
