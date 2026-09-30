# filter_kalman (Operator)

## Name

`filter_kalman` — Estimate the current state of a system with the help of the
Kalman filtering.

## Warning

**`filter_kalman` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`filter_kalman( : : Dimension, Model, Measurement, PredictionIn : PredictionOut, Estimate)`

## Description

The operator `filter_kalman` returns an estimate of the
current state (or also a prediction of a future state) of a discrete,
stochastically disturbed, linear system. In practice, Kalman filters are
used successfully in image processing in the analysis of
image sequences (background identification, lane tracking with the
help of line tracing or region analysis, etc.). A short introduction
concerning the theory of the Kalman filters will be followed by
a detailed description of the routine `filter_kalman`
itself.

KALMAN FILTER:
A discrete, stochastically disturbed, linear system is characterized
by the following markers:

- State $x(t)$: Describes the current state of the system
  (speeds, temperatures,...).
- Parameter $u(t)$: Inputs from outside into the system.
- Measurement $y(t)$: Measurements gained by observing the system.
  They indicate the state of the system (or at least parts of it).
- An output function describing the dependence of the
  measurements on the state.
- A transition function indicating how the state changes with
  regard to time, the current value and the parameters.

The output function and the transition function are linear. Their
application can therefore be written as a multiplication with a matrix.

The transition function is described with the help of the
transition matrix $A(t)$ and the parameter matrix
$G(t)$, the initial function is described by the measurement
matrix $C(t)$. Hereby $C(t)$ characterizes the
dependency of the new state on the old, $G(t)$ indicates the
dependency on the parameters. In practice it is rarely possible (or at
least too time consuming) to describe a real system and its behavior
in a complete and exact way. Normally only a relatively small number of
variables will be used to simulate the behavior of the system. This leads
to an error, the so called system error (also called system disturbance)
$v(t)$.

The output function, too, is usually not exact. Each measurement is
faulty. The measurement errors will be called $w(t)$.
Therefore the following system equations arise:
x(t+1) = A(t)x(t) + G(t)u(t) + v(t)
y(t) = c(t)x(t) + w(t)
The system error $v(t)$ and the measurement error $w(t)$
are not known. As far as systems are concerned which are interpreted with
the help of the Kalman filter, these two errors are considered as
Gaussian distributed random vectors (therefore the expression “stochastically
disturbed systems”). Therefore the system can be calculated, if the
corresponding expected values for $v(t)$ and $w(t)$ as
well as the covariance matrices are known.

The estimation of the state of the system is carried out in the same way
as in the Gaussian-Markov-estimation. However, the Kalman filter is a
recursive algorithm which is based only on the current measurements
$y(t)$ and the latest state $x(t)$. The latter
implicitly also includes the knowledge about earlier measurements.

A suitable estimate value $x_{0}$, which is interpreted as the
expected value of a random variable for $x(0)$, must be indicated
for the initial value $x(0)$. This variable should have an
expected error value of 0 and the covariance matrix $P_{0}$ which
also has to be indicated. At a certain time $t$ the expected
values of both disturbances $v(t)$ and $w(t)$ should be 0
and their covariances should be $Q(t)$ and $R(t)$.
$x(t)$, $v(t)$ and $w(t)$ will usually be assumed
to be not correlated (any kind of noise-process can be modeled - however the
development of the necessary matrices by the user will be considerably
more demanding). The following conditions must be met by the searched
estimate values $x^{t}$:

- The estimate values $x^{t}$ are linearly dependent on the actual
  value $x(t)$
  and on the measurement sequence $y(0)$, $y(1)$,
  $\cdot\cdot\cdot$ , $y(t)$.
- {$x^{t}$ being hereby considered to meet its expectations,
  i.e. $Ex^{t}=Ex(t)$.}
- The grade criterion for $x^{t}$ is the criterion of minimal variance,
  i.e. the variance of the estimation error defined as
  $x(t)-x^{t}$,
  being as small as possible.

