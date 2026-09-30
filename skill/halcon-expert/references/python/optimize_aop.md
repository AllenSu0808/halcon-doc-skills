# optimize_aop (Operator)

## Name

`optimize_aop` — Check hardware regarding its potential for automatic operator
parallelization.

## Signature

`def optimize_aop(operator_name: MaybeSequence[str], iconic_type: MaybeSequence[str], file_name: Union[str, int], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> None`

## Description

HALCON supports automatic operator parallelization (AOP) for various
operators.
`optimize_aop` is necessary for an efficient automatic
parallelization, what HALCON uses to speed up the execution of operators. As
the parallelization of operators is done automatically, there is no need for
the user to explicitly prepare or change programs for their parallelization.
Thus, all HALCON-based programs can be used without adaptations on
multiprocessor hardware and users benefit from the potential of parallel
hardware. By default, HALCON uses the maximum available number of threads
for AOP, up to the number of processors. But, depending on the data size and
the parameter set passed to an operator, parallelizing on the maximum thread
number might be too excessive and inefficient. `optimize_aop`
optimizes the AOP in terms of thread number and checks a given hardware
with respect to a parallel processing of HALCON operators. In doing so,
it examines every
operator, which can be possibly be sped up by an automatic parallelization
on tuple, channel, or domain level (the partial level is not considered).
Each examined operator is executed several times - both sequentially and
parallel - with a changing set of input parameter values/images. The
latter helps to evaluate dependencies between an operator's input parameter
characteristics (e.g., the size of an input image) and the efficiency of its
parallel processing. This may take up to a couple of hours depending on the
settings of the operator's parameters. It is essential for a correct
optimization not to run any other computation-intensive application
simultaneously on the machine, as this would strongly influence the time
measurements of the hardware check and thus would lead to wrong results.

Overall, `optimize_aop` performs several test loops and
collects a lot of hardware-specific information which enables HALCON
to optimize the automatic parallelization for a given hardware. The
hardware information can be stored in a binary file given by
*`file_name`* so that it can be used again in future HALCON sessions
or even transferred to other machines, identical in hardware. When passing an
empty string
*""* as file name, `optimize_aop` stores the optimization data
to the specific HALCON system file '.aop_info' in the HALCON installation
directory (in Linux, see environment variable $HALCONROOT) or within
the common application data folder (Windows). This specific file is
automatically read when
initializing HALCON during the first operator call.
Note that the user must have appropriate privileges
for read and write access. `optimize_aop` will check the file access
before starting the AOP optimization and return an appropriate error when
failing. The written file can be
read by using the operator [`read_aop_knowledge`](read_aop_knowledge.md) again.

Thus, it is sufficient, to start
`optimize_aop` once on each multiprocessor machine that
is used for parallel processing. Of course, it should be started again,
if the hardware of the machine changes, for example, by installing
a new CPU, new memory, or if the operating system of the machine changes.
It is necessary to start `optimize_aop` once for each new processing
environment as the time response of operators may differ. A new processing
environment is given, if different operating systems, such as Windows and
Linux, or different HALCON architectures, different HALCON variants are
used, i.e., HALCON versus HALCON XL, or when updating to a new HALCON
version or revision. Together with
the machine's host name, these dependencies form the knowledge attributes
and are stored to the file together with the AOP optimization data. The
attributes identify the machine-specific AOP knowledge set
and enable the storage of different knowledge sets to the same file.

`optimize_aop` offers a set of parameters to restrict the
extensiveness and specify the behavior of the optimization process. A subset
of HALCON operators can be passed to *`operator_name`*. This will
restrict the optimization process to the operators passed by their name.
When passing an empty string *""*, all operators will be tested.
A subset of iconic types that should be checked can be set by parameter
*`iconic_type`*. Again, passing an empty string *""*
will test all supported iconic types. Further settings to modify the
optimization process can be parameterized by a pair of
values passed to *`gen_param_name`* and *`gen_param_value`*. Every
entry in *`gen_param_name`* must have a corresponding entry in
*`gen_param_value`*, meaning the tuples passed to the parameters must
have the same length. *`gen_param_name`* supports the values in
following list, specifying for each possible value for *`gen_param_name`*
all possible applicable values for *`gen_param_value`*:

