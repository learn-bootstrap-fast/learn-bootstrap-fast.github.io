---
layout: basic-post
author: Cameron
title: What is a Jakarta Servlet Container in Java?
heading: Definition of a Servlet Container in Java Jakarta
blurb: A Jakarta Servlet Container in Java is a logical component that provides runtime management to Java Servlets, JSPS, Sessions and other Java web components.
---


A servlet is a Jakarta technology-based web component, managed by a container, that generates dynamic content. 

<h2>What is a Java Servlet Container in Jakarta?</h2>

The servlet container is a part of a Jakarta web server or Java application server such as Tomcat or Jetty.  

<h2> What does a Java Servlet Container in Jakarta do?</h2>

The responsibility of a Jakarta Servlet Container in Java is to:

- provides the network services over which requests and responses are sent
- decodes MIME-based requests and 
- formats MIME-based responses. 
- a servlet container also contains and manages servlets through their lifecycle

<h3>Java Servlet Container Architecture</h3>

A Java servlet container can be built into a host web server like Apache Tomcat, or installed as an add-on component to a web server such as JBoss Red Hat via that server’s native extension API. Java Servlet containers in Java can also be built into or possibly installed into web-enabled Java application servers like Jetty or WebLogic.

<h3>Jakarta Servlet Container Responsibilities</h3>

All servlet containers must support HTTP as a protocol for requests and responses, but additional request/response-based protocols such as HTTPS (HTTP over SSL) may be supported. The required versions of the HTTP specification that a container must implement are HTTP/1.1 and HTTP/2. When supporting HTTP/2, servlet containers must support the “h2” and “h2c” protocol identifiers (as specified in section 3.1 of the HTTP/2 RFC). This implies all Java and Jakarta servlet containers must support ALPN. Because the servlet container in Java may have a caching mechanism described in RFC 7234 (HTTP/1.1 Caching), it may modify requests from the clients before delivering them to the servlet, may modify responses produced by HttpServlets before sending them to the clients, or may respond to requests without delivering them to the servlet under the compliance with RFC 7234.

A servlet container in Java may place security restrictions on the environment in which a Jakarta servlet or JSP executes. These restrictions may be placed using the permission architecture defined by the Java platform. For example some Java application servers and containers may limit the creation of a Thread object to insure that other components of the servlet container are not negatively impacted.

Java SE 8 is the minimum version of the underlying Java platform with which Jakarta servlet containers in Java must be built.

