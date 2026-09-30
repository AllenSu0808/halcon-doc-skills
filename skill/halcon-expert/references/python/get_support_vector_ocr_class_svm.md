# get_support_vector_ocr_class_svm (Operator)

## Name

`get_support_vector_ocr_class_svm` — Return the index of a support vector from a trained OCR classifier that is
based on support vector machines.

## Signature

`def get_support_vector_ocr_class_svm(ocrhandle: HHandle, index_support_vector: Sequence[int]) -> float`

## Description

The operator `get_support_vector_ocr_class_svm` maps support
vectors of a trained SVM-based OCR classifier (given in
*`ocrhandle`*) to the original training data set. The index of
the SV is specified with *`index_support_vector`*. The index is
counted from 0, i.e., *`index_support_vector`* must be a number
between 0 and `num_support_vectors` - 1, where
`num_support_vectors` can be determined with
[`get_support_vector_num_ocr_class_svm`](get_support_vector_num_ocr_class_svm.md). The index of this SV
in the training data is returned in *`index`*.
`get_support_vector_ocr_class_svm` can, for example, be used
to visualize the support vectors. To do so, the train file that has
been used to train the SVM must be read with
[`read_ocr_trainf`](read_ocr_trainf.md). The value returned in *`index`* must
be incremented by *1* and can then be used to select the
support vectors with [`select_obj`](select_obj.md) from the training
characters. If more than one train file has been used in
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md) *`index`* behaves as if all train
files had been merged into one train file with
[`concat_ocr_trainf`](concat_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

OCR handle.

**`index_support_vector`** (input_control)  integer-array `→` Sequence[int]

Number of stored support vectors.

**`index`** (output_control)  real `→` float

Index of the support vector in the training set.

## Result

If the parameters are valid the operator
`get_support_vector_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`,
`get_support_vector_num_ocr_class_svm`

## See also

`create_ocr_class_svm`,
`read_ocr_trainf`,
`append_ocr_trainf`,
`concat_ocr_trainf`

## Module

OCR/OCV
