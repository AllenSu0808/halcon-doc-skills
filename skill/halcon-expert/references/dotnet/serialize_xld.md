# SerializeXld (Operator)

## Name

`SerializeXld` — Serialize an XLD object.

## Signature

`static void HOperatorSet.SerializeXld(HObject XLD, out HTuple serializedItemHandle)`

`HSerializedItem HXLD.SerializeXld()`

`HSerializedItem HXLDCont.SerializeXld()`

`HSerializedItem HXLDPoly.SerializeXld()`

`HSerializedItem HXLDPara.SerializeXld()`

`HSerializedItem HXLDModPara.SerializeXld()`

`HSerializedItem HXLDExtPara.SerializeXld()`

## Description

`SerializeXld` serializes an XLD object (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The XLD object is defined by the parameter
*`XLD`*. The serialized XLD object is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeXld`](deserialize_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

XLD object.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeXld` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GenContourPolygonXld`,
`GenParallelsXld`,
`GenPolygonsXld`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeXld`

## See also

`DeserializeXld`

## Module

Foundation
