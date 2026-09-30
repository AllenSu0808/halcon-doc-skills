# WriteDistanceTransformXld (Operator)

## Name

`WriteDistanceTransformXld` — Write an XLD distance transform into a file.

## Signature

`static void HOperatorSet.WriteDistanceTransformXld(HTuple distanceTransformID, HTuple fileName)`

`void HXLDDistTrans.WriteDistanceTransformXld(string fileName)`

## Description

`WriteDistanceTransformXld` writes the XLD distance transform
*`distanceTransformID`* into the file given by *`fileName`*.
The default HALCON extension for the XLD distance transform is 'hdtc'.

The stored XLD distance transform can be read in with
[`ReadDistanceTransformXld`](read_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`distanceTransformID`** (input_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file.

File extension:
.`hdtc`

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`CreateDistanceTransformXld`

## Possible Successors

`ClearDistanceTransformXld`

## Alternatives

`SerializeDistanceTransformXld`

## See also

`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`,
`GetDistanceTransformXldContour`,
`ApplyDistanceTransformXld`,
`GetDistanceTransformXldParam`,
`SetDistanceTransformXldParam`

## Module

Foundation
