---
layout: basic-post
author: Cameron
title:  Jakarta Servlet in a Java Container Example
heading: How a Java Servlet runs in a container example
blurb: Here's a simple example of how a Java Servlet is executed and managed at runtime by a Jakarta Servlet container.
---

The following is a typical example of a Java Servlet running inside a servlet container in a Jakarta certified environment:

- a client accesses a web server and makes a web a based HTTP request

- the request is received by the web server and handed off to a Java servlet container such as Tomcat or Jetty or WebLogic

- The Jakarta servlet container can be running in the same process as the host web server, in a different process on the same host, or on a different host from the web server for which it processes requests

- The servlet container in Java determines which Jakarta servlet to invoke based on the configuration of its servlets

- The Java web container calls the associated HttpServlet with objects representing the request and response

- The servlet uses the request object to find out who the remote user is, what HTTP POST parameters may have been sent as part of this request, and other relevant data

- The servlet performs whatever logic it was programmed with, and generates data to send back to the client. It sends this data back to the client via the response object

<h2>HttpServlet and Web Container Example</h2>

Once the HttpServlet has finished processing the request, the Java servlet container ensures that the response is properly flushed, and returns control back to the host web server.

