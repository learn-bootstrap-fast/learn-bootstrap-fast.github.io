---
layout: basic-post
author: Cameron
title:  Jakarta's Servlet Lifecycle in Java
heading: Basic and Advanced Jakarta Servlet Lifecycle in Java
blurb: Here's how the Jakarta Servlet life cycle works in both basic and advanced Java programs explained with examples.
---


A Jakarta servlet in the Servlet 5 API is managed through a well defined life cycle that defines how it is loaded and instantiated, is
initialized, handles requests from clients, and is taken out of service. This Java Servlet life cycle is expressed in the API by the `init`, `service`, and
`destroy` methods of the `jakarta.servlet.Servlet` interface that all servlets must implement directly or indirectly through the
`GenericServlet` or `HttpServlet` abstract classes.

## Jakarta's Servlet Loading & Instantiation Lifecycle

The servlet container is responsible for
loading and instantiating servlets. The loading and instantiation can
occur when the container is started, or delayed until the container
determines the servlet is needed to service a request.

When the servlet engine is started, needed
servlet classes must be located by the servlet container. The servlet
container loads the servlet class using normal Java class loading
facilities. The loading may be from a local file system, a remote file
system, or other network services.

After loading the `Servlet` class, the
container instantiates it for use.

## Java Servlet init and Initialization

After the Jakarta servlet object is instantiated, the
servlet container must initialize the HttpServlet before it can handle requests from
clients. Initialization is provided so that a Java servlet can read
persistent configuration data, initialize costly resources (such as
JDBC™ API-based connections), and perform other one-time activities. The
container initializes the servlet instance by calling the `init` method
of the `Servlet` interface with a unique (per Jakarta servlet declaration)
object implementing the `ServletConfig` interface. This configuration
object allows the servlet to access name-value initialization parameters
from the web application’s configuration information. The configuration
object also gives the servlet access to an object (implementing the
`ServletContext` interface) that describes the Jakarta servlet's runtime
environment. 

## Jakarta Java Serlvet init errors

During initialization, the servlet instance
can throw an `UnavailableException` or a `ServletException`. In this
case, the servlet must not be placed into active service and must be
released by the servlet container. The `destroy` method is not called as
it is considered unsuccessful initialization.

A new instance may be instantiated and
initialized by the container after a failed initialization. The
exception to this rule is when an `UnavailableException` indicates a
minimum time of unavailability, and the container must wait for the
period to pass before creating and initializing a new servlet instance.

## Servlet Lifecycle and EJBs, JSPs, JSF and JPA

The triggering of static initialization
methods when a tool loads and introspects a web application is to be
distinguished from the calling of the `init` method. Developers should
not assume a servlet is in an active container runtime until the `init`
method of the `Servlet` interface is called. For example, a servlet
should not try to establish connections to databases or Jakarta Enterprise
Beans containers when only static (class) initialization methods
have been invoked.
