# SetRegularizationParamsClassMlp (Operator)

## Name

`SetRegularizationParamsClassMlp` — Set the regularization parameters of a multilayer perceptron.

## Signature

`static void HOperatorSet.SetRegularizationParamsClassMlp(HTuple MLPHandle, HTuple genParamName, HTuple genParamValue)`

`void HClassMlp.SetRegularizationParamsClassMlp(string genParamName, HTuple genParamValue)`

`void HClassMlp.SetRegularizationParamsClassMlp(string genParamName, double genParamValue)`

## Description

`SetRegularizationParamsClassMlp` sets the regularization
parameters of the multilayer perceptron (MLP) passed in
*`MLPHandle`*. The regularization parameter to be set is
specified with *`genParamName`*. Its value is specified with
*`genParamValue`*.

*`genParamName`* can assume the following values:

- ***"num_outer_iterations"*:** —

  This parameter determines
  whether the regularization parameters should be determined
  automatically (*`genParamValue`* >= 1) or manually
  (*`genParamValue`* = 0, default), as described below in the
  sections “Technical Background” and “Automatic Determination of
  the Regularization Parameters”. As described in detail in the
  section “Automatic Determination of the Regularization
  Parameters”, *"num_outer_iterations"* should not be set too
  large (in the range of 1 to 5) to enable manual checking of the
  convergence of the automatic determination of the regularization
  parameters.
- ***"num_inner_iterations"*:** —

  This parameter potentially
  enables somewhat faster convergence of the automatic determination
  of the regularization parameters, as described below in the section
  “Automatic Determination of the Regularization Parameters”. It
  should typically be left at its default value of 1.
- ***"weight_prior"*:** —

  On the one hand, this selects the
  regularization model to be used, as described below in the section
  “Technical Background”. On the other hand, if manual
  determination of the regularization parameters has been selected
  (i.e., *"num_outer_iterations"* = 0), the regularization
  parameters are set with *`genParamName`*, whereas the initial
  values of the regularization parameters are set if automatic
  determination of the regularization parameters has been selected
  (i.e., *"num_outer_iterations"* >= 1), as described below in
  the section “Automatic Determination of the Regularization
  Parameters”. Manual determination of the regularization parameters
  (see the section “Regularization Parameters” below) is only
  realistic if a single regularization parameter is used. In all
  other cases, the regularization parameters should be determined
  automatically.
- ***"noise_prior"*:** —

  This allows to specify a noise prior
  for MLPs that have been configured for regression, as described
  below in the section “Application Areas”. If manual determination
  of the regularization parameters has been selected, the noise prior
  is set with *`genParamName`*, whereas the initial value of the
  noise prior is set if automatic determination of the regularization
  parameters has been selected. Typically, it is only useful to use
  this parameter if the regularization parameters are determined
  automatically.

Please note that the automatic determination of the regularization
parameters requires a very large amount of memory and runtime, as
described in detail in the section “Complexity” below. Therefore,
`numHidden` should not be selected too large when the MLP is
created with [`CreateClassMlp`](create_class_mlp.md). For example, normal OCR
applications seldom require `numHidden` to be larger than
30-60.

**Application Areas**

As described at [`CreateClassMlp`](create_class_mlp.md), it may be desirable to
regularize the MLP to enforce a smoother transition of the
confidences between the different classes and to prevent overfitting
of the MLP to the training data. To achieve this, a penalty for
large MLP weights (which are the main reason for very sharp
transitions between classes) can be added to the training of the MLP
in [`TrainClassMlp`](train_class_mlp.md) by setting *`genParamName`* to
*"weight_prior"* and setting *`genParamValue`* to a
value > 0.

If the MLP has been configured for regression (i.e., if
`outputFunction` was set to *"linear"* in
[`CreateClassMlp`](create_class_mlp.md)), an inverse variance of the expected noise
in the data can be specified by setting *`genParamName`* to
*"noise_prior"* and setting *`genParamValue`* to a value
> 0. Setting the noise prior only has an effect if a weight prior
has been specified. In this case, it can be used to weight the data
error term (the output error of the MLP) against the weight error
term.

