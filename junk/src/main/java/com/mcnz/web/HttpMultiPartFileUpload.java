package com.mcnz.web;

import java.io.*;

import org.apache.commons.httpclient.*;
import org.apache.commons.httpclient.methods.*;
import org.apache.commons.httpclient.methods.multipart.*;

public class HttpMultiPartFileUpload {
    private static String url =
      "http://localhost:8080/apache-commons-file-upload/fileuploadservlet";

    public static void main(String[] args) throws IOException {
    	  File file1 = new File("C:\\_tools\\students.xml");
    	  File file2 = new File("C:\\_tools\\rules.xml");
    	  
    	  PostMethod filePost = new PostMethod(url);
    	  Part[] parts = {
    		  new FilePart(file1.getName(), file1),
    	      new FilePart(file2.getName(), file2)
    	  };
    	  filePost.setRequestEntity(
    	      new MultipartRequestEntity(parts, filePost.getParams())
    	      );
    	  HttpClient client = new HttpClient();
    	  int status = client.executeMethod(filePost);
    	  System.out.println(status);
    }
}