# CreateClassMlp (Operator)

## Name

`CreateClassMlp` — Create a multilayer perceptron for classification or regression.

## Signature

`static void HOperatorSet.CreateClassMlp(HTuple numInput, HTuple numHidden, HTuple numOutput, HTuple outputFunction, HTuple preprocessing, HTuple numComponents, HTuple randSeed, out HTuple MLPHandle)`

`public HClassMlp(int numInput, int numHidden, int numOutput, string outputFunction, string preprocessing, int numComponents, int randSeed)`

`void HClassMlp.CreateClassMlp(int numInput, int numHidden, int numOutput, string outputFunction, string preprocessing, int numComponents, int randSeed)`

## Description

`CreateClassMlp` creates a neural net in the form of a
multilayer perceptron (MLP), which can be used for classification or
regression (function approximation), depending on how
*`outputFunction`* is set. The MLP consists of three layers:
an input layer with *`numInput`* input variables (units,
neurons), a hidden layer with *`numHidden`* units, and an
output layer with *`numOutput`* output variables. The MLP
performs the following steps to calculate the activations
$z_{j}$ of the hidden units from the input data
$x_{i}$ (the so-called feature vector):
$$a_j^{(1)} = \sum_{i=1}^{n_i} w_{j i}^{(1)} x_i + b_j^{(1)}, \quad j = 1, \dots, n_h z_j = \tanh(a_j^{(1)}), \quad j = 1, \dots, n_h$$ ![figure](../assets/3e49258c822e7b93.svg)
Here, the matrix $w_{ji}^{(1)}$ and the vector
$b_{j}^{(1)}$ are the weights of the input layer (first
layer) of the MLP. In the hidden layer (second layer), the
activations $z_{j}$ are transformed in a first step by
using linear combinations of the variables in an analogous manner as
above:
$$a_k^{(2)} = \sum_{j=1}^{n_o} w_{kj}^{(2)} z_j + b_k^{(2)}, \quad k = 1, \dots, n_o$$ ![figure](../assets/4a0f975ebe01ecf3.svg)
Here, the matrix $w_{kj}^{(2)}$ and the vector
$b_{k}^{(2)}$ are the weights of the second layer of
the MLP.

The activation function used in the output layer can be determined
by setting *`outputFunction`*. For *`outputFunction`* =
*"linear"*, the data are simply copied:
$$y_{k}=a_{k}^{(2)},k=1,...,n_{o}$$
This type of activation function should be used for regression
problems (function approximation). This activation function is not
suited for classification problems.

For *`outputFunction`* = *"logistic"*, the activations
are computed as follows:
$$y_k = \frac{1}{1 + \exp(-a_k^{(2)})}, \quad k = 1, \dots, n_0$$ ![figure](../assets/90fded2c4aa53ec0.svg)
This type of activation function should be used for classification
problems with multiple (*`numOutput`*) independent logical
attributes as output. This kind of classification problem is
relatively rare in practice.

For *`outputFunction`* = *"softmax"*, the activations
are computed as follows:
$$y_k = \frac{\exp(a_k^{(2)})}{\sum_{l=1}^{n_o} \exp(a_l^{(2)})}, \quad k = 1, \dots, n_o$$ ![figure](../assets/bfecd7ff709f28b4.svg)

This type of activation function should be used for common
classification problems with multiple (*`numOutput`*) mutually
exclusive classes as output. In particular, *`outputFunction`*
= *"softmax"* must be used for the classification of pixel
data with [`ClassifyImageClassMlp`](classify_image_class_mlp.md).

The parameters *`preprocessing`* and *`numComponents`* can
be used to specify a preprocessing of the feature vectors. For
*`preprocessing`* = *"none"*, the feature vectors are
passed unaltered to the MLP. *`numComponents`* is ignored in
this case.

For all other values of *`preprocessing`*, the training data
set is used to compute a transformation of the feature vectors
during the training as well as later in the classification or
evaluation.

For *`preprocessing`* = *"normalization"*, the feature
vectors are normalized by subtracting the mean of the training
vectors and dividing the result by the standard deviation of the
individual components of the training vectors. Hence, the
transformed feature vectors have a mean of 0 and a standard
deviation of 1. The normalization does not change the length of the
feature vector. *`numComponents`* is ignored in this case.
This transformation can be used if the mean and standard deviation
of the feature vectors differs substantially from 0 and 1,
respectively, or for data in which the components of the feature
vectors are measured in different units (e.g., if some of the data
are gray value features and some are region features, or if region
features are mixed, e.g., `'circularity'` (unit: scalar) and
`'area'` (unit: pixel squared)). In these cases, the training
of the net will typically require fewer iterations than without
normalization.

