// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// How it works:	i = R1
// 			while i > 0 
//   		    	    R2 += R0
//   		    	    i -= 1
// 			return R2

    @R1
    D = M          // Load R1 into D-register
    
    @ZERO_CHECK
    D;JEQ          // If R1 is zero, jump to the end (early exit)
    
    @R0
    D = M          // Load R0 into D-register
    
    @R1
    M = M - 1      // Decrement R1 (used as loop counter)

    @product
    M = 0          // Initialize product to zero
    
(MULTIPLY)
    @product
    M = M + D      // Add R0 to product
    
    @R1
    M = M - 1      // Decrement R1 (loop counter)
    
    D = M          // Load updated R1 into D-register
    
    @MULTIPLY
    D;JGT          // If R1 > 0, repeat multiplication
    
    @product       // If R1 <= 0, we're done with the loop
    D = M          // Load product into D-register
    
    @R2
    M = D          // Store result in R2
    
    @END
    0;JMP          // Infinite loop to prevent further operations
    
(ZERO_CHECK)
    @R2
    M = 0          // If early exit, set R2 to zero
    
    @END
    0;JMP          // Infinite loop to end the program