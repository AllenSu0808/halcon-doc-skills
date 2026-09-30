# GetRegularizationParamsOcrClassMlp (Operator)

## Name

`GetRegularizationParamsOcrClassMlp` — Return the regularization parameters of an OCR classifier.

## Signature

`static void HOperatorSet.GetRegularizationParamsOcrClassMlp(HTuple OCRHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HOCRMlp.GetRegularizationParamsOcrClassMlp(string genParamName)`

## Description

`GetRegularizationParamsOcrClassMlp` returns the
regularization parameters of an OCR classifier that were specified
with [`SetRegularizationParamsOcrClassMlp`](set_regularization_params_ocr_class_mlp.md). Furthermore,
`GetRegularizationParamsOcrClassMlp` returns the
parameters that were determined by an automatic determination of the
regularization parameters. For a description of the parameters, see
[`SetRegularizationParamsOcrClassMlp`](set_regularization_params_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the regularization parameter to return.

Default:
"weight_prior"

List of values:
"fraction_well_determined_params", "num_inner_iterations", "num_outer_iterations", "num_well_determined_params", "weight_prior"

**`genParamValue`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Value of the regularization parameter.

## Result

If the parameters are valid, the operator
`GetRegularizationParamsOcrClassMlp` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`SetRegularizationParamsOcrClassMlp`,
`ReadOcrClassMlp`

## Possible Successors

`TrainfOcrClassMlp`

## Module

OCR/OCV
