# create_class_svm (Operator)

## Name

`create_class_svm` — Create a support vector machine for pattern classification.

## Signature

`create_class_svm( : : NumFeatures, KernelType, KernelParam, Nu, NumClasses, Mode, Preprocessing, NumComponents : SVMHandle)`

## Description

`create_class_svm` creates a support vector machine that can
be used for pattern classification. The dimension of the patterns
to be classified is specified in *`NumFeatures`*, the number of
different classes in *`NumClasses`*.

For a binary classification problem in which the classes are
linearly separable the SVM algorithm selects data vectors from the
training set that are utilized to construct the optimal separating
hyperplane between different classes. This hyperplane is optimal in
the sense that the margin between the convex hulls of the different
classes is maximized. The training patterns that are located at the
margin define the hyperplane and are called *support vectors* (SV).

Classification of a feature vector z is performed with the
following formula:
$$f(z) = \mathrm{sign}\left(\sum_{i=1}^{n_{sv}} \alpha_i y_i \langle x_i, z \rangle + b\right)$$ ![figure](../assets/7a6afd6274dfc313.svg)
Here, $x_{i}$ are the support vectors, $y_{i}$
encodes their class membership ($\pm1$) and
$\alpha_{i}$ the weight coefficients. The distance of
the hyperplane to the origin is b. The $\alpha$ and b
are determined during training with [`train_class_svm`](train_class_svm.md). Note
that only a subset of the original training set ($n_{sv}$: number
of support vectors) is necessary for the definition of the decision boundary
and therefore data vectors that are not support vectors are discarded. The
classification speed depends on the evaluation of the dot product between
support vectors and the feature vector to be classified, and hence depends on
the length of the feature vector and the number $n_{sv}$ of support
vectors.

For classification problems in which the classes are not linearly
separable the algorithm is extended in two ways. First, during
training a certain amount of errors (overlaps) is compensated with
the use of slack variables. This means that the $\alpha$
are upper bounded by a regularization constant. To enable an
intuitive control of the amount of training errors, the
*Nu*-SVM version of the training algorithm is used. Here, the
regularization parameter *`Nu`* is an asymptotic upper bound on
the number of training errors and an asymptotic lower bound on the
number of support vectors. As a rule of thumb, the parameter
*`Nu`* should be set to the prior expectation of the
application's specific error ratio, e.g., *0.01*
(corresponding to a maximum training error of 1%). Please note
that a too big value for *`Nu`* might lead to an infeasible
training problem, i.e., the SVM cannot be trained correctly (see
[`train_class_svm`](train_class_svm.md) for more details). Since this can only be
determined during training, an exception can only be raised there.
In this case, a new SVM with *`Nu`* chosen smaller must be
created.

Second, because the above SVM exclusively calculates dot products
between the feature vectors, it is possible to incorporate a kernel
function into the training and testing algorithm. This means that
the dot products are substituted by a kernel function, which
implicitly performs the dot product in a higher dimensional feature
space. Given the appropriate kernel transformation, an originally
not linearly separable classification task becomes linearly
separable in the higher dimensional feature space.

Different kernel functions can be selected with the parameter
*`KernelType`*. For *`KernelType`* = *'linear'* the dot
product, as specified in the above formula is calculated. This kernel should
solely be used for linearly or nearly linearly separable
classification tasks. The parameter *`KernelParam`* is ignored
here.

The radial basis function (RBF) *`KernelType`* =
*'rbf'* is the best choice for a kernel function because it
achieves good results for many classification tasks. It is defined
as:
$$K\left(x,z\right) = e^{-\gamma}\cdot\|x-z\|^{2}$$ ![figure](../assets/1876ba5ca53ae92e.svg)
Here, the parameter *`KernelParam`* is used to select
$\gamma$. The intuitive meaning of $\gamma$ is
the amount of influence of a support vector upon its surroundings. A big
value of $\gamma$ (small influence on the surroundings) means that
each training vector becomes a support vector. The training algorithm learns
the training data “by heart”, but lacks any generalization ability
(over-fitting). Additionally, the training/classification times grow
significantly. A too small value for $\gamma$ (big influence on
the surroundings) leads to few support vectors defining the separating
hyperplane (under-fitting). One typical strategy is to select a
small $\gamma$-*`Nu`* pair and consecutively
increase the values as long as the recognition rate increases.

With *`KernelType`* = *'polynomial_homogeneous'* or
*'polynomial_inhomogeneous'*, polynomial kernels can be
selected. They are defined in the following way:
$$K(x,z) = (<x,z>)^{d} K(x,z) = (<x,z> + 1)^{d}$$ ![figure](../assets/878e917b6ca2f811.svg)
The degree of the polynomial kernel must be set with
*`KernelParam`*. Please note that a too high degree polynomial
(d > 10) might result in numerical problems.

