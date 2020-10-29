---
layout: basic-post
author: Cameron
title:  Jakarta's Servlet Request Handling
heading: Jakarta Servlet 5 API Request Handling
blurb: Here's how the Jakarta Servlet 5 API handles requests
---


After a Jakartaservlet is properly initialized, the
servlet container may use it to handle client requests. Requests are
represented by request objects of type `ServletRequest`. 

The Java servlet
fills out responses to requests by calling methods of a provided object
of type `ServletResponse`.

<h2>Request handling in Java Servlets</h2>

These objects are passed as parameters to
the `service` method of the `Servlet` interface.

In the case of an HTTP request, the objects
provided by the container are of types `HttpServletRequest` and
`HttpServletResponse`.

Note that a servlet instance placed into
service by a Jakarta servlet container may handle no requests during its
lifetime.