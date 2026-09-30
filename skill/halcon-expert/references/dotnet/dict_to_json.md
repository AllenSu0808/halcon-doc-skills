# DictToJson (Operator)

## Name

`DictToJson` — Transform a dictionary into a JSON string.

## Signature

`static void HOperatorSet.DictToJson(HTuple dictHandle, HTuple genParamName, HTuple genParamValue, out HTuple jsonString)`

`static HTuple HDict.DictToJson(HDict[] dictHandle, HTuple genParamName, HTuple genParamValue)`

`string HDict.DictToJson(string genParamName, string genParamValue)`

## Description

`DictToJson` transforms the dictionary passed in
*`dictHandle`* into a JSON string and returns that string
in *`jsonString`*.

Several optional parameters can be set that control the creation of
the JSON strings.
Those parameters can be set via *`genParamName`*
and *`genParamValue`* and are described in the documentation of
[`WriteDict`](write_dict.md):

- *"raise_error_if_content_not_serializable"*,
- *"compact_json"*,
- *"use_json_arrays"*.

`DictToJson` can transform several dictionaries at once.
For this, *`dictHandle`* must contain a tuple of dictionaries.
The output *`jsonString`* will then contain one string
per input dictionary.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dictHandle`** (input_control)  dict(-array) `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"compact_json", "raise_error_if_content_not_serializable", "use_json_arrays"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
"true", "false"

**`jsonString`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

String in JSON format.

## Example (HDevelop)

```
dict_to_json (dict{foo: 'bar', bar: [0:2]}, [], [], JSONString)
```

## Result

If the parameters are valid, the operator `DictToJson` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`CreateDict`,
`ReadDict`,
`JsonToDict`

## Possible Successors

`JsonToDict`

## Alternatives

`ReadDict`,
`CreateDict`

## See also

`JsonToDict`,
`ReadDict`,
`WriteDict`,
`SerializeHandle`,
`DeserializeHandle`,
`CopyDict`

## Module

Foundation