For *`preprocessing`* = *"principal_components"*, a
principal component analysis is performed. First, the feature
vectors are normalized (see above). Then, an orthogonal
transformation (a rotation in the feature space) that decorrelates
the training vectors is computed. After the transformation, the
mean of the training vectors is 0 and the covariance matrix of the
training vectors is a diagonal matrix. The transformation is chosen
such that the transformed features that contain the most variation
is contained in the first components of the transformed feature
vector. With this, it is possible to omit the transformed features
in the last components of the feature vector, which typically are
mainly influenced by noise, without losing a large amount of
information. The parameter *`numComponents`* can be used to
determine how many of the transformed feature vector components
should be used. Up to *`numInput`* components can be selected.
The operator [`GetPrepInfoClassMlp`](get_prep_info_class_mlp.md) can be used to
determine how much information each transformed component contains.
Hence, it aids the selection of *`numComponents`*. Like data
normalization, this transformation can be used if the mean and
standard deviation of the feature vectors differs substantially from
0 and 1, respectively, or for feature vectors in which the
components of the data are measured in different units. In
addition, this transformation is useful if it can be expected that
the features are highly correlated.

In contrast to the above three transformations, which can be used
for all MLP types, the transformation specified by
*`preprocessing`* = *"canonical_variates"* can only be
used if the MLP is used as a classifier with *`outputFunction`*
= *"softmax"*). The computation of the canonical variates
is also called linear discriminant analysis. In this case, a
transformation that first normalizes the training vectors and then
decorrelates the training vectors on average over all classes is
computed. At the same time, the transformation maximally separates
the mean values of the individual classes. As for
*`preprocessing`* = *"principal_components"*, the
transformed components are sorted by information content, and hence
transformed components with little information content can be
omitted. For canonical variates, up to min(*`numOutput`* -
1, *`numInput`*) components can be selected. Also in this
case, the information content of the transformed components can be
determined with [`GetPrepInfoClassMlp`](get_prep_info_class_mlp.md). Like principal
component analysis, canonical variates can be used to reduce the
amount of data without losing a large amount of information, while
additionally optimizing the separability of the classes after the
data reduction.

For the last two types of transformations
(*"principal_components"* and *"canonical_variates"*),
the actual number of input units of the MLP is determined by
*`numComponents`*, whereas *`numInput`* determines the
dimensionality of the input data (i.e., the length of the
untransformed feature vector). Hence, by using one of these two
transformations, the number of input variables, and thus usually
also the number of hidden units can be reduced. With this, the time
needed to train the MLP and to evaluate and classify a feature
vector is typically reduced.

Usually, *`numHidden`* should be selected in the order of
magnitude of *`numInput`* and *`numOutput`*. In many
cases, much smaller values of *`numHidden`* already lead to
very good classification results. If *`numHidden`* is chosen
too large, the MLP may overfit the training data, which typically
leads to bad generalization properties, i.e., the MLP learns the
training data very well, but does not return very good results on
unknown data.

`CreateClassMlp` initializes the above described weights
with random numbers. To ensure that the results of training the
classifier with [`TrainClassMlp`](train_class_mlp.md) are reproducible, the seed
value of the random number generator is passed in *`randSeed`*.
If the training results in a relatively large error, it sometimes
may be possible to achieve a smaller error by selecting a different
value for *`randSeed`* and retraining an MLP.

After the MLP has been created, typically training samples are added
to the MLP by repeatedly calling [`AddSampleClassMlp`](add_sample_class_mlp.md) or
[`ReadSamplesClassMlp`](read_samples_class_mlp.md). After this, the MLP is typically
trained using [`TrainClassMlp`](train_class_mlp.md). Hereafter, the MLP can be
saved using [`WriteClassMlp`](write_class_mlp.md). Alternatively, the MLP can be
used immediately after training to evaluate data using
[`EvaluateClassMlp`](evaluate_class_mlp.md) or, if the MLP is used as a classifier
(i.e., for *`outputFunction`* = *"softmax"*), to
classify data using [`ClassifyClassMlp`](classify_class_mlp.md).

