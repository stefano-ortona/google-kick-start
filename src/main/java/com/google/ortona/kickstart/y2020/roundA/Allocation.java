package com.google.ortona.kickstart.y2020.roundA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Allocation {
  
  public int getMaxHouses(int []prices, int B){
    Arrays.sort(prices);
    int count = 0;
    for(int i = 0; i < prices.length; i++){
      if(B < prices[i]){
        break;
      }
      count++;
      B -= prices[i];
    }
    return count;
  }
  
  
  public static void main(String[] args) {
    final Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    final Allocation solver = new Allocation();
    final int t = in.nextInt();
    in.nextLine();
    for (int i = 1; i <= t; ++i) {
      final String firstLine = in.nextLine();
      final int B = Integer.parseInt(firstLine.split(" ")[1]);
      final String []pricesStrings = in.nextLine().split(" ");
      final int[]prices = new int[pricesStrings.length];
      for (int j = 0; j < pricesStrings.length; j++) {
        prices[j] = Integer.parseInt(pricesStrings[j]);
      }
      final int curSol = solver.getMaxHouses(prices, B);
      System.out.println("Case #" + i + ": " + curSol);
    }
    in.close();
  }

}
