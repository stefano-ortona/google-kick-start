package com.google.ortona.kickstart.y2019.roundA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Parcels {

  private final Logger LOG = LoggerFactory.getLogger(getClass());

  public int minimumDeliveryTime(int[][] grid) {
    LOG.info("Started computation on a {}x{} grid", grid.length, grid[0].length);
    final List<int[]> maxHeap = new ArrayList<>();
    final int[][] originalWaitingTimes = new int[grid.length][grid[0].length];
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        maxHeap.add(new int[] { i, j });
        originalWaitingTimes[i][j] = Integer.MAX_VALUE - 1000;
        if (grid[i][j] == 1) {
          originalWaitingTimes[i][j] = 0;
        }
      }
    }
    computeWaitingTime(originalWaitingTimes);
    LOG.info("Initial distance from delivery points computed");

    Collections.sort(maxHeap, (o1, o2) -> originalWaitingTimes[o2[0]][o2[1]] - originalWaitingTimes[o1[0]][o1[1]]);
    LOG.info("Sorting of all input cells computed");

    int minWaitingTime = originalWaitingTimes[maxHeap.get(0)[0]][maxHeap.get(0)[1]];
    for (int i = 0; i < originalWaitingTimes.length; i++) {
      for (int j = 0; j < originalWaitingTimes[0].length; j++) {
        minWaitingTime = Math.min(minWaitingTime, computeNewWaitingTime(i, j, maxHeap, originalWaitingTimes));
      }
    }
    LOG.info("Final computation ended");
    return minWaitingTime;
  }

  private int computeNewWaitingTime(int row, int col, List<int[]> maxHeap, int[][] waitingTimes) {
    int maxWaitingTime = 0;
    for (int i = 0; i < maxHeap.size(); i++) {
      final int[] curPos = maxHeap.get(i);
      final int newWaitingTime = Math.min(waitingTimes[curPos[0]][curPos[1]],
          manhattanDistance(row, col, curPos[0], curPos[1]));
      maxWaitingTime = Math.max(newWaitingTime, maxWaitingTime);
      if (maxWaitingTime >= waitingTimes[curPos[0]][curPos[1]]) {
        break;
      }
    }
    return maxWaitingTime;
  }

  private int manhattanDistance(int i1, int j1, int i2, int j2) {
    return Math.abs(i1 - i2) + Math.abs(j1 - j2);
  }

  private void computeWaitingTime(int[][] grid) {
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        if (i > 0) {
          grid[i][j] = Math.min(grid[i][j], grid[i - 1][j] + 1);
        }
        if (j > 0) {
          grid[i][j] = Math.min(grid[i][j], grid[i][j - 1] + 1);
        }
      }
    }
    for (int i = grid.length - 1; i >= 0; i--) {
      for (int j = grid[0].length - 1; j >= 0; j--) {
        if (i < (grid.length - 1)) {
          grid[i][j] = Math.min(grid[i][j], grid[i + 1][j] + 1);
        }
        if (j < (grid[0].length - 1)) {
          grid[i][j] = Math.min(grid[i][j], grid[i][j + 1] + 1);
        }
      }
    }
  }

  public static void main(String[] args) {
    final Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    final Parcels solver = new Parcels();
    final int t = in.nextInt();
    in.nextLine();
    for (int i = 1; i <= t; ++i) {
      final String firstLine = in.nextLine();
      final int row = Integer.parseInt(firstLine.split(" ")[0]);
      final int col = Integer.parseInt(firstLine.split(" ")[1]);
      final int[][] grid = new int[row][col];
      for (int j = 0; j < row; j++) {
        final String oneRow = in.nextLine();
        grid[j] = convertStringToInteger(oneRow);
      }
      final int curSol = solver.minimumDeliveryTime(grid);
      System.out.println("Case #" + i + ": " + curSol);
    }
    in.close();
  }

  private static int[] convertStringToInteger(String row) {
    final int[] output = new int[row.length()];
    for (int i = 0; i < output.length; i++) {
      output[i] = row.charAt(i) - '0';
    }
    return output;
  }

}
