# GetHandleParam (Operator)

## Name

`GetHandleParam` — Return information about a handle.

## Signature

`static void HOperatorSet.GetHandleParam(HTuple handle, HTuple genParamName, HTuple key, out HTuple genParamValue)`

## Description

`GetHandleParam` returns details about *`handle`* in
*`genParamValue`*.
It provides a generic mechanism for inspecting and debugging handles of any
type by returning keys of that handle that can later be queried using
[`GetHandleTuple`](get_handle_tuple.md) and [`GetHandleObject`](get_handle_object.md).

Note that this operator is provided only for implementing generic
debug and inspection mechanisms.
The keys returned for certain handle types can change without notice.
Additionally, some handle types might not be supported by this operator.
Also, this operator is not optimized for performance.
To obtain more reliable information about a handle in a program, it is
strongly recommended to use the operators specialized for the particular
handle type, such as [`GetObjectModel3dParams`](get_object_model_3d_params.md),
[`GetGenericShapeModelParam`](get_generic_shape_model_param.md) etc.

Depending on
the value of *`genParamName`*, the following values can be queried:

- ***"keys"*:** —

  Returns a list of keys that this handle supports in *`genParamValue`*.
  Each key contains either a tuple or an iconic object.
  For this query, the parameter *`key`* must be empty.
  Note that due to the generic nature of this operator, some of the returned
  keys might not be valid for the particular handle.
  In this case, [`GetHandleTuple`](get_handle_tuple.md) or [`GetHandleObject`](get_handle_object.md) will
  return an error for those keys.
- ***"key_data_type"*:** —

  Returns the data type of *`key`*.
  The type is returned in *`genParamValue`* and is either *"tuple"*
  or *"object"*.
  Depending on the type, the key's corresponding value can be queried with
  [`GetHandleTuple`](get_handle_tuple.md) or [`GetHandleObject`](get_handle_object.md), respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  handle `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of which to get the parameter.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Parameter to get.

Default:
"keys"

List of values:
"key_data_type", "keys"

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Optional key.

Default:
[]

**`genParamValue`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Returned value.

## Result

If the parameters are valid, the operator `GetHandleParam`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`ClearHandle`,
`GetHandleTuple`,
`GetHandleObject`

## See also

`GetHandleTuple`,
`GetHandleObject`

## Module

Foundation
