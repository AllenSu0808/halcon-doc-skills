# GetBarCodeParamSpecific (Operator)

## Name

`GetBarCodeParamSpecific` — Get parameters that are used by the bar code reader when processing a
specific bar code type.

## Signature

`static void HOperatorSet.GetBarCodeParamSpecific(HTuple barCodeHandle, HTuple codeTypes, HTuple genParamName, out HTuple genParamValue)`

`HTuple HBarCode.GetBarCodeParamSpecific(HTuple codeTypes, HTuple genParamName)`

`HTuple HBarCode.GetBarCodeParamSpecific(string codeTypes, string genParamName)`

## Description

The operator `GetBarCodeParamSpecific` allows to query parameters
of a bar code model, which are of relevance for a successful search and
decoding of a respective class of bar codes. Contrary to
[`GetBarCodeParam`](get_bar_code_param.md), `GetBarCodeParamSpecific` allows
a bar code type specific query for the following parameters. This is useful
when searching different code types in one image. The bar code
types are specified in *`codeTypes`*.
The names of the desired parameters are passed in the generic
parameter *`genParamName`* and the corresponding values are
returned in *`genParamValue`*.
All of these parameters can be set and changed selectively with the
operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md) or for all bar code types with
the operator [`SetBarCodeParam`](set_bar_code_param.md). Which parameters are set
specifically can be determined at runtime with the operator
[`QueryBarCodeParams`](query_bar_code_params.md). These parameters cannot be read with
[`GetBarCodeParam`](get_bar_code_param.md), but must be read with
`GetBarCodeParamSpecific`.

The following parameters can be queried:

- ***"element_size_variable"*:** —

  Specifies if the element size varies across a single bar code.
- ***"num_scanlines"*:** —

  Maximum number of scanlines used during the scanning of a (candidate)
  bar code.
- ***"min_identical_scanlines"*:** —

  Minimum number of decoded scanlines which return
  identical data to read the bar code successfully.
- ***"stop_after_result_num"*:** —

  Number of successfully decoded bar codes of the given code type after
  which the decoding will stop. *0* is the default
  where the reader tries to decode all candidates.
- ***"orientation"*:** —

  Accepted orientation of the decoded bar codes.
- ***"orientation_tol"*:** —

  Tolerance of the accepted orientation.
- ***"quiet_zone"*:** —

  Quiet zone verification mode.
- ***"start_stop_tolerance"*:** —

  Start/stop search criteria tolerance. Currently it is implemented only
  for Code 128 and GS1-128.
- ***"check_char"*:** —

  Handling of an optional check character.
- ***"composite_code"*:** —

  Presence and type of a 2D composite code appended to the bar code.
- ***"min_code_length"*:** —

  Minimum number of decoded characters.
- ***"max_code_length"*:** —

  Maximum number of decoded characters.

Further details on the above parameters can be found with the
description of [`SetBarCodeParam`](set_bar_code_param.md) operator.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barCodeHandle`** (input_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`codeTypes`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the bar code types for which parameters
should be queried.

Default:
"EAN-13"

List of values:
"2/5 Industrial", "2/5 Interleaved", "Codabar", "Code 128", "Code 39", "Code 93", "EAN-13 Add-On 2", "EAN-13 Add-On 5", "EAN-13", "EAN-8 Add-On 2", "EAN-8 Add-On 5", "EAN-8", "GS1 DataBar Expanded Stacked", "GS1 DataBar Expanded", "GS1 DataBar Limited", "GS1 DataBar Omnidir", "GS1 DataBar Stacked Omnidir", "GS1 DataBar Stacked", "GS1 DataBar Truncated", "GS1-128", "MSI", "PharmaCode", "UPC-A Add-On 2", "UPC-A Add-On 5", "UPC-A", "UPC-E Add-On 2", "UPC-E Add-On 5", "UPC-E"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that are to be
queried for the bar code model.

Default:
"check_char"

List of values:
"check_char", "composite_code", "element_size_variable", "max_code_length", "min_code_length", "min_identical_scanlines", "num_scanlines", "orientation", "orientation_tol", "quiet_zone", "start_stop_tolerance", "stop_after_result_num"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters.

## Result

The operator `GetBarCodeParamSpecific` returns the value 2 (
H_MSG_TRUE)
if
the given parameters are correct. Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBarCodeModel`,
`SetBarCodeParam`,
`SetBarCodeParamSpecific`

## Alternatives

`GetBarCodeParam`

## Module

Bar Code
