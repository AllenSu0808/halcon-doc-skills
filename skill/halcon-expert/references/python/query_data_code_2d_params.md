# query_data_code_2d_params (Operator)

## Name

`query_data_code_2d_params` — Get for a given 2D code model the names of the generic
parameters or objects that can be used in the other 2D code
operators.

## Signature

`def query_data_code_2d_params(data_code_handle: HHandle, query_name: str) -> Sequence[str]`

## Description

The operator `query_data_code_2d_params` returns the names of
the generic parameters that are supported by the 2D code
operators [`set_data_code_2d_param`](set_data_code_2d_param.md),
[`get_data_code_2d_param`](get_data_code_2d_param.md), [`find_data_code_2d`](find_data_code_2d.md),
[`get_data_code_2d_results`](get_data_code_2d_results.md), and
[`get_data_code_2d_objects`](get_data_code_2d_objects.md).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

The parameter *`query_name`* is used to select the desired
**parameter group**:

- ***"get_model_params"*:** —

  [`get_data_code_2d_param`](get_data_code_2d_param.md) - Parameters for querying
  the 2D code model.
- ***"set_model_params"*:** —

  [`set_data_code_2d_param`](set_data_code_2d_param.md) - Parameters for adjusting the
  2D code model.
- ***"find_params"*:** —

  [`find_data_code_2d`](find_data_code_2d.md) - Parameters used while
  searching and reading the 2D code symbols.
- ***"get_result_params"*:** —

  [`get_data_code_2d_results`](get_data_code_2d_results.md) - Parameters for querying
  the alphanumerical results of the symbol search.
- ***"get_result_objects"*:** —

  [`get_data_code_2d_objects`](get_data_code_2d_objects.md) - Parameters for accessing
  the iconic objects of the symbol search.
- ***"trained"*:** —

  [`set_data_code_2d_param`](set_data_code_2d_param.md) - Parameters whose values were
  determined by training. The next training will not reset these
  parameters, but extend the parameter space if necessary.

The returned parameter list depends only on the type of the 2D
code and not on the current state of the model or its results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`data_code_handle`** (input_control)  datacode_2d `→` HHandle

Handle of the 2D code model.

**`query_name`** (input_control)  attribute.name `→` str

Name of the parameter group.

Default:
"get_result_params"

List of values:
"find_params", "get_model_params", "get_result_objects", "get_result_params", "set_model_params", "trained"

**`gen_param_name`** (output_control)  attribute.value-array `→` Sequence[str]

List containing the names of the supported generic
parameters.

## Example (HDevelop)

```
* This example demonstrates how the names of all available model parameters
* can be queried.  This is used to request first the settings of the
* untrained and then the settings of the trained model.

* Create a model for reading Data Matrix ECC 200 codes
create_data_code_2d_model ('Data Matrix ECC 200', [], [], DataCodeHandle)
* Query all the names of the generic parameters that can be passed to the
* operator get_data_code_2d_param to request the model
query_data_code_2d_params (DataCodeHandle, 'get_model_params', GenParamName)
* Request the current settings of the (untrained) model
get_data_code_2d_param(DataCodeHandle, GenParamName, ModelParams)

* Read a training image
read_image (Image, 'datacode/ecc200/ecc200_cpu_007')
* train the model with the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, 'train', 'all', \
                   ResultHandles, DecodedDataStrings)
* Request the current settings of the (now trained) model
get_data_code_2d_param(DataCodeHandle, GenParamName, TrainedModelParams)
* Create a tuple that demonstrates the changings
ModelAdaption := GenParamName + ':   ' + ModelParams + '  ->  ' + \
                 TrainedModelParams

* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `query_data_code_2d_params` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`create_data_code_2d_model`

## Possible Successors

`get_data_code_2d_param`,
`get_data_code_2d_results`,
`get_data_code_2d_objects`

## Module

Data Code