The training of the MLP will usually result in very sharp boundaries
between the different classes, i.e., the confidence for one class
will drop from close to 1 (within the region of the class) to close
to 0 (within the region of a different class) within a very narrow
“band” in the feature space. If the classes do not overlap, this
transition happens at a suitable location between the classes; if
the classes overlap, the transition happens at a suitable location
within the overlapping area. While this sharp transition is
desirable in many applications, in some applications a smoother
transition between different classes (i.e., a transition within a
wider “band” in the feature space) is desirable to reflect a level
of uncertainty within the region in the feature space between the
classes. Furthermore, as described above, it may be desirable to
prevent overfitting of the MLP to the training data. For these
purposes, the MLP can be regularized by using
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md).

An MLP, as defined above, has no inherent capability for novelty
detection, i.e., it will classify a random feature vector into one
of the classes with a confidence close to 1 (unless the random
feature vector happens to lie in a region of the feature space in
which the training samples of different classes overlap). In some
applications, however, it is desirable to reject feature vectors
that do not lie close to any class, where “closesness” defined by
the proximity of the feature vector to the collection of feature
vectors in the training set. To provide an MLP with the ability for
novelty detection, i.e., to reject feature vectors that do not
belong to any class, an explicit rejection class can be created by
setting *`numOutput`* to the number of actual classes plus 1.
Then, [`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md) can be used to
configure [`TrainClassMlp`](train_class_mlp.md) to automatically generate samples
for this rejection class.

The combination of regularization and an automatic generation of a
rejection class is useful in many applications since it provides a
smooth transition between the actual classes and from the actual
classes to the rejection class. This reflects the requirement of
these applications that only feature vectors within the area of the
feature space that corresponds to the training samples of each class
should have a confidence close to 1, whereas random feature vectors
not belonging to any class should have a confidence close to 0, and
that transitions between the classes should be smooth, reflecting a
growing degree of uncertainty the farther a feature vector lies from
the respective class. In particular, OCR applications sometimes
have this requirement (see [`CreateOcrClassMlp`](create_ocr_class_mlp.md)).

A comparison of the MLP and the support vector machine (SVM) (see
[`CreateClassSvm`](create_class_svm.md)) typically shows that SVMs are generally
faster at training, especially for huge training sets, and achieve
slightly better recognition rates than MLPs. The MLP is faster at
classification and should therefore be preferred in time critical
applications. Please note that this guideline assumes optimal
tuning of the parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`numInput`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of input variables (features) of the MLP.

Default:
20

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumInput >= 1`

**`numHidden`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of hidden units of the MLP.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150

Restriction:
`NumHidden >= 1`

**`numOutput`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of output variables (classes) of the MLP.

Default:
5

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150

Restriction:
`NumOutput >= 1`

**`outputFunction`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the activation function in the output
layer of the MLP.

Default:
"softmax"

List of values:
"linear", "logistic", "softmax"

**`preprocessing`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

Default:
"normalization"

List of values:
"canonical_variates", "none", "normalization", "principal_components"

**`numComponents`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`* =
*"none"* and *`preprocessing`* =
*"normalization"*).

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumComponents >= 1`

**`randSeed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seed value of the random number generator that
is used to initialize the MLP with random values.

Default:
42

**`MLPHandle`** (output_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Example (HDevelop)

```
* Use the MLP for regression (function approximation)
create_class_mlp (1, NumHidden, 1, 'linear', 'none', 1, 42, MLPHandle)
* Generate the training data
* D = [...]
* T = [...]
* Add the training data
for J := 0 to NumData-1 by 1
    add_sample_class_mlp (MLPHandle, D[J], T[J])
endfor
* Train the MLP
train_class_mlp (MLPHandle, 200, 0.001, 0.001, Error, ErrorLog)
* Generate test data
* X = [...]
* Compute the output of the MLP on the test data
for J := 0 to N-1 by 1
    evaluate_class_mlp (MLPHandle, X[J], Y)
endfor

* Use the MLP for classification
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'normalization', NumIn, 42, MLPHandle)
* Generate and add the training data
for J := 0 to NumData-1 by 1
    * Generate training features and classes
    * Data = [...]
    * Class = [...]
    add_sample_class_mlp (MLPHandle, Data, Class)
endfor
* Train the MLP
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
* Use the MLP to classify unknown data
for J := 0 to N-1 by 1
    * Extract features
    * Features = [...]
    classify_class_mlp (MLPHandle, Features, 1, Class, Confidence)
endfor
```

## Result

If the parameters are valid, the operator `CreateClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`AddSampleClassMlp`,
`SetRegularizationParamsClassMlp`,
`SetRejectionParamsClassMlp`

## Alternatives

`ReadDlModel`,
`CreateClassSvm`,
`CreateClassGmm`

## See also

`ClearClassMlp`,
`TrainClassMlp`,
`ClassifyClassMlp`,
`EvaluateClassMlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
