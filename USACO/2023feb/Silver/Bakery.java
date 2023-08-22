// USACO 2023 February Contest, Silver
// Problem 1. Bakery
// link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1302
// status: AC
// tag: binary search

import java.io.*;
import java.util.*;

public class Bakery {
    static long tc, tm;
    static long[][] friends = new long[101][3];
    static long N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long T = Long.parseLong(st.nextToken());
        for (int t=0; t<T; t++) {
            br.readLine();
            st = new StringTokenizer(br.readLine());
            N = Long.parseLong(st.nextToken());
            tc = Long.parseLong(st.nextToken());
            tm = Long.parseLong(st.nextToken());
            for (int i=0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                friends[i][0] = Long.parseLong(st.nextToken());
                friends[i][1] = Long.parseLong(st.nextToken());
                friends[i][2] = Long.parseLong(st.nextToken());
            }
            long low = 0, high = tc+tm-2;
            while (low < high) {
                long mid = low+(high-low)/2;
                if (works(friends, mid)) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
            pw.println(low);
        }
        pw.close();
    }

    public static boolean works(long[][] friends, long moon) {
        long lowX = Math.max(1, tc-moon), highX = Math.min(tc, tc+tm-1-moon);
        for (int i=0; i<N; i++) {
            long a = friends[i][0];
            long b = friends[i][1];
            long c = friends[i][2];
            long d = tc+tm-moon;
            if (a-b > 0) {
                highX = Math.min(highX, (c-b*d)/(a-b));
                //System.out.println("HI " + lowX + " " + a + " " + b + " " + c + " " + d);
            } else if (a-b < 0) {
                lowX = Math.max(lowX, (-c+b*d + (b-a-1))/(b-a));
                //System.out.println("LO " + highX + " " + a + " " + b + " " + c + " " + d);
            } else { 
                if (c - b * d < 0)
                    return false;
            }
        }
        return lowX <= highX;
    }
}
