# set_regularization_params_ocr_class_mlp (Operator)

## Name

`set_regularization_params_ocr_class_mlp` — Set the regularization parameters of an OCR classifier.

## Signature

`set_regularization_params_ocr_class_mlp( : : OCRHandle, GenParamName, GenParamValue : )`

## Description

`set_regularization_params_ocr_class_mlp` sets the
regularization parameters of the OCR classifier passed in
*`OCRHandle`*. The regularization parameter to be set is
specified with *`GenParamName`*. Its value is specified with
*`GenParamValue`*.

As described at [`create_class_mlp`](create_class_mlp.md), it may be desirable to
regularize the OCR classifier (i.e., the MLP of the OCR classifier)
to enforce a smoother transition of the confidences between the
different classes and to prevent overfitting of the OCR classifier
to the training data. To achieve this, a penalty for large MLP
weights (which are the main reason for very sharp transitions
between classes) can be added to the training of the OCR classifier
in [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md) by setting *`GenParamName`* to
*'weight_prior'* and setting *`GenParamValue`* to a
value > 0. Furthermore, the regularization parameters can be
determined automatically. For details, see
[`set_regularization_params_class_mlp`](set_regularization_params_class_mlp.md). If the regularization
parameters should be determined automatically, please carefully note
the advice in [`set_regularization_params_class_mlp`](set_regularization_params_class_mlp.md) on how to
select the parameters `NumHidden` of the MLP and
*'num_outer_iterations'* and on the memory and runtime
implications of automatically determining the regularization
parameters on the runtime of the training of the OCR classifier.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_mlp `→`  (handle)

Handle of the OCR classifier.

**`GenParamName`** (input_control)  string `→`  (string)

Name of the regularization parameter to return.

Default:
'weight_prior'

List of values:
'num_inner_iterations', 'num_outer_iterations', 'weight_prior'

**`GenParamValue`** (input_control)  number(-array) `→`  (real / integer)

Value of the regularization parameter.

Default:
1.0

Suggested values:
0.01, 0.1, 1.0, 10.0, 100.0, 0, 1, 2, 3, 5, 10, 15, 20

## Example (HDevelop)

```
* This example shows how to determine the regularization parameters
* automatically without examining the convergence of the
* regularization parameters.
* Create the OCR classifier.
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, \
                      40, 'none', |CharacterNames|, 42, OCRHandle)
* Set up the automatic determination of the regularization
* parameters.
set_regularization_params_ocr_class_mlp (OCRHandle, 'weight_prior', \
                                         [0.01,0.01,0.01,0.01])
set_regularization_params_ocr_class_mlp (OCRHandle, \
                                         'num_outer_iterations', 10)
* Train the classifier.
trainf_ocr_class_mlp (OCRHandle, 'ocr.trf', 100, 1, 0.01, Error, \
                      ErrorLog)
* Read out the estimate of the number of well-determined
* parameters.
get_regularization_params_ocr_class_mlp (OCRHandle, \
                                         'fraction_well_determined_params', \
                                          FractionParams)
* If FractionParams differs substantially from 1, consider reducing
* NumHidden appropriately and consider performing a preprocessing that
* reduces the number of input variables to the net, i.e., canonical
* variates or principal components.
write_ocr_class_mlp (OCRHandle, 'ocr.omc')

* This example shows how to determine the regularization parameters
* automatically while examining the convergence of the
* regularization parameters.
* Create the OCR classifier.
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, \
                      40, 'none', |CharacterNames|, 42, OCRHandle)
* Set up the automatic determination of the regularization
* parameters.
set_regularization_params_ocr_class_mlp (OCRHandle, 'weight_prior', \
                                         [0.01,0.01,0.01,0.01])
set_regularization_params_ocr_class_mlp (OCRHandle, \
                                         'num_outer_iterations', 1)
for OuterIt := 1 to 10 by 1
    * Train the classifier.
    trainf_ocr_class_mlp (OCRHandle, 'ocr.trf', 100, 1, 0.01, Error, \
                          ErrorLog)
    * Read out the regularization parameters
    get_regularization_params_ocr_class_mlp (OCRHandle, \
                                             'weight_prior', \
                                             WeightPrior)
    * Inspect the regularization parameters manually for
    * convergence and exit the loop manually if they have
    * converged.
    * [...]
endfor
* Read out the estimate of the number of well-determined
* parameters.
get_regularization_params_ocr_class_mlp (OCRHandle, \
                                         'fraction_well_determined_params', \
                                          FractionParams)
* If FractionParams differs substantially from 1, consider reducing
* NumHidden appropriately and consider performing a preprocessing that
* reduces the number of input variables to the net, i.e., canonical
* variates or principal components.
write_ocr_class_mlp (OCRHandle, 'ocr.omc')
```

## Result

If the parameters are valid, the operator
`set_regularization_params_ocr_class_mlp` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_ocr_class_mlp`

## Possible Successors

`get_regularization_params_ocr_class_mlp`,
`trainf_ocr_class_mlp`

## Module

OCR/OCV
