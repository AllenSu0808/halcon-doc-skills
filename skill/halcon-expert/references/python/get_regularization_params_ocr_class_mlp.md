# get_regularization_params_ocr_class_mlp (Operator)

## Name

`get_regularization_params_ocr_class_mlp` — Return the regularization parameters of an OCR classifier.

## Signature

`def get_regularization_params_ocr_class_mlp(ocrhandle: HHandle, gen_param_name: str) -> Sequence[Union[float, int]]`

`def get_regularization_params_ocr_class_mlp_s(ocrhandle: HHandle, gen_param_name: str) -> Union[float, int]`

## Description

`get_regularization_params_ocr_class_mlp` returns the
regularization parameters of an OCR classifier that were specified
with [`set_regularization_params_ocr_class_mlp`](set_regularization_params_ocr_class_mlp.md). Furthermore,
`get_regularization_params_ocr_class_mlp` returns the
parameters that were determined by an automatic determination of the
regularization parameters. For a description of the parameters, see
[`set_regularization_params_ocr_class_mlp`](set_regularization_params_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`gen_param_name`** (input_control)  string `→` str

Name of the regularization parameter to return.

Default:
"weight_prior"

List of values:
"fraction_well_determined_params", "num_inner_iterations", "num_outer_iterations", "num_well_determined_params", "weight_prior"

**`gen_param_value`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

Value of the regularization parameter.

## Result

If the parameters are valid, the operator
`get_regularization_params_ocr_class_mlp` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`set_regularization_params_ocr_class_mlp`,
`read_ocr_class_mlp`

## Possible Successors

`trainf_ocr_class_mlp`

## Module

OCR/OCV
