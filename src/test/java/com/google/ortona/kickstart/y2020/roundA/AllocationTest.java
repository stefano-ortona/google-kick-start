package com.google.ortona.kickstart.y2020.roundA;

import java.util.Random;

import org.junit.Assert;
import org.junit.Test;


public class AllocationTest {
  
  public static Allocation SOLVER = new Allocation();
  
  @Test
  public void testEmptyHouses() {
    Assert.assertEquals(0, SOLVER.getMaxHouses(new int[]{}, 200));
  }

  @Test
  public void testOneHouse() {
    Assert.assertEquals(1, SOLVER.getMaxHouses(new int[]{10}, 200));
    Assert.assertEquals(0, SOLVER.getMaxHouses(new int[]{201}, 200));
  }

  @Test
  public void testFourHouses() {
    Assert.assertEquals(2, SOLVER.getMaxHouses(new int[]{20,90,40,90}, 100));
    Assert.assertEquals(3, SOLVER.getMaxHouses(new int[]{30,30,10,10}, 50));
  }

  @Test
  public void testNotEnoguhMoney() {
    Assert.assertEquals(0, SOLVER.getMaxHouses(new int[]{201,201,201}, 200));
  }
  
  @Test
  public void testBigInput() {
    Assert.assertTrue(SOLVER.getMaxHouses(generateBigInput(100000), Integer.MAX_VALUE) > 0);
  }
  
  private int[] generateBigInput(int size){
    Random r = new Random();
    int []input = new int[size];
    for(int i = 0; i < size; i++){
      input[i] = r.nextInt(Integer.MAX_VALUE) + 1;
    }
    return input;
  }


}
