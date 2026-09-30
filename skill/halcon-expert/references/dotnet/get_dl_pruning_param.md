# GetDlPruningParam (Operator)

## Name

`GetDlPruningParam` — Get information from a pruning data handle.

## Signature

`static void HOperatorSet.GetDlPruningParam(HTuple DLPruningHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDlPrune.GetDlPruningParam(string genParamName)`

## Description

`GetDlPruningParam` returns the parameter and pruning values
*`genParamValue`* of *`genParamName`* from the pruning data
handle *`DLPruningHandle`*.

The values of following parameters *`genParamName`* can be retrieved:

- ***"mode"*:** —

  Specifies the pruning method
  See [`CreateDlPruning`](create_dl_pruning.md) for further information.

  Default:
   *"oracle"*
- ***"percentage"*:** —

  Determines how much will be removed in
  percents. E.g., in case of *"mode"*=*"oracle"* it specifies
  the relative amount of possibly removable kernels to be removed, whereby
  only removable kernels are considered.

  Default:
   *10*

Additionally, for *"mode"*=*"oracle"*, the following pruning
values can be retrieved using *`genParamName`*:

- ***"prunable_conv_num"*:** —

  Number of prunable convolutional layers
  in the network. Whether a layer is prunable depends on the
  specifications of the layer itself as well as the network architecture.
- ***"prunable_conv_layer_name"*:** —

  Names of the prunable
  convolutional layers in the network.
- ***"prunable_kernel_num"*:** —

  Number of prunable convolution kernels
  in the network. It considers that a pruned convolution has to retain at
  least 1 convolution kernel.
- ***"pruned_kernel_num"*:** —

  Number of pruned convolution kernels in
  the network after a call of [`GenDlPrunedModel`](gen_dl_pruned_model.md).
- ***"pruned_percentage"*:** —

  Actual percentage of pruned convolution
  kernels in the network after a call of [`GenDlPrunedModel`](gen_dl_pruned_model.md): the
  ratio *"pruned_kernel_num"* versus *"prunable_kernel_num"*.

The following table gives an overview, which parameters and values can be set
using [`SetDlPruningParam`](set_dl_pruning_param.md) and which ones can be retrieved
using `GetDlPruningParam`.

| Parameters | `set` | `get` |
| --- | --- | --- |
| *"mode"* | `x` | `x` |
| *"percentage"* | `x` | `x` |
| *"prunable_conv_num"* |  | `x` |
| *"prunable_conv_layer_name"* |  | `x` |
| *"prunable_kernel_num"* |  | `x` |
| *"pruned_kernel_num"* |  | `x` |
| *"pruned_percentage"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLPruningHandle`** (input_control)  dl_pruning `→` [HDlPrune](HDlPrune.md), [HTuple](HTuple.md) (*IntPtr*)

Pruning data handle.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
"percentage"

List of values:
"mode", "percentage", "prunable_conv_layer_name", "prunable_conv_num", "prunable_kernel_num", "pruned_kernel_num", "pruned_percentage"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*int* / long / string / double)

Value of the generic parameter.

## Possible Predecessors

`CreateDlPruning`,
`SetDlPruningParam`

## See also

`SetDlPruningParam`

## Module

Deep Learning Professional
