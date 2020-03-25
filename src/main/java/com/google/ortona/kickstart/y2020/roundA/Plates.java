package com.google.ortona.kickstart.y2020.roundA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Plates {
  
  public int pickPlates(int [][]stack, int P){
    stack = createCumulativeSum(stack);
    int [][]mem = new int[stack.length][P + 1];
    return pickPlates(0, stack, P, mem);
  }
  
  private int[][] createCumulativeSum(int [][]input){
    for(int i = 0; i < input.length; i++){
      for(int j = 1; j < input[i].length; j++){
        input[i][j] = input[i][j - 1] + input[i][j];
      }
    }
    return input;
  }
  
  private int pickPlates(int curStack, int [][]stack, int remaining, int [][]mem){
    if(curStack >= stack.length || remaining == 0){
      return 0;
    }
    if(mem[curStack][remaining] != 0){
      return mem[curStack][remaining];
    }
    int max = 0;
    int startIndex = Math.min(stack[curStack].length, remaining) - 1;
    // pick from the current stack
    for(int i = startIndex; i >=0; i--){
      int newRemaining = remaining - (i+1);
      max = Math.max(max, stack[curStack][i] + pickPlates(curStack+1, stack, newRemaining, mem));
    }
    // do not pick from current stack
    max = Math.max(max, pickPlates(curStack+1, stack, remaining, mem));
    mem[curStack][remaining] = max;
    return max;
  }
  
  public static void main(String[] args) {
    final Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    final Plates solver = new Plates();
    final int t = in.nextInt();
    in.nextLine();
    for (int i = 1; i <= t; ++i) {
      final String firstLine = in.nextLine();
      final int N = Integer.parseInt(firstLine.split(" ")[0]);
      final int P = Integer.parseInt(firstLine.split(" ")[2]);
      final int K = Integer.parseInt(firstLine.split(" ")[1]);
      int [][]stack = new int[N][K];
      for(int j = 0; j < N; j++){
        stack[j] = readLineToInteger(in.nextLine());
      }
      final int curSol = solver.pickPlates(stack, P);
      System.out.println("Case #" + i + ": " + curSol);
    }
    in.close();
  }
  
  private static int[] readLineToInteger(String line){
    String []numberStrings = line.split(" ");
    int []numbers = new int[numberStrings.length];
    for(int i = 0; i < numbers.length; i++){
      numbers[i] = Integer.parseInt(numberStrings[i]);
    }
    return numbers;
  }

}
