# QueryBarCodeParams (Operator)

## Name

`QueryBarCodeParams` — Get the names of the parameters that can be used in set_bar_code* and
get_bar_code* operators for a given bar code model

## Signature

`static void HOperatorSet.QueryBarCodeParams(HTuple barCodeHandle, HTuple properties, out HTuple genParamName)`

`HTuple HBarCode.QueryBarCodeParams(string properties)`

## Description

The operator `QueryBarCodeParams` returns parameter names
of the bar code model that correspond to the selection given in
*`properties`*. To explain this, here first some background:
After creating a bar code model, all parameters
are initially set *"general"*, i.e., they have the same values set
for each supported bar code type. During automatic parameter training or
after calling the operator [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md) some
parameters might become bar code type specific at runtime. These parameters
can not be read with the general operator
[`GetBarCodeParam`](get_bar_code_param.md) but must be read for a given bar code type with
[`GetBarCodeParamSpecific`](get_bar_code_param_specific.md). To make this access easy and generic,
the output *`genParamName`* of `QueryBarCodeParams` can be
used as input parameter *`genParamName`* in
[`GetBarCodeParam`](get_bar_code_param.md) or [`GetBarCodeParamSpecific`](get_bar_code_param_specific.md), depending
on *`properties`*=*"*general"* or
*`properties`*=*"*specific"*.

Please note that you could
alternatively use a static tuple of
parameter names for [`GetBarCodeParam`](get_bar_code_param.md) or
[`GetBarCodeParamSpecific`](get_bar_code_param_specific.md) (e.g., the parameter names described with
these operators), but this
is inflexible and therefore not recommended.

Possible values for *`properties`* are:

- ***"all"*:** —

  Returns the names of all parameters supported by the bar code
  reader. The names are independent of the bar code model given
  in *`barCodeHandle`*.
- ***"general"*:** —

  Returns the names of the parameters that contain the same values
  for all supported bar code types, i.e., there are no specific values
  set for certain bar code types, e.g., with
  [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md). The values of only these
  parameters can be read with [`GetBarCodeParam`](get_bar_code_param.md).

  Please note that the parameter name *"train"* is explicitly excluded
  here. *"train"* in a following call to [`GetBarCodeParam`](get_bar_code_param.md)
  would return a multivalue tuple and therefore couldn't be used
  within one tuple in combination with other parameter names.
- ***"specific"*:** —

  Returns the names of the parameters that contain specific values
  for certain bar code types. The values of these parameters must
  be read with [`GetBarCodeParamSpecific`](get_bar_code_param_specific.md) instead of
  [`GetBarCodeParam`](get_bar_code_param.md). Bar code type specific values can
  occur in conjunction with bar code autodiscrimination, described
  with the operator [`FindBarCode`](find_bar_code.md) or automatic parameter
  training.
- ***"trained_general"*:** —

  Returns the names of parameters that have already been trained
  and contain the same values for all supported bar code types.
  The training mode is described with the operator
  [`SetBarCodeParam`](set_bar_code_param.md).
- ***"trained_specific"*:** —

  Returns the names of the parameters that have already been trained
  and contain specific values for certain bar code types.
  The training mode is described with the operator
  [`SetBarCodeParam`](set_bar_code_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barCodeHandle`** (input_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`properties`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Properties of the parameters.

Default:
"trained_general"

List of values:
"all", "general", "specific", "trained_general", "trained_specific"

**`genParamName`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

## Example (HDevelop)

```
TrainParams := ['element_size_min', 'element_size_max', 'orientation']
Train3times := gen_tuple_const(|TrainParams|,'train')
create_bar_code_model (Train3times, TrainParams, BarCodeHandle)
find_bar_code (Image, SymbolRegions, BarCodeHandle, 'EAN-13', \
               DecodedDataStrings)
query_bar_code_params (BarCodeHandle, 'trained_general', NamesGen)
* returns NamesGen = ['element_size_max', 'element_size_min']
get_bar_code_param (BarCodeHandle, NamesGen, ValGen)
* returns e.g., ValGen = [4.0, 1.5]
query_bar_code_params (BarCodeHandle, 'trained_specific', NamesSpec)
* returns NamesSpec = ['orientation', 'orientation_tol']
get_bar_code_param_specific (BarCodeHandle, 'EAN-13', NamesSpec, ValSpec)
* returns e.g., ValSpec = [89.9127, 0.5]
```

## Result

The operator `QueryBarCodeParams` returns the value 2 (
H_MSG_TRUE)
if the
given parameters are correct. Otherwise, an exception is raised.

## Possible Predecessors

`FindBarCode`,
`DecodeBarCodeRectangle2`

## Possible Successors

`GetBarCodeParam`,
`GetBarCodeParamSpecific`

## Module

Bar Code
