# JsonToDict (Operator)

## Name

`JsonToDict` — Transform a JSON string into a dictionary.

## Signature

`static void HOperatorSet.JsonToDict(HTuple jsonString, HTuple genParamName, HTuple genParamValue, out HTuple dictHandle)`

`static HDict[] HDict.JsonToDict(HTuple jsonString, HTuple genParamName, HTuple genParamValue)`

`void HDict.JsonToDict(string jsonString, string genParamName, string genParamValue)`

## Description

`JsonToDict` transforms the string passed in *`jsonString`*,
which must be valid JSON, into a dictionary and returns the handle of
the dictionary in *`dictHandle`*.

Several optional parameters can be set that control the values of
JSON constants. Those parameters can be set via *`genParamName`*
and *`genParamValue`* and are described in the documentation of
[`ReadDict`](read_dict.md).

`JsonToDict` can transform several strings at once.
For this, *`jsonString`* must contain a tuple of strings.
The output *`dictHandle`* will then contain one dictionary
per input string.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`jsonString`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

String in JSON format.

Default:
["{"key":"value"}"]

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"convert_json_arrays_to", "json_value_false", "json_value_null", "json_value_true"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
0, 1, "HNULL", "true", "false", "dict", "tuple", "tuple_if_possible"

**`dictHandle`** (output_control)  dict(-array) `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

## Example (HDevelop)

```
json_to_dict ('{"capacity": "medium", "image_height": 1024, "image_width": 1024}', [], [], DictHandle)
```

## Result

If the parameters are valid, the operator `JsonToDict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.
This is especially the case if *`jsonString`* does not contain
valid JSON.

## Possible Successors

`WriteDict`,
`CopyDict`

## Alternatives

`ReadDict`,
`CreateDict`

## See also

`ReadDict`,
`WriteDict`,
`SerializeHandle`,
`DeserializeHandle`

## Module

Foundation
