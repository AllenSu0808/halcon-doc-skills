# SetBarCodeParamSpecific (Operator)

## Name

`SetBarCodeParamSpecific` — Set selected parameters of the bar code model for selected bar code types

## Signature

`static void HOperatorSet.SetBarCodeParamSpecific(HTuple barCodeHandle, HTuple codeTypes, HTuple genParamName, HTuple genParamValue)`

`void HBarCode.SetBarCodeParamSpecific(HTuple codeTypes, HTuple genParamName, HTuple genParamValue)`

`void HBarCode.SetBarCodeParamSpecific(string codeTypes, string genParamName, HTuple genParamValue)`

## Description

The operator `SetBarCodeParamSpecific` is used to set or change
the different parameters of a bar code model for selected bar code types
in order to adapt to special properties of the bar codes.
Contrary to [`SetBarCodeParam`](set_bar_code_param.md), only parameters for selected bar
code types will be changed with `SetBarCodeParamSpecific`.
This is useful when searching different code types within one image (see
section Autodiscrimination in [`FindBarCode`](find_bar_code.md)).

The current configuration of the bar code model for a specified bar code
type can be queried with [`GetBarCodeParamSpecific`](get_bar_code_param_specific.md).

The following generic parameters can be set for specific bar code types:

- ***"element_size_variable"*:** —

  Specifies if the element size varies across a single bar code.

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*
- ***"num_scanlines"*:** —

  Maximum number of scanlines used during the scanning of a (candidate)
  bar code.

  Suggested values:
   [*0*, *5*, *10*,
  *20*, ...]

  Default:
   *0*
- ***"min_identical_scanlines"*:** —

  Minimum number of decoded scanlines which return
  identical data to read the bar code successfully.

  Suggested values:
   [*0*, *2*, *3*,
  ...]

  Default:

  | Bar code Type | *"min_identical_scanlines"* |
  | --- | --- |
  | 2/5 Industrial | 2 |
  | 2/5 Interleaved | 2 |
  | all others | 0 |
- ***"stop_after_result_num"*:** —

  Number of successfully decoded bar codes of the given code type after
  which the decoding will stop.

  Suggested values:
   [*0*, *1*, *2*,
  ...]

  Default:
   *0*
- ***"orientation"*:** —

  Expected bar code orientation.

  Suggested values:
   [*-90.0* ... *90.0*]

  Default:
   *0.0*
- ***"orientation_tol"*:** —

  Orientation tolerance.

  Suggested values:
   [*0.0* ... *90.0*]

  Default:
   *90.0*
- ***"quiet_zone"*:** —

  Enforces the verification of quiet zones of a bar code symbol.

  Suggested values:
   *"false"*, *"true"*, *1*,
  *2*, *3*, *4*,
  *5*

  Default:
   *"false"*
- ***"start_stop_tolerance"*:** —

  Start/stop search criteria tolerance. Currently this is implemented
  only for Code 128 and GS1-128.

  List of values:
   *"high"*, *"low"*

  Default:
   *"high"*
- ***"check_char"*:** —

  Handling of an optional check character.

  List of values:
   *"absent"*, *"present"*,
  *"preserved"*

  Default:
   *"absent"*
- ***"composite_code"*:** —

  Find and decode a composite component.

  List of values:
   *"none"*, *"CC-A/B"*

  Default:
   *"none"*
- ***"min_code_length"*:** —

  Minimum number of decoded characters.

  Default:

  | Bar code Type | *"min_code_length"* |
  | --- | --- |
  | 2/5 Industrial | 3 |
  | 2/5 Interleaved | 3 |
  | all others | 0 |
- ***"max_code_length"*:** —

  Maximum number of decoded characters.

  Value range:
   [*1* ...
  *2147483647*]

  Default:
   *2147483647*

Further details on these parameters can be found with the
description of the operator [`SetBarCodeParam`](set_bar_code_param.md).

It is possible to supply multivalue tuples for *`codeTypes`*,
*`genParamName`*, and *`genParamValue`*. The n-th entry
of one multivalue tuple corresponds to the n-th entry of the other
multivalue tuple. The following combinations are allowed:

| *`codeTypes`* | *`genParamName`* | *`genParamValue`* |
| --- | --- | --- |
| single-valued | single-valued | single-valued |
| single-valued | multi-valued | multi-valued |
| multi-valued | single-valued | multi-valued |
| multi-valued | single-valued | single-valued |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- barCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`barCodeHandle`** (input_control, state is modified)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`codeTypes`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the bar code types for which parameters
should be set.

Default:
"EAN-13"

List of values:
"2/5 Industrial", "2/5 Interleaved", "Codabar", "Code 128", "Code 39", "Code 93", "EAN-13 Add-On 2", "EAN-13 Add-On 5", "EAN-13", "EAN-8 Add-On 2", "EAN-8 Add-On 5", "EAN-8", "GS1 DataBar Expanded Stacked", "GS1 DataBar Expanded", "GS1 DataBar Limited", "GS1 DataBar Omnidir", "GS1 DataBar Stacked Omnidir", "GS1 DataBar Stacked", "GS1 DataBar Truncated", "GS1-128", "MSI", "PharmaCode", "UPC-A Add-On 2", "UPC-A Add-On 5", "UPC-A", "UPC-E Add-On 2", "UPC-E Add-On 5", "UPC-E"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that shall be
adjusted for finding and decoding bar codes.

Default:
"check_char"

List of values:
"check_char", "composite_code", "element_size_variable", "max_code_length", "min_code_length", "min_identical_scanlines", "num_scanlines", "orientation", "orientation_tol", "quiet_zone", "start_stop_tolerance", "stop_after_result_num"

**`genParamValue`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters that are
adjusted for finding and decoding bar codes.

Default:
"absent"

Suggested values:
0, 1, 2, 4, 45, 90, "true", "false", "present", "absent", "none", "CC-A/B", "high", "low"

## Result

The operator `SetBarCodeParamSpecific` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBarCodeModel`

## Possible Successors

`FindBarCode`

## Alternatives

`SetBarCodeParam`

## Module

Bar Code