As described in more detail below, the regularization parameters of
the MLP may be determined automatically (at the expense of
significantly increased training times) by setting
*`genParamName`* to *"num_outer_iterations"* and setting
*`genParamValue`* to a value > 0.

**Technical Background**

There are three different kinds of penalty terms that can be set
with *"weight_prior"*. Note that in the following the
parameters $w_{ji}^{(l)}$ and
$b_{k}^{(l)}$ refer to the weights of the different
layers of the MLP, as described in [`CreateClassMlp`](create_class_mlp.md).

If a single value $\alpha$ is specified, all MLP weights are
penalized equally by adding the following term to the optimization
in [`TrainClassMlp`](train_class_mlp.md):
$$E_W = \frac{\alpha}{2}\Biggl(\sum_{i=1}^{n_i}\sum_{j=1}^{n_h} (w_j^{(1,i)})^2 + \sum_{j=1}^{n_h} (b_j^{(1)})^2 + \sum_{i=1}^{n_h}\sum_{j=1}^{n_o} (w_{j}^{(2,i)})^2 + \sum_{k=1}^{n_o} (b_k^{(2)})^2\Biggr)$$ ![figure](../assets/dad1e9cdf060d546.svg)

Alternatively, four values $[\alpha_{w1},\alpha_{b1},\alpha_{w2},\alpha_{b2}]$ can be
specified. These four parameters enable the individual
regularization of the four groups of weights:
$$E_W = \frac{\alpha_w1}{2} \sum_{i=1}^{n_i} \sum_{j=1}^{n_h} \left( w_j^{(1)} \right)^2 + \frac{\alpha_b1}{2} \sum_{j=1}^{n_h} \left( b_j^{(1)} \right)^2 + \frac{\alpha_w2}{2} \sum_{j=1}^{n_h} \sum_{k=1}^{n_o} \left( w_j^{(2)} \right)^2 + \frac{\alpha_b2}{2} \sum_{k=1}^{n_o} \left( b_k^{(2)} \right)^2$$ ![figure](../assets/6965e19cf023ef8f.svg)

Finally, $n_{i}+3$ values
$[\mathcal{A}_{1}, \ldots, \mathcal{A}_{ni}, \mathcal{A}_{b1}, \mathcal{A}_{w2}, \mathcal{A}_{b2}]$ ![figure](../assets/115df9b1debd6ad7.svg)
can be specified.
These $n_{i}+3$ parameters enable the individual
regularization of each input variable
$x_1, \dots, x_{n_i}$ ![figure](../assets/fb528328596af252.svg)
and the regularization of the remaining three groups of weights:
$$E_W = \sum_{i=1}^{n_i} \frac{\alpha_i}{2} \sum_{j=1}^{n_h} (w_j^{(1,i)})^2 + \frac{\alpha_{b1}}{2} \sum_{j=1}^{n_h} (b_j^{(1)})^2 + \frac{\alpha_w}{2} \sum_{j=1}^{n_h} \sum_{k=1}^{n_o} (w_{kj}^{(2)})^2 + \frac{\alpha_{b2}}{2} \sum_{k=1}^{n_o} (b_k^{(2)})^2$$ ![figure](../assets/bb61ddc29a998463.svg)
This kind of regularization is only useful in conjunction with the
automatic determination of the regularization parameters described
below. If the automatic determination of the regularization
parameters returns a very large value of $\alpha_{j}$
(compared to the smallest value of the $n_{i}$ values
$\alpha_{i}$), the corresponding input variable has little
relevance for the MLP output. If this is the case, it should be
tested whether the input variable can be omitted from the input of
the MLP without negatively affecting the MLP's performance. The
advantage of omitting irrelevant input variables is an increased
speed of the MLP for classification.

The parameters $\alpha$ can be regarded as the inverse
variance of a Gaussian prior distribution on the MLP weights, i.e.,
they express an expectation about the size of the MLP weights. The
larger the $\alpha$ are chosen, the smaller the MLP weights
will be.

