# get_dl_pruning_param (Operator)

## Name

`get_dl_pruning_param` — Get information from a pruning data handle.

## Signature

`get_dl_pruning_param( : : DLPruningHandle, GenParamName : GenParamValue)`

## Description

`get_dl_pruning_param` returns the parameter and pruning values
*`GenParamValue`* of *`GenParamName`* from the pruning data
handle *`DLPruningHandle`*.

The values of following parameters *`GenParamName`* can be retrieved:

- ***'mode'*:** —

  Specifies the pruning method
  See [`create_dl_pruning`](create_dl_pruning.md) for further information.

  Default:
   *'oracle'*
- ***'percentage'*:** —

  Determines how much will be removed in
  percents. E.g., in case of *'mode'*=*'oracle'* it specifies
  the relative amount of possibly removable kernels to be removed, whereby
  only removable kernels are considered.

  Default:
   *10*

Additionally, for *'mode'*=*'oracle'*, the following pruning
values can be retrieved using *`GenParamName`*:

- ***'prunable_conv_num'*:** —

  Number of prunable convolutional layers
  in the network. Whether a layer is prunable depends on the
  specifications of the layer itself as well as the network architecture.
- ***'prunable_conv_layer_name'*:** —

  Names of the prunable
  convolutional layers in the network.
- ***'prunable_kernel_num'*:** —

  Number of prunable convolution kernels
  in the network. It considers that a pruned convolution has to retain at
  least 1 convolution kernel.
- ***'pruned_kernel_num'*:** —

  Number of pruned convolution kernels in
  the network after a call of [`gen_dl_pruned_model`](gen_dl_pruned_model.md).
- ***'pruned_percentage'*:** —

  Actual percentage of pruned convolution
  kernels in the network after a call of [`gen_dl_pruned_model`](gen_dl_pruned_model.md): the
  ratio *'pruned_kernel_num'* versus *'prunable_kernel_num'*.

The following table gives an overview, which parameters and values can be set
using [`set_dl_pruning_param`](set_dl_pruning_param.md) and which ones can be retrieved
using `get_dl_pruning_param`.

| Parameters | `set` | `get` |
| --- | --- | --- |
| *'mode'* | `x` | `x` |
| *'percentage'* | `x` | `x` |
| *'prunable_conv_num'* |  | `x` |
| *'prunable_conv_layer_name'* |  | `x` |
| *'prunable_kernel_num'* |  | `x` |
| *'pruned_kernel_num'* |  | `x` |
| *'pruned_percentage'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLPruningHandle`** (input_control)  dl_pruning `→`  (handle)

Pruning data handle.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'percentage'

List of values:
'mode', 'percentage', 'prunable_conv_layer_name', 'prunable_conv_num', 'prunable_kernel_num', 'pruned_kernel_num', 'pruned_percentage'

**`GenParamValue`** (output_control)  attribute.name(-array) `→`  (integer / string / real)

Value of the generic parameter.

## Possible Predecessors

`create_dl_pruning`,
`set_dl_pruning_param`

## See also

`set_dl_pruning_param`

## Module

Deep Learning Professional
