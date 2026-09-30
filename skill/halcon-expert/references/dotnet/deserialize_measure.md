# DeserializeMeasure (Operator)

## Name

`DeserializeMeasure` — Deserialize a serialized measure object.

## Signature

`static void HOperatorSet.DeserializeMeasure(HTuple serializedItemHandle, out HTuple measureHandle)`

`void HMeasure.DeserializeMeasure(HSerializedItem serializedItemHandle)`

## Description

`DeserializeMeasure` deserializes a measure object,
that was serialized by [`SerializeMeasure`](serialize_measure.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized measure object
is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
measure object with the handle *`measureHandle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`measureHandle`** (output_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

## Result

If the parameters are valid, the operator
`DeserializeMeasure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeMeasure`

## Possible Successors

`MeasurePos`,
`MeasurePairs`

## See also

`ReadMeasure`,
`WriteMeasure`

## Module

1D Metrology
