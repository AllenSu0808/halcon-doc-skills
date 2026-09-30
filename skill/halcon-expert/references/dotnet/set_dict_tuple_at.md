# SetDictTupleAt (Operator)

## Name

`SetDictTupleAt` — Assignment of one or several values to one or several tuple elements
in a dictionary

## Signature

`static void HOperatorSet.SetDictTupleAt(HTuple dictHandle, HTuple key, HTuple index, HTuple value)`

`void HDict.SetDictTupleAt(HTuple key, HTuple index, HTuple value)`

`void HDict.SetDictTupleAt(string key, HTuple index, HTuple value)`

## Description

`SetDictTupleAt` assigns a single value to one or several
elements of a tuple, or it assigns a number of values elementwise to the
specified elements of a tuple that is stored in *`dictHandle`*
under the key *`key`*.
The operator allows to efficiently replace parts of a tuple stored
in a dictionary without first reading the previous values from the
dictionary.

If the dictionary does not yet contain a tuple under the given key,
or if the given key maps to an iconic value, a new tuple is created
and stored under the given key. In the latter case, the iconic
object previously stored under that key is removed from the dictionary.

If the passed indices are out of the current range of the tuple stored
in the dictionary, the tuple length is increased and the new values are
initialized to a default value.

The *`key`* has to be a string or an integer.
Strings are treated case sensitive.
The *`index`* parameter can be any expression that evaluates to any
number of positive integer values.
The *`value`* parameter must evaluate to exactly one value or to
the same number of indices that are provided via the *`index`*
parameter.:

The tuple data for the given key can be retrieved again from the dictionary
using [`GetDictTuple`](get_dict_tuple.md).

## Attention

Note that if *`value`* contains any handles, only the handle values
are copied by the operation, not the resources behind those handles.

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

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key string.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

**`index`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the elements that have to be replaced by the new
value(s).

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6

Minimum increment:
1

**`value`** (input_control)  tuple-array `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Value(s) that is to be assigned.

## Example (HDevelop)

```
Dict := dict{}
Dict.some_key := 27

set_dict_tuple_at (Dict, 'some_key', 1, 5)
* Dict.some_key is now [27, 5]

* Alternative TRIAS syntax
Dict.some_key[0] := 66
* Dict.some_key is now [66, 5]
```

## Result

If the operation succeeds, `SetDictTupleAt` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters or resource allocation error.

## Possible Predecessors

`CreateDict`

## Possible Successors

`SetDictTuple`,
`GetDictTuple`

## Alternatives

`SetDictTuple`

## See also

`CreateDict`,
`SetDictTuple`,
`GetDictTuple`,
`SetDictObject`,
`GetDictObject`,
`GetDictParam`,
`RemoveDictKey`

## Module

Foundation
