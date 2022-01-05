<p align="center">
    <img src="img/avl-logo.jpg" alt="AVL Logo" style="height: 200px; width:200px;"/>
</p>

# Agriculture Virtual Laboratory Documentation

## Introduction

The Agriculture Virtual Laboratory (AVL) is an integrated, user-friendly online
environment that helps scientists to discover, explore, analyse, and visualize a
wide variety of agricultural earth observation data.

The AVL integrates a data access layer, a thematic processing subsystem (TAO), a
Python scientific stack including the xcube suite for data cube handling, a
web-based interactive lab notebook (JupyterLab), and an online geodata viewer.

## Contents

### User guide

This section provides a guide for scientific users of the Agriculture Virtual
Laboratory, including both the thematic processing and exploitation subsystems,
and descriptions of the AVL-specific command-line and Python interfaces.

1. [Exploitation subsystem: JupyterLab](guide/exploitation/jupyter.md)
2. [Exploitation subsystem: xcube viewer](guide/exploitation/viewer.md)
<!-- 3. [Exploitation subsystem: xcube catalogue](guide/exploitation/catalogue.md) -->
3. [Thematic processing subsystem](guide/processing/index.md)
4. [AVL Python API](guide/python-api.md)
5. [AVL command-line tools](guide/tools.md)

### Datasets

AVL provides a variety of EO data products from multiple sources (or
collections). They follow a well-defined dataset convention and are grouped
according to sensor type.

1. [Dataset conventions](datasets/conventions.md)
2. [Altimetric datasets](datasets/altimetric.md)
3. [Atmospheric datasets](datasets/atmospheric.md)
4. [Optical datasets](datasets/optical.md)
5. [Passive microwave datasets](datasets/passive_microwave.md)
6. [Radar datasets](datasets/radar.md)

### Design

This section documents the system design, development resources, test
procedures, and test results.

1. [Design overview](design/index.md)
2. [Exploitation system design](design/exploitation/index.md)
3. [Processing system design](design/processing/index.md)
4. [AVL development](design/development.md)
5. [Software reuse file](design/reuse.md)
6. [Testing: exploitation system](design/testing/exploitation.md)
7. [Testing: processing system](design/testing/processing.md)

### About the project

1. [About the project](about/index.md)
2. [License](about/license.md)
