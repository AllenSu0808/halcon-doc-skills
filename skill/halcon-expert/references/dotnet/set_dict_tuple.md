# SetDictTuple (Operator)

## Name

`SetDictTuple` — Add a key/tuple pair to the dictionary.

## Signature

`static void HOperatorSet.SetDictTuple(HTuple dictHandle, HTuple key, HTuple tuple)`

`void HDict.SetDictTuple(HTuple key, HTuple tuple)`

`void HDict.SetDictTuple(string key, HTuple tuple)`

## Description

`SetDictTuple` stores a tuple associated with a key in the
dictionary.
The dictionary is denoted by the *`dictHandle`* parameter.

*`tuple`* including strings is copied by the operation, and can
thus be immediately reused.
An empty tuple is considered as a valid value that can be associated with
the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `SetDictTuple`
and replaced by *`tuple`*.

The *`key`* has to be a string or an integer.
Strings are treated case sensitive.

The tuple data for the given key can be retrieved again from the dictionary
using [`GetDictTuple`](get_dict_tuple.md).

`SetDictTuple` allows setting the values of multiple keys with a
single call.
In this case, the length of *`tuple`* must either be equal to the
number of keys or *1*.
In the first case, *`tuple`* is split into
segments of length *1*, one for each key.
In the second case, if *`tuple`* has length *1*, that one
value is associated with each key.
If no keys are passed, the values in *`tuple`* are ignored.
The following table summarizes the possible combinations of
number of keys and values, where N is an arbitrary
non-negative integer:

| Length of *`key`* | Length of *`tuple`* | Effect |
| --- | --- | --- |
| N | 1 | Value in *`tuple`* is associated with all keys |
| 1 | N | Associate *`tuple`* with *`key`* |
| N | N | Associate tuples of length *1* with each passed key |

### HDevelop In-line Operation

HDevelop provides an in-line operation for `SetDictTuple`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`DictHandle.['Key'] := ['The answer', 42]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`DictHandle.Key := ['The answer', 42]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Attention

If the tuple contains any handles only the handle values are copied by the
operation, not the resources behind those handles (no deep copy is created).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dictHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`dictHandle`** (input_control, state is modified)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Key string.

**`tuple`** (input_control)  tuple-array `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Tuple value to be associated with the key.

## Example (HDevelop)

```
create_dict (Dict)
set_dict_tuple (Dict, 'simple_integer', 27)
set_dict_tuple (Dict, 'simple_string', 'Hello world')
set_dict_tuple (Dict, 'mixed_tuple', ['The answer', 42])
set_dict_tuple (Dict, 0, 'This is zero')
```

## Result

If the operation succeeds, `SetDictTuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`CreateDict`

## Possible Successors

`SetDictTuple`,
`SetDictObject`

## Alternatives

`SetDictObject`,
`SetDictTupleAt`

## See also

`CreateDict`,
`SetDictTupleAt`,
`GetDictTuple`,
`SetDictObject`,
`GetDictObject`,
`GetDictParam`,
`RemoveDictKey`

## Module

Foundation
