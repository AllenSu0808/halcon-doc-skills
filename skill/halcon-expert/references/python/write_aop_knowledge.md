# write_aop_knowledge (Operator)

## Name

`write_aop_knowledge` — Write knowledge about hardware dependent behavior of automatic operator
parallelization to file.

## Signature

`def write_aop_knowledge(file_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, int, float]]) -> None`

## Description

`write_aop_knowledge` stores the automatic parallelization knowledge
of HALCON operators to file. The knowledge hold by the HALCON system is
used to better utilize multiprocessor
hardware in order to speed up the processing of operators. To optimize the
automatic parallelization of operators, HALCON needs some specific
knowledge about the speed of operators on the used hardware.
This hardware-specific knowledge
can be obtained by calling the operator [`optimize_aop`](optimize_aop.md) or read from
file by using [`read_aop_knowledge`](read_aop_knowledge.md), respectively.

With `write_aop_knowledge` it is possible to store this knowledge
explicitly in a binary file. At this, *`file_name`* denotes the
name of this file (incl. path and file extension). If an empty string
*""* is passed to *`file_name`*, HALCON writes the knowledge
to the specific file `.aop_info` in the HALCON installation
directory (Linux) or within the common application data folder
(Windows). This file is read by HALCON during the initialization phase
automatically.
`write_aop_knowledge` adds attributes to the knowledge like
the host name and information about HALCON architecture, variant,
version, and revision. This enables HALCON to write aop knowledge
sets of different machines or HALCON systems into the same file.
Therefore, `write_aop_knowledge` can control the updating of the
files contents by a pair of values passed to *`gen_param_name`* and
*`gen_param_value`*. Every entry in
*`gen_param_name`* must have one corresponding, specifying entry in
*`gen_param_value`*, meaning that the tuples passed to the parameters
must have the same length. *`gen_param_name`* supports the values in
following list, describing the possible applicable values for
*`gen_param_value`*:

- ***"mode"*** —

  sets the way how existing knowledge with same
  attributes would be updated in the file.

  - ***"truncate"*** —

    for *`gen_param_value`* deletes
    the existing knowledge with matching attributes before the new
    information is added to file.
  - ***"renew"*** —

    overwrites existing knowledge and adds new one
    (default).
  - ***"append"*** —

    keeps all existing operator information and just
    adds the knowledge not already contained.
  - ***"nil"*** —

    however refuses any update of the file but
    checks the user privileges, i.e., if read write access is
    available.
- ***"operator"*** —

  denotes that the corresponding index value of
  *`gen_param_value`* contains an operator name. It delimits the storage
  on a dedicated operator set. Multiple definitions
  of operators are possible. By default, information of any
  operator possessing AOP optimization data is written.
- ***"iconic_type"*** —

  focuses on AOP information for a specific
  iconic type, specified by following values of *`gen_param_value`*:
  *"byte"*, *"uint2"*, *"real"*, *"int1"*,
  *"int2"*, *"int4"*, *"int8"*, *"direction"*,
  *"vector_field"*, *"cyclic"*,
  *"complex"*, *"region"*, *"xld"*. Multiple definitions
  of iconic types are possible.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_name`** (input_control)  filename.write `→` str

Name of knowledge file

Default:
""

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Parameter name

Default:
"none"

Suggested values:
"mode", "operator", "iconic_type"

**`gen_param_value`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int, float]]

Parameter value

Number of elements:
GenParamName == GenParamValue

Default:
"none"

Suggested values:
"truncate", "renew", "append"

## Result

`write_aop_knowledge` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
the file could be read. If necessary, an exception is raised.

## Module

Foundation
