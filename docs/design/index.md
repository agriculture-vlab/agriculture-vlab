# AVL System Design



This section describes the system design of the Agricultural Virtual Laboratory. It 
comprises two main building blocks, namely the Thematic processing subsystem and the Exploitation subsystem,
which are based on two existing software packages, TAO and the xcube ecosystem, respectively.
AVL ingests various data sets either from data archives stored in repositories
or from data portal services like SentinelHub or xcube geoDB. Users are provided with
individual workspaces and have the choice between different interfaces: the interface to
the thematic processing subsystem (TAO),  a Jupyter Lab environment, and an interactive visualisation app
(xcube viewer).

The system design documentation consists of three parts, describing the design
of the thematic processing subsystem, the exploitation subsystem, and the
test procedures.

1. [Processing system](processing/index.md)
2. [Exploitation system](exploitation/index.md)
3. [Test procedures and results](testing/index.md)
