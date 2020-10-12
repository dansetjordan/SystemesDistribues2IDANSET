package fr.polytech.web;

import fr.polytech.systemes.SommeProduit;
import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Servlet extends HttpServlet {


	private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.getServletContext().getRequestDispatcher("/WEB-INF/index.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    	double nbr1 = Integer.parseInt(request.getParameter("nbr1"));
    	double nbr2 = Integer.parseInt(request.getParameter("nbr2"));
    	
    	
    	SommeProduit sm = new SommeProduit();
        String resultat = Double.toString(sm.somme(nbr1, nbr2));
    	
        
        request.setAttribute("resultat", resultat);
        
        
        

        this.getServletContext().getRequestDispatcher("/WEB-INF/index.jsp").forward(request, response);

 
    }
}
