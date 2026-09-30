# get_compute_device_param (Operator)

## Name

`get_compute_device_param` — Query compute device parameters.

## Signature

`def get_compute_device_param(device_handle: HHandle, gen_param_name: str) -> Sequence[Union[str, int, float]]`

`def get_compute_device_param_s(device_handle: HHandle, gen_param_name: str) -> Union[str, int, float]`

## Description

`get_compute_device_param` returns parameters of the
compute device *`device_handle`* for the current HALCON thread
in *`gen_param_value`*.

The following parameters can be queried (for more information
see [`set_compute_device_param`](set_compute_device_param.md)) by setting them for
*`gen_param_name`*:

- ***"alloc_pinned"*** —

  If *"true"*, the output image matrices of all operators
  are created in page locked (so called 'pinned') memory.
- ***"asynchronous_execution"*** —

  If *"true"*, operators executed on the compute device
  do not wait for the device computations to finish but
  return after initiation the computations.
- ***"buffer_cache_capacity"*** —

  Maximum size (in bytes) of the compute device buffer cache.
- ***"buffer_cache_used"*** —

  Current size (in bytes) of the compute device buffer cache.
- ***"image_cache_capacity"*** —

  Maximum size (in bytes) of the compute device image cache.
- ***"image_cache_used"*** —

  Current size (in bytes) of the compute device image cache.
- ***"pinned_mem_cache_capacity"*** —

  Maximum size (in bytes) of the page locked (pinned) memory
  cache.
- ***"pinned_mem_cache_used"*** —

  Current size (in bytes) of the page locked (pinned) memory
  cache.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`device_handle`** (input_control)  compute_device `→` HHandle

Compute device handle.

**`gen_param_name`** (input_control)  string `→` str

Name of the parameter to query.

Default:
"buffer_cache_capacity"

List of values:
"alloc_pinned", "asynchronous_execution", "buffer_cache_capacity", "buffer_cache_used", "image_cache_capacity", "image_cache_used", "pinned_mem_cache_capacity", "pinned_mem_cache_used"

**`gen_param_value`** (output_control)  string(-array) `→` Sequence[Union[str, int, float]]

Value of the parameter.

## Result

The operator `get_compute_device_param` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Possible Predecessors

`activate_compute_device`

## See also

`set_compute_device_param`,
`get_compute_device_info`

## Module

Foundation
