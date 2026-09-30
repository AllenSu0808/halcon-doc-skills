# RemoveDictKey (Operator)

## Name

`RemoveDictKey` — Remove keys from a dictionary.

## Signature

`static void HOperatorSet.RemoveDictKey(HTuple dictHandle, HTuple key)`

`void HDict.RemoveDictKey(HTuple key)`

`void HDict.RemoveDictKey(string key)`

## Description

`RemoveDictKey` removes the keys specified in *`key`* from
the dictionary passed in *`dictHandle`* and releases
all the (tuple or object) data associated with those keys.

If an error occurs while processing one or more keys (in particular
if a key is invalid), the operator attempts to continue removing
as many keys as possible before reporting an appropriate failure.

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

Key to remove.

Restriction:
`length(Key) > 0`

## Example (HDevelop)

```
* Remove all keys
get_dict_param (Dict, 'keys', [], Keys)
remove_dict_key (Dict, Keys)
```

## Result

If all the operator parameters are valid, `RemoveDictKey` returns
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`CreateDict`

## Possible Successors

`GetDictParam`

## See also

`CreateDict`,
`SetDictTuple`,
`GetDictTuple`,
`SetDictObject`,
`GetDictObject`,
`GetDictParam`

## Module

Foundation
