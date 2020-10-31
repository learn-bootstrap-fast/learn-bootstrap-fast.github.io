package com.mcnz.web;

import java.io.File;
import java.io.IOException;
import java.util.Iterator;
import java.util.List;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.fileupload.DiskFileUpload;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUpload;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;


@WebServlet(name = "FileUploadServlet", urlPatterns = { "/fileuploadservlet" })
public class FileUploadServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
   


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doget");
		try {
			response.getWriter().append("Served today at: ").append(request.getContextPath());
			System.out.println("Content Type ="+request.getContentType());

			DiskFileUpload fu = new DiskFileUpload();
			// If file size exceeds, a FileUploadException will be thrown
			fu.setSizeMax(1000000);

			List fileItems = fu.parseRequest(request);
			Iterator itr = fileItems.iterator();

			while(itr.hasNext()) {
			  FileItem fi = (FileItem)itr.next();

			  //Check if not form field so as to only handle the file inputs
			  //else condition handles the submit button input
			  if(!fi.isFormField()) {
			    System.out.println("nNAME: "+fi.getName());
			    System.out.println("SIZE: "+fi.getSize());
			    //System.out.println(fi.getOutputStream().toString());
			    File fNew= new File(this.getServletContext().getRealPath("/"), fi.getName());

			    System.out.println(fNew.getAbsolutePath());
			    fi.write(fNew);
			  }
			  else {
			    System.out.println("Field ="+fi.getFieldName());
			  }
			}
		} catch (Exception e) {
			e.printStackTrace();
		} 
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doPost");
		try {
			
			DiskFileItemFactory factory = new DiskFileItemFactory();
			
			File repository = new File("C:\\temp\\");
			factory.setRepository(repository);
			ServletFileUpload upload = new ServletFileUpload(factory);

			FileUpload fu = new FileUpload();
			fu.setSizeMax(1000000);

			List<FileItem> fileItems = upload.parseRequest(request);
			System.out.println("Number of file items: " + fileItems.size());
			for(FileItem fi : fileItems) {
			  if(!fi.isFormField()) {	  
				File file = new File(fi.getName()); 
				  System.out.println(fi.getFieldName());
				  System.out.println(fi.getName());
				  
			    File fNew= new File("C:\\upload\\"  + file.getName());
			    fi.write(fNew);
			  }
			}
		} catch (Exception e) {
			e.printStackTrace();
		} 
	}

}
