---
layout: basic-post
author: Cameron
title:  Jakarta Servlet Interface Methods in Java - doGet, doPost, etc
heading: Listing of the Jakarta Servlet Interface methods in Java
blurb: Mastering the Jakarta Servlet 5 API means mastering the Java Servlet interface methods like doPost and doGet.
---


The Servlet interface is the central abstraction of the Jakarta Servlet API. 

<h2>Jakarta Servlet Interface in Java</h2>

All Jakarta servlets implement this interface either directly, or more commonly, by extending a class that implements the Java Servlet interface. The two classes in the Jakarta Servlet API that implement the Java Servlet interface methods: 

1. GenericServlet 
 
2. HttpServlet

For most purposes, developers will extend the Jakarta HttpServlet class to implement their Java servlets.

<h2>Request Handling Servlet Interface Methods</h2>

The basic Jakarta Servlet 5 interface defines a service method for handling client requests. This method is called for each request that the Java servlet container routes to an instance of a servlet.

The handling of concurrent requests to a web application generally requires that the web developer design servlets that can deal with multiple threads executing within the service method at a particular time.

Generally the Java web container handles concurrent requests to the same Jakarta servlet by concurrent execution of the service method on different threads.

<h2>List of RESTful Servlet Interface Methods in Java</h2>

The HttpServlet abstract subclass adds additional methods beyond the basic Java Servlet interface that are automatically called by the service method in the Jakarta HttpServlet class to aid in processing HTTP-based requests. The following is a list of the Jakarta Servlet Interface methods:

- doGet for handling HTTP GET requests

- doPost for handling HTTP POST requests

- doPut for handling HTTP PUT requests

- doDelete for handling HTTP DELETE requests

- doHead for handling HTTP HEAD requests

- doOptions for handling HTTP OPTIONS requests

- doTrace for handling HTTP TRACE requests

Typically when developing HTTP-based servlets, an Application Developer is concerned with the doGet and doPost methods. The other methods are considered to be methods for use by programmers very familiar with HTTP programming.

<h3>Additional Jakarta Servlet 5 API Methods in Java</h3>
The doPut and doDelete methods allow Jakarta Servlet 5 Developers to support HTTP/1.1 clients that employ these features. The doHead method in HttpServlet is a specialized form of the doGet method that returns only the headers produced by the doGet method. The doOptions method responds with which HTTP methods are supported by the servlet. The doTrace method generates a response containing all instances of the headers sent in the TRACE request.

The CONNECT method is not supported because it applies to proxies and the Jakarta Servlet API is targeted at endpoints.

<h3>Conditional Java Servlet doGet() Support</h3>

The Jakarta HttpServlet class defines the getLastModified method to support conditional GET operations. A conditional GET operation requests a resource be sent only if it has been modified since a specified time. In appropriate situations, implementation of this method may aid efficient utilization of network resources.

