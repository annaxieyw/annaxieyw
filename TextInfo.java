/*
 * TextInfo.java
 *
 * TextInfo is (1) a blueprint class for objects that summarize information
 * about a text file and (2) a program that can be run to allow clients 
 * to obtain information about a text file.
 * 
 * name: Anna Xie
 * BU email: annaxyw@bu.edu
 */

import java.io.*;
import java.util.*;

public class TextInfo {
    // Add your fields here.
	private ChainedHashTable linenum;
	private ChainedHashTable frequency;
    
    /*
     * Creates a TextInfo object based on the text file with the specified name.
     */
    public TextInfo(String filename) throws FileNotFoundException {
        File file = new File(filename);
        long numBytes = file.length();       // number of bytes in the file
        int size = (int)(numBytes / 10);     // size for the hash tables
        
        // some code will probably be needed here!
        ChainedHashTable linenum = new ChainedHashTable(size);
        ChainedHashTable frequency = new ChainedHashTable(size);
        
        Scanner text = new Scanner(file);    // Scanner for reading from file
        while (text.hasNextLine()) {
            String line = text.nextLine();

            // code to process each line goes here
        }
        
        // some additional code may be needed here!
        
    }
    
    
    /*** Add your other methods here. ***
     */
    
    /*
     * getNumWords - returns the number of unique words in the text file represented by the TextInfo object
     */
    public int getNumWords() {
    	return frequency.getNumKeys();
    }
    
    /*
     * linesForWord - returns a string specifying the line numbers on which that word appears in the text file represented by the TextInfo object
     */
    public String linesForWord(String s) {
    	String a = "";
    	Queue<Object> b = linenum.search(s);
    	a += b;
    	if (a == "{}") {
    		a = "none";
    	}
    	return a;
    }
    
    /*
     * frequency - returns an integer specifying the number of times that the word appears in the text file represented by the called TextInfo object
     */
    public int frequency(String s) {
    	Queue<Object> a = frequency.search(s);
    	return ((int) a.peek());
    }
    
    /*
     * kMostCommon - returns an array of strings containing the k most common words in the text file represented by the called TextInfo object 
     */
    public String[] kMostCommon(int k) {
    	String a = "";
    	if (frequency.search(key) == k) {
    		a += key;
    	}
    }
    
    /*
     * getChoice - prints a menu of choices and obtains and returns 
     * the number of the user's choice
     */
    public static int getChoice(Scanner console) {
        System.out.println("1) Find out where a word appears");
        System.out.println("2) Lookup a word's frequency");
        System.out.println("3) List the most common words");
        System.out.println("4) Quit");
        
        int choice;
        do {
            System.out.print("\nEnter your choice: ");
            choice = console.nextInt();
        } while (choice < 1 || choice > 4);
        
        console.nextLine();   // flush the Scanner's buffer
        return choice;
    }
    
    public static void main(String[] args) throws FileNotFoundException {
        Scanner console = new Scanner(System.in);
       
        System.out.print("name of file: ");
        String filename = console.nextLine();
        TextInfo a = new TextInfo(filename);
       
        // Add code to create the TextInfo object and print the number of words.
        
        while (true) {
            System.out.println();
            int choice = getChoice(console);
            
            if (choice == 1) {        
                System.out.print("word: ");
                String word = console.nextLine();

                // Add code to implement choice 1.
                System.out.println(linenum.search(word));
                
                
            } else if (choice == 2) {
                System.out.print("word: ");
                String word = console.nextLine();

                // Add code to implement choice 2.
                System.out.println(a.frequency(word));
                
            } else if (choice == 3) {
                System.out.print("how many words: ");
                int k = console.nextInt();
                console.nextLine();    // flush the Scanner's buffer    
                
                // Add code to implement choice 3.
                String[] b = a.kMostCommon(max);
                System.out.println(b[0]);
                
            } else if (choice == 4) {
                break;
            }
        }
    }
}
