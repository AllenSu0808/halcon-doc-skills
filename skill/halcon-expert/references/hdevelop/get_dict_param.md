# get_dict_param (Operator)

## Name

`get_dict_param` — Query dictionary parameters or information about a dictionary.

## Signature

`get_dict_param( : : DictHandle, GenParamName, Key : GenParamValue)`

## Description

`get_dict_param` queries current values of dictionary
parameters or other information about the dictionary status.

With each call of `get_dict_param`, only a single parameter value
can be queried. However, there are two types of parameters/queries:

- Parameters/queries applicable to the entire dictionary. In this case
  no keys must be specified, the parameter *`Key`* must be an empty
  tuple.
- Parameters/queries applicable to the individual keys. In this case
  a list of keys must be specified in the parameter *`Key`*.
  The keys are processed in the same order as specified in the *`Key`*
  parameter.

Key-independent (global) parameter names:

- ***'keys'*:** —

  Queries all the keys stored in the dictionary, no matter whether they
  are associated with tuple or object data. The list of keys is reported
  as a string tuple via *`GenParamValue`*.
  For this query the parameter *`Key`* must be an empty tuple.

Currently supported key-specific parameter names are:

- ***'key_exists'*:** —

  Reports *1* if the given key is stored in the dictionary,
  *0* otherwise.
  The results are reported via *`GenParamValue`*, one value for
  each key.
- ***'key_data_type'*:** —

  Reports *'tuple'* for keys associated with tuple data within
  the dictionary (the data can be retrieved using [`get_dict_tuple`](get_dict_tuple.md)).
  Reports *'object'* for keys associated with object data
  (the data can be retrieved using [`get_dict_object`](get_dict_object.md)).
  The results are reported via *`GenParamValue`*, one value for
  each key. This parameter is useful to decide dynamically whether to use
  [`get_dict_tuple`](get_dict_tuple.md) or [`get_dict_object`](get_dict_object.md) to get the data of a
  specific key.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DictHandle`** (input_control)  dict `→`  (handle)

Dictionary handle.

Number of elements:
DictHandle == 1

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Names of the dictionary parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
'keys'

List of values:
'key_data_type', 'key_exists', 'keys'

**`Key`** (input_control)  string(-array) `→`  (string / integer)

Dictionary keys the parameter/query should be applied
to (empty for *`GenParamName`* = *'keys'*).

Default:
[]

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (string / integer / real)

Values of the dictionary parameters or info queries.

## Example (HDevelop)

```
get_dict_param (Dict, 'keys', [], AllKeys)
get_dict_param (Dict, 'key_data_type', AllKeys, KeysType)
```

## Result

If all the operator parameters, and the specified keys are valid,
`get_dict_param` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`create_dict`

## See also

`create_dict`,
`set_dict_tuple`,
`get_dict_tuple`,
`set_dict_object`,
`get_dict_object`,
`remove_dict_key`

## Module

Foundation
