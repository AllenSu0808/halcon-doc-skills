# select_feature_set_svm (Operator)

## Name

`select_feature_set_svm` — Selects an optimal combination of features to classify the provided data.

## Signature

`def select_feature_set_svm(class_train_data_handle: HHandle, selection_method: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, str, float]]) -> Tuple[HHandle, Sequence[str], Sequence[float]]`

## Description

`select_feature_set_svm` selects an optimal subset from a set of
features to solve a given classification problem.
The classification problem has to be specified with annotated training data
in *`class_train_data_handle`* and will be classified by a
support vector machine (SVM). Details of the properties of this
classifier can be found in [`create_class_svm`](create_class_svm.md).

The result of the operator is a trained classifier that is returned in
*`svmhandle`*. Additionally, the list of indices or names of the
selected features
is returned in *`selected_feature_indices`*. To use this classifier,
calculate for new input data all features mentioned in
*`selected_feature_indices`* and pass them to the classifier.

A possible application of this operator can be a comparison of
different parameter sets for certain feature extraction techniques. Another
application is to search for a feature that is discriminating between
different classes.

Additionally, the values for *"nu"* and
*"gamma"* can be estimated for the SVM. To only estimate these
two parameters without altering the feature set,
the feature vector has to be specified as one large subfeature.

To define the features that should be selected from
*`class_train_data_handle`*, the dimensions of the
feature vectors in *`class_train_data_handle`* can be grouped into
subfeatures by calling [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md).
A subfeature can contain several subsequent elements of a feature vector.
The operator decides for each of these subfeatures, if it is better to
use it for the classification or leave it out.

The indices of the selected subfeatures are returned in
*`selected_feature_indices`*.
If names were set in [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md), these
names are returned instead of the indices.
If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md) was not called for
*`class_train_data_handle`* before, each element of the feature vector
is considered as a subfeature.

The selection method
*`selection_method`* is either a greedy search *"greedy"*
(iteratively add the feature with highest gain)
or the dynamically oscillating search *"greedy_oscillating"*
(add the feature with highest gain and test then if any of the already added
features can be left out without great loss).
The method *"greedy"* is generally preferable, since it is faster.
Only in cases when the subfeatures are low-dimensional or redundant,
the method *"greedy_oscillating"* should be chosen.

The optimization criterion is the classification rate of
a two-fold cross-validation of the training data.
The best achieved value is returned in *`score`*.

The parameters *"nu"* and *"gamma"* for the SVM that is used
to classify can be set to *"auto"* by using the
parameters *`gen_param_name`* and *`gen_param_value`*. If they are
set to *"auto"*, the estimated optimal *"nu"* and/or
*"gamma"* is estimated. The automatic estimation of *"nu"*
and *"gamma"* can take a substantial amount of time (up to days,
depending on the data set and the number of features).

Additionally, there
is the parameter *"mode"* which can be either set to
*"one-versus-all"* or *"one-versus-one"*. An explanation of
the two modes as well as of the parameters *"nu"* and
*"gamma"* as the kernel parameter of the radial basis function (RBF)
kernel can be found in [`create_class_svm`](create_class_svm.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_svm` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of the training data.

**`selection_method`** (input_control)  string `→` str

Method to perform the selection.

Default:
"greedy"

List of values:
"greedy", "greedy_oscillating"

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of generic parameters to configure the
selection process and the classifier.

Default:
[]

List of values:
"gamma", "mode", "nu"

**`gen_param_value`** (input_control)  number(-array) `→` MaybeSequence[Union[int, str, float]]

Values of generic parameters to configure the
selection process and the classifier.

Default:
[]

Suggested values:
0.02, 0.05, "auto", "one-versus-one", "one-versus-all"

**`svmhandle`** (output_control)  class_svm `→` HHandle

A trained SVM classifier using only the selected
features.

**`selected_feature_indices`** (output_control)  string-array `→` Sequence[str]

The selected feature set, contains
indices.

**`score`** (output_control)  real-array `→` Sequence[float]

The achieved score using two-fold cross-validation.

## Example (HDevelop)

```
* Find out which of the two features distinguishes two Classes
NameFeature1 := 'Good Feature'
NameFeature2 := 'Bad Feature'
LengthFeature1 := 3
LengthFeature2 := 2
* Create training data
create_class_train_data (LengthFeature1+LengthFeature2,\
  ClassTrainDataHandle)
* Define the features which are in the training data
set_feature_lengths_class_train_data (ClassTrainDataHandle, [LengthFeature1,\
  LengthFeature2], [NameFeature1, NameFeature2])
* Add training data
*                                                         |Feat1| |Feat2|
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  2,1  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  2,1  ], 1)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [1,1,1,  3,4  ], 0)
add_sample_class_train_data (ClassTrainDataHandle, 'row', [2,2,2,  3,4  ], 1)
* Add more data
* ...
* Select the better feature with a SVM
select_feature_set_svm (ClassTrainDataHandle, 'greedy', [], [], SVMHandle,\
  SelectedFeatureSVM, Score)
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator `select_feature_set_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`,
`add_sample_class_train_data`,
`set_feature_lengths_class_train_data`

## Possible Successors

`classify_class_svm`

## Alternatives

`select_feature_set_mlp`,
`select_feature_set_knn`,
`select_feature_set_gmm`

## See also

`select_feature_set_trainf_svm`,
`gray_features`,
`region_features`

## Module

Foundation
