# ReadDistanceTransformXld (Operator)

## Name

`ReadDistanceTransformXld` — Read an XLD distance transform from a file.

## Signature

`static void HOperatorSet.ReadDistanceTransformXld(HTuple fileName, out HTuple distanceTransformID)`

`public HXLDDistTrans(string fileName)`

`void HXLDDistTrans.ReadDistanceTransformXld(string fileName)`

## Description

`ReadDistanceTransformXld` reads an XLD distance transform
which previously has been stored with
[`WriteDistanceTransformXld`](write_distance_transform_xld.md) from the file given by
*`fileName`* and returns the handle *`distanceTransformID`*.
The default HALCON extension for the XLD distance
transform is 'hdtc'.

[`GetDistanceTransformXldContour`](get_distance_transform_xld_contour.md)
can be used to get the reference contour that was used
to build the XLD distance transform *`distanceTransformID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file.

File extension:
.`hdtc`

**`distanceTransformID`** (output_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

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

`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`,
`DeserializeDistanceTransformXld`,
`CreateDistanceTransformXld`,
`SetDistanceTransformXldParam`,
`ClearDistanceTransformXld`

## Module

Foundation
