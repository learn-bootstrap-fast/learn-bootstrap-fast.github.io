---
layout: basic-post
author: Cameron
title: What is a Jakarta Servlet in Java?
heading: Definition of a Jakarta Servlet in Java
blurb: A Jakarta Servlet in Java is a web based component designed to handle the HTTP based request-response cycle.
---


A servlet is a Jakarta technology-based web component, managed by a container, that generates dynamic content. 

<h2>What is a Jakarta Servlet in Java?</h2>

Like other Jakarta technology-based components, servlets are platform-independent Java classes that are compiled to platform-neutral byte code that can be loaded dynamically into and run by a Jakarta technology-enabled web server. Containers, sometimes called servlet engines, are web server extensions that provide servlet functionality. Servlets interact with web clients via a request response paradigm implemented by the servlet container.

In short, a Jakarta Servlet in a Java based web component designed to handle the HTTP based request-response cycle.

<h3>How a Jakarta Servlet works</h3>

The way a Java Jakarta Servlet works is as follows:

- a web based request comes into the Java web server
- the request is passed to a Java Servlet
- a method such as doGet or doPost is called depending on how the HttpServlet was invoked
- a developer inspects the request, extracts parameters passed the the client
- backend resources are accessed to fullfill the incoming request
- a response, normally HTML or JSON, packaged in the HttpServletResponse object, is delivered back to the client

<h3>Jakarta Servlets and the Java Servlet Container</h3>

Jakarta Servlets require a Java runtime to operate. The environment in which they are run and managed is known as a Java Sevlet Container

