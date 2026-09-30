# DeserializeDistanceTransformXld (Operator)

## Name

`DeserializeDistanceTransformXld` — Deserialize an XLD distance transform.

## Signature

`static void HOperatorSet.DeserializeDistanceTransformXld(HTuple serializedItemHandle, out HTuple distanceTransformID)`

`void HXLDDistTrans.DeserializeDistanceTransformXld(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDistanceTransformXld` deserializes an XLD distance
transform. The serialized XLD distance transform is defined
by the handle *`serializedItemHandle`*.
The deserialized XLD distance transform is returned in
*`distanceTransformID`*.

Note that the previous values of
*`distanceTransformID`* are overwritten, if the handle already exists.

[`GetDistanceTransformXldContour`](get_distance_transform_xld_contour.md)
can be used to get the reference contour that was used
to build the XLD distance transform *`distanceTransformID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized XLD distance
transform.

**`distanceTransformID`** (output_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deserialized XLD distance
transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`ApplyDistanceTransformXld`,
`GetDistanceTransformXldContour`,
`GetDistanceTransformXldParam`

## See also

`SerializeDistanceTransformXld`,
`WriteDistanceTransformXld`,
`ReadDistanceTransformXld`,
`CreateDistanceTransformXld`,
`SetDistanceTransformXldParam`,
`ClearDistanceTransformXld`

## Module

Foundation
