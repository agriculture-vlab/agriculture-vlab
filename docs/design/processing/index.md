# AVL Processing System Design

---

The thematic processing sub-system is a collection of self-contained (i.e., packed in Docker containers) applications or systems, that produce value-added EO products (such as crop masks, crop types, agricultural practices, etc.).
The sub-system has at its core the TAO Workflow and Integration engine. TAO (stands for Tool Augmentation by user enhancements and Orchestration) is an open-source (under GPLv3 license) lightweight, generic integration, and distributed orchestration framework. It allows the integration of commonly used toolboxes (such as, but not limited to, SNAP, Orfeo Toolbox, GDAL, etc.) into a single user environment. This framework allows for processing composition and distribution in such a way that end users could define by themselves processing workflows and easily integrate additional processing modules (either standalone executables or Python or R scripts).
In terms of use, the TAO platform provides a mean for orchestration of heterogeneous processing components and libraries to process remote sensing data. This is achieved in following steps:
- Preparation of resources (including processing components) and data input,
- Definition of a workflow as a processing chain,
- Execution of workflows,
- Retrieval / visualisation / sharing of the results.
The following diagram details the AVL Thematic Processing subsystem:
![ ](/img/avl-ts.png)

## Dataset Explorer
The Dataset Explorer allows for:
- Listing the available data providers,
- Listing the available data sets for each provider,
- Searching for specific data products in a uniform way (different providers may have different filters for searching data),
- Retrieving the selection of data products to the user workspace.

## Data Sources Manager
The Data Sources Manager component handles the external data source modules in the AVL platform.
The purpose of the Data Sources Manager component is to allow data sources visualization and configuration for their usage in workflows creations.
The main functionalities exposed by the component are:
- find all existing data sources visible by a given user,
- retrieve the parameters of a data source,
- query the remote data source,
- retrieve data products

## Workspace Manager
The following functions are performed by this component:
- View the details about local data products (accessible for both administrator and user roles, with the difference that the user can only view details about his local data products as well as public data products),
- Upload additional files that can be further used in workflows (such as model files, shape files, etc.),
- Publish (share) data products with other users,
- Monitor user quota.

## Workflow Editor
The Workflow Editor allows for building custom processing chains using modules from the supported toolboxes.
Main functionalities are:
- retrieve the list of workflows that a given user can see,
- clone an existing workflow,
- parameterize a workflow according to the user needs,
- create a workflow from existing toolboxes,
- validate a workflow

## Workflow Engine
The Thematic Workflow Engine is in charge with execution of workflows by creating and handling jobs and performing the management of the execution steps from a workflow. The purpose of the Orchestration is to allow the execution of a workflow, by creating a job for each workflow execution, splitting and managing the internal components of the workflow in execution tasks.

## xcube Converter
The xcube Converter handles the format conversion from original raster product formats (specific to external data providers or to thematic processing subsystem components) to Zarr format (specific to data cubes).

---