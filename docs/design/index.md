# AVL system design overview

This section describes the system design of the Agricultural Virtual
Laboratory.

The AVL comprises two main building blocks, namely the thematic processing
subsystem and the exploitation subsystem, which are based on two existing
software packages, TAO and the xcube ecosystem, respectively. AVL ingests
various data sets either from data archives stored in repositories or from
data portal services like SentinelHub or xcube geoDB. Users are provided with
individual workspaces and have the choice between different interfaces: the
interface to the thematic processing subsystem (TAO), a Jupyter Lab
environment, and an interactive visualisation app (xcube viewer).

The system design documentation is divided into the following sections:

1. [Architecture and common components](common.md)
2. [Processing system design](processing/index.md)
3. [Exploitation system design](exploitation/index.md)
4. [Development infrastructure](development.md)
5. [Software reuse file](reuse.md)
6. [Processing system test procedures and results](testing/processing.md)
7. [Exploitation system test procedures and results](testing/exploitation.md)
