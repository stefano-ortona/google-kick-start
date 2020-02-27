package com.google.ortona.kickstart.y2019.roundA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import org.junit.Assert;
import org.junit.Test;

public class ParcelsTest {

  public static Parcels SOLVER = new Parcels();

  @Test
  public void testAllDeliveryPoints() {
    Assert.assertEquals(0, SOLVER.minimumDeliveryTime(new int[][] { { 1, 1, 1 }, { 1, 1, 1 } }));
    Assert.assertEquals(0, SOLVER.minimumDeliveryTime(new int[][] { { 1, 1 } }));
  }

  @Test
  public void test4DeliveryPointsSmall() {
    Assert.assertEquals(1, SOLVER.minimumDeliveryTime(new int[][] { { 1, 0, 1 }, { 0, 0, 0 }, { 1, 0, 1 } }));
  }

  @Test
  public void test4DeliveryPointsBig() {
    Assert.assertEquals(2, SOLVER.minimumDeliveryTime(
        new int[][] { { 1, 0, 0, 0, 1 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 1, 0, 0, 0, 1 } }));
  }

  @Test
  public void testDifferentRowsAndColumns() {
    Assert.assertEquals(3,
        SOLVER.minimumDeliveryTime(new int[][] { { 0, 0, 1, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 } }));
  }

  @Test
  public void bigInput() throws IOException {
    final int[][] input = readInput("bigInput.txt");
    final long curTime = System.currentTimeMillis();
    SOLVER.minimumDeliveryTime(input);
    final long finalTime = System.currentTimeMillis() - curTime;
    // check it took less than 15 seconds
    Assert.assertTrue((finalTime / 1000.) < 15);
  }

  private int[][] readInput(String fileName) throws IOException {
    final BufferedReader bbR = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream(fileName)));
    String line;
    final List<String> allLines = new ArrayList<>();
    while ((line = bbR.readLine()) != null) {
      allLines.add(line);
    }
    final int[][] output = new int[allLines.size()][allLines.get(0).length()];
    for (int i = 0; i < allLines.size(); i++) {
      final String curLine = allLines.get(i);
      for (int j = 0; j < curLine.length(); j++) {
        output[i][j] = curLine.charAt(j) - '0';
      }
    }
    return output;
  }

  @Test
  public void testWith250Big() {
    final List<int[][]> allInputs = new ArrayList<>(100);
    for (int i = 0; i < 100; i++) {
      allInputs.add(generateRandomGrid(250, 250));
    }
    final long curTime = System.currentTimeMillis();
    allInputs.forEach(i -> {
      printInput(i);
      SOLVER.minimumDeliveryTime(i);
      System.out.println("------------------------");
    });
    final long finalTime = System.currentTimeMillis() - curTime;
    // check it took less than 15 seconds
    Assert.assertTrue((finalTime / 1000.) < 15);
  }

  private void printInput(int[][] input) {
    for (final int[] oneRow : input) {
      System.out.println(Arrays.toString(oneRow));
    }
  }

  private int[][] generateRandomGrid(int row, int col) {
    final Random r = new Random();
    final int[][] bigInput = new int[row][col];
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        bigInput[i][j] = r.nextInt(2);
      }
    }
    return bigInput;
  }

}
