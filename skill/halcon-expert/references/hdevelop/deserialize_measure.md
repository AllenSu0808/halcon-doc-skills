# deserialize_measure (Operator)

## Name

`deserialize_measure` — Deserialize a serialized measure object.

## Signature

`deserialize_measure( : : SerializedItemHandle : MeasureHandle)`

## Description

`deserialize_measure` deserializes a measure object,
that was serialized by [`serialize_measure`](serialize_measure.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized measure object
is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
measure object with the handle *`MeasureHandle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`MeasureHandle`** (output_control)  measure `→`  (handle)

Measure object handle.

## Result

If the parameters are valid, the operator
`deserialize_measure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_measure`

## Possible Successors

`measure_pos`,
`measure_pairs`

## See also

`read_measure`,
`write_measure`

## Module

1D Metrology
