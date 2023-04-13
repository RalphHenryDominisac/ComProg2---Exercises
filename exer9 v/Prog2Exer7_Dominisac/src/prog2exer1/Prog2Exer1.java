/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prog2exer1;

import java.io.BufferedWriter;
import java.io.FileWriter;

/**
 *
 * @author RALPH
 */
public class Prog2Exer1 {
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {  
        CustomerForm abc = new CustomerForm();
        abc.setVisible(true);
       //  abc.writeCustomerCSV(); // calls writeCustomerCSV after the user inputs values to the textfields and clicks save 
         abc.readCustomerCSV(); 
         abc.readCustomerProductsCSV();
         abc.readDeletedIDCSV();
         
         
//        Products def = new Products();
        // def.setVisible(true);
//           def.readCustomerCSVProduct();
//           def.readCustomerCSVStocks();
//           def.readLODCSV();
           
           
        
        
        
        
      //  secondClass a = new secondClass(); //Instance of secondClass
       // a.showList();
       // System.out.print(a.Lists()[0]);
        
        
        
      //  CustomerForm b = new CustomerForm(); //Instance of CustomerForm class
        
  //       for (int m = 0; m < b.item.length; m++){   // transfer item string to static 2D array(itemTo2D)
    //        itemTo2D[indexerItem][m] = b.item[m];
      //  }
        
        //  CustomerForm b2 = new CustomerForm();
        //  b2.writeCustomerCSV(); //calls writeCustomerCSV
          
     
        
        
        
    }
    
    
    
    
   
    
    
    
    
    
    
}
