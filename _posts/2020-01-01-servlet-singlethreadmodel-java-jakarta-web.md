---
layout: basic-post
author: Cameron
title:  Jakarta's SingleThreadModel Explained
heading: How the Jakarta Servlet SingleThreadModel works
blurb: When you implement the Jakarta Servlet 5 API's SingleThreadModel, the manner in which HttpServlet isntances are managed changes significantly.
---


The Jakarta servlet 5 API declaration which is either via the annotation as described in Section 8, “Annotations and Pluggability” or part of the deployment descriptor of the web application containing the servlet, as described in Section 14, "Deployment Descriptor", controls how the servlet container provides instances of the servlet.

<h2>How SingleThreadModel Servlets Work</h2>

For a servlet not hosted in a distributed environment (the default), the Jakarta servlet container must use only one instance per Java servlet declaration. However, for a component implementing the Servlet's SingleThreadModel interface, the Java servlet container may instantiate multiple instances to handle a heavy request load and serialize requests to a particular instance.

In the case where a servlet was deployed as part of an application marked in the deployment descriptor as distributable, a container may have only one instance per servlet declaration per Java Virtual Machine (JVM™). However, if the servlet in a distributable application implements the SingleThreadModel interface, the container may instantiate multiple instances of that servlet in each JVM of the container.

<h3> About The Servlet 5 API's Single Thread Model</h3>

The use of the Servlet 5 API's SingleThreadModel interface guarantees that only one thread at a time will execute in a given servlet instance’s service method. It is important to note that this guarantee only applies to each servlet instance, since the container may choose to pool such objects. Objects that are accessible to more than one servlet instance at a time, such as instances of HttpSession, may be available at any particular time to multiple servlets, including those that implement SingleThreadModel.

<h3>SingleThreadModel Deprecation</h3>

It is recommended that a developer take other means to resolve those issues instead of implementing this interface, such as avoiding the usage of an instance variable or synchronizing the block of the code accessing those resources. The Jakarta EE Servlet API's SingleThreadModel Interface has been deprecated since version 2.4 of this specification.

