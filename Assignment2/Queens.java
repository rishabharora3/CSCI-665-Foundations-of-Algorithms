import java.util.Scanner;

/**
 * Queens.java This program checks if the given placement is a solution to the n
 * queens puzzle.
 * 
 * @author Anubhuti Suresh Puppalwar, ap1401@rit.edu
 * @author Rishabh Arora, ra8851@rit.edu
 *
 */
public class Queens {
    static int n = 0;
    static int[] rowarr;
    static int[] colarr;
    static int[] diagRtoL;
    static int[] diagLtoR;

    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	n = in.nextInt();
	// row array that represent all n rows where each cell represent number
	// of elements in that row
	rowarr = new int[n];
	// column array that represent all n columns where each cell represent
	// number of elements in that column
	colarr = new int[n];
	// diagonals with positive slope array where each cell represent number
	// of elements in that diagonal
	diagRtoL = new int[2 * n - 1];
	// diagonals with negative slope array where each cell represent number
	// of elements in that diagonal
	diagLtoR = new int[2 * n - 1];

	fillArrays(in);

	boolean flag = checkMorethan1Queen();

	if (flag) {
	    System.out.println("NO");
	} else {
	    System.out.println("YES");
	}

	in.close();
    }

    /**
     * Loop to check if there is more than 1 element in each row and column.
     * Loop to check if there is more than 1 element in each diagonal.
     * 
     * @return boolean
     */
    private static boolean checkMorethan1Queen() {
	boolean flag = false;

	for (int j = 0; j < n && flag == false; j++) {
	    if (rowarr[j] > 1) {
		flag = true;
	    }
	    if (colarr[j] > 1) {
		flag = true;
	    }
	}

	for (int k = 0; k < 2 * n - 1 && flag == false; k++) {
	    if (diagLtoR[k] > 1) {
		flag = true;
	    }
	    if (diagRtoL[k] > 1) {
		flag = true;
	    }

	}
	return flag;

    }

    /**
     * Fills the 4 arrays in single loop with number of elements in that row,
     * column or diagonal.
     * 
     * @param in
     */
    private static void fillArrays(Scanner in) {

	for (int i = 0; i < n; i++) {
	    int x = in.nextInt();
	    x = x - 1;
	    int y = in.nextInt();
	    y = y - 1;
	    rowarr[x] = rowarr[x] + 1;
	    colarr[y] = colarr[y] + 1;

	    diagRtoL[x + y] = diagRtoL[x + y] + 1;

	    if (x > y) {
		int ind = n - 1 + x - y;
		diagLtoR[ind] = diagLtoR[ind] + 1;
	    } else {
		int ind2 = n - 1 - y + x;
		diagLtoR[ind2] = diagLtoR[ind2] + 1;
	    }
	}

    }

}