**Regularization Parameters**

The larger the regularization parameter(s) *"weight_prior"*
are chosen, the smoother the transition of the confidences between
the different classes will be. The required values for the
regularization parameter(s) depend on the MLP, especially the number
of hidden units, the training data, and the scale of the training
data (if no normalization is used). Typically, a higher value for
the regularization parameter(s) is necessary if the MLP has more
hidden units and if the training data consists of more points. For
typical applications, the regularization parameters are determined
by verifying the MLP performance on a test data set that is
independent from the training data set. If an independent test data
set is unavailable, cross validation can be used. Cross validation
works by splitting the data set into separate parts (for example,
80% of the data set for training and 20% for testing), training
the MLP with the training data set (the 80% of the data in the
above example), and testing the MLP performance on the test set (the
20% of the data in the above example). The procedure can be
repeated for the other possible splits of the data (in the
80%-20% example, there are five possible splits). This
procedure can, for example, start with relatively large values of
the weight regularization parameters (which will typically result in
misclassifications on the test data set). The weight regularization
parameters can then be decreased until an acceptable performance on
the test data sets is reached.

**Automatic Determination of the Regularization Parameters**

The regularization parameters, i.e., the weight priors and the noise
prior, can also be determined automatically by
[`TrainClassMlp`](train_class_mlp.md) using the so-called evidence procedure (for
details about the evidence procedure, please refer to the articles
in the section “References” below). This training mode can be
selected by setting *`genParamName`* to
*"num_outer_iterations"* and setting *`genParamValue`*
to a value > 0. Note that this typically results in training times
that are one to three orders of magnitude larger than simply
training the MLP with fixed regularization parameters.

The evidence procedure is an iterative algorithm that performs the
following two steps for a number of outer iterations: first, the
network is trained using the current values of the regularization
parameters; next, the regularization parameters are re-estimated
using the weights of the optimized MLP. In the first iteration, the
weight priors and noise priors specified with
*"weight_prior"* and *"noise_prior"* are used. Thus,
for the automatic determination of the regularization parameters,
the values specified by the user serve as the starting parameters
for the evidence procedure. The starting parameters for the weight
priors should not be set too large because this might
over-regularize the training and may result in badly determined
regularization parameters. The initial values for the weight priors
should typically be in the range 0.01-0.1.

The number of outer iterations can be set by setting
*`genParamName`* to *"num_outer_iterations"* and setting
*`genParamValue`* to a value > 0. If *`genParamValue`* is
set to 0 (this is the default value), the evidence procedure is not
executed and the MLP is simply trained using the user-specified
regularization parameters.

The number of outer iterations should be set high enough to ensure
the convergence of the regularization parameters. In contrast to
the training of the MLP's weights, a numerical convergence criterion
is typically very difficult to specify and some human judgment is
typically required to decide whether the regularization parameters
have converged sufficiently. Therefore, it might not be possible to
set the number of outer iterations a-priori to ensure convergence of
the regularization parameters. In these cases, the outer loop over
the steps of the evidence procedure can be implemented manually by
setting *"num_outer_iterations"* to 1 and calling
[`TrainClassMlp`](train_class_mlp.md) repeatedly. This has the advantage that the
weight priors and noise prior can be queried after each iteration
and can be checked manually for convergence. In this approach, the
performance of the MLP can even be checked after each iteration on
an independent test set to check the generalization performance of
the classifier.

If the number of outer iterations has been determined
(approximately) for a class of applications, it may be possible to
reduce the run time of the training (if MLPs should be trained in
the future with similar data sets) by setting *`genParamName`*
to *"num_inner_iterations"* and setting
*`genParamValue`* to a value > 1 (the default value is 1) and
by reducing the number of outer iterations. The number of outer
iterations can typically not be reduced by the same factor by which
the number of inner iterations is increased. Using this approach,
the run time of the training can be optimized. However, this approach
is only useful if many MLPs are trained with similar data sets. If
this is not the case, *"num_inner_iterations"* should be left
at its default value of 1.