As a rule of thumb, the RBF kernel provides a good choice for most
of the classification problems and should therefore be used in
almost all cases. Nevertheless, the linear and polynomial kernels
might be better suited for certain applications and can be tested
for comparison. Please note that the novelty-detection *`Mode`*
and the operator [`reduce_class_svm`](reduce_class_svm.md) are provided only for the RBF
kernel.

*`Mode`* specifies the general classification task, which is
either how to break down a multi-class decision problem to binary
sub-cases or whether to use a special classifier mode called
*'novelty-detection'*. *`Mode`* =
*'one-versus-all'* creates a classifier where each class is
compared to the rest of the training data. During testing the
class with the largest output (see the classification formula
without sign) is chosen. *`Mode`* = *'one-versus-one'*
creates a binary classifier between each single class. During
testing a vote is cast and the class with the majority of the votes
is selected. The optimal *`Mode`* for multi-class
classification depends on the number of classes. Given n classes
*'one-versus-all'* creates n classifiers, whereas
*'one-versus-one'* creates n(n-1)/2. Note that for a binary
decision task *'one-versus-one'* would create exactly one,
whereas *'one-versus-all'* unnecessarily creates two
symmetric classifiers. For few classes (approximately up to 10)
*'one-versus-one'* is faster for training and testing, because
the sub-classifier all consist of fewer training data and result in
overall fewer support vectors. In case of many classes
*'one-versus-all'* is preferable, because
*'one-versus-one'* generates a prohibitively large amount of
sub-classifiers, as their number increases to the square of the number
of classes.

A special case of classification is *`Mode`* =
*'novelty-detection'*, where the test data is classified
only with regard to membership to the training data,
i.e., *`NumClasses`* must be set to 1. The separating
hyperplane lies around the training data and thereby implicitly
divides the training data from the rejection class. The advantage is
that the rejection class is not defined explicitly, which is
difficult to do in certain applications like texture classification. The
resulting support vectors are all lying at the border. With the
parameter *`Nu`*, the ratio of outliers in the training data set is
specified. Note, that when classifying in the *'novelty-detection'*
mode, the class of the training data is returned with index 1 and
the rejection class is returned with index 0. Thus, the first class
serves as rejection class. In contrast, when using the MLP
classifier, the last class serves as rejection class by default.

The parameters *`Preprocessing`* and *`NumComponents`* can
be used to specify a preprocessing of the feature vectors. For
*`Preprocessing`* = *'none'*, the feature vectors are
passed unaltered to the SVM. *`NumComponents`* is ignored in
this case.

For all other values of *`Preprocessing`*, the training data
set is used to compute a transformation of the feature vectors
during the training as well as later in the classification.

For *`Preprocessing`* = *'normalization'*, the feature
vectors are normalized. In case of a polynomial kernel, the minimum
and maximum value of the training data set is transformed to -1 and
+1. In case of the RBF kernel, the data is normalized by subtracting
the mean of the training vectors and dividing the result by the
standard deviation of the individual components of the training
vectors. Hence, the transformed feature vectors have a mean of 0
and a standard deviation of 1. The normalization does not change
the length of the feature vector. *`NumComponents`* is ignored
in this case. This transformation can be used if the mean and
standard deviation of the feature vectors differs substantially from
0 and 1, respectively, or for data in which the components of the
feature vectors are measured in different units (e.g., if some of
the data are gray value features and some are region features, or if
region features are mixed, e.g., `'circularity'` (unit: scalar) and
`'area'` (unit: pixel squared)). The normalization transformation
should be performed in general, because it increases the numerical
stability during training/testing.

For *`Preprocessing`* = *'principal_components'*, a
principal component analysis (PCA) is performed. First, the feature
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
information. The parameter *`NumComponents`* can be used to
determine how many of the transformed feature vector components
should be used. Up to *`NumFeatures`* components can be
selected. The operator [`get_prep_info_class_svm`](get_prep_info_class_svm.md) can be used
to determine how much information each transformed component
contains. Hence, it aids the selection of *`NumComponents`*.
Like data normalization, this transformation can be used if the mean
and standard deviation of the feature vectors differs substantially
from 0 and 1, respectively, or for feature vectors in which the
components of the data are measured in different units. In
addition, this transformation is useful if it can be expected that
the features are highly correlated. Please note that the RBF kernel
is very robust against the dimensionality reduction performed by PCA
and should therefore be the first choice when speeding up the
classification time.

