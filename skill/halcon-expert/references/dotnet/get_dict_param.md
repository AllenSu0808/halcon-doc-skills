# GetDictParam (Operator)

## Name

`GetDictParam` — Query dictionary parameters or information about a dictionary.

## Signature

`static void HOperatorSet.GetDictParam(HTuple dictHandle, HTuple genParamName, HTuple key, out HTuple genParamValue)`

`HTuple HDict.GetDictParam(string genParamName, HTuple key)`

`HTuple HDict.GetDictParam(string genParamName, string key)`

## Description

`GetDictParam` queries current values of dictionary
parameters or other information about the dictionary status.

With each call of `GetDictParam`, only a single parameter value
can be queried. However, there are two types of parameters/queries:

- Parameters/queries applicable to the entire dictionary. In this case
  no keys must be specified, the parameter *`key`* must be an empty
  tuple.
- Parameters/queries applicable to the individual keys. In this case
  a list of keys must be specified in the parameter *`key`*.
  The keys are processed in the same order as specified in the *`key`*
  parameter.

Key-independent (global) parameter names:

- ***"keys"*:** —

  Queries all the keys stored in the dictionary, no matter whether they
  are associated with tuple or object data. The list of keys is reported
  as a string tuple via *`genParamValue`*.
  For this query the parameter *`key`* must be an empty tuple.

Currently supported key-specific parameter names are:

- ***"key_exists"*:** —

  Reports *1* if the given key is stored in the dictionary,
  *0* otherwise.
  The results are reported via *`genParamValue`*, one value for
  each key.
- ***"key_data_type"*:** —

  Reports *"tuple"* for keys associated with tuple data within
  the dictionary (the data can be retrieved using [`GetDictTuple`](get_dict_tuple.md)).
  Reports *"object"* for keys associated with object data
  (the data can be retrieved using [`GetDictObject`](get_dict_object.md)).
  The results are reported via *`genParamValue`*, one value for
  each key. This parameter is useful to decide dynamically whether to use
  [`GetDictTuple`](get_dict_tuple.md) or [`GetDictObject`](get_dict_object.md) to get the data of a
  specific key.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dictHandle`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Names of the dictionary parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
"keys"

List of values:
"key_data_type", "key_exists", "keys"

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Dictionary keys the parameter/query should be applied
to (empty for *`genParamName`* = *"keys"*).

Default:
[]

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the dictionary parameters or info queries.

## Example (HDevelop)

```
get_dict_param (Dict, 'keys', [], AllKeys)
get_dict_param (Dict, 'key_data_type', AllKeys, KeysType)
```

## Result

If all the operator parameters, and the specified keys are valid,
`GetDictParam` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`CreateDict`

## See also

`CreateDict`,
`SetDictTuple`,
`GetDictTuple`,
`SetDictObject`,
`GetDictObject`,
`RemoveDictKey`

## Module

Foundation
