package com.google.ortona.kickstart.y2019.roundA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Training {

  public int getMinHoursTraining(Integer[] skills, int players) {
    Arrays.sort(skills, (a, b) -> b - a);
    int curSum = 0;
    for (int i = 0; i < players; i++) {
      curSum += skills[i];
    }
    int minHours = (skills[0] * players) - curSum;
    for (int i = players; i < skills.length; i++) {
      curSum += skills[i];
      curSum -= skills[i - players];
      final int curHours = (skills[(i - players) + 1] * players) - curSum;
      minHours = Math.min(minHours, curHours);
    }
    return minHours;
  }

  public static void main(String[] args) {
    final Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    final Training solver = new Training();
    final int t = in.nextInt();
    in.nextLine();
    for (int i = 1; i <= t; ++i) {
      final String firstLine = in.nextLine();
      final String secondLine = in.nextLine();
      final int players = Integer.parseInt(firstLine.split(" ")[1]);
      final String[] singleSkills = secondLine.split(" ");
      final Integer[] skills = new Integer[singleSkills.length];
      for (int j = 0; j < singleSkills.length; j++) {
        skills[j] = Integer.parseInt(singleSkills[j]);
      }
      final int curSol = solver.getMinHoursTraining(skills, players);
      System.out.println("Case #" + i + ": " + curSol);
    }
    in.close();
  }

}
