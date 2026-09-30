# translate_measure (Operator)

## Name

`translate_measure` — Translate a measure object.

## Signature

`translate_measure( : : MeasureHandle, Row, Column : )`

## Description

`translate_measure` translates the reference point of the
measure object given by *`MeasureHandle`* to the point
(*`Row`*, *`Column`*). If the measure object and the
translated measure object lie completely within the image, the
measure object is shifted to the new reference point in an efficient
manner. Otherwise, the measure object is generated anew with
[`gen_measure_rectangle2`](gen_measure_rectangle2.md) or [`gen_measure_arc`](gen_measure_arc.md) using the
parameters that were specified when the measure object was created
and the new reference point.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MeasureHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MeasureHandle`** (input_control, state is modified)  measure `→`  (handle)

Measure object handle.

**`Row`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the new reference point.

Default:
50.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
Row
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Column`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the new reference point.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
Column
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Result

If the parameter values are correct the operator
`translate_measure` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`

## Possible Successors

`measure_pos`,
`measure_pairs`,
`fuzzy_measure_pos`,
`fuzzy_measure_pairs`,
`fuzzy_measure_pairing`,
`measure_thresh`

## Alternatives

`gen_measure_rectangle2`,
`gen_measure_arc`

## See also

`close_measure`

## Module

1D Metrology
