# SetDistanceTransformXldParam (Operator)

## Name

`SetDistanceTransformXldParam` — Set new parameters for an XLD distance transform.

## Signature

`static void HOperatorSet.SetDistanceTransformXldParam(HTuple distanceTransformID, HTuple genParamName, HTuple genParamValue)`

`void HXLDDistTrans.SetDistanceTransformXldParam(HTuple genParamName, HTuple genParamValue)`

`void HXLDDistTrans.SetDistanceTransformXldParam(string genParamName, string genParamValue)`

## Description

`SetDistanceTransformXldParam` sets new parameters for the
XLD distance transform *`distanceTransformID`*.
The names and values of the parameters are passed in *`genParamName`*
and *`genParamValue`*, respectively. *`genParamName`* can contain
the names of parameters *"mode"* and *"max_distance"*.
The XLD distance transform of the original reference contour is then
rebuilt with updated values of parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- distanceTransformID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`distanceTransformID`** (input_control, state is modified)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"mode"

List of values:
"max_distance", "mode"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double)

Values of the generic parameters.

Default:
"point_to_point"

Suggested values:
"point_to_point", "point_to_segment", 5.0

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`GetDistanceTransformXldParam`

## Possible Successors

`ApplyDistanceTransformXld`

## See also

`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`,
`GetDistanceTransformXldContour`,
`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`,
`ClearDistanceTransformXld`

## Module

Foundation
