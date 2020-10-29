---
layout: basic-post
author: Cameron
title:  Jakarta ServletException and UnavailableException
heading:  UnavailableException and ServletException in Jakarta Servlet Web Apps
blurb: A Jakarta Servlet will throw the UnavailableException and ServletException if problem handling the Java request occurs.
---

A Jakarta servlet may throw either a
`ServletException` or an `UnavailableException` during the service of a
request. A `ServletException` signals that some error occurred during
the processing of the request and that the container should take
appropriate measures to clean up the request.

## Jakarta ServletException in Java

A Java servlet's `UnavailableException` signals that the
servlet is unable to handle requests either temporarily or permanently.

If a permanent unavailability is indicated by
the `UnavailableException`, the servlet container must remove the
servlet from service, call its `destroy` method, and release the servlet
instance. Any requests refused by the container by that cause must be
returned with a `SC_NOT_FOUND` (404) response.

## Java Servlet 5 API UnavailableException

If temporary unavailability is indicated by
the `UnavailableException`, the container may choose to not route any
requests through the servlet during the time period of the temporary
unavailability. Any requests refused by the container during this period
must be returned with a `SC_SERVICE_UNAVAILABLE` (503) response status
along with a `Retry-After` header indicating when the unavailability
will terminate.

The Java servlet container may choose to ignore the
distinction between a permanent and temporary unavailability and treat
all `UnavailableExceptions` as permanent, thereby removing a Jaava servlet
that throws any `UnavailableException` from service.