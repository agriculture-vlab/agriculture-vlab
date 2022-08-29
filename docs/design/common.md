# System Design: overall architecture and common components

This section describes the overall software architectural design, identifying
the software components, their hierarchical relationships, and their
dependencies. It also describes system components common to the two main
subsystems (processing and exploitation).

## Overall Architecture

The following component diagrams present the main software components
that compose the AVL platform:

![Platform components](./../img/image1.png)
**Platform components**

The Exploitation subsystem is closely integrated with the Thematic processing
subsystem, which serves as a source of relevant data sets to be explored by
AVL's users, other data sources such as Sentinel Hub or xcube geoDB, and the
user-facing applications Jupyter Lab and the Interactive Visualisation.
Moreover, both subsystems share a couple of Common Components.

## Software Components Design – Common

The AVL Thematic Processing and AVL Exploitation subsystems share
several common components. This section describes the components
depicted in the following diagram:

![Common Components used by the two subsystems](./../img/image2.png)
**Common Components used by the two subsystems**

Please note that data visualisation is not a component on its own. Each
subsystem is having its own specialised data viewers.

### Authentication and Authorization

#### General

The Authentication and Authorization component contains the
implementation for user access to the AVL platform, secures user access
to the application, and manages user permissions to different parts of
the platform.

#### Function

The Authentication and Authorization component provides an interface
that is implemented by the authentication specific mechanism, so
that this mechanism can be changed or decoupled from the interface.
Also, there is an authorization interface which is implemented by the
authorization mechanism providing the user authorization through the
system.

#### Dependencies

Every graphical user interface module that calls backend business logic
needs to authenticate in order to have access to the desired data.
The Authentication and Authorization component uses encryption and
hashing mechanisms. It also uses the Persistence Manager component
for database users and permissions management.

#### Interfaces

The main interfaces in term of data flow of this component are:

-   As inputs:
    -   The username and password for login,
    -   The user password for password reset.
-   As outputs:
    -   The login action result (successful or not),
    -   The password reset action result (successful or not).

#### Data

The data handled by this component are the user's credentials and
rights, which, depending on the authentication mechanism, can be
retrieved from the AVL database using Persistence Manager or from an
external authentication and authorization user management system. The
service also provides API access tokens to authenticated clients, which
are then used by a service to authorise internal and external access.

#### Remarks

AVL uses the [*Keycloak*](https://www.keycloak.org/)
software for simplifying, but also to increase the spectrum of, the
authentication mechanism. Keycloak adds authentication to applications
and secures services with minimum work. It supports, among others, user
federation, identity brokering and social login.

### User Management

#### General

The User Management component contains the implementation for user
management in the AVL platform. The purpose of the User Management
component is to define the users allowed to use the platform, and to
define their quota in terms of storage and computing resources (CPU,
memory).

#### Function

The User Management component provides an interface so that all other
components interacting with the user management will use the functionalities
exposed by it. The main functionalities of the component are:

-   add a new user by providing a username and an email address,

-   update user credentials (by setting password provided by user after
    account activation),

-   set and update user quota,

-   remove/deactivate a user.

#### Dependencies

The User Management component uses the Persistence Manager component for
storing user details in the AVL database.

#### Interfaces

The module exposes a Java API (for integration with other Java
components) and a REST API (for usage from heterogeneous clients,
including web clients).

#### Data

The data handled by this component are the user details (credentials and
quota), which can be saved/retrieved into/from the AVL database using
Persistence Manager.

### Object Storage

#### General

The main purpose of Object Storage is to be a performant,
cloud-ready, and cost-effective store for the large amounts of data AVL
needs to manage. The Thematic Processing System generates data cubes
into the object storage, while the AVL exploitation system reads the
data cubes from the object storage. The standard data format for the data cubes
is [Zarr](https://zarr.readthedocs.io/en/stable/), but other data formats
are also supported as required (e.g. NetCDF, GeoTIFF).

The Object Storage is provided by the cloud environment used for the AVL
deployment.

Several standard user-accessible AVL object storage buckets are provided, with
particular purposes and access settings:

-   `user-private`: personal, private object storage. Users can only read
    and write under their own user prefix, similar to a home directory.

-   `user-public`: shared user data. Users can only write under their own
    user prefix, but all data is readable to all users.

-   `scratch`: temporary shared storage. All AVL users can read and write
    freely in the whole bucket, and data are deleted automatically after two
    days.

-   `data`: pre-processed, standard data sets made available for all users by
    the AVL project.

-   `staging`: a staging area for the data_store store. Data here are migrated
    to the `data` bucket once they have been thoroughly tested.

-   `test`: A pre-staging area for the `staging` and `data` buckets. Data here
    are migrated to `staging` after some initial testing.

User access to the buckets is managed by the application of appropriate AWS
IAM policies to both buckets and IAM users by a Python module in the AVL
codebase. The module is used at two points in the S3 bucket lifecycle:

-   By the system operator, to create the buckets and associated resources
    (policies, IAM users, and permissions boundaries) during initial set-up
    and configuration of the AVL.

-   By the Jupyter Hub runtime, to create IAM users (if required) on user
    log-in and configure their bucket access via IAM policies; see the
    Jupyter Hub section of this documentation for further details.

#### Function

The function of the Object Storage is similar to that of a traditional
computer file system: to provide persistent storage of and access to blocks of
data (‘files’ in a traditional file system; ‘objects’ in an object storage
system) referenced by string identifiers (‘filenames’ in a traditional file
system; ‘keys’ in an object storage system). The main advantages of the object
storage system are its standardized HTTP API, simplicity of access,
reliability, support for complex, sophisticated access policies, and – perhaps
most importantly – scalability (especially when used with the Zarr data
format) to very large datasets.

#### Dependencies

None.

#### Interfaces

The Object Storage main interface is a REST API compatible with the [AWS
S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html).

Thanks to the AWS S3 compatibility, there are many software tools and
libraries that can be used as middleware to access the Object Storage.

