# SelectFeatureSetTrainfMlp (Operator)

## Name

`SelectFeatureSetTrainfMlp` — Selects an optimal combination of features to classify OCR data.

## Signature

`static void HOperatorSet.SelectFeatureSetTrainfMlp(HTuple trainingFile, HTuple featureList, HTuple selectionMethod, HTuple width, HTuple height, HTuple genParamName, HTuple genParamValue, out HTuple OCRHandle, out HTuple featureSet, out HTuple score)`

`HTuple HOCRMlp.SelectFeatureSetTrainfMlp(HTuple trainingFile, HTuple featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

`HTuple HOCRMlp.SelectFeatureSetTrainfMlp(string trainingFile, string featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

`SelectFeatureSetTrainfMlp` selects an optimal combination of
features, to classify the OCR data given in the training file
*`trainingFile`* with a multilayer perceptron,
for details see [`CreateOcrClassMlp`](create_ocr_class_mlp.md).

Possible features are all OCR features listed and explained in
[`CreateOcrClassMlp`](create_ocr_class_mlp.md). All candidates which should be tested can be
specified in *`featureList`*. A subset of these features is
returned as selected features in *`featureSet`*.

`SelectFeatureSetTrainfMlp` is specialized on OCR problems and
only supports the features in the list mentioned before.
In order to use other features, please use the more general operator
[`SelectFeatureSetMlp`](select_feature_set_mlp.md).

The selection method
*`selectionMethod`* is either a greedy search *"greedy"*
(iteratively add the feature with highest gain)
or the dynamically oscillating search *"greedy_oscillating"*
(add the feature with highest gain and test then if any of the already added
features can be left out without great loss).
The method *"greedy"* is generally preferable, since it is faster.
Only in cases when a large training set is available
the method *"greedy_oscillating"* might return better results.

The optimization criterion is the classification rate of a two-fold
cross-validation of the training data. The best achieved value
is returned in *`score`*.

The parameters *`genParamName`* and *`genParamValue`* allow
to adapt the setting of the number of hidden neurons in the MLP with
*"num_hidden"*. The default value is *80*, a higher value
leads to longer training times but might lead to a more expressive
classifier.

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `SelectFeatureSetTrainfMlp` may deliver a classifier with
a very high score. However, the classifier may perform poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`featureList`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

List of features that should be considered for selection.

Default:
["zoom_factor","ratio","width","height","foreground","foreground_grid_9","foreground_grid_16","anisometry","compactness","convexity","moments_region_2nd_invar","moments_region_2nd_rel_invar","moments_region_3rd_invar","moments_central","phi","num_connect","num_holes","projection_horizontal","projection_vertical","projection_horizontal_invar","projection_vertical_invar","chord_histo","num_runs","pixel","pixel_invar","pixel_binary","gradient_8dir","cooc","moments_gray_plane"]

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`selectionMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to perform the selection.

Default:
"greedy"

List of values:
"greedy", "greedy_oscillating"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
15

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
16

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of generic parameters to configure the selection
process and the classifier.

Default:
[]

List of values:
"nu"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of generic parameters to configure the selection
process and the classifier.

Default:
[]

Suggested values:
"0.1"

**`OCRHandle`** (output_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Trained OCR-MLP classifier.

**`featureSet`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Selected feature set, contains only entries from
*`featureList`*.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Achieved score using tow-fold cross-validation.

## Result

If the parameters are valid, the operator
`SelectFeatureSetTrainfMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Alternatives

`SelectFeatureSetTrainfSvm`,
`SelectFeatureSetTrainfKnn`

## See also

`SelectFeatureSetTrainfMlpProtected`,
`SelectFeatureSetMlp`

## Module

OCR/OCV
