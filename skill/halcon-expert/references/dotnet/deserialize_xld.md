# DeserializeXld (Operator)

## Name

`DeserializeXld` — Deserialize a serialized XLD object.

## Signature

`static void HOperatorSet.DeserializeXld(out HObject XLD, HTuple serializedItemHandle)`

`void HXLD.DeserializeXld(HSerializedItem serializedItemHandle)`

`void HXLDCont.DeserializeXld(HSerializedItem serializedItemHandle)`

`void HXLDPoly.DeserializeXld(HSerializedItem serializedItemHandle)`

`void HXLDPara.DeserializeXld(HSerializedItem serializedItemHandle)`

`void HXLDModPara.DeserializeXld(HSerializedItem serializedItemHandle)`

`void HXLDExtPara.DeserializeXld(HSerializedItem serializedItemHandle)`

## Description

`DeserializeXld` deserializes an XLD object, that was serialized
by [`SerializeXld`](serialize_xld.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized XLD object is defined by the parameter
*`serializedItemHandle`*. The deserialized XLD object is stored
in the XLD object defined by the parameter *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (output_object)  xld(-array) `→` [HXLD](HXLD.md)

XLD object.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`DeserializeXld` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeXld`

## Possible Successors

`ClipContoursXld`,
`SplitContoursXld`

## See also

`SerializeXld`

## Module

Foundation
