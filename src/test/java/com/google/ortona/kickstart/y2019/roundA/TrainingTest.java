package com.google.ortona.kickstart.y2019.roundA;

import org.junit.Assert;
import org.junit.Test;

public class TrainingTest {

  private static Training SOLVER = new Training();

  @Test
  public void testJustEnoughPlayers() {
    Assert.assertEquals(6, SOLVER.getMinHoursTraining(new Integer[] { 7, 7, 1, 7, 7 }, 5));
    Assert.assertEquals(0, SOLVER.getMinHoursTraining(new Integer[] { 3, 3 }, 2));
    Assert.assertEquals(0, SOLVER.getMinHoursTraining(new Integer[] { 5 }, 1));
  }

  @Test
  public void threeOutOfFourPlayers() {
    Assert.assertEquals(14, SOLVER.getMinHoursTraining(new Integer[] { 3, 1, 9, 100 }, 3));
  }

  @Test
  public void twoOutOfSixPlayers() {
    Assert.assertEquals(0, SOLVER.getMinHoursTraining(new Integer[] { 5, 5, 1, 2, 3, 4 }, 2));
    Assert.assertEquals(1, SOLVER.getMinHoursTraining(new Integer[] { 5, 6, 1, 2, 3, 4 }, 2));
  }

}