The automatically determined weight priors and noise prior can be
queried after the training using
[`GetRegularizationParamsClassMlp`](get_regularization_params_class_mlp.md) by setting
`genParamName` to *"weight_prior"* or
*"noise_prior"*, respectively.

In addition to the weight prior and noise prior, the evidence
procedure determines an estimate of the number of parameters of the
MLP that can be determined well using the training data. This
result can be queried using
[`GetRegularizationParamsClassMlp`](get_regularization_params_class_mlp.md) by setting
`genParamName` to *"num_well_determined_params"*.
Alternatively, the fraction of well-determined parameters can be
queried by setting `genParamName` to
*"fraction_well_determined_params"*. If the number of
well-determined parameters is significantly smaller than
$n_{w}$ (where $n_{w}$ is the number of weights in
the MLP, as described in the section “Complexity” below) or the
fraction of well-determined parameters is significantly smaller than
1, consider reducing the number of hidden units or, if the number of
hidden units cannot be decreased without increasing the error rate
of the MLP significantly, consider performing a preprocessing that
reduces the number of input variables to the net, i.e., canonical
variates or principal components.

Please note that the number of well-determined parameters can only
be determined after the weight priors and noise prior have been
determined. This is the reason why the evidence procedure ends with
the determination of the regularization parameters and not with the
training of the MLP weights. Hence, after the evidence procedure
the MLP will not have been trained with the latest regularization
parameters. This should make no difference if they have converged.
If you want the training to end with an optimization of the weights
using the latest values of the regularization parameters, you can
set *"num_outer_iterations"* to 0 and can call
[`TrainClassMlp`](train_class_mlp.md) again. If you do so, please note, however,
that the number of well-determined parameters may change and,
therefore, the value returned by
[`GetRegularizationParamsClassMlp`](get_regularization_params_class_mlp.md) is technically
inconsistent.

**Saved Parameters**

Note that the parameters *"num_outer_iterations"* and
*"num_inner_iterations"* only affect the training of the MLP.
Therefore, they are not saved when the MLP is stored using
[`WriteClassMlp`](write_class_mlp.md) or [`SerializeClassMlp`](serialize_class_mlp.md). Thus, they
must be set anew if the MLP is loaded again using
[`ReadClassMlp`](read_class_mlp.md) or [`DeserializeClassMlp`](deserialize_class_mlp.md) and if
training using the automatic determination of the regularization
parameters should be continued. All other parameters described
above (*"weight_prior"*, *"noise_prior"*,
*"num_well_determined_params"*, and
*"fraction_well_determined_params"*) are saved.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the regularization parameter to set.

Default:
"weight_prior"

List of values:
"noise_prior", "num_inner_iterations", "num_outer_iterations", "weight_prior"

**`genParamValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Value of the regularization parameter.

Default:
1.0

Suggested values:
0.01, 0.1, 1.0, 10.0, 100.0, 0, 1, 2, 3, 5, 10, 15, 20

## Example (HDevelop)

```
* This example shows how to determine the regularization parameters
* automatically without examining the convergence of the
* regularization parameters.
* Create the MLP.
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'normalization', NumIn, 42, MLPHandle)
* Generate and add the training data
for J := 0 to NumData-1 by 1
    * Generate training features and classes.
    * Data = [...]
    * Class = [...]
    add_sample_class_mlp (MLPHandle, Data, Class)
endfor
* Set up the automatic determination of the regularization
* parameters.
set_regularization_params_class_mlp (MLPHandle, 'weight_prior', \
                                     [0.01,0.01,0.01,0.01])
set_regularization_params_class_mlp (MLPHandle, \
                                     'num_outer_iterations', 10)
* Train the MLP.
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
* Read out the estimate of the number of well-determined
* parameters.
get_regularization_params_class_mlp (MLPHandle, \
                                     'fraction_well_determined_params', \
                                     FractionParams)
* If FractionParams differs substantially from 1, consider reducing
* NumHidden appropriately and consider performing a preprocessing that
* reduces the number of input variables to the net, i.e., canonical
* variates or principal components.
write_class_mlp (MLPHandle, 'classifier.mlp')

