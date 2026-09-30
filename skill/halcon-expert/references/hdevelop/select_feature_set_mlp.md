# select_feature_set_mlp (Operator)

## Name

`select_feature_set_mlp` — Selects an optimal combination of features to classify the provided data.

## Signature

`select_feature_set_mlp( : : ClassTrainDataHandle, SelectionMethod, GenParamName, GenParamValue : MLPHandle, SelectedFeatureIndices, Score)`

## Description

`select_feature_set_mlp` selects an optimal subset from a set of
features to solve a given classification problem.
The classification problem has to be specified with annotated training data
in *`ClassTrainDataHandle`* and will be classified by a
Multilayer Perceptron. Details of the properties of this
classifier can be found in [`create_class_mlp`](create_class_mlp.md).

The result of the operator is a trained classifier that is returned in
*`MLPHandle`*. Additionally, the list of indices or names of the
selected features
is returned in *`SelectedFeatureIndices`*. To use this classifier,
calculate for new input data all features mentioned in
*`SelectedFeatureIndices`* and pass them to the classifier.

A possible application of this operator can be a comparison of
different parameter sets for certain feature extraction techniques. Another
application is to search for a feature that is discriminating between
different classes.

To define the features that should be selected from
*`ClassTrainDataHandle`*, the dimensions of the
feature vectors in *`ClassTrainDataHandle`* can be grouped into
subfeatures by calling [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md).
A subfeature can contain several subsequent elements of a feature vector.
`select_feature_set_mlp` decides for each of these subfeatures,
if it is better to use it for the classification or leave it out.

The indices of the selected subfeatures are returned in
*`SelectedFeatureIndices`*.
If names were set in [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md), these
names are returned instead of the indices.
If [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md) was not called for
*`ClassTrainDataHandle`* before, each element of the feature vector
is considered as a subfeature.

The selection method
*`SelectionMethod`* is either a greedy search *'greedy'*
(iteratively add the feature with highest gain)
or the dynamically oscillating search *'greedy_oscillating'*
(add the feature with highest gain and test then if any of the already added
features can be left out without great loss).
The method *'greedy'* is generally preferable, since it is faster.
Only in cases when the subfeatures are low-dimensional or redundant,
the method *'greedy_oscillating'* should be chosen.

The optimization criterion is the classification rate of
a two-fold cross-validation of the training data.
The best achieved value is returned in *`Score`*.

With *`GenParamName`* and *`GenParamValue`* the number
of hidden layer can be set by
*'num_hidden'*. The default value is *80*. Larger values
for this parameter lead to longer classification times, while it allows
a more expressive classifier.

## Attention

This operator may take considerable time, depending on the size of the
data and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `select_feature_set_mlp` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of the training data.

**`SelectionMethod`** (input_control)  string `→`  (string)

Method to perform the selection.

Default:
'greedy'

List of values:
'greedy', 'greedy_oscillating'

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of generic parameters to configure the
selection process and the classifier.

Default:
[]

List of values:
'num_hidden'

**`GenParamValue`** (input_control)  number(-array) `→`  (real / integer / string)

Values of generic parameters to configure the
selection process and the classifier.

Default:
[]

Suggested values:
50, 80, 100

**`MLPHandle`** (output_control)  class_mlp `→`  (handle)

A trained MLP classifier using only the selected
features.

**`SelectedFeatureIndices`** (output_control)  string-array `→`  (string)

The selected feature set, contains
indices referring.

**`Score`** (output_control)  real-array `→`  (real)

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
* Select the better feature with a MLP
select_feature_set_mlp (ClassTrainDataHandle, 'greedy', [], [], MLPHandle,\
  SelectedFeatureMLP, Score)
* Use the classifier
* ...
```

## Result

If the parameters are valid, the operator `select_feature_set_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`,
`add_sample_class_train_data`,
`set_feature_lengths_class_train_data`

## Possible Successors

`classify_class_mlp`

## Alternatives

`select_feature_set_knn`,
`select_feature_set_svm`,
`select_feature_set_gmm`

## See also

`select_feature_set_trainf_mlp`,
`gray_features`,
`region_features`

## Module

Foundation
