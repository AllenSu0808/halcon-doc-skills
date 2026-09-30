# SerializeMeasure (Operator)

## Name

`SerializeMeasure` — Serialize a measure object.

## Signature

`static void HOperatorSet.SerializeMeasure(HTuple measureHandle, out HTuple serializedItemHandle)`

`HSerializedItem HMeasure.SerializeMeasure()`

## Description

`SerializeMeasure` serializes the data of a measure object
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteMeasure`](write_measure.md) is converted to a serialized
item. The measure object is defined by the handle
*`measureHandle`*. The serialized measure object is returned
by the handle *`serializedItemHandle`* and can be
deserialized by [`DeserializeMeasure`](deserialize_measure.md).

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- measureHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`measureHandle`** (input_control, state is modified)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeMeasure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeMeasure`

## See also

`ReadMeasure`,
`WriteMeasure`

## Module

1D Metrology
