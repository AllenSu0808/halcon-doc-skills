# create_class_gmm (Operator)

## Name

`create_class_gmm` — Create a Gaussian Mixture Model for classification

## Signature

`def create_class_gmm(num_dim: int, num_classes: int, num_centers: MaybeSequence[int], covar_type: str, preprocessing: str, num_components: int, rand_seed: int) -> HHandle`

## Description

`create_class_gmm` creates a Gaussian Mixture Model (GMM) for
classification. *`num_dim`* specifies the number of dimensions
of the feature space, *`num_classes`* specifies the number of
classes. A GMM consists of *`num_centers`* *Gaussian
centers* per class. *`num_centers`* can not only be the exact
number of centers to be used, but, depending on the number of
parameters, can specify upper and lower bounds for the number of
centers:

- **exactly one parameter:** —

  The parameter determines the exact
  number of centers to be used for all classes.
- **exactly two parameters:** —

  The first parameter determines the
  minimum number of centers, the second determines the maximum
  number of centers for all classes.
- **exactly $2\cdot NumClasses$ parameters:** —

  Alternatingly every first parameter determines the minimum number of
  centers per class and every second parameters determines the maximum
  number of centers per class.

When upper and lower bounds are specified, the optimum number of
centers will be determined with the help of the Minimum Message
Length Criterion (MML). In general, we recommend to start the
training with (too) many centers as maximum and the
expected number of centers as minimum.

Each center is described by the parameters center $\mathbf{m}_{j}$, covariance matrix $\mathbf{C}_{j}$, and mixing
coefficient $P_{j}$. These parameters are calculated from
the training data by means of the Expectation Maximization (EM)
algorithm. A GMM can approximate an arbitrary probability density,
provided that enough centers are being used. The covariance matrices
$\mathbf{C}_{j}$ have the dimensions *`num_dim`*
x *`num_dim`* (*`num_components`*
x *`num_components`* if preprocessing is used) and
are symmetric. Further constraints can be given by
*`covar_type`*:

For *`covar_type`* = *"spherical"*, $\mathbf{C}_{j}$ is a scalar multiple of the identity matrix
$\mathbf{C}_{j}=s_{j}^{2}\mathbf{I}$.
The center density function $p(\mathbf{x}|j)$ is
$$p(x|j) = \frac{1}{(2\pi s_j^2)^{d/2}} \exp\left(-\frac{\|x - m_j\|^2}{2 s_j^2}\right)$$ ![figure](../assets/a6c837f57c0647bf.svg)

For *`covar_type`* = *"diag"*, $\mathbf{C}_{j}$
is a diagonal matrix
$$\mathbf{C}_{j}=diag(s_{j,1}^{2},...,s_{j,d}^{2})$$.
The center density function $p(\mathbf{x}|j)$ is
$$p(x|j) = \frac{1}{(2\pi)^{d/2} \prod_{i=1}^{d} s_{j,i}^{2}} \exp\Big(-\sum_{i=1}^{d} \frac{(x_i - m_{j,i})^2}{2 s_{j,i}^2}\Big)$$ ![figure](../assets/64c9dec2f71834b6.svg)

For *`covar_type`* = *"full"*, $\mathbf{C}_{j}$
is a positive definite matrix. The center density function
$p(\mathbf{x}|j)$ is
$$p(\mathbf{x}|\mathbf{j}) = \frac{1}{(2\pi)^{d/2}|\mathbf{C}_j|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{m}_j)^T \mathbf{C}_j^{-1}(\mathbf{x}-\mathbf{m}_j)\right)$$ ![figure](../assets/512e7f4f4e400bd9.svg)

The complexity of the calculations increases from *`covar_type`*
= *"spherical"* over *`covar_type`* = *"diag"*
to *`covar_type`* = *"full"*. At the same time the
flexibility of the centers increases. In general,
*"spherical"* therefore needs higher values for
*`num_centers`* than *"full"*.

The procedure to use GMM is as follows: First, a GMM is created by
`create_class_gmm`. Then, training vectors are added by
[`add_sample_class_gmm`](add_sample_class_gmm.md), afterwards they can be written to disk
with [`write_samples_class_gmm`](write_samples_class_gmm.md). With [`train_class_gmm`](train_class_gmm.md)
the classifier center parameters (defined above) are determined.
Furthermore, they can be saved with [`write_class_gmm`](write_class_gmm.md) for
later classifications.

From the mixing probabilities $P_{j}$ and the
center density function $p(\mathbf{x}|j)$, the probability
density function p(x) can be calculated by:
$$p(x) = \sum_{j=1}^{n_{comp}} P(j) p(x|j)$$ ![figure](../assets/24db9347c08d8b15.svg)

The probability density function p(x) can be
evaluated with [`evaluate_class_gmm`](evaluate_class_gmm.md) for a feature
vector x. [`classify_class_gmm`](classify_class_gmm.md) sorts the
p(x) and therefore discovers the most probable
class of the feature vector.

The parameters *`preprocessing`* and *`num_components`* can
be used to preprocess the training data and reduce its dimensions.
These parameters are explained in the description of the operator
[`create_class_mlp`](create_class_mlp.md).

`create_class_gmm` initializes the coordinates of the centers
with random numbers. To ensure that the results of training the
classifier with [`train_class_gmm`](train_class_gmm.md) are reproducible, the seed
value of the random number generator is passed in
*`rand_seed`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`num_dim`** (input_control)  integer `→` int

Number of dimensions of the feature space.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumDim >= 1`

**`num_classes`** (input_control)  integer `→` int

Number of classes of the GMM.

Default:
5

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`NumClasses >= 1`

**`num_centers`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of centers per class.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30

Restriction:
`NumClasses >= 1`

**`covar_type`** (input_control)  string `→` str

Type of the covariance matrices.

Default:
"spherical"

List of values:
"diag", "full", "spherical"

**`preprocessing`** (input_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

Default:
"normalization"

List of values:
"canonical_variates", "none", "normalization", "principal_components"

**`num_components`** (input_control)  integer `→` int

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`*
= *"none"* and *`preprocessing`*
= *"normalization"*).

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumComponents >= 1`

**`rand_seed`** (input_control)  integer `→` int

Seed value of the random number generator that
is used to initialize the GMM with random
values.

Default:
42

**`gmmhandle`** (output_control)  class_gmm `→` HHandle

GMM handle.

## Example (HDevelop)

```
* Classification with Gaussian Mixture Models
create_class_gmm (NumDim , NumClasses, [1,5], 'full', 'none',\
                  NumComponents, 42, GMMHandle)
* Add the training data
for J := 0 to NumData-1 by 1
    * Features := [...]
    * ClassID := [...]
    add_sample_class_gmm (GMMHandle, Features, ClassID, Randomize)
endfor
* Train the GMM
train_class_gmm (GMMHandle, 100, 0.001, 'training', 0.0001, Centers, Iter)
* Classify unknown data in 'Features'
classify_class_gmm (GMMHandle, Features, 1, ID, Prob, Density, KSigmaProb)
```

## Result

If the parameters are valid, the operator `create_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Successors

`add_sample_class_gmm`,
`add_samples_image_class_gmm`

## Alternatives

`create_class_mlp`,
`create_class_svm`

## See also

`clear_class_gmm`,
`train_class_gmm`,
`classify_class_gmm`,
`evaluate_class_gmm`,
`classify_image_class_gmm`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Mario A.T. Figueiredo: “Unsupervised Learning of Finite Mixture
Models”; IEEE Transactions on Pattern Analysis and Machine
Intelligence, Vol. 24, No. 3; March 2002.

## Module

Foundation
