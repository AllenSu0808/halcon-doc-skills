# get_handle_param (Operator)

## Name

`get_handle_param` — Return information about a handle.

## Signature

`get_handle_param( : : Handle, GenParamName, Key : GenParamValue)`

## Description

`get_handle_param` returns details about *`Handle`* in
*`GenParamValue`*.
It provides a generic mechanism for inspecting and debugging handles of any
type by returning keys of that handle that can later be queried using
[`get_handle_tuple`](get_handle_tuple.md) and [`get_handle_object`](get_handle_object.md).

Note that this operator is provided only for implementing generic
debug and inspection mechanisms.
The keys returned for certain handle types can change without notice.
Additionally, some handle types might not be supported by this operator.
Also, this operator is not optimized for performance.
To obtain more reliable information about a handle in a program, it is
strongly recommended to use the operators specialized for the particular
handle type, such as [`get_object_model_3d_params`](get_object_model_3d_params.md),
[`get_generic_shape_model_param`](get_generic_shape_model_param.md) etc.

Depending on
the value of *`GenParamName`*, the following values can be queried:

- ***'keys'*:** —

  Returns a list of keys that this handle supports in *`GenParamValue`*.
  Each key contains either a tuple or an iconic object.
  For this query, the parameter *`Key`* must be empty.
  Note that due to the generic nature of this operator, some of the returned
  keys might not be valid for the particular handle.
  In this case, [`get_handle_tuple`](get_handle_tuple.md) or [`get_handle_object`](get_handle_object.md) will
  return an error for those keys.
- ***'key_data_type'*:** —

  Returns the data type of *`Key`*.
  The type is returned in *`GenParamValue`* and is either *'tuple'*
  or *'object'*.
  Depending on the type, the key's corresponding value can be queried with
  [`get_handle_tuple`](get_handle_tuple.md) or [`get_handle_object`](get_handle_object.md), respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Handle`** (input_control)  handle `→`  (handle)

Handle of which to get the parameter.

**`GenParamName`** (input_control)  string `→`  (string)

Parameter to get.

Default:
'keys'

List of values:
'key_data_type', 'keys'

**`Key`** (input_control)  string(-array) `→`  (string)

Optional key.

Default:
[]

**`GenParamValue`** (output_control)  tuple(-array) `→`  (string / integer / real)

Returned value.

## Result

If the parameters are valid, the operator `get_handle_param`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`clear_handle`,
`get_handle_tuple`,
`get_handle_object`

## See also

`get_handle_tuple`,
`get_handle_object`

## Module

Foundation
