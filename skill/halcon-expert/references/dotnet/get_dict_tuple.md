# GetDictTuple (Operator)

## Name

`GetDictTuple` — Retrieve a tuple associated with the key from the dictionary.

## Signature

`static void HOperatorSet.GetDictTuple(HTuple dictHandle, HTuple key, out HTuple tuple)`

`HTuple HDict.GetDictTuple(HTuple key)`

`HTuple HDict.GetDictTuple(string key)`

## Description

`GetDictTuple` retrieves a tuple associated with the *`key`*
from the dictionary denoted by the *`dictHandle`*.
The tuple has to be previously stored to the dictionary using
[`SetDictTuple`](set_dict_tuple.md).

The operator returns the data in the parameter *`tuple`*.
The data including strings is copied by the operation, the dictionary can
thus be immediately reused.

If the given *`key`* is not present in the dictionary or if the data
associated with the key is not a tuple, `GetDictTuple` fails.
Presence of keys and information about the data associated with the key
can be verified using [`GetDictParam`](get_dict_param.md).

Obtaining the values for multiple keys at once is only possible if for each
of those keys, the dictionary contains a tuple with a single element.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `GetDictTuple`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`Tuple := DictHandle.['Key']`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`Tuple := DictHandle.Key`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dictHandle`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Key string.

**`tuple`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Tuple value retrieved from the dictionary.

## Example (HDevelop)

```
* ...
get_dict_param (Dict, 'key_exists', ['simple_string','foo','my_image'], \
                KeysPresence)
get_dict_param (Dict, 'key_data_type', ['simple_string','my_image'], \
                KeysType)
get_dict_tuple (Dict, 'simple_string', TupleString)
*
* Access multiple keys, if their tuple all have length 1
get_dict_tuple (Dict, ['key1','key2','key3'], MultipleValues)
```

## Result

If the operation succeeds, `GetDictTuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
dictionary, or other than tuple data associated with given key.

## Possible Predecessors

`SetDictTuple`

## Possible Successors

`GetDictTuple`,
`SetDictTuple`,
`SetDictTupleAt`

## Alternatives

`GetDictObject`

## See also

`CreateDict`,
`SetDictTuple`,
`SetDictObject`,
`GetDictObject`,
`RemoveDictKey`,
`GetDictParam`

## Module

Foundation