The transformation specified by *`Preprocessing`* =
*'canonical_variates'* first normalizes the training vectors
and then decorrelates the training vectors on average over all
classes. At the same time, the transformation maximally separates
the mean values of the individual classes. As for
*`Preprocessing`* = *'principal_components'*, the
transformed components are sorted by information content, and hence
transformed components with little information content can be
omitted. For canonical variates, up to min(*`NumClasses`*-1,
*`NumFeatures`*) components can be selected. Also in this
case, the information content of the transformed components can be
determined with [`get_prep_info_class_svm`](get_prep_info_class_svm.md). Like principal
component analysis, canonical variates can be used to reduce the
amount of data without losing a large amount of information, while
additionally optimizing the separability of the classes after the
data reduction. The computation of the canonical variates is also
called linear discriminant analysis.

For the last two types of transformations
(*'principal_components'* and *'canonical_variates'*),
the length of input data of the SVM is determined by
*`NumComponents`*, whereas *`NumFeatures`* determines the
dimensionality of the input data (i.e., the length of the
untransformed feature vector). Hence, by using one of these two
transformations, the size of the SVM with respect to data length is
reduced, leading to shorter training/classification times by the
SVM.

After the SVM has been created with `create_class_svm`,
typically training samples are added to the SVM by repeatedly
calling [`add_sample_class_svm`](add_sample_class_svm.md) or
[`read_samples_class_svm`](read_samples_class_svm.md). After this, the SVM is typically
trained using [`train_class_svm`](train_class_svm.md). Hereafter, the SVM can be
saved using [`write_class_svm`](write_class_svm.md). Alternatively, the SVM can be
used immediately after training to classify data using
[`classify_class_svm`](classify_class_svm.md).

A comparison of the SVM and the multi-layer perceptron (MLP) (see
[`create_class_mlp`](create_class_mlp.md)) typically shows that SVMs are generally
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

**`NumFeatures`** (input_control)  integer `→`  (integer)

Number of input variables (features) of the SVM.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumFeatures >= 1`

**`KernelType`** (input_control)  string `→`  (string)

The kernel type.

Default:
'rbf'

List of values:
'linear', 'polynomial_homogeneous', 'polynomial_inhomogeneous', 'rbf'

**`KernelParam`** (input_control)  real `→`  (real)

Additional parameter for the kernel function.
In case of RBF kernel the value for
$\gamma$. For polynomial kernel the
degree

Default:
0.02

Suggested values:
0.01, 0.02, 0.05, 0.1, 0.5

**`Nu`** (input_control)  real `→`  (real)

Regularization constant of the SVM.

Default:
0.05

Suggested values:
0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.3

Restriction:
`Nu > 0.0 && Nu < 1.0`

**`NumClasses`** (input_control)  integer `→`  (integer)

Number of classes.

Default:
5

Suggested values:
2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`NumClasses >= 1`

**`Mode`** (input_control)  string `→`  (string)

The mode of the SVM.

Default:
'one-versus-one'

List of values:
'novelty-detection', 'one-versus-all', 'one-versus-one'

**`Preprocessing`** (input_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

Default:
'normalization'

List of values:
'canonical_variates', 'none', 'normalization', 'principal_components'

**`NumComponents`** (input_control)  integer `→`  (integer)

Preprocessing parameter: Number of transformed
features (ignored for *`Preprocessing`* =
*'none'* and *`Preprocessing`* =
*'normalization'*).

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumComponents >= 1`

**`SVMHandle`** (output_control)  class_svm `→`  (handle)

SVM handle.

## Example (HDevelop)

```
create_class_svm (NumFeatures, 'rbf', 0.01, 0.01, NumClasses,\
                  'one-versus-all', 'normalization', NumFeatures,\
                  SVMHandle)
* Generate and add the training data
for J := 0 to NumData-1 by 1
    * Generate training features and classes
    * Data = [...]
    * Class = ...
    add_sample_class_svm (SVMHandle, Data, Class)
endfor
* Train the SVM
train_class_svm (SVMHandle, 0.001, 'default')
* Use the SVM to classify unknown data
for J := 0 to N-1 by 1
    * Extract features
    * Features = [...]
    classify_class_svm (SVMHandle, Features, 1, Class)
endfor
```

## Result

If the parameters are valid the operator `create_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`add_sample_class_svm`

## Alternatives

`read_dl_model`,
`create_class_mlp`,
`create_class_gmm`

## See also

`clear_class_svm`,
`train_class_svm`,
`classify_class_svm`

## References

Bernhard Schölkopf, Alexander J.Smola: “Learning with Kernels”;
MIT Press, London; 1999.
  
John Shawe-Taylor, Nello Cristianini: “Kernel Methods for Pattern
Analysis”; Cambridge University Press, Cambridge; 2004.

## Module

Foundation
