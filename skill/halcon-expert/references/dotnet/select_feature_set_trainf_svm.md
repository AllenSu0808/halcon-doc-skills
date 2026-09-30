# SelectFeatureSetTrainfSvm (Operator)

## Name

`SelectFeatureSetTrainfSvm` — Selects an optimal combination of features to classify OCR data.

## Signature

`static void HOperatorSet.SelectFeatureSetTrainfSvm(HTuple trainingFile, HTuple featureList, HTuple selectionMethod, HTuple width, HTuple height, HTuple genParamName, HTuple genParamValue, out HTuple OCRHandle, out HTuple featureSet, out HTuple score)`

`HTuple HOCRSvm.SelectFeatureSetTrainfSvm(HTuple trainingFile, HTuple featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

`HTuple HOCRSvm.SelectFeatureSetTrainfSvm(string trainingFile, string featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

`SelectFeatureSetTrainfSvm` selects an optimal combination of
features, to classify the data given in the training file
*`trainingFile`* with a Support Vector Machine (SVM),
for details see [`CreateOcrClassSvm`](create_ocr_class_svm.md).

Possible features are all OCR features listed and explained in
[`CreateOcrClassSvm`](create_ocr_class_svm.md). All candidates which should be tested can be
specified in *`featureList`*. A subset of these features is
returned as selected features in *`featureSet`*.

`SelectFeatureSetTrainfSvm` is specialized on OCR problems and
only supports the features in the list mentioned before.
In order to use other features, please use the more general operator
[`SelectFeatureSetSvm`](select_feature_set_svm.md).

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

The parameters *"nu"* and *"gamma"* for the SVM that is used
to classify can be set to *"auto"* by using the
parameters *`genParamName`* and *`genParamValue`*. If they are
set to *"auto"*, the estimated optimal *"nu"* and/or
*"gamma"* is estimated. The automatic estimation of *"nu"*
and *"gamma"* can take a substantial amount of time (up to days,
depending on the data set and the number of features). Alternatively,
a certain value for both can be set the same way.
An explanation of the parameters *"nu"* and
*"gamma"* as the kernel parameter of the radial basis function (RBF)
kernel can be found in [`CreateClassSvm`](create_class_svm.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `SelectFeatureSetTrainfSvm` may deliver a classifier with
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
"gamma", "nu"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of generic parameters to configure the selection
process and the classifier.

Default:
[]

Suggested values:
"auto", "0.1", "0.3"

**`OCRHandle`** (output_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Trained OCR-SVM Classifier.

**`featureSet`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Selected feature set, contains only entries from
*`featureList`*.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Achieved score using tow-fold cross-validation.

## Result

If the parameters are valid, the operator
`SelectFeatureSetTrainfSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Alternatives

`SelectFeatureSetTrainfMlp`,
`SelectFeatureSetTrainfKnn`,
`SelectFeatureSetTrainfMlpProtected`

## See also

`SelectFeatureSetTrainfSvmProtected`,
`SelectFeatureSetSvm`

## Module

OCR/OCV
