# SetDictObject (Operator)

## Name

`SetDictObject` — Add a key/object pair to the dictionary.

## Signature

`static void HOperatorSet.SetDictObject(HObject objectVal, HTuple dictHandle, HTuple key)`

`void HDict.SetDictObject(HObject objectVal, HTuple key)`

`void HDict.SetDictObject(HObject objectVal, string key)`

## Description

`SetDictObject` stores an object associated with a key in the
dictionary.
The dictionary is denoted by the *`dictHandle`* parameter.

*`objectVal`* is copied by the operation and can thus be
immediately reused.
Thereby the object data is copied in HALCON's object database,
meaning the new object contains a reference to *`objectVal`*,
see [`CopyObj`](copy_obj.md).

Both an empty object or an object tuple are considered
as a valid value that can be associated with the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `SetDictObject`
and replaced by *`objectVal`*.

The *`key`* has to be a string or an integer.
Strings are treated case sensitive.

The object data for the given key can be retrieved again from the dictionary
using [`GetDictObject`](get_dict_object.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `SetDictObject`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`DictHandle.['Key'] := Object`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`DictHandle.Key := Object`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dictHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`objectVal`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object to be associated with the key.

**`dictHandle`** (input_control, state is modified)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

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
create_dict (Dict)
read_image (Image, 'filename')
set_dict_object (Image, Dict, 'my_image')
```

## Result

If the operation succeeds, `SetDictObject` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`CreateDict`

## Possible Successors

`SetDictObject`,
`SetDictTuple`

## Alternatives

`SetDictTuple`

## See also

`CreateDict`,
`SetDictTuple`,
`GetDictTuple`,
`GetDictObject`,
`RemoveDictKey`,
`GetDictParam`

## Module

Foundation