* This example shows how to determine the regularization parameters
* automatically while examining the convergence of the
* regularization parameters.
* Create the MLP.
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'normalization', NumIn, 42, MLPHandle)
* Generate and add the training data.
for J := 0 to NumData-1 by 1
    * Generate training features and classes
    * Data = [...]
    * Class = [...]
    add_sample_class_mlp (MLPHandle, Data, Class)
endfor
* Set up the automatic determination of the regularization
* parameters.
set_regularization_params_class_mlp (MLPHandle, 'weight_prior', \
                                     [0.01,0.01,0.01,0.01])
set_regularization_params_class_mlp (MLPHandle, \
                                     'num_outer_iterations', 1)
for OuterIt := 1 to 10 by 1
    * Train the MLP
    train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
    * Read out the regularization parameters
    get_regularization_params_class_mlp (MLPHandle, 'weight_prior', \
                                         WeightPrior)
    * Inspect the regularization parameters manually for
    * convergence and exit the loop manually if they have
    * converged.
    * [...]
endfor
* Read out the estimate of the number of well-determined
* parameters.
get_regularization_params_class_mlp (MLPHandle,\
                                     'fraction_well_determined_params',\
                                     FractionParams)
* If FractionParams differs substantially from 1, consider reducing
* NumHidden appropriately and consider performing a preprocessing that
* reduces the number of input variables to the net, i.e., canonical
* variates or principal components.
write_class_mlp (MLPHandle, 'classifier.mlp')
```

## Complexity

Let $n_{i}$ denote the number of input units of the MLP
(i.e., $n_{i}=\texttt{NumHidden}$ or
$n_{i}=\texttt{NumComponents}$,
depending on the value of
`preprocessing`, as described at [`CreateClassMlp`](create_class_mlp.md)),
$n_{h}$ the number of hidden units, and $n_{o}$
the number of output units. Then, the number of weights of the MLP is
$n_{w}=(n_{i}+1)n_{h}+(n_{h}+1)n_{o}$.
Let $n_{d}$ denote the number of training
samples. Let $n_{M}$ denote the number of iterations set
with `maxIterations` in [`TrainClassMlp`](train_class_mlp.md). Let
$n_{O}$ and $n_{I}$ denote the number of outer and
inner iterations, respectively.

The run time of the training without regularization or with
regularization with fixed regularization parameters is of complexity
$O(n_{M}n_{w}n_{d})$. In contrast, the
runtime of the training with automatic determination of the
regularization parameters is of complexity
$$O(n_{O}n_{M}n_{w}n_{d})+O(n_{O}n_{w}^{2}n_{d})+O(n_{O}n_{w}^{3})+O(n_{O}n_{I}n_{w}^{3})$$.

The training without regularization or with regularization with
fixed regularization parameters requires at least
$48n_{w}+24n_{h}n_{d}+16n_{o}n_{d}$
bytes of memory. The training with automatic determination of the
regularization parameters requires at least $24n_{w}^{2}+48n_{w}+72n_{h}n_{d}+56n_{o}n_{d}$ bytes of memory. Under special
circumstances, another $24n_{w}^{2}+8n_{w}$ bytes of memory are required.

## Result

If the parameters are valid, the operator
`SetRegularizationParamsClassMlp` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`GetRegularizationParamsClassMlp`,
`TrainClassMlp`

## References

David J. C. MacKay: “Bayesian Interpolation”; Neural Computation
4(3):415-447; 1992.
  
David J. C. MacKay: “A Practical Bayesian Framework for
Backpropagation Networks”; Neural Computation 4(3):448-472;
1992.
  
David J. C. MacKay: “The Evidence Framework Applied to
Classification Networks”; Neural Computation 4(5):720-736;
1992.
  
David J. C. MacKay: “Comparison of Approximate Methods for Handling
Hyperparameters”; Neural Computation 11(5):1035-1068; 1999.

## Module

Foundation
