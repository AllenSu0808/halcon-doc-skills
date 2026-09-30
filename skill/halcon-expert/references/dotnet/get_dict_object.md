# GetDictObject (Operator)

## Name

`GetDictObject` — Retrieve an object associated with the key from the dictionary.

## Signature

`static void HOperatorSet.GetDictObject(out HObject objectVal, HTuple dictHandle, HTuple key)`

`HObject HDict.GetDictObject(HTuple key)`

`HObject HDict.GetDictObject(string key)`

## Description

`GetDictObject` retrieves an object associated with the *`key`*
from the dictionary denoted by the *`dictHandle`*.
The object has to be previously stored to the dictionary using
[`SetDictObject`](set_dict_object.md).

The operator returns the data in the parameter *`objectVal`*. The
iconic object is copied by the operation. Therefore, clearing or reusing
the dictionary object afterwards will not have any side-effect on the
returned iconic object.

If the given *`key`* is not present in the dictionary or if the data
associated with the key is not an object, `GetDictObject` fails.
Presence of keys and information about the data associated with the key can
be verified using [`GetDictParam`](get_dict_param.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `GetDictObject`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`Object := DictHandle.['Key']`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`Object := DictHandle.Key`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Object value retrieved from the dictionary.

**`dictHandle`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key string.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

## Example (HDevelop)

```
* ...
get_dict_param (Dict, 'key_exists', ['simple_string','foo','my_image'], \
                KeysPresence)
get_dict_param (Dict, 'key_data_type', ['simple_string','my_image'], \
                KeysType)
get_dict_object (Image, Dict, 'my_image')
```

## Result

If the operation succeeds, `GetDictObject` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
dictionary or other than object data associated with given key.

## Possible Predecessors

`SetDictObject`

## Possible Successors

`GetDictObject`

## Alternatives

`GetDictTuple`

## See also

`CreateDict`,
`SetDictTuple`,
`GetDictTuple`,
`SetDictObject`,
`RemoveDictKey`,
`GetDictParam`

## Module

Foundation
