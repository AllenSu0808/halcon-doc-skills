# SerializeRegion (Operator)

## Name

`SerializeRegion` — Serialize a region.

## Signature

`static void HOperatorSet.SerializeRegion(HObject region, out HTuple serializedItemHandle)`

`HSerializedItem HRegion.SerializeRegion()`

## Description

`SerializeRegion` serializes a region (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The region is defined by the parameter
*`region`*. The serialized region is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeRegion`](deserialize_region.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeRegion` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`ReadRegion`,
`Threshold`,
`Regiongrowing`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeRegion`

## See also

`DeserializeRegion`

## Module

Foundation
