# SelectFeatureSetMlp (Operator)

## Name

`SelectFeatureSetMlp` — Selects an optimal combination of features to classify the provided data.

## Signature

`static void HOperatorSet.SelectFeatureSetMlp(HTuple classTrainDataHandle, HTuple selectionMethod, HTuple genParamName, HTuple genParamValue, out HTuple MLPHandle, out HTuple selectedFeatureIndices, out HTuple score)`

`HTuple HClassMlp.SelectFeatureSetMlp(HClassTrainData classTrainDataHandle, string selectionMethod, HTuple genParamName, HTuple genParamValue, out HTuple score)`

`HTuple HClassMlp.SelectFeatureSetMlp(HClassTrainData classTrainDataHandle, string selectionMethod, string genParamName, double genParamValue, out HTuple score)`

`HClassMlp HClassTrainData.SelectFeatureSetMlp(string selectionMethod, HTuple genParamName, HTuple genParamValue, out HTuple selectedFeatureIndices, out HTuple score)`

`HClassMlp HClassTrainData.SelectFeatureSetMlp(string selectionMethod, string genParamName, double genParamValue, out HTuple selectedFeatureIndices, out HTuple score)`

## Description

`SelectFeatureSetMlp` selects an optimal subset from a set of
features to solve a given classification problem.
The classification problem has to be specified with annotated training data
in *`classTrainDataHandle`* and will be classified by a
Multilayer Perceptron. Details of the properties of this
classifier can be found in [`CreateClassMlp`](create_class_mlp.md).

The result of the operator is a trained classifier that is returned in
*`MLPHandle`*. Additionally, the list of indices or names of the
selected features
is returned in *`selectedFeatureIndices`*. To use this classifier,
calculate for new input data all features mentioned in
*`selectedFeatureIndices`* and pass them to the classifier.

A possible application of this operator can be a comparison of
different parameter sets for certain feature extraction techniques. Another
application is to search for a feature that is discriminating between
different classes.

To define the features that should be selected from
*`classTrainDataHandle`*, the dimensions of the
feature vectors in *`classTrainDataHandle`* can be grouped into
subfeatures by calling [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md).
A subfeature can contain several subsequent elements of a feature vector.
`SelectFeatureSetMlp` decides for each of these subfeatures,
if it is better to use it for the classification or leave it out.

The indices of the selected subfeatures are returned in
*`selectedFeatureIndices`*.
If names were set in [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md), these
names are returned instead of the indices.
If [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md) was not called for
*`classTrainDataHandle`* before, each element of the feature vector
is considered as a subfeature.

The selection method
*`selectionMethod`* is either a greedy search *"greedy"*
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

With *`genParamName`* and *`genParamValue`* the number
of hidden layer can be set by
*"num_hidden"*. The default value is *80*. Larger values
for this parameter lead to longer classification times, while it allows
a more expressive classifier.

## Attention

This operator may take considerable time, depending on the size of the
data and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `SelectFeatureSetMlp` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

**`selectionMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to perform the selection.

Default:
"greedy"

List of values:
"greedy", "greedy_oscillating"

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of generic parameters to configure the
selection process and the classifier.

Default:
[]

List of values:
"num_hidden"

**`genParamValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of generic parameters to configure the
selection process and the classifier.

Default:
[]

Suggested values:
50, 80, 100

**`MLPHandle`** (output_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

A trained MLP classifier using only the selected
features.

**`selectedFeatureIndices`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The selected feature set, contains
indices referring.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

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

If the parameters are valid, the operator `SelectFeatureSetMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassTrainData`,
`AddSampleClassTrainData`,
`SetFeatureLengthsClassTrainData`

## Possible Successors

`ClassifyClassMlp`

## Alternatives

`SelectFeatureSetKnn`,
`SelectFeatureSetSvm`,
`SelectFeatureSetGmm`

## See also

`SelectFeatureSetTrainfMlp`,
`GrayFeatures`,
`RegionFeatures`

## Module

Foundation
