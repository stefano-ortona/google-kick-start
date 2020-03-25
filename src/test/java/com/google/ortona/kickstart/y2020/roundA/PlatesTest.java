package com.google.ortona.kickstart.y2020.roundA;

import java.util.Random;

import org.junit.Assert;
import org.junit.Test;

public class PlatesTest {
public static Plates SOLVER = new Plates();
  
  @Test
  public void testEmptyStack() {
    Assert.assertEquals(0, SOLVER.pickPlates(new int[][]{}, 5));
  }

  @Test
  public void testOneSinglePlate() {
    Assert.assertEquals(200, SOLVER.pickPlates(new int[][]{{100,2,1000,40},{200,2,1000,30},{99,5000,6000,7000}}, 1));
  }

  @Test
  public void testFivePlatesTwoStacks() {
    Assert.assertEquals(250, SOLVER.pickPlates(new int[][]{{10,10,100,30},{80,50,10,50}}, 5));
  }

  @Test
  public void testTwoPlatesThreStacks() {
    Assert.assertEquals(180, SOLVER.pickPlates(new int[][]{{80,80},{15,50},{20,10}}, 3));
  }
  
  @Test
  public void testBigInput() {
    for(int i = 1; i <= 50*30; i++){
      Assert.assertTrue(SOLVER.pickPlates(createBigInput(50, 30), i) > 0);
    }
  }
  
  private int[][] createBigInput(int row, int column){
    Random r = new Random();
    int [][]input = new int[row][column];
    for(int i = 0; i < row; i++){
      for(int j = 0; j < column; j++){
        input[i][j] = r.nextInt(100) + 1;
      }
    }
    return input;
  }

}