After the initialization
$$\hat{x}(0) = x_0, \hat{P}(0) = P_0$$ ![figure](../assets/cf8bb21ea20b6d44.svg)
at each point in time $t$ the Kalman filter executes the
following calculation steps:
$$(K-III)\quad K(t) = \frac{\hat{P}(t)C'(t)}{C(t)\hat{P}(t)C'(t)+R(t)}\\ (K-IV)\quad x^t = \hat{x}(t) + K(t)(y(t) - C(t)\hat{x}(t))\\ (K-V)\quad \tilde{P}(t) = \hat{P}(t) - K(t)C(t)\hat{P}(t)\\ (K-I)\quad \hat{x}(t+1) = A(t)x^t + G(t)u(t)\\ (K-II)\quad \hat{P}(t+1) = A(t)\hat{P}(t)A'(t) + Q(t)$$ ![figure](../assets/288f2cc5812f866a.svg)
Hereby $\tilde{P}(t)$ ![figure](../assets/f312e6379403f8e6.svg) is the covariance matrix of the estimation
error, $\hat{x}(t)$ ![figure](../assets/15354c2aac2d32de.svg) is the extrapolation value respective the
prediction value of the state, $\hat{P}(t)$ ![figure](../assets/edc89d864bd74472.svg) are the covariances of
the prediction error $\hat{x} - x, K$ ![figure](../assets/141422cd77573e7a.svg) is the amplifier
matrix (the so called Kalman gain), and $X^{\prime}$ is the transposed of
a matrix $X$.

Please note that the prediction of the future state is also possible with
the equation (K-I). Sometimes this is very useful in image
processing in order to determine “regions of interest” in the next image.