- ***"none"*** —

  does nothing specific but ignores the parameter
  *`gen_param_value`*.
- ***"system_mode"*, *"file_mode"*** —

  set the way how the
  information of the system or file, respectively, gets updated.

  - ***"truncate"*** —

    for *`gen_param_value`* deletes
    all the existing information before the new knowledge loaded from file
    is added.
  - ***"renew"*** —

    overwrites existing knowledge and adds new one
    (default).
  - ***"append"*** —

    keeps all existing operator information and just
    adds the knowledge not already contained.
  - ***"nil"*** —

    performs the optimization process but refuses any
    update of the system or file, respectively.
- ***"parameters"*** —

  also tests for appropriate operator
  parameters if the corresponding value of *`gen_param_value`* is
  set to *"true"*. These operator parameters are supposed to
  show significant influence on the operator's processing time like
  string parameters
  picking up a certain operator mode or method or, e.g., parameters
  setting a filter size. *"false"* dismisses the parameter check
  in favor of a faster knowledge identification (default).
- ***"model"*** —

  sets the underlying simulation of the behavior of
  parallelizing operators on the current hardware. Different
  models can be selected by *`gen_param_value`* differing in
  hardware adaptability and computation time:

  - ***"threshold"*** —

    determines if it is profitable
    to run on the maximum thread number or not. This is default on
    dual processor systems.
  - ***"linear"*** —

    specifies a linear scale model to determine
    the best thread number for a given data size and parameter set. This
    is default on multiprocessor systems.
  - ***"mlp"*** —

    is the most complex but also most adaptable model.
    Note that the optimization process can take a couple of hours
    depending on the used hardware topology.
- ***"timeout"*** —

  sets a maximum execution time for a
  tested operator. If the execution of an operator exceeds the timeout,
  the test on this operator is aborted. No information about this
  operator will be stored in this case. The timeout value is set by
  *`gen_param_value`* in seconds. Specifying *"infinite"*
  prevents any abortion of an operator's optimization process (default).
- ***"split_level"*** —

  restricts the optimization process on a
  certain parallelization method. The corresponding value of
  *`gen_param_value`* can contain one of the following values,
  therefore:

  - ***"split_domain"*** —

    performs the check on all image
    processing operators supporting data parallelization on domain level.
  - ***"split_channel"*** —

    performs the check on all image
    processing operators supporting data parallelization on channel
    level.
  - ***"split_tuple"*** —

    performs the check on all
    operators supporting data parallelization on tuple level.

## Attention

During its test loops `optimize_aop` has to start
every examined operator several times. Thus, the processing time of
`optimize_aop` can be rather long depending on the operator's
parameter settings. It is essential for a correct
optimization not run any other computation-intensive application
simultaneously on the machine, as this would strongly influence the time
measurements of the hardware check and thus would lead to wrong results.
Note that according to the file location
`optimize_aop` must be called by users with the appropriate
privileges for storing the
parallelization information. See the operator's description
above for more details about these subjects.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Operators to check

Default:
""

**`iconic_type`** (input_control)  string(-array) `→` MaybeSequence[str]

Iconic object types to check

Default:
""

Suggested values:
"", "byte", "int1", "int2", "uint2", "int4", "int8", "direction", "cyclic", "vector_field", "complex", "region", "xld", "xld_cont", "xld_poly"

**`file_name`** (input_control)  filename.write `→` Union[str, int]

Knowledge file name

Default:
""

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Parameter name

Default:
"none"

Suggested values:
"parameters", "model", "timeout", "file_mode", "system_mode", "split_level"

**`gen_param_value`** (input_control)  string-array `→` Sequence[Union[str, float, int]]

Parameter value

Number of elements:
GenParamName == GenParamValue

Default:
"none"

Suggested values:
"true", "renew", "truncate", "threshold", "linear", "mlp", -1.0

## Result

`optimize_aop` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
the file could be read. If necessary, an exception is raised.

## Module

Foundation
