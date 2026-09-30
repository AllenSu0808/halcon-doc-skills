# deserialize_xld (Operator)

## Name

`deserialize_xld` — Deserialize a serialized XLD object.

## Signature

`deserialize_xld( : XLD : SerializedItemHandle : )`

## Description

`deserialize_xld` deserializes an XLD object, that was serialized
by [`serialize_xld`](serialize_xld.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized XLD object is defined by the parameter
*`SerializedItemHandle`*. The deserialized XLD object is stored
in the XLD object defined by the parameter *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (output_object)  xld(-array) `→` object

XLD object.

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`deserialize_xld` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`fread_serialized_item`,
`receive_serialized_item`,
`serialize_xld`

## Possible Successors

`clip_contours_xld`,
`split_contours_xld`

## See also

`serialize_xld`

## Module

Foundation