As mentioned above, it is much more demanding to model any kind of
noise processes. If for example the system noise and the measurement
noise are correlated with the corresponding covariance matrix
$L$, the equations for the Kalman gain and the error covariance
matrix have to be modified:
$$(K-III) K(t) = \frac{\hat{P}(t)C'(t) + L(t)}{C(t)\hat{P}(t) + C(t)l(t) + L'(t)C'(t) + R(t)} \\ (K-V) \tilde{P}(t) = ( \tilde{P}(t) - K(t)C(t)\hat{P}(t)\hat{P}(t) ) - K(t)L(t)$$ ![figure](../assets/bef9fcd085a9037a.svg)
This means that the user himself has to establish the linear system
equations from (K-I) up to (K-V) with respect to the actual problem.
The user must therefore develop a mathematical model upon which the
solution to the problem can be based. Statistical characteristics
describing the inaccuracies of the system as well as the measurement
errors, which are to be expected, thereby have to be estimated if
they cannot be calculated exactly. Therefore the following individual
steps are necessary:

1. Developing a mathematical model
2. Selecting characteristic state variables
3. Establishing the equations describing the changes of these
   state variables and their linearization
   (matrices $A$ and $G$)
4. Establishing the equations describing the dependency of the
   measurement values of the system on the state variables
   and their linearization (matrix $C$)
5. Developing or estimating of statistical dependencies
   between the system disturbances (matrix $Q$)
6. Developing or estimating of statistical dependencies
   between the measurement errors (matrix $R$)
7. Initialization of the initial state

As mentioned above, the initialization of the system (point 7)
hereby necessitates to indicate an estimate $x_{0}$ of
the state of the system at the time 0 and the corresponding
covariance matrix $P_{0}$. If the exact initial state is
not known, it is recommendable to set the components of the vector
$x_{0}$ to the average values of the corresponding range,
and to set high values for $P_{0}$ (about the size
of the squares of the range). After a few iterations (when the
number of the accumulated measurement values in total has exceeded
the number of the system values), the values which have been
determined in this way are also usable.

If on the other hand the initial state is known exactly, all entries
for $P_{0}$ have to be set to 0, because $P_{0}$
describes the covariances of the error between the estimated value
$x_{0}$ and the actual value $x(0)$.

THE FILTER ROUTINE:

A Kalman filter is dependent on a range of data which can be
organized in four groups:

- **Model parameter:** —

  transition matrix $A$, control matrix $G$
  including the parameter $u$ and the measurement matrix $C$
- **Model stochastic:** —

  system-error covariance matrix $Q$,
  system-error - measurement-error covariance matrix $L$, and
  measurement-error covariance matrix $R$
- **Measurement vector:** —

  $y$
- **History of the system:** —

  extrapolation vector $\hat{x}$ ![figure](../assets/45170b4d5c95d84b.svg) and
  extrapolation-error covariance matrix $\hat{P}$ ![figure](../assets/3a73586742c2d851.svg)

Thereby many systems can work without input “from outside”,
i.e. without $G$ and $u$. Further, system errors and
measurement errors are normally not correlated ($L$ is dropped).

Actually the data necessary for the routine will be set by the
following parameters:

- ***`Dimension`*:** —

  This parameter includes the dimensions of the status vector, the
  measurement vector and the controller vector. *`Dimension`*
  thereby is a vector $[n,m,p]$, whereby
  $n$ indicates the number of the state variables,
  $m$ the number of the measurement values and
  $p$ the number of the controller members.
  For a system without determining control (i.e. without influence
  “from outside”) therefore $[n,m,0]$ has to be passed.
- ***`Model`*:** —

  This parameter includes the lined up matrices (vectors)
  $A,C,Q,G,u$ and (if necessary) $L$
  having been stored in row-major order. *`Model`* therefore is a vector
  of the length $n\times n+n\times m+n\times n+n\times p+p[+n\times m]$.
  The last summand is dropped, in case the system errors and measurement
  errors are not correlated, i.e. there is no value for $L$.
- ***`Measurement`*:** —

  This parameter includes the matrix $R$ which has been
  stored in row-major order, and the measurement vector $y$ lined up.
  *`Measurement`* therefore is a vector of the dimension
  $m\times m+m$.
- ***`PredictionIn`* / *`PredictionOut`*:** —

  These two parameters include the matrix $\hat{P}$ ![figure](../assets/3a73586742c2d851.svg) (the
  extrapolation-error covariance matrix) which has been stored in
  row-major order and the extrapolation vector $\hat{x}$ ![figure](../assets/45170b4d5c95d84b.svg) lined up.
  This means, they are vectors of the
  length $n\times n+n$. *`PredictionIn`* therefore is an
  input parameter, which must contain $\hat{P}(t)$ ![figure](../assets/edc89d864bd74472.svg) and
  $\hat{x}(t)$ ![figure](../assets/15354c2aac2d32de.svg) at the current time $t$. With
  *`PredictionOut`* the routine returns the
  corresponding predictions $\hat{P}(t+1)$ ![figure](../assets/924568309bc539a1.svg) and
  $\hat{x}(t+1)$ ![figure](../assets/3e71e3e52d96c7db.svg).
- ***`Estimate`*:** —

  With this parameter the routine returns the matrix $\tilde{P}$ ![figure](../assets/43b9ac71d09709e7.svg)
  (the estimation-error covariance matrix) which has been stored
  in row-major order and the estimated state $\tilde{x}$ ![figure](../assets/6baa76fbea84eba0.svg) lined up.
  *`Estimate`* therefore is a
  vector of the length $n\times n+n$.

Please note that the covariance matrices $$(Q,R,\hat{P},\tilde{P})$$ ![figure](../assets/c877a775b8d028f1.svg) must of course be symmetric.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Dimension`** (input_control)  integer-array `→`  (integer)

The dimensions of the state vector, the measurement
and the controller vector.

Default:
[3,1,0]

Value range:
`0
≤
Dimension
≤
30`

**`Model`** (input_control)  real-array `→`  (real)

The lined up matrices $A,C,Q$, possibly
$G$ and $u$, and if necessary $L$
which have been stored in row-major order.

Default:
[1.0,1.0,0.5,0.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,54.3,37.9,48.0,37.9,34.3,42.5,48.0,42.5,43.7]

Value range:
`0.0
≤
Model
≤
10000.0`

**`Measurement`** (input_control)  real-array `→`  (real)

The matrix $R$ stored in row-major order
and the measurement vector $y$ lined up.

Default:
[1.2,1.0]

Value range:
`0.0
≤
Measurement
≤
10000.0`

**`PredictionIn`** (input_control)  real-array `→`  (real)

The matrix $\hat{P}$ ![figure](../assets/3a73586742c2d851.svg) (the extrapolation-error
covariances) stored in row-major order and the
extrapolation vector $\hat{x}$ ![figure](../assets/45170b4d5c95d84b.svg) lined up.

Default:
[0.0,0.0,0.0,0.0,180.5,0.0,0.0,0.0,100.0,0.0,100.0,0.0]

Value range:
`0.0
≤
PredictionIn
≤
10000.0`

**`PredictionOut`** (output_control)  real-array `→`  (real)

The matrix $\text{P}\ast$ (the extrapolation-error
covariances)stored in row-major order and the
extrapolation vector $\hat{x}$ ![figure](../assets/45170b4d5c95d84b.svg) lined up.

**`Estimate`** (output_control)  real-array `→`  (real)

The matrix $\tilde{P}$ ![figure](../assets/43b9ac71d09709e7.svg) (the estimation-error
covariances) stored in row-major order and the
estimated state $\tilde{x}$ ![figure](../assets/6baa76fbea84eba0.svg) lined up.

## Example (HDevelop)

```
* Typical procedure:
* To initialize the variables, which describe the model, e.g., with
read_kalman('kalman.init',Dim,Mod,Meas,Pred)

* Generation of the first measurements (typical of the first image of an
* image series) with an appropriate problem-specific procedure (there is a
* fictitious procedure extract_features in example):
* extract_features(Image1,Meas,Meas1)

* first Kalman-Filtering:
filter_kalman(Dim,Mod,Meas1,Pred,Pred1,Est1)

* To use the estimate value (if need be the prediction too)
* with a problem-specific procedure (here use_est):
* use_est(Est1)

* To get the next measurements (e.g., from the next image):
* extract_next_features(Image2,Meas1,Meas2)

* if need be Update of the model parameter (a constant model)
* second Kalman-Filtering:
filter_kalman(Dim,Mod,Meas2,Pred1,Pred2,Est2)
* use_est(Est2)
* extract_next_features(Image3,Meas2,Meas3)
* etc.
```

## Result

If the parameter values are correct, the operator
`filter_kalman` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`read_kalman`

## Possible Successors

`update_kalman`

## See also

`read_kalman`,
`update_kalman`

## References

W.Hartinger: “Entwurf eines anwendungsunabhängigen Kalman-Filters mit
Untersuchungen im Bereich der Bildfolgenanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik, Lehrstuhl
Prof. Radig; 1991.
  
R.E.Kalman: “A New Approach to Linear Filtering and Prediction Problems”;
Transactions ASME, Ser.D: Journal of Basic Engineering; Vol. 82, S.34-45;
1960.
  
R.E.Kalman, P.l.Falb, M.A.Arbib: “Topics in Mathematical System Theory”;
McGraw-Hill Book Company, New York; 1969.
  
K-P. Karmann, A.von Brandt: “Moving Object Recognition Using an Adaptive
Background Memory”; Time-Varying Image Processing and Moving Object
Recognition 2 (ed.: V. Cappellini), Proc. of the 3rd Interantional
Workshop, Florence, Italy, May, 29th - 31st, 1989; Elsevier, Amsterdam;
1990.

## Module

Foundation
