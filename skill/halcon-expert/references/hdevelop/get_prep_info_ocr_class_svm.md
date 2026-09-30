# get_prep_info_ocr_class_svm (Operator)

## Name

`get_prep_info_ocr_class_svm` — Compute the information content of the preprocessed feature vectors
of an SVM-based OCR classifier.

## Signature

`get_prep_info_ocr_class_svm( : : OCRHandle, TrainingFile, Preprocessing : InformationCont, CumInformationCont)`

## Description

`get_prep_info_ocr_class_svm` computes the information content
of the training vectors that have been transformed with the
preprocessing given by *`Preprocessing`*.
*`Preprocessing`* can be set to *'principal_components'*
or *'canonical_variates'*. The OCR classifier
*`OCRHandle`* must have been created with
[`create_ocr_class_svm`](create_ocr_class_svm.md). The preprocessing methods are
described with [`create_class_svm`](create_class_svm.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`NumFeatures` for
*'principal_components'* and min(`NumClasses` - 1,
`NumFeatures`) for *'canonical_variates'*, see
[`create_class_svm`](create_class_svm.md)), and is returned in
*`InformationCont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`CumInformationCont`*, i.e., *`CumInformationCont`*
contains the sums of the first n elements of
*`InformationCont`*. To use
`get_prep_info_ocr_class_svm`, a sufficient number of samples
must be stored in the training files given by *`TrainingFile`*
(see [`write_ocr_trainf`](write_ocr_trainf.md)).

*`InformationCont`* and *`CumInformationCont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
total data. This can be decided easily from the first value of
*`CumInformationCont`* that lies above x%. The number thus
obtained can be used as the value for `NumComponents` in a
new call to [`create_ocr_class_svm`](create_ocr_class_svm.md). The call to
`get_prep_info_ocr_class_svm` already requires the creation of
a classifier, and hence the setting of `NumComponents` in
[`create_ocr_class_svm`](create_ocr_class_svm.md) to an initial value. However, if
`get_prep_info_ocr_class_svm` is called it is typically not
known how many components are relevant, and hence how to set
`NumComponents` in this call. Therefore, the following
two-step approach should typically be used to select
`NumComponents`: In a first step, a classifier with the
maximum number for `NumComponents` is created
(`NumFeatures` for *'principal_components'* and
min(`NumClasses` - 1,
`NumFeatures`) for *'canonical_variates'*). Then,
the training samples are saved in a training file using
[`write_ocr_trainf`](write_ocr_trainf.md). Subsequently,
`get_prep_info_ocr_class_svm` is used to determine the
information content of the components, and with this
`NumComponents`. After this, a new classifier with the
desired number of components is created, and the classifier is
trained with [`trainf_ocr_class_svm`](trainf_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

**`TrainingFile`** (input_control)  filename.read(-array) `→`  (string)

Names of the training files.

Default:
'ocr.trf'

File extension:
.`trf`, .`otr`

**`Preprocessing`** (input_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

Default:
'principal_components'

List of values:
'canonical_variates', 'principal_components'

**`InformationCont`** (output_control)  real-array `→`  (real)

Relative information content of the transformed
feature vectors.

**`CumInformationCont`** (output_control)  real-array `→`  (real)

Cumulative information content of the transformed
feature vectors.

## Example (HDevelop)

```
* Create the initial OCR classifier.
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_svm (8, 10, 'constant', 'default', CharacterNames, \
                      'rbf', 0.01, 0.01, 'one-versus-one', \
                      'principal_components', 81, OCRHandle)
* Get the information content of the transformed feature vectors.
get_prep_info_ocr_class_svm (OCRHandle, 'ocr.trf', 'principal_components', \
                             InformationCont, CumInformationCont)
* Determine the number of transformed components.
* NumComp = [...]
* Create the final OCR classifier.
create_ocr_class_svm (8, 10, 'constant', 'default', CharacterNames, \
                      'rbf', 0.01, 0.01,'one-versus-one', \
                      'principal_components', NumComp, OCRHandle)
* Train the final classifier.
trainf_ocr_class_svm (OCRHandle, 'ocr.trf', 0.001, 'default')
write_ocr_class_svm (OCRHandle, 'ocr.osc')
```

## Result

If the parameters are valid the operator
`get_prep_info_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

`get_prep_info_ocr_class_svm` may return the error 9211
(Matrix is not positive definite) if *`Preprocessing`* =
*'canonical_variates'* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`create_ocr_class_svm`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`

## Possible Successors

`clear_ocr_class_svm`,
`create_ocr_class_svm`

## Module

OCR/OCV
