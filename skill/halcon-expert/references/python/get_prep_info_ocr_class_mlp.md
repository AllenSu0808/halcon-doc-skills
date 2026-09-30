# get_prep_info_ocr_class_mlp (Operator)

## Name

`get_prep_info_ocr_class_mlp` — Compute the information content of the preprocessed feature vectors
of an OCR classifier.

## Signature

`def get_prep_info_ocr_class_mlp(ocrhandle: HHandle, training_file: MaybeSequence[str], preprocessing: str) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`get_prep_info_ocr_class_mlp` computes the information content
of the training vectors that have been transformed with the
preprocessing given by *`preprocessing`*.
*`preprocessing`* can be set to *"principal_components"*
or *"canonical_variates"*. The OCR classifier
*`ocrhandle`* must have been created with
[`create_ocr_class_mlp`](create_ocr_class_mlp.md). The preprocessing methods are
described with [`create_class_mlp`](create_class_mlp.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`num_input` for
*"principal_components"* and min(`num_output` - 1,
`num_input`) for *"canonical_variates"*, see
[`create_class_mlp`](create_class_mlp.md)), and is returned in
*`information_cont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`cum_information_cont`*, i.e., *`cum_information_cont`*
contains the sums of the first n elements of
*`information_cont`*. To use
`get_prep_info_ocr_class_mlp`, a sufficient number of samples
must be stored in the training files given by *`training_file`*
(see [`write_ocr_trainf`](write_ocr_trainf.md)).

*`information_cont`* and *`cum_information_cont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
total data. This can be decided easily from the first value of
*`cum_information_cont`* that lies above x%. The number thus
obtained can be used as the value for `num_components` in a
new call to [`create_ocr_class_mlp`](create_ocr_class_mlp.md). The call to
`get_prep_info_ocr_class_mlp` already requires the creation of
a classifier, and hence the setting of `num_components` in
[`create_ocr_class_mlp`](create_ocr_class_mlp.md) to an initial value. However, if
`get_prep_info_ocr_class_mlp` is called it is typically not
known how many components are relevant, and hence how to set
`num_components` in this call. Therefore, the following
two-step approach should typically be used to select
`num_components`: In a first step, a classifier with the
maximum number for `num_components` is created
(`num_input` for *"principal_components"* and
min(`num_output` - 1,
`num_input`) for *"canonical_variates"*). Then, the
training samples are saved in a training file using
[`write_ocr_trainf`](write_ocr_trainf.md). Subsequently,
`get_prep_info_ocr_class_mlp` is used to determine the
information content of the components, and with this
`num_components`. After this, a new classifier with the
desired number of components is created, and the classifier is
trained with [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`preprocessing`** (input_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

Default:
"principal_components"

List of values:
"canonical_variates", "principal_components"

**`information_cont`** (output_control)  real-array `→` Sequence[float]

Relative information content of the transformed
feature vectors.

**`cum_information_cont`** (output_control)  real-array `→` Sequence[float]

Cumulative information content of the transformed
feature vectors.

## Example (HDevelop)

```
* Create the initial OCR classifier.
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 80, \
                      'canonical_variates', |CharacterNames|, 42, OCRHandle)
* Get the information content of the transformed feature vectors.
get_prep_info_ocr_class_mlp (OCRHandle, 'ocr.trf', 'canonical_variates', \
                             InformationCont, CumInformationCont)
* Determine the number of transformed components.
* NumComp = [...]
* Create the final OCR classifier.
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 80, \
                      'canonical_variates', NumComp, 42, OCRHandle)
* Train the final classifier.
trainf_ocr_class_mlp (OCRHandle, 'ocr.trf', 100, 1, 0.01, Error, ErrorLog)
write_ocr_class_mlp (OCRHandle, 'ocr.omc')
```

## Result

If the parameters are valid, the operator
`get_prep_info_ocr_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

`get_prep_info_ocr_class_mlp` may return the error 9211
(Matrix is not positive definite) if *`preprocessing`* =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`create_ocr_class_mlp`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`

## Possible Successors

`clear_ocr_class_mlp`,
`create_ocr_class_mlp`

## Module

OCR/OCV
